#!/usr/bin/env python3
"""
Fix bare URLs in markdown files by wrapping them in backticks.
This prevents mkdocs from trying to validate URLs in conversation logs.
"""

import re
import sys
from pathlib import Path

def fix_urls_in_line(line):
    """
    Fix bare URLs in a line by wrapping them in backticks.
    File path links are handled at the file level to support multiline links.
    """
    # Pattern 1: Fetch(URL) - wrap URL in backticks
    if 'Fetch(' in line and ('http://' in line or 'https://' in line):
        line = re.sub(
            r'Fetch\((https?://[^\)]+)\)',
            r'Fetch(`\1`)',
            line
        )

    # Pattern 2: Bare URLs at end of lines (like "- Added reference #50: https://...")
    if re.search(r':\s+(https?://\S+)\s*$', line):
        line = re.sub(
            r':\s+(https?://\S+)\s*$',
            r': `\1`',
            line
        )

    # Pattern 3: URLs after "it to this blog: " or similar
    if re.search(r'blog:\s+(https?://\S+)', line):
        line = re.sub(
            r'blog:\s+(https?://\S+)',
            r'blog: `\1`',
            line
        )

    # Pattern 4: Standalone "URL" text that appears as an unrecognized link
    if " 'URL'" in line:
        line = line.replace(" 'URL'", " `'URL'`")

    return line

def fix_file(filepath):
    """Fix all URLs in a markdown file."""
    print(f"Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, handle multiline markdown links by joining them
    # Find patterns where a link spans multiple lines
    original_content = content

    # Fix markdown links - wrap them to prevent mkdocs validation
    # Since these are conversation logs, ALL file links should be escaped

    # Fix links with ../ prefix (up directory) - do this first for specificity
    content = re.sub(
        r'(?<!`)\[([^\]]+)\]\((\.\.\/[^\)]+)\)(?!`)',
        lambda m: f'`[{m.group(1)}]({m.group(2)})`',
        content,
        flags=re.DOTALL
    )

    # Fix links with ./ prefix
    content = re.sub(
        r'(?<!`)\[([^\]]+)\]\((\./[^\)]+)\)(?!`)',
        lambda m: f'`[{m.group(1)}]({m.group(2)})`',
        content,
        flags=re.DOTALL
    )

    # Fix multiline markdown links with relative paths: [text\nmore text](path/file.md)
    content = re.sub(
        r'(?<!`)\[([^\]]+)\]\(([a-zA-Z0-9_-][a-zA-Z0-9_/.-]*\.(?:md|html|json))\)(?!`)',
        lambda m: f'`[{m.group(1)}]({m.group(2)})`',
        content,
        flags=re.DOTALL
    )

    # Clean up double and triple backticks
    # `[text](path)`` becomes `[text](path)`
    content = re.sub(r'`\[([^\]]+)\]\(([^\)]+)\)`{2,}', r'`[\1](\2)`', content)
    # ``[text](path)`` becomes `[text](path)`
    content = re.sub(r'`{2,}\[([^\]]+)\]\(([^\)]+)\)`{2,}', r'`[\1](\2)`', content)

    # Now process line by line for other patterns
    lines = content.splitlines(keepends=True)
    fixed_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue

        # Don't modify lines inside code blocks
        if in_code_block:
            fixed_lines.append(line)
            continue

        # Apply other URL fixes
        fixed_line = fix_urls_in_line(line)
        fixed_lines.append(fixed_line)

    final_content = ''.join(fixed_lines)

    changes_made = final_content != original_content

    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"  ✓ Fixed content")
    else:
        print(f"  - No changes needed")

    return 1 if changes_made else 0

def main():
    """Process all markdown files in docs/prompts/"""
    if len(sys.argv) > 1:
        prompts_dir = Path(sys.argv[1])
    else:
        prompts_dir = Path('docs/prompts')

    if not prompts_dir.exists():
        print(f"Error: Directory {prompts_dir} not found")
        sys.exit(1)

    md_files = sorted(prompts_dir.glob('*.md'))

    if not md_files:
        print(f"No markdown files found in {prompts_dir}")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files to process\n")

    total_changes = 0
    for md_file in md_files:
        changes = fix_file(md_file)
        total_changes += changes

    print(f"\n✓ Complete! Fixed {total_changes} total lines across {len(md_files)} files")

if __name__ == '__main__':
    main()
