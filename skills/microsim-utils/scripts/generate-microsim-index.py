#!/usr/bin/env python3
"""Generate the MicroSim index page and a TODO list for missing screenshots.

Scans ``docs/sims/`` for MicroSim subdirectories, reads ``title`` and
``description`` from each ``index.md`` YAML frontmatter block, and writes
``docs/sims/index.md`` as an mkdocs-material grid-card page sorted by title.
MicroSims without a ``<name>/<name>.png`` screenshot are logged to
``docs/sims/TODO.md``.

Usage::

    python3 generate-microsim-index.py                     # course name from mkdocs.yml
    python3 generate-microsim-index.py --course-name "Physics 101"
    python3 generate-microsim-index.py --base-dir docs/sims --dry-run

The course name defaults to ``site_name`` from ``mkdocs.yml``.

Frontmatter handling
--------------------
* A file is treated as having frontmatter ONLY if it opens with ``---`` on line
  one. Splitting unconditionally would treat a ``---`` markdown table rule or
  horizontal rule in the body as a delimiter and corrupt the file on rewrite.
* ``title`` and ``description`` values are read with surrounding quotes stripped
  and written back quoted, so a colon or apostrophe in either can never break
  the YAML. Files are rewritten only when their content actually changes.
"""
import argparse
import os
import re
import sys

# Directories under base_dir that are never MicroSims: scaffolds and shared code.
EXCLUDED_DIRS = {"TODO", "template", "shared-libs"}


def unquote(value):
    """Strip surrounding YAML quotes from a scalar value."""
    value = str(value).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        value = value[1:-1].strip()
    return value


def yaml_quote(value):
    """Wrap a scalar in quotes so colons/apostrophes cannot break the YAML."""
    value = unquote(value)
    if '"' in value:
        return "'" + value.replace("'", "''") + "'"
    return '"' + value + '"'


def split_frontmatter(text):
    """Return ``(frontmatter, body)``, or ``None`` if there is no frontmatter.

    Frontmatter must open with ``---`` on the first line. This guard is what
    keeps a ``|---|---|`` table separator in the body from being mistaken for a
    delimiter.
    """
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None


def get_field(frontmatter, key):
    """Return the unquoted value of ``key``, or None if absent."""
    match = re.search(rf'^{key}:[ \t]*(.*)$', frontmatter, re.MULTILINE)
    if not match:
        return None
    value = unquote(match.group(1))
    return value or None


def set_field(frontmatter, key, value):
    """Set ``key`` to a quoted ``value``, appending it if not already present."""
    quoted = yaml_quote(value)
    match = re.search(rf'^{key}:[ \t]*(.*)$', frontmatter, re.MULTILINE)
    if match:
        return frontmatter[:match.start()] + f"{key}: {quoted}" + frontmatter[match.end():]
    return frontmatter.rstrip("\n") + f"\n{key}: {quoted}"


