#!/usr/bin/env python3
"""
Diagram and MicroSim Report Generator

This script analyzes all chapter markdown files and generates a comprehensive
report of all diagrams and MicroSims, including:
- Chapter number and name
- Diagram/MicroSim title
- Type (diagram or microsim)
- Bloom's Taxonomy level
- Number of UI elements
- Estimated implementation difficulty

The script should be run from the repository home directory. It will automatically
look for docs/chapters/ and output to docs/learning-graph/.

Usage:
    # Run from repository home directory (default paths)
    python diagram-report.py

    # Specify custom paths
    python diagram-report.py --chapters-dir path/to/chapters --output-dir path/to/output

    # Generate different formats
    python diagram-report.py --format html
    python diagram-report.py --format csv

    # Enable verbose output for debugging
    python diagram-report.py -v
"""

import re
import csv
import html as html_lib
import os
import unicodedata
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import argparse


@dataclass
class VisualElement:
    """Represents a diagram or MicroSim in the course"""
    chapter_num: str
    chapter_name: str
    chapter_dir: str  # Directory name for linking
    element_title: str
    element_type: str  # 'diagram' or 'microsim'
    bloom_levels: List[str]
    ui_elements_count: int
    estimated_difficulty: str  # 'Easy', 'Medium', 'Hard', 'Very Hard'
    status: str = ""  # Implementation status
    learning_objective: str = ""
    specifications: str = ""
    source_file: str = ""
    microsim_recommendations: List[Tuple[str, int]] = field(default_factory=list)
    microsim_recommendations_text: str = ""

    def to_dict(self) -> Dict:
        """Convert to dictionary for CSV export"""
        return {
            'Chapter': self.chapter_num,
            'Chapter Name': self.chapter_name,
            'Element Title': self.element_title,
            'Status': self.status,
            'Type': self.element_type.title(),
            'Bloom Levels': ', '.join(self.bloom_levels),
            'UI Keyword Mentions': self.ui_elements_count,
            'Planning Heuristic': self.estimated_difficulty,
            'Learning Objective': self.learning_objective[:100] + '...' if len(self.learning_objective) > 100 else self.learning_objective,
            'MicroSim Recommendations': '; '.join(
                f"{name} ({score})" for name, score in self.microsim_recommendations
            ),
        }


