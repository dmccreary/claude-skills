#!/usr/bin/env python3
"""Crop a full-page MicroSim screenshot down to a legible region for a slide.

Used mainly for the learning-graph viewer screenshot, which is too dense at
full size to read once shrunk into a carousel slide.

Usage:
    python3 crop-screenshot.py <input.png> <output.png> --box LEFT,TOP,RIGHT,BOTTOM

Open the input screenshot first to pick a box that lands on a readable
cluster of labeled nodes with a spread of taxonomy colors.
"""

import argparse
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to the full screenshot")
    parser.add_argument("output", help="Path to write the cropped image")
    parser.add_argument(
        "--box",
        required=True,
        help="Crop box as left,top,right,bottom in pixels",
    )
    args = parser.parse_args()

    box = tuple(int(v) for v in args.box.split(","))
    if len(box) != 4:
        parser.error("--box must have exactly 4 comma-separated values")

    with Image.open(args.input) as img:
        cropped = img.crop(box)
        cropped.save(args.output)
        print(f"Cropped {args.input} {box} -> {args.output} ({cropped.size[0]}x{cropped.size[1]})")


if __name__ == "__main__":
    main()
