#!/usr/bin/env python3
"""
Equation List Generator

Generates a comprehensive list of all LaTeX equations in an intelligent textbook,
with links to their source locations. This report is useful for verifying that
all equations render correctly.

Usage:
    python generate-equation-list.py [docs_directory] [output_file]

Examples:
    python generate-equation-list.py docs docs/learning-graph/list-equations.md
    python generate-equation-list.py  # Uses defaults: docs and docs/learning-graph/list-equations.md
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Any
from datetime import datetime
from dataclasses import dataclass

# Version of the Equation List Generator
VERSION = "1.0.0"


@dataclass
class Equation:
    """Represents a single equation found in a markdown file."""
    content: str          # The equation content (including delimiters)
    equation_type: str    # 'display' or 'inline'
    file_path: Path       # Path to the source file
    line_number: int      # Line number where equation starts
    chapter_name: str     # Name of the chapter (if in chapters dir)
    chapter_number: int   # Chapter number (0 if not in chapters dir)


class EquationListGenerator:
    """Generates a comprehensive list of all equations in a textbook."""

    # Directories to exclude from scanning
    EXCLUDED_DIRS = {'prompts', 'learning-graph', '.git', '__pycache__', 'site'}

    def __init__(self, docs_dir: str = "docs"):
        """Initialize the equation list generator.

        Args:
            docs_dir: Path to the docs directory (default: "docs")
        """
        self.docs_dir = Path(docs_dir)
        self.chapters_dir = self.docs_dir / "chapters"
        self.learning_graph_dir = self.docs_dir / "learning-graph"

    def _is_excluded_path(self, path: Path) -> bool:
        """Check if a path is in an excluded directory.

        Args:
            path: Path to check

        Returns:
            True if path is in an excluded directory
        """
        try:
            relative_path = path.relative_to(self.docs_dir)
            return any(part in self.EXCLUDED_DIRS for part in relative_path.parts)
        except ValueError:
            return False

    def _get_chapter_info(self, file_path: Path) -> Tuple[int, str]:
        """Extract chapter number and name from file path.

        Args:
            file_path: Path to the markdown file

        Returns:
            Tuple of (chapter_number, chapter_name)
        """
        try:
            relative_path = file_path.relative_to(self.chapters_dir)
            chapter_dir = relative_path.parts[0]

            # Extract chapter number from directory name (e.g., "01-scientific-foundations")
            match = re.match(r'^0*(\d+)-(.+)$', chapter_dir)
            if match:
                chapter_num = int(match.group(1))
                # Convert directory name to title case
                chapter_name = match.group(2).replace('-', ' ').title()

                # Try to get actual title from index.md
                index_file = self.chapters_dir / chapter_dir / "index.md"
                if index_file.exists():
                    actual_title = self._extract_title(index_file)
                    if actual_title:
                        chapter_name = actual_title

                return chapter_num, chapter_name
        except (ValueError, IndexError):
            pass

        return 0, "Other"

    def _extract_title(self, markdown_file: Path) -> str:
        """Extract the first H1 title from a markdown file.

        Args:
            markdown_file: Path to the markdown file

        Returns:
            The title string, or empty string if no title found
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                for line in f:
                    match = re.match(r'^#\s+(.+)$', line.strip())
                    if match:
                        return match.group(1)
        except Exception:
            pass
        return ""

    def _is_valid_equation(self, content: str) -> bool:
        """Check if content looks like a valid LaTeX equation.

        Args:
            content: The inner content of the equation (without delimiters)

        Returns:
            True if it looks like a valid equation
        """
        # Too short to be a real equation
        if len(content) < 2:
            return False

        # If it's just plain text words without any math symbols, it's probably not an equation
        # Valid equations typically contain: =, +, -, *, /, ^, _, \, numbers, Greek letters, etc.
        math_indicators = [
            '=', '+', '-', '*', '/', '^', '_', '\\',  # Common operators and LaTeX commands
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  # Numbers
            'frac', 'sqrt', 'sum', 'int', 'sin', 'cos', 'tan', 'log', 'ln',  # Functions
            'alpha', 'beta', 'gamma', 'delta', 'theta', 'omega', 'pi', 'mu',  # Greek
            'vec', 'text', 'cdot', 'times', 'div', 'pm', 'mp', 'leq', 'geq',  # LaTeX
            'neq', 'approx', 'equiv', 'propto', 'infty', 'partial',
            '(', ')', '[', ']', '{', '}',  # Brackets
        ]

        # Check if content contains any math indicators
        content_lower = content.lower()
        has_math = any(indicator in content_lower for indicator in math_indicators)

        if not has_math:
            return False

        # Filter out common false positives that are just text fragments
        false_positive_patterns = [
            r'^,?\s*(and|or|where|with|for|if|is|are|the|to|in|of|a|an)\s*,?$',  # Just connective words
            r'^[a-z]+\s*-\s*$',  # Word followed by dash
            r'^\s*-\s*$',  # Just a dash
            r'^[A-Za-z\s,]+$',  # Just letters, spaces, and commas (no math symbols)
        ]

        for pattern in false_positive_patterns:
            if re.match(pattern, content, re.IGNORECASE):
                return False

        # If content is mostly text (more than 80% letters/spaces), it's probably not an equation
        alphanumeric_count = sum(1 for c in content if c.isalpha() or c.isspace())
        if len(content) > 10 and alphanumeric_count / len(content) > 0.9:
            # Exception: if it contains backslash commands, it's probably valid LaTeX
            if '\\' not in content:
                return False

        return True

    def extract_equations_from_file(self, markdown_file: Path) -> List[Equation]:
        """Extract all LaTeX equations from a single markdown file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            List of Equation objects
        """
        equations = []

        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return equations

        # Get chapter info
        chapter_num, chapter_name = self._get_chapter_info(markdown_file)

        # Track positions of display math to avoid double-counting
        display_positions = set()

        # Find display math: $$...$$
        for match in re.finditer(r'\$\$([^$]+?)\$\$', content, re.DOTALL):
            start_pos = match.start()
            equation_content = match.group(0)
            inner_content = match.group(1).strip()

            # Calculate line number
            line_number = content[:start_pos].count('\n') + 1

            # Track this position
            display_positions.add((start_pos, match.end()))

            # Display math is usually valid, but still check
            if self._is_valid_equation(inner_content):
                equations.append(Equation(
                    content=inner_content,
                    equation_type='display',
                    file_path=markdown_file,
                    line_number=line_number,
                    chapter_name=chapter_name,
                    chapter_number=chapter_num
                ))

        # Find inline math: $...$
        # Need to exclude display math positions and dollar amounts
        for match in re.finditer(r'\$(?!\d)([^\$]+?)\$', content):
            start_pos = match.start()
            end_pos = match.end()

            # Skip if this is part of a display math block
            is_in_display = False
            for disp_start, disp_end in display_positions:
                if disp_start <= start_pos < disp_end:
                    is_in_display = True
                    break

            if is_in_display:
                continue

            inner_content = match.group(1).strip()

            # Validate that this looks like a real equation
            if not self._is_valid_equation(inner_content):
                continue

            # Calculate line number
            line_number = content[:start_pos].count('\n') + 1

            equations.append(Equation(
                content=inner_content,
                equation_type='inline',
                file_path=markdown_file,
                line_number=line_number,
                chapter_name=chapter_name,
                chapter_number=chapter_num
            ))

        return equations

    def extract_all_equations(self) -> List[Equation]:
        """Extract all equations from all markdown files in docs.

        Returns:
            List of all Equation objects, sorted by chapter then line number
        """
        all_equations = []

        # Search all markdown files in docs directory
        for md_file in self.docs_dir.rglob('*.md'):
            if self._is_excluded_path(md_file):
                continue
            equations = self.extract_equations_from_file(md_file)
            all_equations.extend(equations)

        # Sort by chapter number, then by file path, then by line number
        all_equations.sort(key=lambda e: (e.chapter_number, str(e.file_path), e.line_number))

        return all_equations

    def generate_equation_list_md(self) -> str:
        """Generate the list-equations.md content.

        Returns:
            Markdown content as string
        """
        equations = self.extract_all_equations()

        # Get current timestamp
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

        # Count statistics
        total_equations = len(equations)
        display_count = sum(1 for e in equations if e.equation_type == 'display')
        inline_count = sum(1 for e in equations if e.equation_type == 'inline')

        # Build markdown
        md = "# Equation List\n\n"
        md += f"**Generated by**: Equation List Generator v{VERSION}  \n"
        md += f"**Generated on**: {timestamp}\n\n"
        md += "This file lists all LaTeX equations in the textbook for verification that they render correctly.\n\n"

        # Summary statistics
        md += "## Summary\n\n"
        md += f"| Metric | Count |\n"
        md += f"|--------|-------|\n"
        md += f"| Total Equations | {total_equations} |\n"
        md += f"| Display Equations (`$$...$$`) | {display_count} |\n"
        md += f"| Inline Equations (`$...$`) | {inline_count} |\n\n"

        # Group equations by chapter
        chapters: Dict[int, List[Equation]] = {}
        for eq in equations:
            if eq.chapter_number not in chapters:
                chapters[eq.chapter_number] = []
            chapters[eq.chapter_number].append(eq)

        # Generate sections for each chapter
        md += "## Equations by Chapter\n\n"

        for chapter_num in sorted(chapters.keys()):
            chapter_equations = chapters[chapter_num]
            if not chapter_equations:
                continue

            # Get chapter name from first equation
            chapter_name = chapter_equations[0].chapter_name

            if chapter_num == 0:
                md += f"### Other Content\n\n"
            else:
                md += f"### Chapter {chapter_num}: {chapter_name}\n\n"

            # Count equations in this chapter
            ch_display = sum(1 for e in chapter_equations if e.equation_type == 'display')
            ch_inline = sum(1 for e in chapter_equations if e.equation_type == 'inline')
            md += f"*{len(chapter_equations)} equations ({ch_display} display, {ch_inline} inline)*\n\n"

            # Create table of equations
            md += "| # | Type | Equation | Source |\n"
            md += "|---|------|----------|--------|\n"

            for i, eq in enumerate(chapter_equations, 1):
                # Create relative path for link
                try:
                    relative_path = eq.file_path.relative_to(self.docs_dir)
                    # Convert to URL-friendly path (for mkdocs)
                    # Keep the .md extension for proper MkDocs link resolution
                    url_path = str(relative_path).replace('\\', '/')
                    source_link = f"[Line {eq.line_number}](../{url_path})"
                except ValueError:
                    source_link = f"Line {eq.line_number}"

                # Format equation type
                eq_type = "Display" if eq.equation_type == 'display' else "Inline"

                # Format equation content for table
                # Escape pipe characters and limit length for readability
                eq_content = eq.content.replace('|', '\\|').replace('\n', ' ')

                # Wrap in appropriate delimiters for rendering
                if eq.equation_type == 'display':
                    eq_display = f"$${eq_content}$$"
                else:
                    eq_display = f"${eq_content}$"

                # Truncate very long equations for the table
                if len(eq_display) > 100:
                    eq_display = eq_display[:97] + "..."

                md += f"| {i} | {eq_type} | {eq_display} | {source_link} |\n"

            md += "\n"

        # Add usage notes
        md += "## Usage Notes\n\n"
        md += "- **Display equations** (`$$...$$`) are rendered on their own line, centered\n"
        md += "- **Inline equations** (`$...$`) are rendered within text\n"
        md += "- Click the source link to navigate to the equation in context\n"
        md += "- If an equation doesn't render correctly, check for:\n"
        md += "  - Missing or mismatched delimiters\n"
        md += "  - Invalid LaTeX syntax\n"
        md += "  - Special characters that need escaping\n"

        return md

    def generate_report(self, output_file: Path = None):
        """Generate the equation list report.

        Args:
            output_file: Path to write the report (defaults to learning-graph/list-equations.md)
        """
        if output_file is None:
            output_file = self.learning_graph_dir / "list-equations.md"

        # Create output directory if it doesn't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Generate content
        content = self.generate_equation_list_md()

        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Generated {output_file}")

        # Print summary
        equations = self.extract_all_equations()
        print(f"\n📊 Found {len(equations)} equations:")
        print(f"   - Display equations: {sum(1 for e in equations if e.equation_type == 'display')}")
        print(f"   - Inline equations: {sum(1 for e in equations if e.equation_type == 'inline')}")


def main():
    """Main entry point."""
    import sys

    # Get docs directory from command line or use default
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else "docs"

    # Get output file from command line or use default
    output_file = None
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])

    # Check if docs directory exists
    if not Path(docs_dir).exists():
        print(f"❌ Error: Directory '{docs_dir}' does not exist")
        sys.exit(1)

    # Generate report
    generator = EquationListGenerator(docs_dir)
    generator.generate_report(output_file)

    print(f"\n✅ Equation list generation v{VERSION} complete!")


if __name__ == "__main__":
    main()
