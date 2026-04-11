#!/usr/bin/env python3
"""Fix iframe heights in each MicroSim's index.md to match the actual sim height.

Parses JS files to detect canvas/container heights and updates the iframe tag
in each sim's index.md accordingly.

Height detection (in priority order):
  1. // CANVAS_HEIGHT: <int> comment in the JS file — universal source of truth
     for ALL library types (Mermaid, Chart.js, Leaflet, vis-network, p5.js, etc.).
     The iframe height is set to CANVAS_HEIGHT + 2 (2px for the iframe border).
  2. vis-network: container height from JS + 80px for info panel/legend
  3. p5.js: createCanvas() height + 2px, or named height variables + 2px

Usage:
  python3 fix-iframe-heights.py --project-dir /path/to/project --verbose
  python3 fix-iframe-heights.py --project-dir /path/to/project --sim volcano-plot
  python3 fix-iframe-heights.py --project-dir /path/to/project --dry-run
"""
import argparse
import os
import re
import glob
import sys


def detect_height(sim_dir, sim_name):
    """Detect the correct iframe height for a MicroSim by parsing its JS and HTML."""
    js_path = os.path.join(sim_dir, f'{sim_name}.js')
    if not os.path.isfile(js_path):
        return None, 'no JS file'

    with open(js_path) as f:
        js_content = f.read()

    # PRIMARY: Look for the universal `// CANVAS_HEIGHT: <int>` comment.
    # This is the single source of truth for all library types per the
    # microsim-generator skill spec. The iframe height = CANVAS_HEIGHT + 2
    # (2px for the iframe border).
    canvas_height_match = re.search(
        r'^\s*//\s*CANVAS_HEIGHT\s*:\s*(\d+)\s*$',
        js_content,
        re.MULTILINE,
    )
    if canvas_height_match:
        return int(canvas_height_match.group(1)) + 2, 'CANVAS_HEIGHT comment + 2px'

    # Detect library type from main.html
    main_html = os.path.join(sim_dir, 'main.html')
    is_vis = False
    if os.path.isfile(main_html):
        with open(main_html) as f:
            html = f.read()
        if 'vis-network' in html:
            is_vis = True

    if is_vis:
        # vis-network: look for height in JS
        # Common patterns: height:450px, height:'450px', style="...height:450px..."
        h_match = re.search(r"height['\"]?\s*[:=]\s*['\"]?(\d+)", js_content)
        if h_match:
            container_h = int(h_match.group(1))
            return container_h + 80, 'vis-network container + 80px'
        return 530, 'vis-network default'
    else:
        # p5.js: look for createCanvas(width, height)
        canvas_match = re.search(r'createCanvas\s*\(\s*\w+\s*,\s*(\d+)', js_content)
        if canvas_match:
            return int(canvas_match.group(1)) + 2, 'createCanvas height + 2px'

        # Named height variables
        h_var = re.search(
            r'(?:canvasHeight|drawHeight|cHeight)\s*=\s*(\d+)', js_content
        )
        if h_var:
            return int(h_var.group(1)) + 2, 'named height var + 2px'

        # Generic height variable declaration
        h_var2 = re.search(
            r'(?:let|const|var)\s+(?:h|height)\s*=\s*(\d+)', js_content
        )
        if h_var2:
            return int(h_var2.group(1)) + 2, 'generic height var + 2px'

        return None, 'could not detect height from JS'


def fix_sim_height(sim_dir, sim_name, dry_run=False, verbose=False):
    """Fix the iframe height in a single sim's index.md. Returns (old, new) or None."""
    index_path = os.path.join(sim_dir, 'index.md')
    if not os.path.isfile(index_path):
        if verbose:
            print(f'  SKIP {sim_name}: no index.md')
        return None

    height, reason = detect_height(sim_dir, sim_name)
    if height is None:
        if verbose:
            print(f'  SKIP {sim_name}: {reason}')
        return None

    with open(index_path) as f:
        index_content = f.read()

    # Match iframe with height attribute
    iframe_pattern = r'(<iframe\s[^>]*?)height\s*=\s*["\']?(\d+)[px]*["\']?([^>]*>)'
    match = re.search(iframe_pattern, index_content)
    if not match:
        if verbose:
            print(f'  SKIP {sim_name}: no iframe found in index.md')
        return None

    old_height = int(match.group(2))
    if old_height == height:
        if verbose:
            print(f'  OK   {sim_name}: {old_height}px (already correct, {reason})')
        return None

    if not dry_run:
        new_iframe = f'{match.group(1)}height="{height}"{match.group(3)}'
        new_content = (
            index_content[: match.start()] + new_iframe + index_content[match.end() :]
        )
        with open(index_path, 'w') as f:
            f.write(new_content)

    label = 'WOULD FIX' if dry_run else 'FIXED'
    print(f'  {label} {sim_name}: {old_height} → {height}  ({reason})')
    return (old_height, height)


def main():
    parser = argparse.ArgumentParser(
        description='Fix iframe heights in MicroSim index.md files to match JS dimensions.'
    )
    parser.add_argument(
        '--project-dir',
        default=None,
        help='Project root (auto-detect from cwd if omitted)',
    )
    parser.add_argument(
        '--sim', default=None, help='Fix a single sim by name (default: all sims)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show changes without writing files',
    )
    parser.add_argument('--verbose', action='store_true', help='Show all sims, not just changes')
    args = parser.parse_args()

    # Resolve project dir
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
            print('ERROR: mkdocs.yml not found. Use --project-dir.', file=sys.stderr)
            sys.exit(1)

    sims_dir = os.path.join(project_dir, 'docs', 'sims')
    if not os.path.isdir(sims_dir):
        print(f'ERROR: {sims_dir} not found.', file=sys.stderr)
        sys.exit(1)

    if args.sim:
        sim_dirs = [os.path.join(sims_dir, args.sim)]
        if not os.path.isdir(sim_dirs[0]):
            print(f'ERROR: sim directory {sim_dirs[0]} not found.', file=sys.stderr)
            sys.exit(1)
    else:
        sim_dirs = sorted(glob.glob(os.path.join(sims_dir, '*/')))

    changes = 0
    for sim_dir in sim_dirs:
        sim_name = os.path.basename(sim_dir.rstrip('/'))
        result = fix_sim_height(sim_dir, sim_name, dry_run=args.dry_run, verbose=args.verbose)
        if result is not None:
            changes += 1

    action = 'Would update' if args.dry_run else 'Updated'
    print(f'\n{action} {changes} iframe height{"s" if changes != 1 else ""}')


if __name__ == '__main__':
    main()
