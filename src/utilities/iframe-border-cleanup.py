#!/usr/bin/env python3
"""
iframe-border-cleanup.py

This script processes CSS files to create clean, borderless designs optimized for iframe embedding.
It removes extra padding and margins, sets aliceblue backgrounds, and eliminates decorative borders.

Usage:
    python iframe-border-cleanup.py <css_file_path>
    python iframe-border-cleanup.py --all  # Process all MicroSim CSS files

Author: Generated for Claude Skills project
"""

import re
import sys
import os
from pathlib import Path


def clean_css_rule(css_content, selector, changes):
    """
    Apply CSS property changes to a specific selector.

    Args:
        css_content: The full CSS file content
        selector: CSS selector to modify (e.g., 'body', '.container')
        changes: Dict of property:value pairs to apply

    Returns:
        Modified CSS content
    """
    # Pattern to match the selector and its rule block
    pattern = rf'({re.escape(selector)}\s*{{[^}}]*}})'

    def replace_rule(match):
        rule = match.group(1)

        # Apply each change
        for prop, value in changes.items():
            # Remove existing property if it exists
            rule = re.sub(rf'\s*{re.escape(prop)}:\s*[^;]+;', '', rule)

            # Add the new property before the closing brace
            rule = rule.rstrip('}').rstrip()
            rule += f'\n    {prop}: {value};\n}}'

        return rule

    return re.sub(pattern, replace_rule, css_content, flags=re.DOTALL)


def remove_css_properties(css_content, selector, properties):
    """
    Remove specific CSS properties from a selector.

    Args:
        css_content: The full CSS file content
        selector: CSS selector to modify
        properties: List of property names to remove (e.g., ['border-radius', 'box-shadow'])

    Returns:
        Modified CSS content
    """
    pattern = rf'({re.escape(selector)}\s*{{[^}}]*}})'

    def replace_rule(match):
        rule = match.group(1)

        # Remove each specified property
        for prop in properties:
            rule = re.sub(rf'\s*{re.escape(prop)}:\s*[^;]+;', '', rule)

        return rule

    return re.sub(pattern, replace_rule, css_content, flags=re.DOTALL)


def cleanup_iframe_css(css_file_path, dry_run=False):
    """
    Clean up a CSS file for iframe embedding.

    Modifications:
    - Set body background to aliceblue
    - Remove body padding
    - Set container background to aliceblue
    - Remove container padding, margin, border-radius, box-shadow
    - Set diagram-container background to aliceblue
    - Remove diagram-container padding, margin, border-radius, box-shadow

    Args:
        css_file_path: Path to the CSS file
        dry_run: If True, print changes without modifying file

    Returns:
        True if successful, False otherwise
    """
    css_path = Path(css_file_path)

    if not css_path.exists():
        print(f"Error: CSS file not found: {css_file_path}")
        return False

    print(f"Processing: {css_file_path}")

    # Read the CSS file
    with open(css_path, 'r') as f:
        css_content = f.read()

    original_content = css_content

    # Apply changes to body
    css_content = clean_css_rule(css_content, 'body', {
        'background': 'aliceblue',
        'padding': '0px'
    })

    # Apply changes to .container
    css_content = clean_css_rule(css_content, '.container', {
        'background': 'aliceblue',
        'padding': '0px',
        'margin': '0 auto'
    })

    # Remove decorative properties from .container
    css_content = remove_css_properties(css_content, '.container', [
        'border-radius',
        'box-shadow'
    ])

    # Apply changes to .diagram-container
    css_content = clean_css_rule(css_content, '.diagram-container', {
        'background': 'aliceblue',
        'padding': '0px',
        'margin': '0px'
    })

    # Remove decorative properties from .diagram-container
    css_content = remove_css_properties(css_content, '.diagram-container', [
        'border-radius',
        'box-shadow'
    ])

    if dry_run:
        print("=" * 60)
        print("DRY RUN - Changes that would be made:")
        print("=" * 60)
        print(css_content)
        return True

    # Check if anything changed
    if css_content == original_content:
        print("  No changes needed - file already clean")
        return True

    # Write the modified CSS back to file
    with open(css_path, 'w') as f:
        f.write(css_content)

    print(f"  ✓ Successfully cleaned up {css_file_path}")
    return True


def find_microsim_css_files(base_path="/Users/dan/Documents/ws/claude-skills/docs/sims"):
    """
    Find all style.css files in MicroSim directories.

    Args:
        base_path: Base directory containing MicroSims

    Returns:
        List of CSS file paths
    """
    sims_path = Path(base_path)

    if not sims_path.exists():
        print(f"Error: Sims directory not found: {base_path}")
        return []

    css_files = []
    for sim_dir in sims_path.iterdir():
        if sim_dir.is_dir():
            css_file = sim_dir / "style.css"
            if css_file.exists():
                css_files.append(str(css_file))

    return css_files


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python iframe-border-cleanup.py <css_file_path>")
        print("  python iframe-border-cleanup.py --all")
        print("  python iframe-border-cleanup.py --dry-run <css_file_path>")
        sys.exit(1)

    dry_run = False
    if "--dry-run" in sys.argv:
        dry_run = True
        sys.argv.remove("--dry-run")

    if sys.argv[1] == "--all":
        print("Finding all MicroSim CSS files...")
        css_files = find_microsim_css_files()

        if not css_files:
            print("No CSS files found in MicroSim directories")
            sys.exit(1)

        print(f"Found {len(css_files)} CSS files to process\n")

        success_count = 0
        for css_file in css_files:
            if cleanup_iframe_css(css_file, dry_run):
                success_count += 1
            print()

        print(f"Processed {success_count}/{len(css_files)} files successfully")
    else:
        css_file = sys.argv[1]
        if cleanup_iframe_css(css_file, dry_run):
            sys.exit(0)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
