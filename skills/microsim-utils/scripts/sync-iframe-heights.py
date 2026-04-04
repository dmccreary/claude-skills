#!/usr/bin/env python3
"""Synchronize iframe heights across MicroSim index.md files and chapter files.

Uses the CANVAS_HEIGHT comment in each sim's .js file as the single source of
truth.  If CANVAS_HEIGHT is missing, computes it from drawHeight + controlHeight
(or other named variables) and inserts the comment on line 2 of the .js file.

Then updates iframe height attributes in:
  1. The sim's own docs/sims/<sim-id>/index.md
  2. Any chapter file (docs/chapters/*/index.md) that embeds the sim

Iframe height = CANVAS_HEIGHT + 2  (2px for the iframe border)

Usage:
  python3 sync-iframe-heights.py --project-dir /path/to/project --verbose
  python3 sync-iframe-heights.py --project-dir /path/to/project --sim gradient-explorer
  python3 sync-iframe-heights.py --project-dir /path/to/project --dry-run --verbose
"""

import argparse
import glob
import os
import re
import sys

# ── ANSI helpers ─────────────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
CHECK = "\u2714"
ARROW = "\u2192"


# ── Height detection ─────────────────────────────────────────────────

def read_canvas_height_comment(js_content):
    """Extract CANVAS_HEIGHT from a // CANVAS_HEIGHT: <int> comment.

    Returns the integer value or None if not found.
    Searches within the first 15 lines only.
    """
    for line in js_content.splitlines()[:15]:
        m = re.match(r'^\s*//\s*CANVAS_HEIGHT\s*[:=]\s*(\d+)', line)
        if m:
            return int(m.group(1))
    return None


def compute_canvas_height(js_content):
    """Compute CANVAS_HEIGHT from named height variables in the JS file.

    Looks for patterns like:
      let drawHeight = 400;
      let controlHeight = 80;
      let graphHeight = 180;   (optional, for sims with a graph panel)

    Returns (height, explanation) or (None, reason).
    """
    draw_h = _extract_var(js_content, r'(?:drawHeight|draw_height)')
    ctrl_h = _extract_var(js_content, r'(?:controlHeight|control_height|controlAreaHeight)')
    graph_h = _extract_var(js_content, r'(?:graphHeight|graph_height)')

    if draw_h is not None and ctrl_h is not None:
        total = draw_h + ctrl_h + (graph_h or 0)
        parts = f"drawHeight({draw_h}) + controlHeight({ctrl_h})"
        if graph_h:
            parts += f" + graphHeight({graph_h})"
        return total, parts

    # Fallback: canvasHeight directly
    canvas_h = _extract_var(js_content, r'(?:canvasHeight|canvas_height|containerHeight)')
    if canvas_h is not None:
        return canvas_h, f"canvasHeight({canvas_h})"

    # Fallback: createCanvas(w, h)
    m = re.search(r'createCanvas\s*\(\s*\w+\s*,\s*(\d+)\s*\)', js_content)
    if m:
        return int(m.group(1)), f"createCanvas height({m.group(1)})"

    return None, "could not detect height variables"


def _extract_var(js_content, pattern):
    """Extract an integer value from a JS variable declaration matching pattern."""
    m = re.search(
        rf'(?:let|const|var)\s+{pattern}\s*=\s*(\d+)',
        js_content
    )
    return int(m.group(1)) if m else None


def insert_canvas_height_comment(js_path, height, dry_run=False):
    """Insert a // CANVAS_HEIGHT: <height> comment on line 2 of the JS file.

    Preserves the existing first line (typically a title comment).
    Returns True if the file was modified.
    """
    with open(js_path, 'r') as f:
        lines = f.readlines()

    comment = f"// CANVAS_HEIGHT: {height}\n"

    # Check if line 2 already has a CANVAS_HEIGHT comment
    if len(lines) > 1 and re.match(r'^\s*//\s*CANVAS_HEIGHT', lines[1]):
        # Update existing
        if lines[1].strip() == comment.strip():
            return False  # already correct
        if not dry_run:
            lines[1] = comment
            with open(js_path, 'w') as f:
                f.writelines(lines)
        return True

    # Insert after first line
    if not dry_run:
        lines.insert(1, comment)
        with open(js_path, 'w') as f:
            f.writelines(lines)
    return True


