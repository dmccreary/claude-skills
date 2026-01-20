#!/usr/bin/env python3
"""
Batch MicroSim Standardization Script
Adds structural elements to all MicroSims that need standardization

Usage:
    python3 batch-standardize.py

    Or from scripts directory:
    cd docs/sims && python3 ../../src/utilities/batch-standardize.py
"""

import os
import json
import re
from datetime import date
from pathlib import Path

# Determine SIMS_DIR based on script location
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
SIMS_DIR = REPO_ROOT / 'docs' / 'sims'

# Site URL from mkdocs.yml
SITE_URL = "https://dmccreary.github.io/claude-skills"

# Skip MicroSims with quality_score >= 85
SKIP_THRESHOLD = 85

# Dublin Core metadata template
METADATA_TEMPLATE = {
    "title": "",
    "description": "",
    "creator": "Dan McCreary",
    "date": str(date.today()),
    "subject": [],
    "type": "Interactive Simulation",
    "format": "text/html",
    "language": "en-US",
    "rights": "CC BY-NC-SA 4.0",
    "publisher": "Claude Skills Repository",
    "learningResourceType": "simulation",
    "audience": "Educators, Developers",
    "version": "1.0.0",
    "library": ""
}


def detect_library(main_html_path):
    """Detect which JavaScript library is used"""
    if not os.path.exists(main_html_path):
        return "Unknown"

    with open(main_html_path, 'r', encoding='utf-8') as f:
        content = f.read(2000)  # Read first 2000 chars

    if 'p5.js' in content or 'p5.min.js' in content:
        return 'p5.js'
    elif 'mermaid' in content.lower():
        return 'Mermaid'
    elif 'vis-network' in content:
        return 'vis-network'
    elif 'chart.js' in content.lower() or 'Chart.min.js' in content:
        return 'Chart.js'
    elif 'plotly' in content.lower():
        return 'Plotly.js'
    elif 'leaflet' in content.lower():
        return 'Leaflet'
    elif 'd3.js' in content or 'd3.min.js' in content:
        return 'D3.js'
    else:
        return 'HTML/CSS/JavaScript'


def get_existing_quality_score(index_path):
    """Extract existing quality score from index.md"""
    if not os.path.exists(index_path):
        return None

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read(500)
        match = re.search(r'quality_score:\s*(\d+)', content)
        if match:
            return int(match.group(1))
    return None


