#!/usr/bin/env python3
"""
Book Metrics Generator

Generates comprehensive metrics for intelligent textbooks, including:
- Book-level metrics (overall statistics)
- Chapter-level metrics (per-chapter statistics)

Usage:
    python book-metrics.py [docs_directory]
"""

import os
import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple, Any
from collections import defaultdict


class BookMetricsGenerator:
    """Generates metrics for intelligent textbooks."""

    def __init__(self, docs_dir: str = "docs"):
        """Initialize the metrics generator.

        Args:
            docs_dir: Path to the docs directory (default: "docs")
        """
        self.docs_dir = Path(docs_dir)
        self.chapters_dir = self.docs_dir / "chapters"
        self.learning_graph_dir = self.docs_dir / "learning-graph"
        self.sims_dir = self.docs_dir / "sims"
        self.glossary_file = self.docs_dir / "glossary.md"
        self.faq_file = self.docs_dir / "faq.md"

    def count_chapters(self) -> Tuple[int, List[Dict[str, Any]]]:
        """Count number of chapter directories and collect chapter info.

        Returns:
            Tuple of (chapter_count, list of chapter info dicts)
        """
        chapters = []

        if not self.chapters_dir.exists():
            return 0, []

        # Look for directories with index.md files
        for item in sorted(self.chapters_dir.iterdir()):
            if item.is_dir() and (item / "index.md").exists():
                # Extract chapter number from directory name
                match = re.match(r'^0*(\d+)', item.name)
                if match:
                    chapter_num = int(match.group(1))
                    index_file = item / "index.md"

                    # Read chapter title from index.md
                    title = self._extract_title(index_file)

                    chapters.append({
                        'number': chapter_num,
                        'name': title,
                        'path': item,
                        'index_file': index_file
                    })

        return len(chapters), chapters

    def _extract_title(self, markdown_file: Path) -> str:
        """Extract the first H1 title from a markdown file.

        Args:
            markdown_file: Path to the markdown file

        Returns:
            The title string, or the filename if no title found
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                for line in f:
                    match = re.match(r'^#\s+(.+)$', line.strip())
                    if match:
                        return match.group(1)
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")

        return markdown_file.parent.name

    def count_concepts(self) -> int:
        """Count concepts from learning-graph.csv.

        Returns:
            Number of concepts
        """
        csv_file = self.learning_graph_dir / "learning-graph.csv"

        if not csv_file.exists():
            return 0

        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return sum(1 for _ in reader)
        except Exception as e:
            print(f"Warning: Could not read learning graph CSV: {e}")
            return 0

    def count_glossary_terms(self) -> int:
        """Count glossary terms from glossary.md.

        Returns:
            Number of glossary terms
        """
        if not self.glossary_file.exists():
            return 0

        try:
            with open(self.glossary_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count H4 headers as glossary terms
                h4_count = len(re.findall(r'^####\s+', content, re.MULTILINE))
                return h4_count
        except Exception as e:
            print(f"Warning: Could not read glossary: {e}")
            return 0

    def count_faqs(self) -> int:
        """Count FAQ items from faq.md.

        Returns:
            Number of FAQ items
        """
        if not self.faq_file.exists():
            return 0

        try:
            with open(self.faq_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count H3 headers as FAQ questions
                return len(re.findall(r'^###\s+', content, re.MULTILINE))
        except Exception as e:
            print(f"Warning: Could not read FAQ: {e}")
            return 0

    def count_quiz_questions(self) -> int:
        """Count quiz questions across all chapters.

        Returns:
            Total number of quiz questions
        """
        total = 0

        if not self.chapters_dir.exists():
            return 0

        # Look for quiz.md files in chapter directories
        for chapter_dir in self.chapters_dir.iterdir():
            if chapter_dir.is_dir():
                quiz_file = chapter_dir / "quiz.md"
                if quiz_file.exists():
                    total += self._count_quiz_in_file(quiz_file)

        return total

    def _count_quiz_in_file(self, quiz_file: Path) -> int:
        """Count quiz questions in a single quiz file.

        Args:
            quiz_file: Path to quiz.md file

        Returns:
            Number of questions in the file
        """
        try:
            with open(quiz_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count H4 headers with numbered questions (e.g., "#### 1.")
                h4_pattern = len(re.findall(r'^####\s+\d+\.', content, re.MULTILINE))
                # Also count H2 headers as questions (legacy format)
                h2_pattern = len(re.findall(r'^##\s+', content, re.MULTILINE))
                return h4_pattern + h2_pattern
        except Exception as e:
            print(f"Warning: Could not read {quiz_file}: {e}")
            return 0

    def count_diagrams_in_file(self, markdown_file: Path) -> int:
        """Count diagrams in a single markdown file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            Number of diagrams (H4 headers starting with "#### Diagram:")
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                return len(re.findall(r'^####\s+Diagram:', content, re.MULTILINE))
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return 0

    def count_all_diagrams(self) -> int:
        """Count all diagrams in all markdown files.

        Returns:
            Total number of diagrams
        """
        total = 0

        # Search all markdown files in docs directory
        for md_file in self.docs_dir.rglob('*.md'):
            total += self.count_diagrams_in_file(md_file)

        return total

    # TODO: Fix bug in equation counting to avoid double counting dollar amounts in numbers
    def count_equations_in_file(self, markdown_file: Path) -> int:
        """Count LaTeX equations in a single markdown file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            Number of equations (LaTeX expressions)
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count inline math: $...$
                inline = len(re.findall(r'\$[^$]+\$', content))
                # Count display math: $$...$$
                display = len(re.findall(r'\$\$[^$]+\$\$', content))
                return inline + display
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return 0

    # TODO: Fix bug in equation counting to avoid double counting dollar amounts in numbers
    def count_all_equations(self) -> int:
        """Count all equations in all markdown files.

        Returns:
            Total number of equations
        """
        total = 0

        # Search all markdown files in docs directory
        for md_file in self.docs_dir.rglob('*.md'):
            total += self.count_equations_in_file(md_file)

        return total

    def count_microsims(self) -> int:
        """Count MicroSim directories in docs/sims.

        Returns:
            Number of MicroSim directories
        """
        if not self.sims_dir.exists():
            return 0

        count = 0
        for item in self.sims_dir.iterdir():
            if item.is_dir() and (item / "index.md").exists():
                count += 1

        return count

    def count_words_in_file(self, markdown_file: Path) -> int:
        """Count words in a single markdown file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            Number of words
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Remove code blocks
                content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
                # Remove inline code
                content = re.sub(r'`[^`]+`', '', content)
                # Remove URLs
                content = re.sub(r'https?://\S+', '', content)
                # Count words
                words = re.findall(r'\b\w+\b', content)
                return len(words)
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return 0

    def count_total_words(self) -> int:
        """Count total words in all markdown files.

        Returns:
            Total word count
        """
        total = 0

        # Search all markdown files in docs directory
        for md_file in self.docs_dir.rglob('*.md'):
            total += self.count_words_in_file(md_file)

        return total

    def count_links_in_file(self, markdown_file: Path) -> int:
        """Count markdown links in a single file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            Number of links
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count markdown links [text](url)
                return len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content))
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return 0

    def count_all_links(self) -> int:
        """Count all links in all markdown files.

        Returns:
            Total number of links
        """
        total = 0

        # Search all markdown files in docs directory
        for md_file in self.docs_dir.rglob('*.md'):
            total += self.count_links_in_file(md_file)

        return total

    def calculate_equivalent_pages(self, total_words: int, diagrams: int, microsims: int) -> int:
        """Calculate equivalent pages based on words, diagrams, and MicroSims.

        Assumptions:
        - 250 words per page
        - Each diagram takes 0.25 page
        - Each MicroSim takes 0.5 page

        Args:
            total_words: Total word count
            diagrams: Number of diagrams
            microsims: Number of MicroSims

        Returns:
            Estimated page count
        """
        words_per_page = 250
        diagram_pages = diagrams * 0.25
        microsim_pages = microsims * 0.5
        text_pages = total_words / words_per_page

        return int(text_pages + diagram_pages + microsim_pages)

    def count_sections_in_file(self, markdown_file: Path) -> int:
        """Count sections (H2 and H3 headers) in a markdown file.

        Args:
            markdown_file: Path to markdown file

        Returns:
            Number of sections
        """
        try:
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
                h2_count = len(re.findall(r'^##\s+', content, re.MULTILINE))
                h3_count = len(re.findall(r'^###\s+', content, re.MULTILINE))
                return h2_count + h3_count
        except Exception as e:
            print(f"Warning: Could not read {markdown_file}: {e}")
            return 0

    def get_chapter_metrics(self, chapter: Dict[str, Any]) -> Dict[str, Any]:
        """Get metrics for a single chapter.

        Args:
            chapter: Chapter info dict

        Returns:
            Dict with chapter metrics
        """
        index_file = chapter['index_file']
        chapter_dir = chapter['path']

        # Count sections in index.md
        sections = self.count_sections_in_file(index_file)

        # Count diagrams in all markdown files in chapter directory
        diagrams = 0
        words = 0
        for md_file in chapter_dir.rglob('*.md'):
            diagrams += self.count_diagrams_in_file(md_file)
            words += self.count_words_in_file(md_file)

        return {
            'number': chapter['number'],
            'name': chapter['name'],
            'sections': sections,
            'diagrams': diagrams,
            'words': words
        }

    def generate_book_metrics_md(self) -> str:
        """Generate the book-metrics.md content.

        Returns:
            Markdown content as string
        """
        # Collect all metrics
        chapter_count, chapters = self.count_chapters()
        concepts = self.count_concepts()
        glossary_terms = self.count_glossary_terms()
        faqs = self.count_faqs()
        quiz_questions = self.count_quiz_questions()
        diagrams = self.count_all_diagrams()
        equations = self.count_all_equations()
        microsims = self.count_microsims()
        total_words = self.count_total_words()
        links = self.count_all_links()
        equivalent_pages = self.calculate_equivalent_pages(total_words, diagrams, microsims)

        # Build markdown table
        md = "# Book Metrics\n\n"
        md += "This file contains overall metrics for the intelligent textbook.\n\n"
        md += "| Metric Name | Value | Link | Notes |\n"
        md += "|-------------|-------|------|-------|\n"

        # Add rows
        md += f"| Chapters | {chapter_count} | [Chapters](../chapters/index.md) | Number of chapter directories |\n"
        md += f"| Concepts | {concepts} | [Concept List](./concept-list.md) | Concepts from learning graph |\n"
        md += f"| Glossary Terms | {glossary_terms} | [Glossary](../glossary.md) | Defined terms |\n"
        md += f"| FAQs | {faqs} | [FAQ](../faq.md) | Frequently asked questions |\n"
        md += f"| Quiz Questions | {quiz_questions} | - | Questions across all chapters |\n"
        md += f"| Diagrams | {diagrams} | - | Level 4 headers starting with '#### Diagram:' |\n"
        md += f"| Equations | {equations} | - | LaTeX expressions (inline and display) |\n"
        md += f"| MicroSims | {microsims} | [Simulations](../sims/index.md) | Interactive MicroSims |\n"
        md += f"| Total Words | {total_words:,} | - | Words in all markdown files |\n"
        md += f"| Links | {links} | - | Hyperlinks in markdown format |\n"
        md += f"| Equivalent Pages | {equivalent_pages} | - | Estimated pages (250 words/page + visuals) |\n"

        md += "\n## Metrics Explanation\n\n"
        md += "- **Chapters**: Count of chapter directories containing index.md files\n"
        md += "- **Concepts**: Number of rows in learning-graph.csv\n"
        md += "- **Glossary Terms**: H4 headers in glossary.md\n"
        md += "- **FAQs**: H3 headers in faq.md\n"
        md += "- **Quiz Questions**: H4 headers with numbered questions (e.g., '#### 1.') or H2 headers in quiz.md files\n"
        md += "- **Diagrams**: H4 headers starting with '#### Diagram:'\n"
        md += "- **Equations**: LaTeX expressions using $ and $$ delimiters\n"
        md += "- **MicroSims**: Directories in docs/sims/ with index.md files\n"
        md += "- **Total Words**: All words in markdown files (excluding code blocks and URLs)\n"
        md += "- **Links**: Markdown-formatted links `[text](url)`\n"
        md += "- **Equivalent Pages**: Based on 250 words/page + 0.25 page/diagram + 0.5 page/MicroSim\n"

        return md

    def generate_chapter_metrics_md(self) -> str:
        """Generate the chapter-metrics.md content.

        Returns:
            Markdown content as string
        """
        # Collect chapter info
        chapter_count, chapters = self.count_chapters()

        if chapter_count == 0:
            return "# Chapter Metrics\n\nNo chapters found.\n"

        # Build markdown table
        md = "# Chapter Metrics\n\n"
        md += "This file contains chapter-by-chapter metrics.\n\n"
        md += "| Chapter | Name | Sections | Diagrams | Words |\n"
        md += "|---------|------|----------|----------|-------|\n"

        # Add rows for each chapter
        for chapter in chapters:
            metrics = self.get_chapter_metrics(chapter)
            # Create link to chapter index.md (relative to learning-graph directory)
            chapter_dir_name = chapter['path'].name
            chapter_link = f"[{metrics['name']}](../chapters/{chapter_dir_name}/index.md)"
            md += f"| {metrics['number']} | {chapter_link} | {metrics['sections']} | {metrics['diagrams']} | {metrics['words']:,} |\n"

        md += "\n## Metrics Explanation\n\n"
        md += "- **Chapter**: Chapter number (leading zeros removed)\n"
        md += "- **Name**: Chapter title from index.md\n"
        md += "- **Sections**: Count of H2 and H3 headers in chapter markdown files\n"
        md += "- **Diagrams**: Count of H4 headers starting with '#### Diagram:'\n"
        md += "- **Words**: Word count across all markdown files in the chapter\n"

        return md

    def generate_metrics(self, output_dir: Path = None):
        """Generate both metrics files.

        Args:
            output_dir: Directory to write files to (defaults to learning-graph directory)
        """
        if output_dir is None:
            output_dir = self.learning_graph_dir

        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate book metrics
        book_metrics_content = self.generate_book_metrics_md()
        book_metrics_file = output_dir / "book-metrics.md"
        with open(book_metrics_file, 'w', encoding='utf-8') as f:
            f.write(book_metrics_content)
        print(f"✅ Generated {book_metrics_file}")

        # Generate chapter metrics
        chapter_metrics_content = self.generate_chapter_metrics_md()
        chapter_metrics_file = output_dir / "chapter-metrics.md"
        with open(chapter_metrics_file, 'w', encoding='utf-8') as f:
            f.write(chapter_metrics_content)
        print(f"✅ Generated {chapter_metrics_file}")


def main():
    """Main entry point."""
    import sys

    # Get docs directory from command line or use default
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else "docs"

    # Check if docs directory exists
    if not Path(docs_dir).exists():
        print(f"❌ Error: Directory '{docs_dir}' does not exist")
        sys.exit(1)

    # Generate metrics
    generator = BookMetricsGenerator(docs_dir)
    generator.generate_metrics()

    print("\n✅ Book metrics generation version 0.02 complete!")
    print("\nhttp://localhost:8000/conversational-ai/learning-graph/book-metrics/")
    print("http://localhost:8000/conversational-ai/learning-graph/chapter-metrics/")



if __name__ == "__main__":
    main()