# ── Iframe updating ──────────────────────────────────────────────────

IFRAME_HEIGHT_RE = re.compile(
    r'(<iframe\b[^>]*?)height\s*=\s*["\']?(\d+)\s*(?:px)?["\']?([^>]*>)',
    re.IGNORECASE
)


def update_iframes_in_file(filepath, sim_id, target_height, dry_run=False):
    """Update iframe height for a specific sim_id in a markdown file.

    Matches iframes whose src contains the sim_id.
    Returns list of (old_height, new_height) for each changed iframe.
    """
    with open(filepath, 'r') as f:
        content = f.read()

    changes = []
    new_content = content

    for m in IFRAME_HEIGHT_RE.finditer(content):
        full_match = m.group(0)
        prefix = m.group(1)
        old_h = int(m.group(2))
        suffix = m.group(3)

        # Check if this iframe is for our sim
        if sim_id not in full_match:
            # For sim's own index.md, also match src="main.html"
            if 'main.html' in full_match and filepath.endswith(
                os.path.join(sim_id, 'index.md')
            ):
                pass  # This is the sim's own iframe
            else:
                continue

        if old_h == target_height:
            continue

        new_iframe = f'{prefix}height="{target_height}"{suffix}'
        new_content = new_content.replace(full_match, new_iframe, 1)
        changes.append((old_h, target_height))

    if changes and not dry_run:
        with open(filepath, 'w') as f:
            f.write(new_content)

    return changes


# ── Main logic ───────────────────────────────────────────────────────

