#!/usr/bin/env python3
"""
generate-todo.py — Generate TODO.md for unimplemented MicroSims.

Extracts specs from chapter markdown, cross-references with the filesystem
to find sims that lack a substantive JS file, and writes a compact,
self-contained specification file that Claude can use to generate each sim.

Usage:
    python3 generate-todo.py [--project-dir PATH] [--output FILE] [--verbose]
"""

import argparse
import os
import re
import sys
from collections import OrderedDict
from datetime import date

# Allow running from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import (
    find_project_root, detect_library, parse_yaml_frontmatter,
    GREEN, RED, YELLOW, CYAN, BOLD, DIM, RESET, CHECK, CROSS, WARN, ARROW,
)

# Import the scanning function from extract-sim-specs
from importlib.util import spec_from_file_location, module_from_spec

_this_dir = os.path.dirname(os.path.abspath(__file__))
_spec_mod_spec = spec_from_file_location(
    "extract_sim_specs",
    os.path.join(_this_dir, "extract-sim-specs.py"),
)
_extract_mod = module_from_spec(_spec_mod_spec)
_spec_mod_spec.loader.exec_module(_extract_mod)
scan_chapters = _extract_mod.scan_chapters


# ── Helpers ──────────────────────────────────────────────────────────

def _strip_details_wrapper(spec_text):
    """Remove <details>/<summary>/</details> HTML wrapper, return inner content."""
    if not spec_text:
        return ""
    text = spec_text
    # Remove opening <details markdown="1">
    text = re.sub(r'<details\s+markdown=["\']1["\']\s*>\s*\n?', '', text, count=1)
    # Remove <summary>...</summary>
    text = re.sub(r'<summary>.*?</summary>\s*\n?', '', text, count=1, flags=re.DOTALL)
    # Remove closing </details>
    text = re.sub(r'\s*</details>\s*$', '', text)
    # Remove **Status:** lines (redundant — everything in TODO is unimplemented)
    text = re.sub(r'\*\*Status:\*\*\s*\S+.*\n?', '', text)
    return text.strip()


def _determine_status(sim_id, sims_dir):
    """Determine the lifecycle status of a sim from the filesystem."""
    sim_path = os.path.join(sims_dir, sim_id)
    if not os.path.isdir(sim_path):
        return "specified"

    html_path = os.path.join(sim_path, "main.html")
    if not os.path.isfile(html_path):
        return "specified"

    # Check for substantive JS (>50 lines)
    try:
        for f in os.listdir(sim_path):
            if f.endswith(".js"):
                jspath = os.path.join(sim_path, f)
                with open(jspath, encoding="utf-8", errors="ignore") as fh:
                    if len(fh.readlines()) > 50:
                        return "implemented"
    except OSError:
        pass

    # Diagram-architecture sims use shared diagram.js + local data.json
    data_json = os.path.join(sim_path, "data.json")
    if os.path.isfile(data_json):
        return "implemented"

    return "scaffolded"


def _bloom_short(bloom):
    """Return short Bloom label like 'Understand (L2)'."""
    levels = {
        "remember": "L1", "understand": "L2", "apply": "L3",
        "analyze": "L4", "evaluate": "L5", "create": "L6",
    }
    if not bloom:
        return ""
    code = levels.get(bloom.lower().split()[0], "")
    if code:
        return f"{bloom} ({code})"
    return bloom


# ── Main generation ──────────────────────────────────────────────────

