#!/usr/bin/env python3
"""
Flood-fill white background to transparent.

Starts from the four corners of the image and flood-fills any connected
white-ish pixels (within a configurable tolerance) to fully transparent.
Interior white regions that are not connected to a corner are left intact.

Usage:
    python floodfill-transparent.py input.png [-o output.png] [-t 30]

Options:
    -o, --output    Output file path (default: overwrites input)
    -t, --tolerance Distance from pure white (255,255,255) to still count
                    as "white". Default 30 (catches off-white / JPEG artifacts).
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def floodfill_transparent(image_path: str, output_path: str | None = None,
                          tolerance: int = 30) -> None:
    img = Image.open(image_path).convert("RGBA")
    w, h = img.size

    # Work on a copy of pixel data
    pixels = img.load()

    # Seed points: four corners
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]

    visited = set()
    stack = []

    def is_white_ish(r, g, b, a):
        return (255 - r) + (255 - g) + (255 - b) <= tolerance and a > 0

    # Initialize stack with valid corner seeds
    for sx, sy in seeds:
        r, g, b, a = pixels[sx, sy]
        if is_white_ish(r, g, b, a) and (sx, sy) not in visited:
            stack.append((sx, sy))
            visited.add((sx, sy))

    # Flood fill
    while stack:
        x, y = stack.pop()
        pixels[x, y] = (0, 0, 0, 0)  # fully transparent

        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                visited.add((nx, ny))
                r, g, b, a = pixels[nx, ny]
                if is_white_ish(r, g, b, a):
                    stack.append((nx, ny))

    out = output_path or image_path
    img.save(out)
    print(f"Saved: {out}  ({len(visited)} pixels visited, background removed)")


def main():
    parser = argparse.ArgumentParser(
        description="Flood-fill white background to transparent from corners"
    )
    parser.add_argument("input", help="Input PNG image path")
    parser.add_argument("-o", "--output", default=None,
                        help="Output file path (default: overwrite input)")
    parser.add_argument("-t", "--tolerance", type=int, default=30,
                        help="Color distance from white to treat as background (default: 30)")
    args = parser.parse_args()
    floodfill_transparent(args.input, args.output, args.tolerance)


if __name__ == "__main__":
    main()