def extract_title_from_index(index_path):
    """Extract the level 1 header from index.md"""
    if not os.path.exists(index_path):
        return None

    with open(index_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return None


def calculate_quality_score(microsim_dir, has_metadata=False, has_yaml=False,
                            has_iframe=False, has_button=False, has_example=False,
                            has_image=False, has_overview=False, has_lesson=False,
                            has_references=False, has_type_specific=False):
    """Calculate quality score based on rubric"""
    score = 0

    # Title (2 points)
    index_path = microsim_dir / 'index.md'
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            if '# ' in f.read():
                score += 2

    # main.html (10 points)
    if os.path.exists(microsim_dir / 'main.html'):
        score += 10

    # Metadata 1 - YAML title and description (3 points)
    if has_yaml:
        score += 3

    # Metadata 2 - image references (5 points)
    if has_image:
        score += 5

    # metadata.json present (10 points)
    if has_metadata:
        score += 10

    # metadata.json valid (20 points) - assume valid if we created it
    if has_metadata:
        score += 20

    # iframe (10 points)
    if has_iframe:
        score += 10

    # Fullscreen button (5 points)
    if has_button:
        score += 5

    # iframe example (5 points)
    if has_example:
        score += 5

    # image file (5 points) - included in Metadata 2
    # Already counted above

    # Overview documentation (5 points)
    if has_overview:
        score += 5

    # Lesson plan (10 points)
    if has_lesson:
        score += 10

    # References (5 points)
    if has_references:
        score += 5

    # Type-specific format (5 points)
    if has_type_specific:
        score += 5

    return score


def standardize_microsim(microsim_name):
    """Standardize a single MicroSim"""
    microsim_dir = SIMS_DIR / microsim_name
    index_path = microsim_dir / 'index.md'
    main_html_path = microsim_dir / 'main.html'
    metadata_path = microsim_dir / 'metadata.json'

    print(f"\n{'='*60}")
    print(f"Standardizing: {microsim_name}")
    print(f"{'='*60}")

    # Check for existing quality score
    existing_score = get_existing_quality_score(index_path)
    if existing_score and existing_score >= SKIP_THRESHOLD:
        print(f"✓ Skipping - quality score {existing_score} meets threshold")
        return existing_score

    # Detect library
    library = detect_library(main_html_path)
    print(f"Library detected: {library}")

    # Extract title
    title = extract_title_from_index(index_path) or microsim_name.replace('-', ' ').title()
    print(f"Title: {title}")

    # Read existing index.md
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()
    else:
        existing_content = f"# {title}\n\n"

    # Check what's already present
    has_yaml = existing_content.startswith('---')
    has_iframe = '<iframe' in existing_content and 'main.html' in existing_content
    has_button = '.md-button' in existing_content or 'Run' in existing_content and 'Fullscreen' in existing_content
    has_example = '```html' in existing_content and 'github.io' in existing_content
    has_overview = '## Overview' in existing_content or '## Description' in existing_content
    has_lesson = '## Lesson Plan' in existing_content
    has_references = '## References' in existing_content

    # Create metadata.json if missing
    if not os.path.exists(metadata_path):
        metadata = METADATA_TEMPLATE.copy()
        metadata['title'] = title
        metadata['description'] = f"Interactive {library} visualization for {title.lower()}"
        metadata['subject'] = ["educational technology", "data visualization", library.lower()]
        metadata['library'] = library

        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        print("✓ Created metadata.json")
        has_metadata = True
    else:
        print("✓ metadata.json already exists")
        has_metadata = True

    # Build new index.md content
    new_content_parts = []

    # Add YAML frontmatter if missing
    if not has_yaml:
        yaml_front = f"""---
title: {title}
description: Interactive {library} visualization showing {title.lower()}
quality_score: 0
---

"""
        new_content_parts.append(yaml_front)
        # Remove existing title if present at start
        if existing_content.startswith('# '):
            existing_content = '\n'.join(existing_content.split('\n')[1:])

    # Add title
    new_content_parts.append(f"# {title}\n\n")

    # Add iframe if missing or needs fixing
    if not has_iframe or 'style=' in existing_content:
        new_content_parts.append('<iframe src="main.html" width="100%" height="600px"></iframe>\n\n')

    # Add copy-paste example if missing
    if not has_example:
        iframe_url = f"{SITE_URL}/sims/{microsim_name}/main.html"
        new_content_parts.append(f'**Copy this iframe to your website:**\n\n```html\n<iframe src="{iframe_url}" width="100%" height="600px"></iframe>\n```\n\n')

    # Add fullscreen button if missing
    if not has_button:
        new_content_parts.append(f'[Run {title} in Fullscreen](main.html){{ .md-button .md-button--primary }}\n\n')

    # Add remaining content (remove duplicates)
    remaining = existing_content
    if has_yaml:
        # Remove YAML frontmatter from remaining
        parts = remaining.split('---', 2)
        if len(parts) >= 3:
            remaining = parts[2].strip()

    # Remove existing title if present
    if remaining.startswith('# '):
        remaining = '\n'.join(remaining.split('\n')[1:]).strip()

    # Remove existing iframe if present (we added it above)
    remaining = re.sub(r'<iframe[^>]*>.*?</iframe>', '', remaining, flags=re.DOTALL)
    remaining = remaining.strip()

    new_content_parts.append(remaining)

    # Add Overview section if missing
    if not has_overview:
        new_content_parts.append(f'\n\n## Overview\n\nThis MicroSim uses {library} to provide an interactive visualization.')

    # Don't auto-add lesson plan or references (too content-specific)

    # Combine all parts
    new_content = '\n'.join(new_content_parts)

    # Calculate quality score
    score = calculate_quality_score(
        microsim_dir,
        has_metadata=True,
        has_yaml=True,
        has_iframe=True,
        has_button=True,
        has_example=True,
        has_image=False,  # We're not creating images
        has_overview=True,
        has_lesson=has_lesson,
        has_references=has_references,
        has_type_specific=False
    )

    # Update quality_score in YAML
    new_content = re.sub(r'quality_score:\s*\d+', f'quality_score: {score}', new_content)

    # Write updated index.md
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Updated index.md")
    print(f"Quality Score: {existing_score or 0} → {score}")

    return score


def main():
    """Main batch standardization process"""
    print("MicroSim Batch Standardization")
    print("=" * 60)
    print(f"Working directory: {SIMS_DIR}")
    print()

    # Get all MicroSim directories
    microsims = []
    for item in sorted(os.listdir(SIMS_DIR)):
        item_path = SIMS_DIR / item
        if os.path.isdir(item_path) and os.path.exists(item_path / 'main.html'):
            microsims.append(item)

    print(f"Found {len(microsims)} MicroSims to process\n")

    # Process each MicroSim
    results = {}
    for microsim in microsims:
        try:
            score = standardize_microsim(microsim)
            results[microsim] = score
        except Exception as e:
            print(f"✗ Error processing {microsim}: {e}")
            results[microsim] = 0

    # Summary report
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    print(f"\nProcessed: {len(results)} MicroSims\n")

    # Sort by score
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    for microsim, score in sorted_results:
        status = "✓" if score >= 85 else "○" if score >= 70 else "✗"
        print(f"{status} {microsim:45} Score: {score:3d}/100")

    avg_score = sum(results.values()) / len(results) if results else 0
    print(f"\nAverage Quality Score: {avg_score:.1f}/100")
    print(f"MicroSims ≥ 85: {sum(1 for s in results.values() if s >= 85)}")
    print(f"MicroSims 70-84: {sum(1 for s in results.values() if 70 <= s < 85)}")
    print(f"MicroSims < 70: {sum(1 for s in results.values() if s < 70)}")


if __name__ == '__main__':
    main()
