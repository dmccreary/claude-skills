#!/usr/bin/env python3
"""
generate-sim-scaffold.py — Generate MicroSim scaffold files from specs JSON.

Reads the specs JSON produced by extract-sim-specs.py and generates
``main.html``, ``index.md``, and ``metadata.json`` scaffold files.
The agent then only needs to write the ``.js`` file.

Usage:
    python3 generate-sim-scaffold.py --spec-file SPECS.json
        [--sim-id NAME] [--project-dir PATH] [--dry-run] [--force] [--verbose]
"""

import argparse
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import (
    find_project_root, kebab_case, LIBRARY_CDNS, LIBRARY_CSS,
    GREEN, RED, YELLOW, CYAN, BOLD, DIM, RESET, CHECK, CROSS, WARN, ARROW,
)


def _html_template(sim_id, title, library):
    """Generate the main.html content for a given library."""
    cdn = LIBRARY_CDNS.get(library, LIBRARY_CDNS["p5.js"])
    css_cdn = LIBRARY_CSS.get(library, "")

    css_link = ""
    if css_cdn:
        css_link = f'    <link rel="stylesheet" href="{css_cdn}">\n'

    # Determine script tag
    if library == "p5.js":
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'
    elif library in ("vis-network", "vis-timeline", "Leaflet"):
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'
    elif library == "Chart.js":
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'
    elif library == "Mermaid":
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'
    elif library == "Plotly":
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'
    else:
        # Default to p5.js
        cdn = LIBRARY_CDNS["p5.js"]
        script_src = f'    <script src="{cdn}"></script>\n    <script src="{sim_id}.js"></script>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="schema" content="https://dmccreary.github.io/intelligent-textbooks/ns/microsim/v1">
    <title>{title} using {library}</title>
{css_link}    <style>
        body {{ margin: 0px; padding: 0px; font-family: Arial, Helvetica, sans-serif; }}
    </style>
{script_src}
</head>
<body>
    <main></main>
    <br/>
    <a href=".">Back to Lesson Plan</a>
</body>
</html>
"""


def _index_md_template(sim_id, title, library, bloom_level, chapter):
    """Generate the index.md scaffold."""
    display_title = title.replace("-", " ").title() if title == sim_id else title
    today = date.today().isoformat()

    return f"""---
title: {display_title}
description: Interactive {library or 'p5.js'} MicroSim for {display_title.lower()}.
image: /sims/{sim_id}/{sim_id}.png
og:image: /sims/{sim_id}/{sim_id}.png
twitter:image: /sims/{sim_id}/{sim_id}.png
social:
   cards: false
quality_score: 0
---

# {display_title}

<iframe src="main.html" height="450px" width="100%" scrolling="no"></iframe>

