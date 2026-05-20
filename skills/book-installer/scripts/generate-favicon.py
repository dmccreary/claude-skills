"""Generate a multi-resolution favicon.ico from a mascot PNG.

Reads docs/img/mascot/neutral.png (or a path you supply), centers the
visible content on a square canvas, then writes a web-compliant
multi-resolution favicon.ico to docs/img/favicon.ico.

Usage:
    python generate-favicon.py
    python generate-favicon.py --src docs/img/mascot/neutral.png
    python generate-favicon.py --src docs/img/mascot/neutral.png --out docs/img/favicon.ico
    python generate-favicon.py --bg white   # white square background
    python generate-favicon.py --bg transparent  # (default)
    python generate-favicon.py --padding 10  # percent of canvas to pad (default 8)

Requirements:
    pip install Pillow

The .ico output embeds these sizes: 16, 32, 48, 64, 128, 256 pixels.
All six are needed for full cross-platform compatibility (browser tabs,
taskbars, bookmarks, Windows explorer icons).
"""
import argparse
import sys
from pathlib import Path

FAVICON_SIZES = [16, 32, 48, 64, 128, 256]
ALPHA_THRESH = 10   # alpha ≤ this is treated as transparent padding
DEFAULT_SRC = Path("docs/img/mascot/neutral.png")
DEFAULT_OUT = Path("docs/img/favicon.ico")


def find_content_bbox(img):
    """Return (left, upper, right, lower) bounding box of non-transparent pixels."""
    rgba = img.convert("RGBA")
    alpha = rgba.getchannel("A")
    px = alpha.load()
    w, h = rgba.size
    min_x, max_x, min_y, max_y = w, -1, h, -1
    for y in range(h):
        for x in range(w):
            if px[x, y] > ALPHA_THRESH:
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
    if max_x == -1:
        return None  # fully transparent
    return (min_x, min_y, max_x + 1, max_y + 1)


def make_square_canvas(cropped, padding_pct, bg_color):
    """Center cropped image on a square canvas with padding."""
    cw, ch = cropped.size
    content_size = max(cw, ch)
    pad = max(1, int(content_size * padding_pct / 100))
    canvas_size = content_size + 2 * pad

    if bg_color == "white":
        canvas = __import__("PIL.Image", fromlist=["Image"]).Image.new(
            "RGBA", (canvas_size, canvas_size), (255, 255, 255, 255)
        )
    else:
        canvas = __import__("PIL.Image", fromlist=["Image"]).Image.new(
            "RGBA", (canvas_size, canvas_size), (0, 0, 0, 0)
        )

    paste_x = (canvas_size - cw) // 2
    paste_y = (canvas_size - ch) // 2
    canvas.paste(cropped, (paste_x, paste_y), mask=cropped.getchannel("A"))
    return canvas


def generate_favicon(src: Path, out: Path, bg_color: str, padding_pct: int) -> int:
    try:
        from PIL import Image
    except ImportError:
        sys.stderr.write(
            "error: Pillow is not installed.\n"
            "Fix: pip install Pillow\n"
        )
        return 1

    if not src.is_file():
        sys.stderr.write(f"error: source file not found: {src}\n")
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)

    img = Image.open(src).convert("RGBA")
    print(f"source : {src}  ({img.size[0]}x{img.size[1]})")

    bbox = find_content_bbox(img)
    if bbox is None:
        sys.stderr.write("error: the source image appears to be fully transparent\n")
        return 1

    cropped = img.crop(bbox)
    print(f"content: {cropped.size[0]}x{cropped.size[1]} px (after transparent trim)")

    square = make_square_canvas(cropped, padding_pct, bg_color)
    print(f"canvas : {square.size[0]}x{square.size[1]} px (square, {padding_pct}% padding, bg={bg_color})")

    # Pillow's ICO saver takes a list of (w, h) tuples; it downscales from the
    # large canvas for each requested size using high-quality Lanczos resampling.
    ico_sizes = [(s, s) for s in FAVICON_SIZES]
    square.save(
        out,
        format="ICO",
        sizes=ico_sizes,
    )
    print(f"wrote  : {out}  (sizes: {', '.join(str(s) for s in FAVICON_SIZES)})")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Generate favicon.ico from a mascot PNG."
    )
    parser.add_argument(
        "--src",
        type=Path,
        default=DEFAULT_SRC,
        help=f"Source PNG (default: {DEFAULT_SRC})",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output .ico path (default: {DEFAULT_OUT})",
    )
    parser.add_argument(
        "--bg",
        choices=["transparent", "white"],
        default="transparent",
        help="Canvas background (default: transparent)",
    )
    parser.add_argument(
        "--padding",
        type=int,
        default=8,
        metavar="PCT",
        help="Padding as %% of content size (default: 8)",
    )
    args = parser.parse_args()
    sys.exit(generate_favicon(args.src, args.out, args.bg, args.padding))


if __name__ == "__main__":
    main()