class DiagramAnalyzer:
    """Analyzes markdown files to extract diagram and MicroSim information"""

    # A specification belongs only to the Diagram heading immediately before it.
    HEADER_PATTERN = re.compile(r'^####\s+Diagram:\s*([^\n]+)', re.MULTILINE)
    DETAILS_PATTERN = re.compile(r'<details[^>]*>(.*?)</details>', re.DOTALL)
    SUMMARY_PATTERN = re.compile(r'<summary>(.*?)</summary>', re.DOTALL)
    TYPE_PATTERN = re.compile(r'\*\*Type:\*\*\s*(.*?)(?:\n|\r|\*\*)', re.IGNORECASE)
    BLOOM_PATTERN = re.compile(r'Bloom\'?s Taxonomy[:\s]+(.*?)(?:\)|\.|\n|\r)', re.IGNORECASE)
    LEARNING_OBJ_PATTERN = re.compile(r'\*\*Learning Objective:\*\*\s*(.*?)(?:\n\*\*|\r\n\*\*|\n\n|\r\r)', re.DOTALL | re.IGNORECASE)
    STATUS_PATTERN = re.compile(r'\*\*Status:\*\*\s*(.*?)(?:\n\n|\r\n\r\n|\n\*\*|\r\*\*|\n|\r)', re.IGNORECASE)
    MICROSIM_RECOMMENDATIONS_PATTERN = re.compile(
        r'\*\*MicroSim Generator Recommendations:\*\*\s*(.*?)(?=</details>|$)',
        re.DOTALL | re.IGNORECASE,
    )
    RECOMMENDATION_LINE_PATTERN = re.compile(
        r'\d+\.\s+([a-z0-9-]+)\s+\((\d+)/100\)', re.IGNORECASE
    )

    # UI element keywords to count
    UI_KEYWORDS = [
        'slider', 'button', 'dropdown', 'checkbox', 'input', 'toggle',
        'menu', 'control', 'panel', 'display', 'text box', 'selector'
    ]

    def __init__(self, chapters_dir: str, verbose: bool = False):
        self.chapters_dir = Path(chapters_dir)
        self.elements: List[VisualElement] = []
        self.verbose = verbose
        self.chapter_files: List[Path] = []
        self.errors: List[str] = []

    def discover_chapter_files(self) -> List[Path]:
        """Find numbered chapters in either flat or nested textbook layouts."""
        candidates = sorted(
            (*self.chapters_dir.glob('[0-9][0-9]-*.md'),
             *self.chapters_dir.glob('[0-9][0-9]-*/index.md')),
            key=lambda path: path.relative_to(self.chapters_dir).as_posix(),
        )
        chapter_numbers = {}
        for path in candidates:
            chapter_slug = path.parent.name if path.name == 'index.md' else path.stem
            chapter_number = chapter_slug[:2]
            if chapter_number in chapter_numbers:
                first = chapter_numbers[chapter_number].relative_to(self.chapters_dir)
                second = path.relative_to(self.chapters_dir)
                self.errors.append(
                    f"ambiguous chapter {chapter_number}: both {first} and {second} exist"
                )
            else:
                chapter_numbers[chapter_number] = path
        return candidates

    def analyze_all_chapters(self):
        """Analyze all chapter directories"""
        self.chapter_files = self.discover_chapter_files()

        if self.verbose:
            print(f"\nFound {len(self.chapter_files)} chapter files:")
            for path in self.chapter_files:
                print(f"  - {path.relative_to(self.chapters_dir)}")

        for chapter_file in self.chapter_files:
            self.analyze_chapter_file(chapter_file)

    def analyze_chapter_file(self, file_path: Path):
        """Analyze a single chapter markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            relative_source = file_path.relative_to(self.chapters_dir).as_posix()
            chapter_slug = file_path.parent.name if file_path.name == 'index.md' else file_path.stem
            match = re.match(r'^(\d{2})-(.*)', chapter_slug)
            if match:
                chapter_num = match.group(1)
                chapter_name = match.group(2).replace('-', ' ').title()
            else:
                chapter_num = "??"
                chapter_name = chapter_slug

            headers = list(self.HEADER_PATTERN.finditer(content))

            if self.verbose:
                print(f"\n  Analyzing {relative_source}:")
                print(f"    Found {len(headers)} Diagram headers")

            elements_found = 0
            for index, header in enumerate(headers):
                segment_end = headers[index + 1].start() if index + 1 < len(headers) else len(content)
                segment = content[header.end():segment_end]
                details_blocks = list(self.DETAILS_PATTERN.finditer(segment))
                header_title = header.group(1).strip()
                if len(details_blocks) != 1:
                    self.errors.append(
                        f"{relative_source}: Diagram '{header_title}' has "
                        f"{len(details_blocks)} complete <details> specifications; expected exactly 1"
                    )
                    return
                details_content = details_blocks[0].group(1)
                element = self.parse_details_block(
                    details_content,
                    chapter_num,
                    chapter_name,
                    relative_source,
                    header_title,
                )
                if element:
                    self.elements.append(element)
                    elements_found += 1
                elif self.verbose:
                    print(f"      Skipped: {header_title[:50]}")

            if self.verbose:
                print(f"    Added {elements_found} elements")

        except Exception as e:
            message = f"Error analyzing {file_path}: {e}"
            self.errors.append(message)
            print(message)
            if self.verbose:
                import traceback
                traceback.print_exc()

    def parse_details_block(self, content: str, chapter_num: str, chapter_name: str, source_file: str, header_title: str = None) -> VisualElement:
        """Parse a single <details> block to extract element information"""
        # Use header title if provided, otherwise extract from <summary>
        if header_title:
            title = header_title
        else:
            summary_match = self.SUMMARY_PATTERN.search(content)
            if not summary_match:
                return None
            title = summary_match.group(1).strip()

        # Extract type - be more lenient
        type_match = self.TYPE_PATTERN.search(content)
        if type_match:
            element_type = type_match.group(1).strip().lower()
        else:
            # Try to infer from content
            content_lower = content.lower()
            if 'microsim' in content_lower or 'p5.js' in content_lower or 'p5' in content_lower:
                element_type = 'microsim'
            elif 'diagram' in content_lower:
                element_type = 'diagram'
            else:
                element_type = 'unknown'

        # Normalize type
        if 'microsim' in element_type or 'p5' in element_type:
            element_type = 'microsim'
        elif 'diagram' in element_type:
            element_type = 'diagram'
        elif element_type != 'unknown':
            element_type = 'unknown'

        # Extract Bloom's taxonomy levels
        bloom_levels = self.extract_bloom_levels(content)

        # Extract learning objective
        learning_obj = self.extract_learning_objective(content)

        # Extract status
        status = self.extract_status(content)

        # Extract optional recommendations produced by the MicroSim router.
        microsim_recommendations, microsim_text = self.extract_microsim_recommendations(content)

        # Count UI elements
        ui_count = self.count_ui_elements(content)

        # Estimate difficulty
        difficulty = self.estimate_difficulty(content, ui_count, element_type)

        return VisualElement(
            chapter_num=chapter_num,
            chapter_name=chapter_name,
            chapter_dir=str(Path(source_file).parent),
            element_title=title,
            element_type=element_type,
            bloom_levels=bloom_levels,
            ui_elements_count=ui_count,
            estimated_difficulty=difficulty,
            status=status,
            learning_objective=learning_obj,
            specifications=content[:500],  # Store first 500 chars of specs
            source_file=source_file,
            microsim_recommendations=microsim_recommendations,
            microsim_recommendations_text=microsim_text,
        )

    def extract_bloom_levels(self, content: str) -> List[str]:
        """Extract Bloom's taxonomy levels from content"""
        bloom_match = self.BLOOM_PATTERN.search(content)
        if not bloom_match:
            return ['Not specified']

        bloom_text = bloom_match.group(1)

        # Common Bloom's levels
        levels = []
        if re.search(r'\bremember(?:ing)?\b', bloom_text, re.IGNORECASE):
            levels.append('Remembering')
        if re.search(r'\bunderstand(?:ing)?\b', bloom_text, re.IGNORECASE):
            levels.append('Understanding')
        if re.search(r'\bapply(?:ing)?\b', bloom_text, re.IGNORECASE):
            levels.append('Applying')
        if re.search(r'\banalyz(?:e|ing)\b', bloom_text, re.IGNORECASE):
            levels.append('Analyzing')
        if re.search(r'\bevaluat(?:e|ing)\b', bloom_text, re.IGNORECASE):
            levels.append('Evaluating')
        if re.search(r'\bcreat(?:e|ing)\b', bloom_text, re.IGNORECASE):
            levels.append('Creating')

        return levels if levels else ['Not specified']

    def extract_learning_objective(self, content: str) -> str:
        """Extract learning objective from content"""
        obj_match = self.LEARNING_OBJ_PATTERN.search(content)
        if obj_match:
            return obj_match.group(1).strip().replace('\n', ' ')
        return ""

    def extract_status(self, content: str) -> str:
        """Extract status from content"""
        status_match = self.STATUS_PATTERN.search(content)
        if status_match:
            return status_match.group(1).strip()
        return ""

    def extract_microsim_recommendations(self, content: str) -> Tuple[List[Tuple[str, int]], str]:
        """Extract optional generator recommendations and their scores."""
        recommendations_match = self.MICROSIM_RECOMMENDATIONS_PATTERN.search(content)
        if not recommendations_match:
            return ([], "")

        recommendations_text = recommendations_match.group(1).strip()
        recommendations = [
            (match.group(1), int(match.group(2)))
            for match in self.RECOMMENDATION_LINE_PATTERN.finditer(recommendations_text)
        ]
        return (
            recommendations,
            f"**MicroSim Generator Recommendations:**\n{recommendations_text}",
        )

    def count_ui_elements(self, content: str) -> int:
        """Count the number of UI elements mentioned in specifications"""
        content_lower = content.lower()
        count = 0

        for keyword in self.UI_KEYWORDS:
            # Count occurrences of each keyword
            count += len(re.findall(rf'\b{keyword}s?\b', content_lower))

        return count

    def estimate_difficulty(self, content: str, ui_count: int, element_type: str) -> str:
        """Estimate implementation difficulty based on various factors"""
        content_lower = content.lower()

        # Factors that increase difficulty
        difficulty_score = 0

        # Base score by type
        if element_type == 'microsim':
            difficulty_score += 2  # MicroSims are inherently more complex

        # UI elements
        if ui_count == 0:
            difficulty_score += 1  # Static
        elif ui_count <= 3:
            difficulty_score += 2  # Simple interactivity
        elif ui_count <= 6:
            difficulty_score += 3  # Moderate interactivity
        else:
            difficulty_score += 4  # High interactivity

        # Check for complex features
        complex_features = [
            'animation', 'rotate', 'transform', '3d', 'isometric',
            'graph', 'plot', 'calculation', 'real-time', 'dynamic',
            'comparison', 'overlay', 'multiple panels', 'side-by-side'
        ]

        for feature in complex_features:
            if feature in content_lower:
                difficulty_score += 1

        # Check for canvas size (larger = more complex)
        canvas_match = re.search(r'canvas.*?(\d{3,4})\s*[x×]\s*(\d{3,4})', content_lower)
        if canvas_match:
            width = int(canvas_match.group(1))
            height = int(canvas_match.group(2))
            if width > 900 or height > 700:
                difficulty_score += 1

        # Categorize difficulty
        if difficulty_score <= 3:
            return 'Easy'
        elif difficulty_score <= 6:
            return 'Medium'
        elif difficulty_score <= 9:
            return 'Hard'
        else:
            return 'Very Hard'


