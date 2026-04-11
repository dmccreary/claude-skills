#!/usr/bin/env python3
"""
Scaffold MicroSim directories from TODO JSON specification files.

For each docs/sims/TODO/<sim-id>.json that does NOT already have a
docs/sims/<sim-id>/main.html, create a new directory with stub files:
  - main.html       (placeholder canvas + spec embedded as a comment)
  - index.md        (frontmatter, learning objective, iframe embed, spec)
  - metadata.json   (mapped from the TODO JSON)

Usage:
    python scaffold-microsims-from-todo.py [--project-dir /path/to/project] [--force]

--force overwrites existing scaffold files (but never main.html if it
already exists, since that may contain a real implementation).
"""

import argparse
import glob
import json
import os
import sys
from datetime import date


def find_project_root(start_path):
    current = os.path.abspath(start_path)
    while True:
        if os.path.isfile(os.path.join(current, "mkdocs.yml")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f8f9fa;
            color: #212529;
        }}
        #container {{
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: white;
        }}
        h1 {{
            font-size: 22px;
            margin-bottom: 10px;
            color: #1a3a6c;
        }}
        .placeholder {{
            border: 2px dashed #adb5bd;
            border-radius: 8px;
            padding: 40px 20px;
            text-align: center;
            color: #6c757d;
            margin: 20px 0;
            min-height: 400px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .placeholder .badge {{
            display: inline-block;
            background: #ffc107;
            color: #212529;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 12px;
        }}
        .placeholder h2 {{
            font-size: 18px;
            color: #495057;
            margin-bottom: 8px;
        }}
        .placeholder p {{
            font-size: 14px;
            max-width: 480px;
        }}
        .meta {{
            margin-top: 20px;
            font-size: 13px;
            color: #6c757d;
            border-top: 1px solid #dee2e6;
            padding-top: 12px;
        }}
        .meta strong {{ color: #495057; }}
    </style>
</head>
<body>
    <div id="container">
        <h1>{title}</h1>
        <div class="placeholder">
            <span class="badge">SCAFFOLD</span>
            <h2>MicroSim Not Yet Implemented</h2>
            <p>This MicroSim has been scaffolded from its specification but the
            interactive content has not been built yet. See the chapter source
            and the <code>index.md</code> in this directory for the full spec.</p>
        </div>
        <div class="meta">
            <p><strong>Sim ID:</strong> {sim_id}</p>
            <p><strong>Library:</strong> {library}</p>
            <p><strong>Bloom Level:</strong> {bloom_level}</p>
            <p><strong>Learning Objective:</strong> {learning_objective}</p>
        </div>
    </div>

    <!--
    SPECIFICATION (from chapter index.md):

{spec_block}
    -->
</body>
</html>
"""


INDEX_MD_TEMPLATE = """---
title: {title}
description: {description}
status: scaffold
library: {library}
bloom_level: {bloom_level}
---

# {title}

!!! warning "Scaffold"
    This MicroSim has been scaffolded from its specification. The interactive
    implementation has not been built yet.

## Learning Objective

{learning_objective}

- **Bloom Level:** {bloom_level}
- **Bloom Verb:** {bloom_verb}
- **Library:** {library}

## Preview

<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){{ .md-button .md-button--primary }}

## Specification

The full specification below is extracted from
[Chapter {chapter_number}: {chapter_title}](../../chapters/{chapter_dir}/index.md).

```text
{specification}
```

## Related Resources

- [Chapter {chapter_number}: {chapter_title}](../../chapters/{chapter_dir}/index.md)
"""


def make_metadata(spec):
    return {
        "title": spec["diagram_name"],
        "description": (spec.get("learning_objective") or spec["diagram_name"]),
        "creator": "Dementia Education Project",
        "date": str(date.today()),
        "subject": ["dementia"],
        "type": "Interactive Simulation",
        "format": "text/html",
        "language": "en-US",
        "rights": "CC BY 4.0",
        "identifier": spec["sim_id"],
        "library": spec.get("library") or "TBD",
        "bloomLevel": spec.get("bloom_level") or "TBD",
        "bloomVerb": spec.get("bloom_verb") or "TBD",
        "completion_status": "scaffold",
        "chapter_number": spec.get("chapter_number"),
        "chapter_title": spec.get("chapter_title"),
        "chapter_dir": spec.get("chapter_dir"),
    }


def indent_block(text, indent="    "):
    return "\n".join(indent + line for line in text.splitlines())


def scaffold_one(spec, sims_dir, force=False):
    sim_id = spec["sim_id"]
    sim_dir = os.path.join(sims_dir, sim_id)
    main_html = os.path.join(sim_dir, "main.html")
    index_md = os.path.join(sim_dir, "index.md")
    meta_json = os.path.join(sim_dir, "metadata.json")

    # If main.html already exists, the sim is implemented; skip entirely.
    if os.path.isfile(main_html):
        return "skipped-implemented"

    os.makedirs(sim_dir, exist_ok=True)

    title = spec["diagram_name"]
    library = spec.get("library") or "TBD"
    bloom_level = spec.get("bloom_level") or "TBD"
    bloom_verb = spec.get("bloom_verb") or "TBD"
    learning_objective = spec.get("learning_objective") or "TBD"
    description = (spec.get("learning_objective") or title).split("\n")[0]
    specification = spec.get("specification") or ""

    html_out = HTML_TEMPLATE.format(
        title=title,
        sim_id=sim_id,
        library=library,
        bloom_level=bloom_level,
        learning_objective=learning_objective,
        spec_block=indent_block(specification, "    "),
    )

    md_out = INDEX_MD_TEMPLATE.format(
        title=title,
        description=description,
        library=library,
        bloom_level=bloom_level,
        bloom_verb=bloom_verb,
        learning_objective=learning_objective,
        chapter_number=spec.get("chapter_number") or "?",
        chapter_title=spec.get("chapter_title") or "",
        chapter_dir=spec.get("chapter_dir") or "",
        specification=specification,
    )

    # Write main.html (we know it doesn't exist - early return above)
    with open(main_html, "w", encoding="utf-8") as f:
        f.write(html_out)

    # index.md - write if missing or force
    if force or not os.path.isfile(index_md):
        with open(index_md, "w", encoding="utf-8") as f:
            f.write(md_out)

    # metadata.json - write if missing or force
    if force or not os.path.isfile(meta_json):
        with open(meta_json, "w", encoding="utf-8") as f:
            json.dump(make_metadata(spec), f, indent=2, ensure_ascii=False)

    return "scaffolded"


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold MicroSim directories from TODO JSON specs."
    )
    parser.add_argument(
        "--project-dir",
        help="Path to the project root (containing mkdocs.yml). Auto-detected if omitted.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing index.md and metadata.json (never overwrites main.html).",
    )
    args = parser.parse_args()

    if args.project_dir:
        project_root = os.path.abspath(args.project_dir)
    else:
        project_root = find_project_root(os.path.dirname(os.path.abspath(__file__)))

    if not project_root or not os.path.isfile(os.path.join(project_root, "mkdocs.yml")):
        print("ERROR: Could not find project root (no mkdocs.yml found).", file=sys.stderr)
        sys.exit(1)

    sims_dir = os.path.join(project_root, "docs", "sims")
    todo_dir = os.path.join(sims_dir, "TODO")

    if not os.path.isdir(todo_dir):
        print(f"ERROR: TODO directory not found: {todo_dir}", file=sys.stderr)
        sys.exit(1)

    todo_files = sorted(glob.glob(os.path.join(todo_dir, "*.json")))

    scaffolded = 0
    skipped = 0
    for todo_path in todo_files:
        with open(todo_path, "r", encoding="utf-8") as f:
            spec = json.load(f)
        result = scaffold_one(spec, sims_dir, force=args.force)
        if result == "scaffolded":
            scaffolded += 1
            print(f"  scaffolded: {spec['sim_id']}")
        else:
            skipped += 1
            print(f"  skipped (already implemented): {spec['sim_id']}")

    print()
    print(f"Project root: {project_root}")
    print(f"TODO specs processed: {len(todo_files)}")
    print(f"Scaffolded: {scaffolded}")
    print(f"Skipped (already implemented): {skipped}")


if __name__ == "__main__":
    main()