[Run the {display_title} MicroSim Fullscreen](./main.html){{ .md-button .md-button--primary }}
<br/>
[Edit in the p5.js Editor](https://editor.p5js.org/)

## About This MicroSim

TODO: Describe what this MicroSim demonstrates.

## How to Use

TODO: Describe how students should interact with this MicroSim.

## Iframe Embed Code

```html
<iframe src="main.html"
        height="450px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
9-12 (High School Geometry)

### Duration
10-15 minutes

### Prerequisites
TODO: List prerequisites.

### Activities

1. **Exploration** (5 min): TODO
2. **Guided Practice** (5 min): TODO
3. **Assessment** (5 min): TODO

### Assessment
TODO: List assessment criteria.

## References

1. TODO: Add references.
"""


def _metadata_json_template(sim_id, title, library, bloom_level, chapter):
    """Generate the metadata.json scaffold."""
    display_title = title.replace("-", " ").title() if title == sim_id else title
    today = date.today().isoformat()

    return json.dumps({
        "title": display_title,
        "creator": "Dan McCreary",
        "subject": "High School Geometry",
        "description": f"Interactive MicroSim for {display_title.lower()}",
        "date": today,
        "educational": {
            "gradeLevel": ["9", "10", "11", "12"],
            "subjectArea": "Mathematics",
            "topic": display_title,
            "learningObjectives": [
                "TODO: Add learning objectives"
            ],
            "bloomsTaxonomy": bloom_level or "Understand",
            "duration": "10-15 minutes",
            "prerequisites": [],
            "standards": []
        },
        "technical": {
            "framework": library or "p5.js",
            "version": "1.0",
            "canvasDimensions": {"width": "responsive", "height": 450},
            "responsive": True,
            "dependencies": [],
            "accessibility": {
                "hasAltText": False,
                "keyboardNavigable": False
            }
        },
        "pedagogical": {
            "teachingStrategy": "Interactive exploration",
            "keyQuestions": [],
            "commonMisconceptions": [],
            "assessmentOpportunities": []
        },
        "chapter": chapter
    }, indent=2) + "\n"


def scaffold_sim(spec, project_dir, dry_run=False, force=False, verbose=False):
    """Create scaffold files for a single sim spec."""
    sim_id = spec["sim_id"]
    title = spec["title"]
    library = spec.get("library", "") or "p5.js"
    bloom = spec.get("bloom_level", "")
    chapter = spec.get("chapter", "")

    sim_dir = os.path.join(project_dir, "docs", "sims", sim_id)

    if verbose:
        print(f"\n{CYAN}{BOLD}{sim_id}{RESET}")
        print(f"  Library: {library}  Bloom: {bloom or 'unset'}  Chapter: {chapter or 'none'}")

    if os.path.isdir(sim_dir) and not force:
        if verbose:
            print(f"  {YELLOW}{WARN} Directory exists, skipping (use --force to overwrite){RESET}")
        return False

    files = {
        "main.html":     _html_template(sim_id, title, library),
        "index.md":      _index_md_template(sim_id, title, library, bloom, chapter),
        "metadata.json": _metadata_json_template(sim_id, title, library, bloom, chapter),
    }

    if dry_run:
        for name in files:
            path = os.path.join(sim_dir, name)
            print(f"  {DIM}[dry-run]{RESET} Would create {path}")
        return True

    os.makedirs(sim_dir, exist_ok=True)
    for name, content in files.items():
        path = os.path.join(sim_dir, name)
        if os.path.exists(path) and not force:
            if verbose:
                print(f"  {YELLOW}{WARN} {name} exists, skipping{RESET}")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        if verbose:
            print(f"  {GREEN}{CHECK}{RESET} Created {name}")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate MicroSim scaffold files from specs JSON."
    )
    parser.add_argument(
        "--spec-file", required=True,
        help="Path to specs JSON from extract-sim-specs.py",
    )
    parser.add_argument(
        "--sim-id", default=None,
        help="Only scaffold this specific sim_id (default: all unscaffolded)",
    )
    parser.add_argument(
        "--project-dir", default=None,
        help="Project root (auto-detect if omitted)",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be created without writing files")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    project_dir = args.project_dir or find_project_root()

    with open(args.spec_file, encoding="utf-8") as f:
        specs = json.load(f)

    if args.sim_id:
        specs = [s for s in specs if s["sim_id"] == args.sim_id]
        if not specs:
            print(f"{RED}{CROSS} sim_id '{args.sim_id}' not found in specs file{RESET}")
            sys.exit(1)

    created = 0
    skipped = 0
    for spec in specs:
        if scaffold_sim(spec, project_dir, dry_run=args.dry_run,
                        force=args.force, verbose=args.verbose):
            created += 1
        else:
            skipped += 1

    mode = "[dry-run] " if args.dry_run else ""
    print(f"\n{GREEN}{CHECK} {mode}Scaffolded: {created}  Skipped: {skipped}  Total: {len(specs)}{RESET}")


if __name__ == "__main__":
    main()
