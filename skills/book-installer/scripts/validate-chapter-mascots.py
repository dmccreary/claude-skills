#!/usr/bin/env python3
"""Validate mascot admonition placement in a chapter markdown file.

Checks the rules from learning-mascot.md:
- Total count <= 6
- Only one mascot-welcome and one mascot-celebration per chapter
- No two mascot admonitions back-to-back
- Each mascot admonition includes an <img> with class mascot-admonition-img
- Body text is 1-3 sentences (warn if clearly too short or too long)

Usage:
    validate-chapter-mascots.py <path-to-chapter.md>

Exits 0 if clean, 1 if any flags found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

POSE_TYPES = {
    "mascot-welcome",
    "mascot-thinking",
    "mascot-tip",
    "mascot-warning",
    "mascot-encouraging",
    "mascot-encourage",  # legacy name
    "mascot-celebration",
    "mascot-neutral",
}

MAX_TOTAL = 6
SINGLETON_TYPES = {"mascot-welcome", "mascot-celebration"}
ADMONITION_RE = re.compile(r"^!!!\s+(mascot-[a-z]+)\b")
SENTENCE_RE = re.compile(r"[.!?](?:\s|$)")


def parse_admonitions(lines: list[str]) -> list[dict]:
    """Return a list of {type, line, body_lines} for each mascot admonition."""
    admonitions = []
    i = 0
    while i < len(lines):
        m = ADMONITION_RE.match(lines[i])
        if not m:
            i += 1
            continue
        pose = m.group(1)
        if pose not in POSE_TYPES:
            i += 1
            continue
        start_line = i + 1  # 1-based for user-facing reports
        body = []
        j = i + 1
        while j < len(lines):
            line = lines[j]
            if line.strip() == "":
                body.append(line)
                j += 1
                continue
            if line.startswith("    ") or line.startswith("\t"):
                body.append(line)
                j += 1
                continue
            break
        admonitions.append({"type": pose, "line": start_line, "body": body})
        i = j
    return admonitions


def sentence_count(body_text: str) -> int:
    return len(SENTENCE_RE.findall(body_text))


def validate(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    adms = parse_admonitions(lines)

    flags = []

    # Total count
    if len(adms) > MAX_TOTAL:
        flags.append(f"Total mascot admonitions: {len(adms)} (limit is {MAX_TOTAL})")

    # Singleton types
    from collections import Counter
    type_counts = Counter(a["type"] for a in adms)
    for singleton in SINGLETON_TYPES:
        if type_counts.get(singleton, 0) > 1:
            matching = [a["line"] for a in adms if a["type"] == singleton]
            flags.append(
                f"{singleton} appears {type_counts[singleton]} times "
                f"(should be at most 1) — lines {matching}"
            )

    # Back-to-back: any two admonitions with no non-admonition, non-empty
    # content between them
    for a, b in zip(adms, adms[1:]):
        between = lines[a["line"] - 1 + len(a["body"]) : b["line"] - 1]
        has_prose = any(
            line.strip() and not line.startswith("    ") and not line.startswith("\t")
            for line in between
        )
        if not has_prose:
            flags.append(
                f"Back-to-back mascots: {a['type']} (line {a['line']}) "
                f"immediately followed by {b['type']} (line {b['line']}) "
                f"with no prose between them"
            )

    # Per-admonition checks
    for a in adms:
        body_text_lines = [
            ln.strip() for ln in a["body"] if ln.strip() and "<img" not in ln
        ]
        body_text = " ".join(body_text_lines)

        has_img = any(
            "<img" in ln and "mascot-admonition-img" in ln for ln in a["body"]
        )
        if not has_img:
            flags.append(
                f"{a['type']} at line {a['line']}: missing "
                f"<img ... class=\"mascot-admonition-img\"> tag"
            )

        if not body_text:
            flags.append(
                f"{a['type']} at line {a['line']}: no body text "
                f"(admonition is empty or image-only)"
            )
            continue

        sc = sentence_count(body_text)
        if sc == 0:
            flags.append(
                f"{a['type']} at line {a['line']}: body text has no sentence "
                f"terminator (., !, ?)"
            )
        elif sc > 4:
            flags.append(
                f"{a['type']} at line {a['line']}: body text has {sc} sentences "
                f"(target is 1-3)"
            )

    # Report
    print(f"Chapter: {path}")
    print(f"Total mascot admonitions: {len(adms)}")
    if type_counts:
        for pose, count in sorted(type_counts.items()):
            print(f"  {pose}: {count}")
    print()

    if not flags:
        print("OK — no placement rule violations.")
        return 0

    print(f"Found {len(flags)} issue(s):")
    for f in flags:
        print(f"  - {f}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate-chapter-mascots.py <path-to-chapter.md>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 2
    return validate(path)


if __name__ == "__main__":
    sys.exit(main())
