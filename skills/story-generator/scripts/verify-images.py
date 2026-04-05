#!/usr/bin/env python3
"""
verify-images.py — Read-only audit tool for graphic novel story images.

Checks that every image referenced by a story's index.md exists on disk and
matches the expected aspect ratio. Reports missing panels, wrong-size files,
and zero-byte files. Exit code 0 on clean, 1 on any issue found.

Usage
-----
    python verify-images.py docs/stories/rene-descartes
    python verify-images.py docs/stories/rene-descartes --aspect-ratio 16:9
    python verify-images.py docs/stories/rene-descartes --min-size 50000

Useful for:
- Pre-commit hooks ("did someone check in a zero-byte PNG?")
- Finding leftover square images from older generation tools
- Sanity-checking that all 13 panels exist after a partial run
- Auditing an entire textbook: find docs/stories -maxdepth 1 -type d | xargs ...
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

SUPPORTED_ASPECT_RATIOS = {
    "21:9", "16:9", "4:3", "3:2", "1:1",
    "9:16", "3:4", "2:3", "5:4", "4:5",
}


def parse_aspect_ratio(value: str) -> float:
    w, h = value.split(":")
    return int(w) / int(h)


def get_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        out = subprocess.check_output(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            text=True,
        )
        w = int(re.search(r"pixelWidth:\s*(\d+)", out).group(1))
        h = int(re.search(r"pixelHeight:\s*(\d+)", out).group(1))
        return w, h
    except Exception:
        return None


def matches_aspect(w: int, h: int, target: float, tol: float = 0.03) -> bool:
    return abs((w / h) - target) / target < tol


def expected_panel_names(index_md: Path) -> list[str]:
    """
    Infer the expected panel filenames from the story's index.md by counting
    image-prompt <details> blocks. First block = cover.png; remaining blocks
    = panel-01.png through panel-NN.png.
    """
    text = index_md.read_text(encoding="utf-8")
    pattern = re.compile(
        r"<details>\s*<summary>([^<]*?Prompt[^<]*?)</summary>",
        re.DOTALL,
    )
    count = sum(1 for m in pattern.finditer(text) if "Image Prompt" in m.group(1))
    if count == 0:
        return []
    names = ["cover.png"]
    for i in range(1, count):
        names.append(f"panel-{i:02d}.png")
    return names


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("story_dir", help="Path to story directory containing index.md")
    ap.add_argument("--aspect-ratio", default="16:9",
                    choices=sorted(SUPPORTED_ASPECT_RATIOS),
                    help="Expected aspect ratio (default: 16:9)")
    ap.add_argument("--min-size", type=int, default=10_000,
                    help="Minimum file size in bytes (default: 10000). "
                         "Files smaller than this are flagged as suspicious.")
    ap.add_argument("--quiet", action="store_true",
                    help="Print only errors, not OK lines")
    args = ap.parse_args()

    story_dir = Path(args.story_dir)
    index_md = story_dir / "index.md"
    if not index_md.exists():
        print(f"ERROR: {index_md} not found", file=sys.stderr)
        return 1

    target_ratio = parse_aspect_ratio(args.aspect_ratio)
    expected = expected_panel_names(index_md)
    if not expected:
        print(f"ERROR: no image prompts found in {index_md}", file=sys.stderr)
        return 1

    issues = 0
    print(f"Verifying {story_dir} against {args.aspect_ratio} "
          f"({len(expected)} expected images)")
    print()

    for name in expected:
        path = story_dir / name
        if not path.exists():
            print(f"  MISSING   {name}")
            issues += 1
            continue
        size = path.stat().st_size
        if size < args.min_size:
            print(f"  TOO SMALL {name}  ({size:,} bytes, expected >= {args.min_size:,})")
            issues += 1
            continue
        dims = get_dimensions(path)
        if dims is None:
            print(f"  UNREADABLE {name}  (sips could not read dimensions)")
            issues += 1
            continue
        w, h = dims
        if not matches_aspect(w, h, target_ratio):
            print(f"  WRONG ASPECT {name}  ({w}x{h}, expected {args.aspect_ratio})")
            issues += 1
            continue
        if not args.quiet:
            print(f"  OK        {name}  ({w}x{h}, {size:,} bytes)")

    # Also report any unexpected files in the directory
    actual_pngs = {p.name for p in story_dir.glob("*.png")}
    expected_set = set(expected)
    extras = actual_pngs - expected_set
    if extras:
        print()
        print(f"  Extra PNG files not referenced in index.md:")
        for name in sorted(extras):
            print(f"    {name}")
        # Extras are a warning, not an error — they might be legitimate
        # (e.g., a preserved -sq.png debugging artifact)

    print()
    if issues == 0:
        print(f"PASS: all {len(expected)} images present and matching {args.aspect_ratio}")
        return 0
    else:
        print(f"FAIL: {issues} issue(s) found")
        return 1


if __name__ == "__main__":
    sys.exit(main())