def generate_todo_md(specs, project_dir, output_path, verbose=False):
    """Generate the TODO.md file from extracted specs."""
    sims_dir = os.path.join(project_dir, "docs", "sims")

    # Annotate each spec with filesystem status
    for spec in specs:
        spec["_fs_status"] = _determine_status(spec["sim_id"], sims_dir)

    # Filter to only unimplemented sims (specified or scaffolded)
    todo_specs = [s for s in specs if s["_fs_status"] in ("specified", "scaffolded")]

    # Sort by chapter (natural sort)
    todo_specs.sort(key=lambda s: s["chapter"])

    total_specs = len(specs)
    remaining = len(todo_specs)

    if verbose:
        print(f"\n{BOLD}Total specs:{RESET} {total_specs}")
        print(f"{BOLD}Remaining (TODO):{RESET} {remaining}")

    # ── Build chapter summary table ──
    chapter_counts = OrderedDict()  # chapter -> {total, done, remaining}
    for spec in specs:
        ch = spec["chapter"]
        if ch not in chapter_counts:
            chapter_counts[ch] = {"total": 0, "done": 0, "remaining": 0}
        chapter_counts[ch]["total"] += 1
        if spec["_fs_status"] in ("specified", "scaffolded"):
            chapter_counts[ch]["remaining"] += 1
        else:
            chapter_counts[ch]["done"] += 1

    # ── Build library summary table ──
    lib_counts = {}
    for spec in todo_specs:
        lib = spec["library"] or "Unknown"
        lib_counts[lib] = lib_counts.get(lib, 0) + 1

    # ── Generate markdown ──
    lines = []
    lines.append("# MicroSim TODO — Remaining Implementations\n")
    lines.append(f"**Generated:** {date.today().isoformat()} | "
                 f"**Remaining:** {remaining} of {total_specs}\n")

    # Chapter summary
    lines.append("## Summary by Chapter\n")
    lines.append("| Chapter | Total | Done | Remaining |")
    lines.append("|---------|-------|------|-----------|")
    for ch in sorted(chapter_counts):
        c = chapter_counts[ch]
        lines.append(f"| {ch} | {c['total']} | {c['done']} | {c['remaining']} |")
    lines.append("")

    # Library summary
    lines.append("## Summary by Library\n")
    lines.append("| Library | Count |")
    lines.append("|---------|-------|")
    for lib in sorted(lib_counts, key=lambda x: -lib_counts[x]):
        lines.append(f"| {lib} | {lib_counts[lib]} |")
    lines.append("")

    lines.append("---\n")

    # ── Individual sim entries ──
    for spec in todo_specs:
        sid = spec["sim_id"]
        lines.append(f"## {sid}\n")
        lines.append(f"- **Title:** {spec['title']}")
        lines.append(f"- **Chapter:** {spec['chapter']}")
        if spec["library"]:
            lines.append(f"- **Library:** {spec['library']}")
        bloom_str = _bloom_short(spec["bloom_level"])
        if bloom_str:
            lines.append(f"- **Bloom:** {bloom_str}")
        lines.append(f"- **Status:** {spec['_fs_status']}")
        lines.append(f"- **Target:** `docs/sims/{sid}/{sid}.js`")
        lines.append("")

        # Spec text
        inner = _strip_details_wrapper(spec["spec_text"])
        if inner:
            lines.append("### Specification\n")
            lines.append(inner)
            lines.append("")

        lines.append("---\n")

    # Write output
    content = "\n".join(lines)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{GREEN}{CHECK} Wrote {remaining} TODO entries to {output_path}{RESET}")
    return remaining


def main():
    parser = argparse.ArgumentParser(
        description="Generate TODO.md for unimplemented MicroSims."
    )
    parser.add_argument(
        "--project-dir", default=None,
        help="Project root (auto-detect if omitted)",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output file path (default: docs/sims/TODO.md)",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    project_dir = args.project_dir or find_project_root()
    output_path = args.output or os.path.join(project_dir, "docs", "sims", "TODO.md")

    if args.verbose:
        print(f"{BOLD}Project root:{RESET} {project_dir}")
        print(f"{BOLD}Output:{RESET} {output_path}")

    specs = scan_chapters(project_dir, verbose=args.verbose)
    generate_todo_md(specs, project_dir, output_path, verbose=args.verbose)


if __name__ == "__main__":
    main()
