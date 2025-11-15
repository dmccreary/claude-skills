#!/usr/bin/env python3
"""
Social Media Image Resizer

Resizes images to 1200x630 pixels for optimal social media preview display
(Open Graph, Twitter Cards, LinkedIn, etc.)

Usage:
    python social-media.py input.jpg output.jpg [--mode MODE] [--background COLOR]

Modes:
    - fit: Resize to fit within 1200x630, add letterboxing if needed (default)
    - fill: Resize to fill 1200x630, crop excess from center
    - stretch: Stretch to exactly 1200x630 (may distort aspect ratio)
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps

# Standard social media preview dimensions
TARGET_WIDTH = 1200
TARGET_HEIGHT = 630


def resize_fit(img: Image.Image, bg_color: str = 'white') -> Image.Image:
    """
    Resize image to fit within 1200x630, adding letterboxing/pillarboxing if needed.
    Maintains aspect ratio without cropping.
    """
    # Calculate the aspect ratios
    img_aspect = img.width / img.height
    target_aspect = TARGET_WIDTH / TARGET_HEIGHT

    # Determine scaling factor
    if img_aspect > target_aspect:
        # Image is wider than target - fit to width
        new_width = TARGET_WIDTH
        new_height = int(TARGET_WIDTH / img_aspect)
    else:
        # Image is taller than target - fit to height
        new_height = TARGET_HEIGHT
        new_width = int(TARGET_HEIGHT * img_aspect)

    # Resize the image
    resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Create new image with target dimensions and paste resized image centered
    result = Image.new('RGB', (TARGET_WIDTH, TARGET_HEIGHT), bg_color)
    x_offset = (TARGET_WIDTH - new_width) // 2
    y_offset = (TARGET_HEIGHT - new_height) // 2
    result.paste(resized, (x_offset, y_offset))

    return result


def resize_fill(img: Image.Image) -> Image.Image:
    """
    Resize image to fill 1200x630, cropping excess from center.
    Maintains aspect ratio with center cropping.
    """
    # Calculate the aspect ratios
    img_aspect = img.width / img.height
    target_aspect = TARGET_WIDTH / TARGET_HEIGHT

    # Determine scaling factor
    if img_aspect > target_aspect:
        # Image is wider - scale to height and crop width
        new_height = TARGET_HEIGHT
        new_width = int(TARGET_HEIGHT * img_aspect)
    else:
        # Image is taller - scale to width and crop height
        new_width = TARGET_WIDTH
        new_height = int(TARGET_WIDTH / img_aspect)

    # Resize the image
    resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Crop from center
    left = (new_width - TARGET_WIDTH) // 2
    top = (new_height - TARGET_HEIGHT) // 2
    right = left + TARGET_WIDTH
    bottom = top + TARGET_HEIGHT

    return resized.crop((left, top, right, bottom))


def resize_stretch(img: Image.Image) -> Image.Image:
    """
    Stretch image to exactly 1200x630.
    May distort aspect ratio but no cropping or letterboxing.
    """
    return img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)


def process_image(input_path: str, output_path: str, mode: str = 'fit',
                 bg_color: str = 'white', verbose: bool = False) -> bool:
    """
    Process a single image file.

    Args:
        input_path: Path to input image
        output_path: Path for output image
        mode: Resize mode ('fit', 'fill', or 'stretch')
        bg_color: Background color for 'fit' mode
        verbose: Print detailed information

    Returns:
        True if successful, False otherwise
    """
    try:
        # Open the image
        img = Image.open(input_path)

        if verbose:
            print(f"Input: {input_path}")
            print(f"  Size: {img.width}x{img.height}")
            print(f"  Format: {img.format}")
            print(f"  Mode: {img.mode}")

        # Convert to RGB if necessary (handles RGBA, P, L, etc.)
        if img.mode not in ('RGB', 'L'):
            if verbose:
                print(f"  Converting from {img.mode} to RGB")
            img = img.convert('RGB')

        # Apply resize mode
        if mode == 'fit':
            result = resize_fit(img, bg_color)
        elif mode == 'fill':
            result = resize_fill(img)
        elif mode == 'stretch':
            result = resize_stretch(img)
        else:
            print(f"Error: Unknown mode '{mode}'", file=sys.stderr)
            return False

        # Ensure output directory exists
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the result
        result.save(output_path, 'JPEG', quality=95, optimize=True)

        if verbose:
            print(f"Output: {output_path}")
            print(f"  Size: {result.width}x{result.height}")
            print(f"  Mode: {mode}")
            print("Success!")
        else:
            print(f"Saved: {output_path}")

        return True

    except FileNotFoundError:
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Resize images to 1200x630 for social media previews',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Fit image with white letterboxing
  python social-media.py input.jpg output.jpg

  # Fill image with center crop
  python social-media.py input.jpg output.jpg --mode fill

  # Stretch to fit (may distort)
  python social-media.py input.jpg output.jpg --mode stretch

  # Custom background color for letterboxing
  python social-media.py input.jpg output.jpg --background "#1a73e8"
        """
    )

    parser.add_argument(
        'input',
        help='Input image path'
    )
    parser.add_argument(
        'output',
        help='Output image path'
    )
    parser.add_argument(
        '-m', '--mode',
        choices=['fit', 'fill', 'stretch'],
        default='fit',
        help='Resize mode: fit (letterbox), fill (crop), stretch (distort). Default: fit'
    )
    parser.add_argument(
        '-b', '--background',
        default='white',
        help='Background color for fit mode (name or hex code). Default: white'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed information'
    )

    args = parser.parse_args()

    # Process the image
    success = process_image(
        args.input,
        args.output,
        args.mode,
        args.background,
        args.verbose
    )

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
