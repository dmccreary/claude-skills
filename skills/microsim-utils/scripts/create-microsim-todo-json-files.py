#!/usr/bin/env python3
"""
Extract unimplemented MicroSim specifications from chapter index.md files
and write a TODO JSON file for each one into docs/sims/TODO/.

Detects diagram specs by looking for "#### Diagram:" headers followed by
an iframe and a <details> block containing a sim-id. Skips any sim-id
that already has a directory under docs/sims/.

Usage:
    python create-microsim-todo-json-files.py [--project-dir /path/to/project]

If --project-dir is omitted, the script walks up from its own location
looking for an mkdocs.yml file.
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import date


def find_project_root(start_path):
    """Walk up from start_path until we find mkdocs.yml."""
    current = os.path.abspath(start_path)
    while True:
        if os.path.isfile(os.path.join(current, "mkdocs.yml")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def extract_field(text, field_name):
    """Extract a field value from the details block text.

    Supports two formats:
      1. Bold markdown: **Field Name:** value
      2. Plain text:    Field Name: value (at start of line)
    """
    # Try bold markdown format first
    pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+?)(?:<br/>|$)"
    match = re.search(pattern, text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    # Fall back to plain-text format (line starts with field name)
    pattern = rf"^{re.escape(field_name)}:\s*(.+)$"
    match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_diagrams_from_chapter(filepath):
    """Parse a chapter index.md and return a list of diagram spec dicts."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract chapter number and title from frontmatter or first heading
    chapter_dir = os.path.basename(os.path.dirname(filepath))
    chapter_match = re.match(r"(\d+)-(.+)", chapter_dir)
    chapter_num = int(chapter_match.group(1)) if chapter_match else 0
    chapter_title_raw = chapter_match.group(2).replace("-", " ").title() if chapter_match else chapter_dir

    # Try to get actual title from frontmatter
    title_match = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
    chapter_title = title_match.group(1).strip() if title_match else chapter_title_raw

    diagrams = []

    # Split on #### Diagram: headers
    diagram_splits = re.split(r"(#### Diagram:\s*.+)", content)

    # Process pairs: header + body
    for i in range(1, len(diagram_splits), 2):
        header_line = diagram_splits[i]
        body = diagram_splits[i + 1] if i + 1 < len(diagram_splits) else ""

        # Extract diagram name from header
        diagram_name_match = re.match(r"#### Diagram:\s*(.+)", header_line)
        if not diagram_name_match:
            continue
        diagram_name = diagram_name_match.group(1).strip()

        # Find the <details> block
        details_match = re.search(
            r"<details[^>]*>(.*?)</details>", body, re.DOTALL
        )
        if not details_match:
            continue
        details_text = details_match.group(1)

        # Extract sim-id: try explicit field first, then derive from iframe src
        sim_id = extract_field(details_text, "sim-id")
        if not sim_id:
            # Derive from iframe src path (e.g. ../../sims/my-sim/main.html -> my-sim)
            iframe_match_id = re.search(r'<iframe\s+src="[^"]*sims/([^/]+)/main\.html"', body)
            if iframe_match_id:
                sim_id = iframe_match_id.group(1)
            else:
                # Last resort: slugify the diagram name
                sim_id = re.sub(r"[^a-z0-9]+", "-", diagram_name.lower()).strip("-")
        if not sim_id:
            continue

        # Extract other fields (supports both bold-markdown and plain-text formats)
        library = extract_field(details_text, "Library") or extract_field(details_text, "Implementation")
        status = extract_field(details_text, "Status")
        bloom_level = extract_field(details_text, "Bloom Level") or extract_field(details_text, "Bloom Taxonomy Level")
        bloom_verb = extract_field(details_text, "Bloom Verb")

        # Extract learning objective (bold or plain-text format)
        lo_match = re.search(
            r"\*\*Learning Objective:\*\*\s*(.+?)(?:\n\n|\n\*\*)",
            details_text,
            re.DOTALL,
        )
        if not lo_match:
            lo_match = re.search(
                r"^Learning Objective:\s*(.+?)(?:\n\n|\n[A-Z])",
                details_text,
                re.DOTALL | re.MULTILINE,
            )
        learning_objective = lo_match.group(1).strip() if lo_match else None

        # Extract the iframe src to see if it references a real path
        iframe_match = re.search(r'<iframe\s+src="([^"]+)"', body)
        iframe_src = iframe_match.group(1) if iframe_match else None

        # Extract the full spec text (everything inside <details>)
        summary_match = re.search(r"<summary>.*?</summary>\s*", details_text, re.DOTALL)
        spec_text = details_text
        if summary_match:
            spec_text = details_text[summary_match.end():].strip()

        diagram = {
            "sim_id": sim_id,
            "diagram_name": diagram_name,
            "chapter_number": chapter_num,
            "chapter_title": chapter_title,
            "chapter_dir": chapter_dir,
            "library": library,
            "status": status,
            "bloom_level": bloom_level,
            "bloom_verb": bloom_verb,
            "learning_objective": learning_objective,
            "iframe_src": iframe_src,
            "completion_status": "specified",
            "specification": spec_text,
        }
        diagrams.append(diagram)

    return diagrams


