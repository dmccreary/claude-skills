#!/usr/bin/env python3
"""
Generate Medium Diagrams with High Match Scores

This script analyzes the diagrams.csv file and identifies Medium difficulty diagrams
with MicroSim recommendation scores > 90. It then extracts the full specifications
from the chapter files and prepares them for MicroSim generation.

Usage:
    # Generate report and specification files
    python generate-medium-diagrams.py

    # Just show the report without creating files
    python generate-medium-diagrams.py --dry-run

    # Specify custom CSV path
    python generate-medium-diagrams.py --csv path/to/diagrams.csv
"""

import csv
import re
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class DiagramCandidate:
    """Represents a diagram candidate for generation"""
    chapter_num: str
    chapter_name: str
    chapter_dir: str
    element_title: str
    difficulty: str
    recommended_generator: str
    match_score: int
    specification: str


class DiagramSpecExtractor:
    """Extracts diagram specifications from chapter markdown files"""

    # Pattern to find the diagram section with details block
    DIAGRAM_SECTION_PATTERN = re.compile(
        r'####\s+Diagram:\s*([^\n]+)\n(.*?)<details[^>]*>(.*?)</details>',
        re.DOTALL
    )

    def __init__(self, chapters_dir: Path):
        self.chapters_dir = chapters_dir

    def extract_specification(self, chapter_dir: str, element_title: str) -> Optional[str]:
        """Extract the full specification for a diagram from the chapter file"""
        chapter_path = self.chapters_dir / chapter_dir / 'index.md'

        if not chapter_path.exists():
            print(f"  Warning: Chapter file not found: {chapter_path}")
            return None

        try:
            with open(chapter_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find the matching diagram section
            for match in self.DIAGRAM_SECTION_PATTERN.finditer(content):
                header_title = match.group(1).strip()
                if header_title == element_title:
                    # Extract the details content (group 3)
                    details_content = match.group(3)
                    # Remove the MicroSim recommendations section
                    spec = re.sub(
                        r'---\s*\*\*MicroSim Generator Recommendations:\*\*.*',
                        '',
                        details_content,
                        flags=re.DOTALL
                    )
                    return spec.strip()

            print(f"  Warning: Could not find specification for '{element_title}' in {chapter_path}")
            return None

        except Exception as e:
            print(f"  Error reading {chapter_path}: {e}")
            return None


class MediumDiagramGenerator:
    """Main class for processing medium diagrams"""

    def __init__(self, csv_path: Path, chapters_dir: Path, output_dir: Path):
        self.csv_path = csv_path
        self.chapters_dir = chapters_dir
        self.output_dir = output_dir
        self.spec_extractor = DiagramSpecExtractor(chapters_dir)
        self.candidates: List[DiagramCandidate] = []

    def parse_recommendations(self, recommendations_str: str) -> List[Tuple[str, int]]:
        """Parse the MicroSim Recommendations column

        Example: "timeline-generator (98); chartjs-generator (70); microsim-p5 (75)"
        Returns: [("timeline-generator", 98), ("chartjs-generator", 70), ...]
        """
        if not recommendations_str or recommendations_str.strip() == '':
            return []

        recommendations = []
        # Split by semicolon
        parts = recommendations_str.split(';')
        for part in parts:
            part = part.strip()
            # Match "generator-name (score)"
            match = re.match(r'([a-z0-9-]+)\s+\((\d+)\)', part)
            if match:
                generator_name = match.group(1)
                score = int(match.group(2))
                recommendations.append((generator_name, score))

        return recommendations

    def load_candidates(self, min_score: int = 90) -> None:
        """Load diagram candidates from CSV file"""
        print(f"Reading CSV: {self.csv_path}")

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Filter: Difficulty = Medium
                if row['Difficulty'] != 'Medium':
                    continue

                # Parse recommendations
                recommendations = self.parse_recommendations(row['MicroSim Recommendations'])

                # Filter: Has recommendations and first score > min_score
                if not recommendations or recommendations[0][1] <= min_score:
                    continue

                # Get chapter directory name from chapter number
                chapter_num = row['Chapter']
                # Find the actual chapter directory
                chapter_dirs = list(self.chapters_dir.glob(f"{chapter_num}-*"))
                if not chapter_dirs:
                    print(f"  Warning: Could not find chapter directory for chapter {chapter_num}")
                    continue

                chapter_dir = chapter_dirs[0].name

                # Extract specification
                specification = self.spec_extractor.extract_specification(
                    chapter_dir,
                    row['Element Title']
                )

                if not specification:
                    continue

                # Create candidate
                candidate = DiagramCandidate(
                    chapter_num=chapter_num,
                    chapter_name=row['Chapter Name'],
                    chapter_dir=chapter_dir,
                    element_title=row['Element Title'],
                    difficulty=row['Difficulty'],
                    recommended_generator=recommendations[0][0],
                    match_score=recommendations[0][1],
                    specification=specification
                )

                self.candidates.append(candidate)

        print(f"Found {len(self.candidates)} candidates (Medium difficulty, score > {min_score})")

    def generate_report(self) -> str:
        """Generate a markdown report of all candidates"""
        lines = [
            "# Medium Diagram Generation Report",
            "",
            f"**Total Candidates:** {len(self.candidates)}",
            f"**Filter Criteria:** Difficulty = Medium, First Recommendation Score > 90",
            "",
            "## Summary by Generator",
            ""
        ]

        # Count by generator
        generator_counts = {}
        for candidate in self.candidates:
            generator_counts[candidate.recommended_generator] = \
                generator_counts.get(candidate.recommended_generator, 0) + 1

        for generator, count in sorted(generator_counts.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"- **{generator}:** {count} diagrams")

        lines.extend([
            "",
            "## Diagram Details",
            ""
        ])

        # Group by chapter
        by_chapter = {}
        for candidate in self.candidates:
            key = (candidate.chapter_num, candidate.chapter_name, candidate.chapter_dir)
            if key not in by_chapter:
                by_chapter[key] = []
            by_chapter[key].append(candidate)

        for chapter_key in sorted(by_chapter.keys(), key=lambda x: x[0]):
            chapter_num, chapter_name, chapter_dir = chapter_key
            candidates = by_chapter[chapter_key]

            lines.extend([
                f"### Chapter {int(chapter_num)}: {chapter_name}",
                "",
                f"**Diagrams:** {len(candidates)}",
                ""
            ])

            for candidate in sorted(candidates, key=lambda c: c.element_title):
                lines.append(f"#### {candidate.element_title}")
                lines.append(f"- **Generator:** {candidate.recommended_generator}")
                lines.append(f"- **Match Score:** {candidate.match_score}/100")
                lines.append(f"- **Specification File:** `specs/{candidate.chapter_num}-{self._slugify(candidate.element_title)}.md`")
                lines.append("")

        return '\n'.join(lines)

    def _slugify(self, text: str) -> str:
        """Convert text to a filename-safe slug"""
        slug = text.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = slug.strip('-')
        return slug

    def save_specifications(self) -> None:
        """Save individual specification files for each candidate"""
        specs_dir = self.output_dir / 'specs'
        specs_dir.mkdir(parents=True, exist_ok=True)

        print(f"\nSaving specification files to: {specs_dir}")

        for candidate in self.candidates:
            filename = f"{candidate.chapter_num}-{self._slugify(candidate.element_title)}.md"
            spec_path = specs_dir / filename

            content = [
                f"# {candidate.element_title}",
                "",
                f"**Chapter:** {candidate.chapter_num} - {candidate.chapter_name}",
                f"**Generator:** {candidate.recommended_generator}",
                f"**Match Score:** {candidate.match_score}/100",
                f"**Difficulty:** {candidate.difficulty}",
                "",
                "## Specification",
                "",
                candidate.specification
            ]

            with open(spec_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))

        print(f"Saved {len(self.candidates)} specification files")

    def generate_execution_script(self) -> str:
        """Generate a batch script for executing all MicroSim generations"""
        lines = [
            "# Medium Diagram Generation Execution Plan",
            "",
            "This document lists all the diagrams that need to be generated, organized by MicroSim generator.",
            "",
            "## Execution Instructions",
            "",
            "For each diagram below:",
            "1. Read the specification file",
            "2. Invoke the recommended MicroSim generator skill",
            "3. Provide the specification content to the skill",
            "4. Review and save the generated MicroSim",
            "",
        ]

        # Group by generator
        by_generator = {}
        for candidate in self.candidates:
            if candidate.recommended_generator not in by_generator:
                by_generator[candidate.recommended_generator] = []
            by_generator[candidate.recommended_generator].append(candidate)

        for generator in sorted(by_generator.keys()):
            candidates = by_generator[generator]
            lines.extend([
                f"## {generator} ({len(candidates)} diagrams)",
                ""
            ])

            for i, candidate in enumerate(candidates, 1):
                spec_file = f"specs/{candidate.chapter_num}-{self._slugify(candidate.element_title)}.md"
                lines.extend([
                    f"### {i}. {candidate.element_title}",
                    f"- **Chapter:** {candidate.chapter_num} - {candidate.chapter_name}",
                    f"- **Match Score:** {candidate.match_score}/100",
                    f"- **Specification:** `{spec_file}`",
                    f"- **Command:** Invoke `/skill {generator}` with specification from `{spec_file}`",
                    ""
                ])

        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate Medium diagrams with high MicroSim match scores',
        epilog='This script identifies Medium difficulty diagrams with recommendation scores > 90'
    )
    parser.add_argument(
        '--csv',
        default=None,
        help='Path to diagrams.csv (default: docs/learning-graph/diagrams.csv)'
    )
    parser.add_argument(
        '--chapters-dir',
        default=None,
        help='Path to chapters directory (default: docs/chapters)'
    )
    parser.add_argument(
        '--output-dir',
        default=None,
        help='Output directory for specifications (default: docs/learning-graph/medium-diagrams)'
    )
    parser.add_argument(
        '--min-score',
        type=int,
        default=90,
        help='Minimum match score threshold (default: 90)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Generate report only, do not save specification files'
    )

    args = parser.parse_args()

    # Use current working directory as base
    cwd = Path.cwd()

    # Determine paths
    csv_path = Path(args.csv) if args.csv else cwd / 'docs' / 'learning-graph' / 'diagrams.csv'
    chapters_dir = Path(args.chapters_dir) if args.chapters_dir else cwd / 'docs' / 'chapters'
    output_dir = Path(args.output_dir) if args.output_dir else cwd / 'docs' / 'learning-graph' / 'medium-diagrams'

    # Validate CSV exists
    if not csv_path.exists():
        print(f"Error: CSV file not found: {csv_path}")
        return 1

    # Validate chapters directory exists
    if not chapters_dir.exists():
        print(f"Error: Chapters directory not found: {chapters_dir}")
        return 1

    print("=" * 70)
    print("Medium Diagram Generation Tool")
    print("=" * 70)
    print(f"CSV File: {csv_path}")
    print(f"Chapters Dir: {chapters_dir}")
    print(f"Output Dir: {output_dir}")
    print(f"Min Score: {args.min_score}")
    print(f"Dry Run: {args.dry_run}")
    print("=" * 70)
    print()

    # Process diagrams
    generator = MediumDiagramGenerator(csv_path, chapters_dir, output_dir)
    generator.load_candidates(min_score=args.min_score)

    if len(generator.candidates) == 0:
        print("\nNo candidates found matching the criteria.")
        return 0

    # Generate and save report
    report_content = generator.generate_report()
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / 'generation-report.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"\nReport saved to: {report_path}")
    else:
        print("\n" + report_content)

    # Generate and save execution script
    if not args.dry_run:
        execution_script = generator.generate_execution_script()
        script_path = output_dir / 'execution-plan.md'
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(execution_script)
        print(f"Execution plan saved to: {script_path}")

        # Save specification files
        generator.save_specifications()

        print("\n" + "=" * 70)
        print("NEXT STEPS:")
        print("=" * 70)
        print(f"1. Review the generation report: {report_path}")
        print(f"2. Review the execution plan: {script_path}")
        print(f"3. Specification files are in: {output_dir / 'specs'}")
        print("4. Use Claude Code to invoke the recommended skills with each specification")
        print("=" * 70)

    return 0


if __name__ == '__main__':
    exit(main())