def sync_sim(sim_dir, sim_name, chapters_dir, dry_run=False, verbose=False):
    """Synchronize iframe heights for a single MicroSim.

    Returns a dict with sync results.
    """
    js_path = os.path.join(sim_dir, f'{sim_name}.js')
    if not os.path.isfile(js_path):
        if verbose:
            print(f"  {DIM}SKIP {sim_name}: no JS file{RESET}")
        return None

    with open(js_path, 'r') as f:
        js_content = f.read()

    # Step 1: Get or compute CANVAS_HEIGHT
    canvas_height = read_canvas_height_comment(js_content)
    comment_inserted = False

    if canvas_height is None:
        canvas_height, explanation = compute_canvas_height(js_content)
        if canvas_height is None:
            if verbose:
                print(f"  {YELLOW}WARN{RESET} {sim_name}: {explanation}")
            return None

        # Insert the comment into the JS file
        comment_inserted = insert_canvas_height_comment(
            js_path, canvas_height, dry_run
        )
        label = "WOULD INSERT" if dry_run else "INSERTED"
        print(
            f"  {CYAN}{label}{RESET} {sim_name}: "
            f"// CANVAS_HEIGHT: {canvas_height}  (from {explanation})"
        )
    else:
        # Validate: does the comment match the actual variables?
        computed, explanation = compute_canvas_height(js_content)
        if computed is not None and computed != canvas_height:
            if verbose:
                print(
                    f"  {YELLOW}NOTE{RESET} {sim_name}: CANVAS_HEIGHT comment "
                    f"({canvas_height}) differs from computed ({computed} = {explanation})"
                )

    target_iframe_height = canvas_height + 2
    total_changes = 0

    # Step 2: Update sim's own index.md
    sim_index = os.path.join(sim_dir, 'index.md')
    if os.path.isfile(sim_index):
        changes = update_iframes_in_file(
            sim_index, sim_name, target_iframe_height, dry_run
        )
        for old_h, new_h in changes:
            label = "WOULD FIX" if dry_run else "FIXED"
            print(
                f"  {GREEN}{label}{RESET} {sim_name}/index.md: "
                f"{old_h} {ARROW} {new_h}"
            )
            total_changes += 1

    # Step 3: Update chapter files that embed this sim
    if os.path.isdir(chapters_dir):
        for ch_index in sorted(glob.glob(
            os.path.join(chapters_dir, '*/index.md')
        )):
            with open(ch_index, 'r') as f:
                ch_content = f.read()

            # Only process if this chapter references our sim
            if sim_name not in ch_content:
                continue

            changes = update_iframes_in_file(
                ch_index, sim_name, target_iframe_height, dry_run
            )
            ch_name = os.path.basename(os.path.dirname(ch_index))
            for old_h, new_h in changes:
                label = "WOULD FIX" if dry_run else "FIXED"
                print(
                    f"  {GREEN}{label}{RESET} chapters/{ch_name}/index.md: "
                    f"{old_h} {ARROW} {new_h}"
                )
                total_changes += 1

    if total_changes == 0 and not comment_inserted and verbose:
        print(
            f"  {DIM}OK   {sim_name}: "
            f"CANVAS_HEIGHT={canvas_height}, iframe={target_iframe_height}px{RESET}"
        )

    return {
        'sim': sim_name,
        'canvas_height': canvas_height,
        'iframe_height': target_iframe_height,
        'comment_inserted': comment_inserted,
        'iframes_updated': total_changes,
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Synchronize iframe heights from CANVAS_HEIGHT in JS files "
            "to sim index.md and chapter index.md files."
        )
    )
    parser.add_argument(
        '--project-dir', default=None,
        help='Project root containing mkdocs.yml (auto-detect if omitted)'
    )
    parser.add_argument(
        '--sim', default=None,
        help='Sync a single sim by name (default: all sims)'
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Preview changes without writing files'
    )
    parser.add_argument(
        '--verbose', action='store_true',
        help='Show status for all sims, not just changes'
    )
    args = parser.parse_args()

    # Resolve project root
    if args.project_dir:
        project_dir = os.path.abspath(args.project_dir)
    else:
        d = os.path.abspath('.')
        while d != os.path.dirname(d):
            if os.path.isfile(os.path.join(d, 'mkdocs.yml')):
                project_dir = d
                break
            d = os.path.dirname(d)
        else:
            print("ERROR: mkdocs.yml not found. Use --project-dir.", file=sys.stderr)
            sys.exit(1)

    sims_dir = os.path.join(project_dir, 'docs', 'sims')
    chapters_dir = os.path.join(project_dir, 'docs', 'chapters')

    if not os.path.isdir(sims_dir):
        print(f"ERROR: {sims_dir} not found.", file=sys.stderr)
        sys.exit(1)

    print(f"{BOLD}Project root:{RESET} {project_dir}")

    # Collect sim directories
    if args.sim:
        sim_dirs = [os.path.join(sims_dir, args.sim)]
        if not os.path.isdir(sim_dirs[0]):
            print(f"ERROR: sim directory {sim_dirs[0]} not found.", file=sys.stderr)
            sys.exit(1)
    else:
        sim_dirs = sorted(
            d for d in glob.glob(os.path.join(sims_dir, '*/'))
            if os.path.basename(d.rstrip('/')) != 'TODO'
        )

    # Process each sim
    stats = {
        'total': 0,
        'comments_inserted': 0,
        'iframes_updated': 0,
        'skipped': 0,
    }

    for sim_dir in sim_dirs:
        sim_name = os.path.basename(sim_dir.rstrip('/'))
        result = sync_sim(
            sim_dir, sim_name, chapters_dir,
            dry_run=args.dry_run, verbose=args.verbose
        )

        if result is None:
            stats['skipped'] += 1
        else:
            stats['total'] += 1
            stats['comments_inserted'] += 1 if result['comment_inserted'] else 0
            stats['iframes_updated'] += result['iframes_updated']

    # Summary
    print()
    verb = "Would sync" if args.dry_run else "Synced"
    print(f"{GREEN}{CHECK}{RESET} {verb} {stats['total']} sims")
    if stats['comments_inserted']:
        verb2 = "Would insert" if args.dry_run else "Inserted"
        print(f"  {verb2} CANVAS_HEIGHT comment in {stats['comments_inserted']} JS files")
    if stats['iframes_updated']:
        verb3 = "Would update" if args.dry_run else "Updated"
        print(f"  {verb3} {stats['iframes_updated']} iframe heights")
    if stats['skipped']:
        print(f"  Skipped {stats['skipped']} (no JS file)")


if __name__ == '__main__':
    main()
