#!/usr/bin/env python3
"""
Update index.md YAML metadata with PNG image references
Adds image and og:image fields for MicroSims with screenshots
"""

import os
import re
from pathlib import Path

SIMS_DIR = Path(__file__).parent

def update_yaml_metadata(index_path, microsim_name):
    """Update YAML frontmatter to include image references"""

    if not os.path.exists(index_path):
        print(f"  ✗ index.md not found")
        return False

    # Check if PNG exists
    png_path = index_path.parent / f"{microsim_name}.png"
    if not os.path.exists(png_path):
        print(f"  ○ No PNG file found, skipping")
        return False

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if content has YAML frontmatter
    if not content.startswith('---'):
        print(f"  ✗ No YAML frontmatter found")
        return False

    # Split YAML frontmatter from content
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"  ✗ Invalid YAML frontmatter")
        return False

    yaml_content = parts[1]
    body_content = parts[2]

    # Check if image fields already exist
    has_image = 'image:' in yaml_content
    has_og_image = 'og:image' in yaml_content

    if has_image and has_og_image:
        # Update existing values
        image_path = f"/sims/{microsim_name}/{microsim_name}.png"
        yaml_content = re.sub(r'image:\s*.*', f'image: {image_path}', yaml_content)
        yaml_content = re.sub(r'og:image:\s*.*', f'og:image: {image_path}', yaml_content)
        print(f"  ✓ Updated existing image metadata")
    else:
        # Add new image fields after description
        image_path = f"/sims/{microsim_name}/{microsim_name}.png"
        lines = yaml_content.split('\n')
        new_lines = []
        image_added = False

        for line in lines:
            new_lines.append(line)
            if line.startswith('description:') and not image_added:
                new_lines.append(f'image: {image_path}')
                new_lines.append(f'og:image: {image_path}')
                image_added = True

        yaml_content = '\n'.join(new_lines)
        print(f"  ✓ Added image metadata")

    # Reconstruct the file
    new_content = f"---{yaml_content}---{body_content}"

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def recalculate_quality_score(microsim_dir, microsim_name):
    """Recalculate quality score now that image is present"""
    index_path = microsim_dir / 'index.md'

    if not os.path.exists(index_path):
        return 0

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    score = 0

    # Title (2 points)
    if '# ' in content:
        score += 2

    # main.html (10 points)
    if os.path.exists(microsim_dir / 'main.html'):
        score += 10

    # Metadata 1 - YAML title and description (3 points)
    if 'title:' in content and 'description:' in content:
        score += 3

    # Metadata 2 - image references (5 points)
    if 'image:' in content and 'og:image' in content:
        score += 5

    # metadata.json present (10 points)
    if os.path.exists(microsim_dir / 'metadata.json'):
        score += 10

    # metadata.json valid (20 points) - assume valid
    if os.path.exists(microsim_dir / 'metadata.json'):
        score += 20

    # iframe (10 points)
    if '<iframe' in content and 'main.html' in content:
        score += 10

    # Fullscreen button (5 points)
    if '.md-button' in content:
        score += 5

    # iframe example (5 points)
    if '```html' in content and 'github.io' in content:
        score += 5

    # image file (5 points)
    if os.path.exists(microsim_dir / f'{microsim_name}.png'):
        score += 5

    # Overview documentation (5 points)
    if '## Overview' in content or '## Description' in content:
        score += 5

    # Lesson plan (10 points)
    if '## Lesson Plan' in content:
        score += 10

    # References (5 points)
    if '## References' in content:
        score += 5

    # Type-specific (5 points) - assume no
    # score += 0

    return score


def update_quality_score(index_path, new_score):
    """Update the quality_score field in YAML frontmatter"""

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update quality_score
    new_content = re.sub(r'quality_score:\s*\d+', f'quality_score: {new_score}', content)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    """Main update process"""
    print("Updating Image Metadata in index.md Files")
    print("=" * 60)

    # Get all MicroSim directories
    microsims = []
    for item in sorted(os.listdir(SIMS_DIR)):
        item_path = SIMS_DIR / item
        if os.path.isdir(item_path) and os.path.exists(item_path / 'main.html'):
            microsims.append(item)

    print(f"Found {len(microsims)} MicroSims\n")

    updated_count = 0
    skipped_count = 0

    for microsim in microsims:
        print(f"{microsim}:")
        microsim_dir = SIMS_DIR / microsim
        index_path = microsim_dir / 'index.md'

        # Update YAML metadata
        if update_yaml_metadata(index_path, microsim):
            updated_count += 1

            # Recalculate quality score
            new_score = recalculate_quality_score(microsim_dir, microsim)
            update_quality_score(index_path, new_score)
            print(f"  ✓ Updated quality score to {new_score}")
        else:
            skipped_count += 1

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✓ Updated: {updated_count}")
    print(f"○ Skipped: {skipped_count}")
    print(f"Total: {len(microsims)}")
    print("=" * 60)


if __name__ == '__main__':
    main()