class ReportGenerator:
    """Generates reports in various formats"""

    def __init__(
        self,
        elements: List[VisualElement],
        chapters_dir: Path = None,
        output_dir: Path = None,
    ):
        self.elements = elements
        self.chapters_dir = Path(chapters_dir).resolve() if chapters_dir else None
        self.output_dir = Path(output_dir).resolve() if output_dir else None

    @staticmethod
    def markdown_text(value: str) -> str:
        """Escape source text used in generated Markdown tables and links."""
        return (
            value.replace('\\', '\\\\')
            .replace('|', '\\|')
            .replace('[', '\\[')
            .replace(']', '\\]')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('\r\n', '<br>')
            .replace('\n', '<br>')
        )

    @staticmethod
    def markdown_anchor(value: str) -> str:
        """Match Python-Markdown's default heading slug behavior."""
        normalized = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        normalized = re.sub(r'[^\w\s-]', '', normalized.lower())
        return re.sub(r'[-\s]+', '-', normalized).strip('-')

    def chapter_link(self, element: VisualElement) -> str:
        """Build a link for either a flat chapter file or nested index file."""
        anchor = self.markdown_anchor(f"diagram-{element.element_title}")
        if self.chapters_dir and self.output_dir:
            source = self.chapters_dir / element.source_file
            relative_source = Path(os.path.relpath(source, start=self.output_dir)).as_posix()
        else:
            relative_source = f"../chapters/{element.source_file}"
        return f"{relative_source}#{anchor}"

    def generate_markdown_table(self) -> str:
        """Generate Markdown table report"""
        lines = [
            "---",
            "hide:",
            "  - toc",
            "---",
            "",
            "# Diagram and MicroSim Specification Table",
            "",
            f"**Total Specification Blocks:** {len(self.elements)}",
            f"**Diagram Specifications:** {sum(1 for e in self.elements if e.element_type == 'diagram')}",
            f"**MicroSim Specifications:** {sum(1 for e in self.elements if e.element_type == 'microsim')}",
            "",
            "## Summary by Planning Heuristic",
            "",
        ]

        # Count by difficulty
        difficulty_counts = {}
        for element in self.elements:
            difficulty_counts[element.estimated_difficulty] = difficulty_counts.get(element.estimated_difficulty, 0) + 1

        for difficulty in ['Easy', 'Medium', 'Hard', 'Very Hard']:
            count = difficulty_counts.get(difficulty, 0)
            lines.append(f"- **{difficulty}:** {count}")

        lines.extend([
            "",
            "## All Specification Blocks",
            "",
            "| Chapter | Element Title | Status | Type | Bloom Levels | UI Mentions | Planning Heuristic | Recommended MicroSims |",
            "|---------|---------------|--------|------|--------------|-------------|--------------------|-----------------------|"
        ])

        for element in sorted(self.elements, key=lambda e: (e.chapter_num, e.element_title)):
            bloom_str = self.markdown_text(', '.join(element.bloom_levels))
            title = self.markdown_text(element.element_title)
            element_link = f"[{title}]({self.chapter_link(element)})"
            status_display = self.markdown_text(element.status) if element.status else ""
            microsim_str = '<br>'.join(
                f"{self.markdown_text(name)} ({score})"
                for name, score in element.microsim_recommendations
            )
            lines.append(
                f"| {int(element.chapter_num)} | {element_link} | "
                f"{status_display} | {element.element_type.title()} | {bloom_str} | "
                f"{element.ui_elements_count} | {element.estimated_difficulty} | {microsim_str} |"
            )

        return '\n'.join(lines)

    def generate_markdown_details(self) -> str:
        """Generate Markdown details report organized by chapter"""
        lines = [
            "# Diagram and MicroSim Specification Details",
            "",
            f"**Total Specification Blocks:** {len(self.elements)}",
            f"**Diagram Specifications:** {sum(1 for e in self.elements if e.element_type == 'diagram')}",
            f"**MicroSim Specifications:** {sum(1 for e in self.elements if e.element_type == 'microsim')}",
            ""
        ]

        # Group by chapter
        by_chapter = {}
        for element in self.elements:
            key = (element.chapter_num, element.chapter_name, element.chapter_dir)
            if key not in by_chapter:
                by_chapter[key] = []
            by_chapter[key].append(element)

        # Sort chapters by chapter number
        for chapter_key in sorted(by_chapter.keys(), key=lambda x: x[0]):
            chapter_num, chapter_name, chapter_dir = chapter_key
            elements = by_chapter[chapter_key]

            lines.extend([
                f"## Chapter {int(chapter_num)}: {chapter_name}",
                "",
                f"**Total elements:** {len(elements)}",
                ""
            ])

            for element in sorted(elements, key=lambda e: e.element_title):
                title = self.markdown_text(element.element_title)
                lines.append(f"### [{title}]({self.chapter_link(element)})")
                if element.status:
                    lines.append(f"- **Status:** {self.markdown_text(element.status)}")
                lines.append(f"- **Type:** {element.element_type.title()}")
                lines.append(f"- **Bloom's Taxonomy:** {', '.join(element.bloom_levels)}")
                lines.append(f"- **UI keyword mentions:** {element.ui_elements_count}")
                lines.append(f"- **Planning heuristic:** {element.estimated_difficulty}")
                if element.learning_objective:
                    lines.append(f"- **Learning Objective:** {element.learning_objective[:150]}...")
                if element.microsim_recommendations_text:
                    lines.extend(["", element.microsim_recommendations_text])
                lines.append("")

        return '\n'.join(lines)

    def generate_csv(self, output_file: str):
        """Generate CSV format report"""
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Chapter', 'Chapter Name', 'Element Title', 'Status', 'Type',
                         'Bloom Levels', 'UI Keyword Mentions', 'Planning Heuristic', 'Learning Objective',
                         'MicroSim Recommendations']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for element in sorted(self.elements, key=lambda e: (e.chapter_num, e.element_title)):
                writer.writerow(element.to_dict())

    def generate_html(self) -> str:
        """Generate HTML format report"""
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagram and MicroSim Specification Report</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1, h2, h3 { color: #2c3e50; }
        .summary {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .stat-card {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stat-card h3 { margin-top: 0; font-size: 1.1em; color: #7f8c8d; }
        .stat-card .number { font-size: 2em; font-weight: bold; color: #3498db; }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background: #3498db;
            color: white;
            font-weight: 600;
        }
        tr:hover { background: #f8f9fa; }
        .difficulty-easy { color: #27ae60; font-weight: bold; }
        .difficulty-medium { color: #f39c12; font-weight: bold; }
        .difficulty-hard { color: #e74c3c; font-weight: bold; }
        .difficulty-very-hard { color: #c0392b; font-weight: bold; }
        .type-microsim { background: #e8f4fd; }
        .type-diagram { background: #fff5e6; }
        .filter-buttons {
            margin: 20px 0;
        }
        .filter-buttons button {
            padding: 8px 16px;
            margin: 0 5px;
            border: none;
            background: #3498db;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        .filter-buttons button:hover {
            background: #2980b9;
        }
        .filter-buttons button.active {
            background: #27ae60;
        }
    </style>
</head>
<body>
    <h1>Diagram and MicroSim Specification Report</h1>

    <div class="summary">
        <h2>Overview</h2>
        <div class="stats">
"""

        # Calculate statistics
        total = len(self.elements)
        diagrams = sum(1 for e in self.elements if e.element_type == 'diagram')
        microsims = sum(1 for e in self.elements if e.element_type == 'microsim')

        difficulty_counts = {}
        for element in self.elements:
            difficulty_counts[element.estimated_difficulty] = difficulty_counts.get(element.estimated_difficulty, 0) + 1

        html += f"""
            <div class="stat-card">
                <h3>Total Specification Blocks</h3>
                <div class="number">{total}</div>
            </div>
            <div class="stat-card">
                <h3>Diagram Specifications</h3>
                <div class="number">{diagrams}</div>
            </div>
            <div class="stat-card">
                <h3>MicroSim Specifications</h3>
                <div class="number">{microsims}</div>
            </div>
            <div class="stat-card">
                <h3>Easy</h3>
                <div class="number difficulty-easy">{difficulty_counts.get('Easy', 0)}</div>
            </div>
            <div class="stat-card">
                <h3>Medium</h3>
                <div class="number difficulty-medium">{difficulty_counts.get('Medium', 0)}</div>
            </div>
            <div class="stat-card">
                <h3>Hard</h3>
                <div class="number difficulty-hard">{difficulty_counts.get('Hard', 0)}</div>
            </div>
            <div class="stat-card">
                <h3>Very Hard</h3>
                <div class="number difficulty-very-hard">{difficulty_counts.get('Very Hard', 0)}</div>
            </div>
        </div>
    </div>

    <h2>All Specification Blocks</h2>
    <table id="elementsTable">
        <thead>
            <tr>
                <th>Chapter</th>
                <th>Element Title</th>
                <th>Status</th>
                <th>Type</th>
                <th>Bloom Levels</th>
                <th>UI Mentions</th>
                <th>Planning Heuristic</th>
                <th>Recommended MicroSims</th>
            </tr>
        </thead>
        <tbody>
"""

        for element in sorted(self.elements, key=lambda e: (e.chapter_num, e.element_title)):
            bloom_str = html_lib.escape(', '.join(element.bloom_levels))
            difficulty_class = f"difficulty-{element.estimated_difficulty.lower().replace(' ', '-')}"
            type_class = f"type-{element.element_type}"
            recommendations = '<br>'.join(
                f"{html_lib.escape(name)} ({score})"
                for name, score in element.microsim_recommendations
            )

            html += f"""
            <tr class="{type_class}">
                <td><strong>{int(element.chapter_num)}</strong></td>
                <td>{html_lib.escape(element.element_title)}</td>
                <td>{html_lib.escape(element.status)}</td>
                <td><em>{html_lib.escape(element.element_type.title())}</em></td>
                <td><small>{bloom_str}</small></td>
                <td style="text-align: center;">{element.ui_elements_count}</td>
                <td class="{difficulty_class}">{html_lib.escape(element.estimated_difficulty)}</td>
                <td><small>{recommendations}</small></td>
            </tr>
"""

        html += """
        </tbody>
    </table>
</body>
</html>
"""
        return html


def main():
    parser = argparse.ArgumentParser(
        description='Generate report of diagrams and MicroSims from chapter markdown files',
        epilog='Run this script from the repository home directory. '
               'It will look for docs/chapters/ by default.'
    )
    parser.add_argument(
        '--output-dir',
        default=None,
        help='Output directory path (default: docs/learning-graph from current directory)'
    )
    parser.add_argument(
        '--format',
        choices=['markdown', 'csv', 'html'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '--chapters-dir',
        default=None,
        help='Path to chapters directory (default: docs/chapters from current directory)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output for debugging'
    )
    parser.add_argument(
        '--allow-empty',
        action='store_true',
        help='Write an empty report instead of failing when no legacy specification blocks are found'
    )

    args = parser.parse_args()

    # Use current working directory as the base
    cwd = Path.cwd()

    # Determine chapters directory
    if args.chapters_dir:
        chapters_dir = Path(args.chapters_dir)
        if not chapters_dir.is_absolute():
            chapters_dir = (cwd / chapters_dir).resolve()
    else:
        chapters_dir = (cwd / 'docs' / 'chapters').resolve()

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = (cwd / output_dir).resolve()
    else:
        output_dir = (cwd / 'docs' / 'learning-graph').resolve()

    # Validate chapters directory exists
    if not chapters_dir.exists():
        print(f"Error: Chapters directory not found: {chapters_dir}")
        print(f"\nThis script should be run from a repository home directory that contains:")
        print(f"  - docs/chapters/  (with numbered chapter subdirectories like 01-*, 02-*, etc.)")
        print(f"\nCurrent working directory: {cwd}")
        print(f"\nYou can specify a custom chapters directory with --chapters-dir")
        return 1

    if not chapters_dir.is_dir():
        print(f"Error: Chapters path exists but is not a directory: {chapters_dir}")
        return 1

    # Validate or create output directory
    if not output_dir.exists():
        print(f"Warning: Output directory does not exist: {output_dir}")
        print(f"Creating output directory...")
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created: {output_dir}")
        except Exception as e:
            print(f"Error: Could not create output directory: {e}")
            return 1

    print(f"Analyzing chapters in: {chapters_dir}")

    # Analyze chapters
    analyzer = DiagramAnalyzer(str(chapters_dir), verbose=args.verbose)
    analyzer.analyze_all_chapters()

    if not analyzer.chapter_files:
        print(
            "Error: No numbered chapter files found. Expected either "
            "docs/chapters/01-name.md or docs/chapters/01-name/index.md."
        )
        return 1

    if analyzer.errors:
        print(f"Error: {len(analyzer.errors)} chapter file(s) could not be analyzed.")
        return 1

    print(f"Found {len(analyzer.elements)} diagram specification blocks")

    if not analyzer.elements and not args.allow_empty:
        print(
            "Error: No legacy diagram specification blocks were found. This utility "
            "only inventories '#### Diagram:' headers followed by <details> specs; "
            "it does not inventory rendered figures, images, or iframes. Use "
            "--allow-empty only when an empty specification report is intentional."
        )
        return 2

    # Generate report
    generator = ReportGenerator(analyzer.elements, chapters_dir, output_dir)

    if args.format == 'markdown':
        # Generate table report
        table_content = generator.generate_markdown_table()
        table_output = output_dir / 'diagram-table.md'
        with open(table_output, 'w', encoding='utf-8') as f:
            f.write(table_content)
        print(f"Table report saved to: {table_output}")

        # Generate details report
        details_content = generator.generate_markdown_details()
        details_output = output_dir / 'diagram-details.md'
        with open(details_output, 'w', encoding='utf-8') as f:
            f.write(details_content)
        print(f"Details report saved to: {details_output}")

    elif args.format == 'csv':
        csv_output = output_dir / 'diagrams.csv'
        generator.generate_csv(str(csv_output))
        print(f"CSV report saved to: {csv_output}")

    elif args.format == 'html':
        html_output = output_dir / 'diagrams.html'
        content = generator.generate_html()
        with open(html_output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"HTML report saved to: {html_output}")

    # Print summary to console
    print("\n=== SUMMARY ===")
    print(f"Total specification blocks: {len(analyzer.elements)}")
    print(f"Diagram specifications: {sum(1 for e in analyzer.elements if e.element_type == 'diagram')}")
    print(f"MicroSim specifications: {sum(1 for e in analyzer.elements if e.element_type == 'microsim')}")

    print("\nBy Planning Heuristic:")
    difficulty_counts = {}
    for element in analyzer.elements:
        difficulty_counts[element.estimated_difficulty] = difficulty_counts.get(element.estimated_difficulty, 0) + 1

    for difficulty in ['Easy', 'Medium', 'Hard', 'Very Hard']:
        count = difficulty_counts.get(difficulty, 0)
        print(f"  {difficulty}: {count}")

    print("\nBy Chapter:")
    by_chapter = {}
    for element in analyzer.elements:
        key = element.chapter_num
        by_chapter[key] = by_chapter.get(key, 0) + 1

    for chapter_num in sorted(by_chapter.keys()):
        print(f"  Chapter {chapter_num}: {by_chapter[chapter_num]} elements")

    return 0


if __name__ == '__main__':
    exit(main())