def read_site_name(mkdocs_path="mkdocs.yml"):
    """Read ``site_name`` from mkdocs.yml to use as the course name."""
    if not os.path.exists(mkdocs_path):
        return None
    with open(mkdocs_path, encoding="utf-8") as handle:
        for line in handle:
            match = re.match(r'^site_name:\s*(.+)$', line)
            if match:
                return unquote(match.group(1))
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-dir", default="docs/sims",
                        help="directory holding the MicroSim subdirectories (default: docs/sims)")
    parser.add_argument("--course-name", default=None,
                        help="course name for the page title (default: site_name from mkdocs.yml)")
    parser.add_argument("--mkdocs", default="mkdocs.yml",
                        help="path to mkdocs.yml (default: mkdocs.yml)")
    parser.add_argument("--dry-run", action="store_true",
                        help="report what would change without writing any files")
    args = parser.parse_args()

    base_dir = args.base_dir
    if not os.path.isdir(base_dir):
        sys.exit(f"error: base directory not found: {base_dir}")

    course_name = args.course_name or read_site_name(args.mkdocs)
    if not course_name:
        sys.exit("error: could not determine the course name -- pass --course-name "
                 "or add site_name to mkdocs.yml")

    sims = []
    missing_screenshots = []
    no_frontmatter = []
    updated_files = []

    for item in sorted(os.listdir(base_dir)):
        sim_dir = os.path.join(base_dir, item)
        if not os.path.isdir(sim_dir) or item in EXCLUDED_DIRS:
            continue

        index_file = os.path.join(sim_dir, "index.md")
        if not os.path.exists(index_file):
            continue

        with open(index_file, encoding="utf-8") as handle:
            content = handle.read()

        split = split_frontmatter(content)
        if split is None:
            # No frontmatter: report it rather than guessing, and never rewrite
            # the file -- the body may contain '---' rules.
            heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            no_frontmatter.append((item, heading.group(1).strip() if heading else None))
            continue

        frontmatter, body = split
        title = get_field(frontmatter, "title") or item
        description = (get_field(frontmatter, "description")
                       or f"Interactive MicroSim for {title.lower()}.")

        # Normalize: ensure title/description are present and quoted. Write only
        # if this actually changes the file, so reruns are no-ops.
        new_frontmatter = set_field(set_field(frontmatter, "title", title),
                                    "description", description)
        if new_frontmatter != frontmatter:
            if not args.dry_run:
                with open(index_file, "w", encoding="utf-8") as handle:
                    handle.write("---\n" + new_frontmatter.strip("\n") + "\n---\n" + body)
            updated_files.append(item)

        sims.append({"name": item, "title": title, "description": description})

        if not os.path.exists(os.path.join(sim_dir, f"{item}.png")):
            missing_screenshots.append(item)

    sims.sort(key=lambda sim: sim["title"].lower())

    index_content = f"""---
title: "List of MicroSims for {course_name}"
description: "A list of all the MicroSims used in the {course_name} course"
image: /sims/index-screen-image.png
og:image: /sims/index-screen-image.png
hide:
    toc
---

# List of MicroSims for {course_name}

Interactive Micro Simulations to help students learn {course_name.lower()} fundamentals.

<div class="grid cards" markdown>

"""
    for sim in sims:
        index_content += f"-   **[{sim['title']}](./{sim['name']}/index.md)**\n\n"
        index_content += f"    ![{sim['title']}](./{sim['name']}/{sim['name']}.png)\n\n"
        index_content += f"    {sim['description']}\n\n"
    index_content += "</div>\n"

    # TODO.md is rewritten every run (not just when something is missing) so it
    # can never keep listing screenshots that have since been captured.
    todo_content = ("# MicroSim Screenshot TODO\n\n"
                    "This file tracks MicroSims that need screenshots captured.\n\n"
                    "## Missing Screenshots\n\n")
    if missing_screenshots:
        todo_content += "Run the following commands to capture missing screenshots:\n\n"
        for item in sorted(missing_screenshots):
            todo_content += (f"### {item}\n```bash\n"
                             f"~/.local/bin/bk-capture-screenshot {base_dir}/{item}\n```\n\n")
    else:
        todo_content += (f"None. All {len(sims)} MicroSims listed in `index.md` have a "
                         "`<name>/<name>.png` screenshot.\n\n"
                         "To capture a screenshot for a new MicroSim:\n\n"
                         "```bash\n~/.local/bin/bk-capture-screenshot "
                         f"{base_dir}/<microsim-name>\n```\n")

    if not args.dry_run:
        with open(os.path.join(base_dir, "index.md"), "w", encoding="utf-8") as handle:
            handle.write(index_content)
        with open(os.path.join(base_dir, "TODO.md"), "w", encoding="utf-8") as handle:
            handle.write(todo_content)

    prefix = "[dry run] " if args.dry_run else ""
    print(f"{prefix}Course name: {course_name}")
    print(f"{prefix}Processed {len(sims)} MicroSims.")
    if updated_files:
        print(f"{prefix}Frontmatter normalized in {len(updated_files)}: {', '.join(updated_files)}")
    print(f"{prefix}Missing screenshots: {len(missing_screenshots)}")
    if missing_screenshots:
        print("   " + ", ".join(sorted(missing_screenshots)))
    if no_frontmatter:
        print(f"{prefix}Skipped -- no YAML frontmatter (add one to include these): "
              f"{len(no_frontmatter)}")
        for name, heading in no_frontmatter:
            print(f"   {name}" + (f'   (H1: "{heading}")' if heading else ""))


if __name__ == "__main__":
    main()
