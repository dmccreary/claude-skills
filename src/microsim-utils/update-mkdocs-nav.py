#!/usr/bin/env python3
"""
update-mkdocs-nav.py — Regenerate the MicroSims nav section in mkdocs.yml.

Scans ``docs/sims/`` for directories that contain ``index.md``, extracts
display titles, and replaces the MicroSims nav block in ``mkdocs.yml``
with an alphabetically sorted list.  Idempotent and safe to run multiple
times.

Usage:
    python3 update-mkdocs-nav.py [--project-dir PATH] [--dry-run] [--verbose]
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import (
    find_project_root, parse_yaml_frontmatter,
    GREEN, RED, YELLOW, CYAN, BOLD, DIM, RESET, CHECK, CROSS, WARN, ARROW,
)


def _extract_title(index_path):
    """Get the display title from an index.md file.

    Priority: frontmatter ``title`` > first ``# Heading`` > directory name.
    """
    with open(index_path, encoding="utf-8") as f:
        content = f.read()

    fm, rest = parse_yaml_frontmatter(content)
    if fm.get("title"):
        return fm["title"]

    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip()

    # Fallback to directory name title-cased
    dirname = os.path.basename(os.path.dirname(index_path))
    return dirname.replace("-", " ").title()


def scan_sims(project_dir, verbose=False):
    """Return a sorted list of (display_title, nav_path) tuples."""
    sims_dir = os.path.join(project_dir, "docs", "sims")
    if not os.path.isdir(sims_dir):
        print(f"{RED}{CROSS} docs/sims/ not found in {project_dir}{RESET}")
        return []

    entries = []
    for name in sorted(os.listdir(sims_dir)):
        index_path = os.path.join(sims_dir, name, "index.md")
        if not os.path.isfile(index_path):
            continue
        title = _extract_title(index_path)
        nav_path = f"sims/{name}/index.md"
        entries.append((title, nav_path))

    # Sort alphabetically by title (case-insensitive)
    entries.sort(key=lambda e: e[0].lower())

    if verbose:
        print(f"{BOLD}Found {len(entries)} MicroSims with index.md{RESET}")

    return entries


def rebuild_nav_section(entries, indent="    "):
    """Build the MicroSims nav YAML lines."""
    lines = []
    lines.append("  - MicroSims:")
    lines.append(f"{indent}- List of MicroSims: sims/index.md")
    for title, path in entries:
        lines.append(f"{indent}- {title}: {path}")
    return lines


def update_mkdocs_yml(project_dir, entries, dry_run=False, verbose=False):
    """Replace the MicroSims nav section in mkdocs.yml."""
    yml_path = os.path.join(project_dir, "mkdocs.yml")
    with open(yml_path, encoding="utf-8") as f:
        original = f.read()

    lines = original.splitlines()

    # Find the MicroSims section boundaries
    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Find "- MicroSims:" at nav level (typically 2-space indent)
        if stripped == "- MicroSims:" and start_idx is None:
            start_idx = i
            continue

        # After finding start, look for the next top-level nav entry
        # (a line matching "  - SomethingElse:" at the same indent level)
        if start_idx is not None and end_idx is None:
            # Check if this is a comment or blank line within the section
            if stripped == "" or stripped.startswith("#"):
                continue
            # Check if it's a child entry (deeper indent, starts with -)
            if line.startswith("    ") and stripped.startswith("-"):
                continue
            # This must be the next top-level nav section
            end_idx = i
            break

    if start_idx is None:
        print(f"{RED}{CROSS} Could not find '- MicroSims:' in mkdocs.yml{RESET}")
        return False

    # If we didn't find an end, it goes to end of file
    if end_idx is None:
        end_idx = len(lines)

    # Also include any blank/comment lines between start and the next section
    # by searching backward from end_idx to skip trailing blanks
    while end_idx > start_idx and lines[end_idx - 1].strip() == "":
        end_idx -= 1
    # Add one blank line back for spacing
    end_idx_for_insert = end_idx

    new_section = rebuild_nav_section(entries)
    new_lines = lines[:start_idx] + new_section + ["", ""] + lines[end_idx_for_insert:]

    new_content = "\n".join(new_lines) + "\n"

    if dry_run:
        # Count differences
        old_count = end_idx - start_idx
        new_count = len(new_section)
        print(f"{DIM}[dry-run]{RESET} Would replace lines {start_idx+1}-{end_idx} "
              f"({old_count} lines) with {new_count} lines")
        print(f"{DIM}[dry-run]{RESET} MicroSims nav entries: {len(entries)}")
        if verbose:
            print(f"\n{CYAN}New MicroSims section:{RESET}")
            for line in new_section[:5]:
                print(f"  {line}")
            print(f"  ... ({len(new_section) - 5} more lines)")
        return True

    with open(yml_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"{GREEN}{CHECK} Updated mkdocs.yml MicroSims section: {len(entries)} entries{RESET}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate the MicroSims nav section in mkdocs.yml."
    )
    parser.add_argument("--project-dir", default=None,
                        help="Project root (auto-detect if omitted)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    project_dir = args.project_dir or find_project_root()

    if args.verbose:
        print(f"{BOLD}Project root:{RESET} {project_dir}")

    entries = scan_sims(project_dir, verbose=args.verbose)
    if not entries:
        print(f"{YELLOW}{WARN} No MicroSims found{RESET}")
        return

    update_mkdocs_yml(project_dir, entries, dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    main()