def main():
    parser = argparse.ArgumentParser(
        description="Extract unimplemented MicroSim specs and create TODO JSON files."
    )
    parser.add_argument(
        "--project-dir",
        help="Path to the project root (containing mkdocs.yml). "
        "Auto-detected if omitted.",
    )
    args = parser.parse_args()

    # Find project root
    if args.project_dir:
        project_root = os.path.abspath(args.project_dir)
    else:
        project_root = find_project_root(os.path.dirname(os.path.abspath(__file__)))

    if not project_root or not os.path.isfile(
        os.path.join(project_root, "mkdocs.yml")
    ):
        print("ERROR: Could not find project root (no mkdocs.yml found).", file=sys.stderr)
        sys.exit(1)

    docs_dir = os.path.join(project_root, "docs")
    sims_dir = os.path.join(docs_dir, "sims")
    todo_dir = os.path.join(sims_dir, "TODO")
    chapters_pattern = os.path.join(docs_dir, "chapters", "*", "index.md")

    # Ensure TODO directory exists
    os.makedirs(todo_dir, exist_ok=True)

    # Collect existing sim directories (already implemented)
    existing_sims = set()
    if os.path.isdir(sims_dir):
        for entry in os.listdir(sims_dir):
            entry_path = os.path.join(sims_dir, entry)
            if os.path.isdir(entry_path):
                # Check if it has a main.html (actually implemented)
                if os.path.isfile(os.path.join(entry_path, "main.html")):
                    existing_sims.add(entry)

    # Also check the DONE directory for previously completed items
    done_dir = os.path.join(sims_dir, "DONE")
    done_sims = set()
    if os.path.isdir(done_dir):
        for entry in os.listdir(done_dir):
            if entry.endswith(".json"):
                done_sims.add(entry.replace(".json", ""))

    # Process all chapter files
    chapter_files = sorted(glob.glob(chapters_pattern))
    all_diagrams = []

    for chapter_file in chapter_files:
        diagrams = extract_diagrams_from_chapter(chapter_file)
        all_diagrams.extend(diagrams)

    # Filter to only unimplemented diagrams
    todo_diagrams = []
    skipped_existing = 0
    for diagram in all_diagrams:
        if diagram["sim_id"] in existing_sims:
            skipped_existing += 1
            continue
        todo_diagrams.append(diagram)

    # Write individual JSON files
    written = 0
    for diagram in todo_diagrams:
        output = {
            "sim_id": diagram["sim_id"],
            "diagram_name": diagram["diagram_name"],
            "chapter_number": diagram["chapter_number"],
            "chapter_title": diagram["chapter_title"],
            "chapter_dir": diagram["chapter_dir"],
            "library": diagram["library"],
            "bloom_level": diagram["bloom_level"],
            "bloom_verb": diagram["bloom_verb"],
            "learning_objective": diagram["learning_objective"],
            "completion_status": diagram["completion_status"],
            "extracted_date": str(date.today()),
            "specification": diagram["specification"],
        }

        filename = f"{diagram['sim_id']}.json"
        output_path = os.path.join(todo_dir, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        written += 1

    # Print summary
    print(f"Project root: {project_root}")
    print(f"Chapters scanned: {len(chapter_files)}")
    print(f"Total diagram specs found: {len(all_diagrams)}")
    print(f"Already implemented (have main.html): {skipped_existing}")
    print(f"TODO JSON files written: {written}")
    print(f"Output directory: {todo_dir}")


if __name__ == "__main__":
    main()
