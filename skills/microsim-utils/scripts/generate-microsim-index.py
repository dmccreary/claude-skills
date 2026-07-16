#!/usr/bin/env python3
"""Generate a MicroSim catalog and screenshot TODO without implicit writes."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MicroSim:
    name: str
    title: str
    description: str
    index_path: Path
    needs_description: bool
    has_screenshot: bool


def resolve_project_root(value: str | None) -> Path:
    root = Path(value).expanduser().resolve() if value else Path.cwd().resolve()
    if not (root / "mkdocs.yml").is_file():
        raise ValueError(
            f"Project root must contain mkdocs.yml: {root}. "
            "Pass --project-dir explicitly when running outside the project root."
        )
    if not (root / "docs" / "sims").is_dir():
        raise ValueError(f"Project root has no docs/sims directory: {root}")
    return root


def read_site_name(root: Path) -> str:
    text = (root / "mkdocs.yml").read_text(encoding="utf-8")
    match = re.search(r"^site_name:\s*[\"']?(.+?)[\"']?\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else root.name.replace("-", " ").title()


def parse_frontmatter(text: str) -> tuple[str, str, str] | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[0], parts[1], parts[2]


def discover_sims(sims_dir: Path) -> list[MicroSim]:
    sims: list[MicroSim] = []
    for sim_dir in sorted(path for path in sims_dir.iterdir() if path.is_dir()):
        index_path = sim_dir / "index.md"
        if sim_dir.name == "TODO" or not (sim_dir / "main.html").is_file() or not index_path.is_file():
            continue
        content = index_path.read_text(encoding="utf-8")
        parsed = parse_frontmatter(content)
        if parsed:
            _, frontmatter, _ = parsed
        else:
            frontmatter = ""
        title_match = re.search(r"^title:\s*(.+)$", frontmatter, re.MULTILINE)
        heading_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = (
            title_match.group(1).strip().strip("\"'")
            if title_match
            else heading_match.group(1).strip()
            if heading_match
            else sim_dir.name.replace("-", " ").title()
        )
        description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        description = (
            description_match.group(1).strip().strip("\"'")
            if description_match
            else f"Interactive MicroSim for {title.lower()}."
        )
        sims.append(
            MicroSim(
                name=sim_dir.name,
                title=title,
                description=description,
                index_path=index_path,
                needs_description=parsed is not None and description_match is None,
                has_screenshot=(sim_dir / f"{sim_dir.name}.png").is_file(),
            )
        )
    return sorted(sims, key=lambda sim: (sim.title.casefold(), sim.name))


def add_description(index_path: Path, description: str) -> None:
    content = index_path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(content)
    if not parsed:
        raise ValueError(f"Cannot add description without YAML frontmatter: {index_path}")
    prefix, frontmatter, body = parsed
    updated = frontmatter.rstrip() + f"\ndescription: {description}\n"
    index_path.write_text(prefix + "---" + updated + "---" + body, encoding="utf-8")


def render_index(course_name: str, sims: list[MicroSim]) -> str:
    lines = [
        "---",
        f"title: List of MicroSims for {course_name}",
        f"description: A list of all the MicroSims used in the {course_name} course",
        "image: /sims/index-screen-image.png",
        "og:image: /sims/index-screen-image.png",
        "hide:",
        "    toc",
        "---",
        "",
        f"# List of MicroSims for {course_name}",
        "",
        f"Interactive Micro Simulations to help students learn {course_name}.",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]
    for sim in sims:
        lines.extend(
            [
                f"-   **[{sim.title}](./{sim.name}/index.md)**",
                "",
                f"    ![{sim.title}](./{sim.name}/{sim.name}.png)",
                "",
                f"    {sim.description}",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_todo(missing: list[MicroSim]) -> str:
    lines = [
        "# MicroSim Screenshot TODO",
        "",
        "This file tracks MicroSims that need screenshots captured.",
        "",
        "## Missing Screenshots",
        "",
        "Run the following commands to capture missing screenshots:",
        "",
    ]
    for sim in missing:
        lines.extend(
            [
                f"### {sim.name}",
                "```bash",
                f"~/.local/bin/bk-capture-screenshot docs/sims/{sim.name}",
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def generate(root: Path, dry_run: bool = False, course_name: str | None = None) -> dict[str, int | str]:
    sims_dir = root / "docs" / "sims"
    sims = discover_sims(sims_dir)
    missing = [sim for sim in sims if not sim.has_screenshot]
    description_updates = [sim for sim in sims if sim.needs_description]
    resolved_course = course_name or read_site_name(root)

    if not dry_run:
        for sim in description_updates:
            add_description(sim.index_path, sim.description)
        (sims_dir / "index.md").write_text(render_index(resolved_course, sims), encoding="utf-8")
        if missing:
            (sims_dir / "TODO.md").write_text(render_todo(missing), encoding="utf-8")

    return {
        "project_root": str(root),
        "course_name": resolved_course,
        "processed": len(sims),
        "missing_screenshots": len(missing),
        "description_updates": len(description_updates),
        "dry_run": str(dry_run).lower(),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate docs/sims/index.md and the missing-screenshot TODO for a validated MkDocs project."
    )
    parser.add_argument(
        "--project-dir",
        help="Project root containing mkdocs.yml and docs/sims. Defaults to the current directory after validation.",
    )
    parser.add_argument("--course-name", help="Override the course name derived from mkdocs.yml site_name.")
    parser.add_argument("--dry-run", action="store_true", help="Report planned work without writing any files.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = resolve_project_root(args.project_dir)
        result = generate(root, dry_run=args.dry_run, course_name=args.course_name)
    except ValueError as error:
        build_parser().error(str(error))
    mode = "Would process" if args.dry_run else "Processed"
    print(f"{mode} {result['processed']} MicroSims in {result['project_root']}.")
    print(f"Missing screenshots: {result['missing_screenshots']}")
    print(f"Descriptions to add: {result['description_updates']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
