#!/usr/bin/env python3
"""
Feature Checklist Generator for Intelligent Textbooks

Combines the feature detection results with the template to generate
a complete feature-checklist.md file for the project.

Usage:
    python generate-feature-checklist.py /path/to/project
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Import the detection module
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
from detect_features import detect_features


def status_icon(detected: bool) -> str:
    """Convert boolean to status icon."""
    return ":white_check_mark:" if detected else ":x:"


def generate_checklist(project_path: Path) -> str:
    """Generate the feature checklist markdown content."""

    # Run detection
    results = detect_features(project_path)

    # Read the template
    template_path = script_dir.parent / "references" / "assets" / "templates" / "docs" / "feature-checklist.md"
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Build replacements dictionary
    replacements = {
        # Counts
        "{chapter_count}": str(results["chapter_count"]),
        "{microsim_count}": str(results["microsim_count"]),
        "{glossary_term_count}": str(results["glossary_term_count"]) if results["glossary_term_count"] > 0 else "0",
        "{faq_question_count}": str(results["faq_question_count"]) if results["faq_question_count"] > 0 else "0",
        "{quiz_file_count}": str(results["quiz_file_count"]),
        "{generation_date}": datetime.now().strftime("%B %Y"),

        # Basic Features
        "{navigation_sidebar}": status_icon(results["basic"]["navigation_sidebar"]),
        "{search_functionality}": status_icon(results["basic"]["search_functionality"]),
        "{table_of_contents}": status_icon(results["basic"]["table_of_contents"]),
        "{site_title}": status_icon(results["basic"]["site_title"]),
        "{site_author}": status_icon(results["basic"]["site_author"]),
        "{github_repo}": status_icon(results["basic"]["github_repo"]),
        "{custom_logo}": status_icon(results["basic"]["custom_logo"]),
        "{custom_favicon}": status_icon(results["basic"]["custom_favicon"]),
        "{color_theme}": status_icon(results["basic"]["color_theme"]),
        "{footer_navigation}": status_icon(results["basic"]["footer_navigation"]),
        "{navigation_expand}": status_icon(results["basic"]["navigation_expand"]),
        "{back_to_top}": status_icon(results["basic"]["back_to_top"]),
        "{breadcrumbs}": status_icon(results["basic"]["breadcrumbs"]),
        "{section_index}": status_icon(results["basic"]["section_index"]),
        "{license_page}": status_icon(results["basic"]["license_page"]),
        "{contact_page}": status_icon(results["basic"]["contact_page"]),
        "{about_page}": status_icon(results["basic"]["about_page"]),
        "{how_we_built}": status_icon(results["basic"]["how_we_built"]),
        "{copyright_footer}": status_icon(results["basic"]["copyright_footer"]),

        # Content Enhancement
        "{glightbox}": status_icon(results["content_enhancement"]["glightbox"]),
        "{katex}": status_icon(results["content_enhancement"]["katex"]),
        "{mathjax}": status_icon(results["content_enhancement"]["mathjax"]),
        "{admonitions}": status_icon(results["content_enhancement"]["admonitions"]),
        "{code_copy_button}": status_icon(results["content_enhancement"]["code_copy_button"]),
        "{syntax_highlighting}": status_icon(results["content_enhancement"]["syntax_highlighting"]),
        "{tabbed_content}": status_icon(results["content_enhancement"]["tabbed_content"]),
        "{task_lists}": status_icon(results["content_enhancement"]["task_lists"]),
        "{mark_highlight}": status_icon(results["content_enhancement"]["mark_highlight"]),
        "{strikethrough}": status_icon(results["content_enhancement"]["strikethrough"]),
        "{magic_links}": status_icon(results["content_enhancement"]["magic_links"]),
        "{snippets}": status_icon(results["content_enhancement"]["snippets"]),
        "{emoji}": status_icon(results["content_enhancement"]["emoji"]),
        "{collapsible_details}": status_icon(results["content_enhancement"]["collapsible_details"]),
        "{mermaid}": status_icon(results["content_enhancement"]["mermaid"]),

        # Site Resources
        "{glossary}": status_icon(results["site_resources"]["glossary"]),
        "{faq}": status_icon(results["site_resources"]["faq"]),
        "{references}": status_icon(results["site_resources"]["references"]),
        "{custom_css}": status_icon(results["site_resources"]["custom_css"]),
        "{custom_js}": status_icon(results["site_resources"]["custom_js"]),
        "{google_analytics}": status_icon(results["site_resources"]["google_analytics"]),

        # Publishing
        "{social_media_cards}": status_icon(results["publishing"]["social_media_cards"]),
        "{edit_page_button}": status_icon(results["publishing"]["edit_page_button"]),

        # Interactive Learning
        "{microsims}": status_icon(results["interactive_learning"]["microsims"]),
        "{microsim_index}": status_icon(results["interactive_learning"]["microsim_index"]),
        "{per_chapter_quizzes}": status_icon(results["interactive_learning"]["per_chapter_quizzes"]),

        # Learning Graph
        "{course_description}": status_icon(results["learning_graph"]["course_description"]),
        "{concept_list}": status_icon(results["learning_graph"]["concept_list"]),
        "{learning_graph_csv}": status_icon(results["learning_graph"]["learning_graph_csv"]),
        "{learning_graph_json}": status_icon(results["learning_graph"]["learning_graph_json"]),
        "{graph_viewer}": status_icon(results["learning_graph"]["graph_viewer"]),
        "{concept_taxonomy}": status_icon(results["learning_graph"]["concept_taxonomy"]),
        "{quality_metrics}": status_icon(results["learning_graph"]["quality_metrics"]),
        "{book_metrics}": status_icon(results["learning_graph"]["book_metrics"]),
        "{chapter_metrics}": status_icon(results["learning_graph"]["chapter_metrics"]),
        "{glossary_quality_report}": status_icon(results["learning_graph"]["glossary_quality_report"]),
        "{faq_quality_report}": status_icon(results["learning_graph"]["faq_quality_report"]),
        "{faq_coverage_gaps}": status_icon(results["learning_graph"]["faq_coverage_gaps"]),
        "{quiz_generation_report}": status_icon(results["learning_graph"]["quiz_generation_report"]),

        # Content Generation
        "{chapters}": status_icon(results["content_generation"]["chapters"]),
        "{prompts_collection}": status_icon(results["content_generation"]["prompts_collection"]),
    }

    # Apply replacements
    content = template
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    return content, results


def main():
    parser = argparse.ArgumentParser(
        description="Generate feature-checklist.md for an MkDocs intelligent textbook"
    )
    parser.add_argument(
        "project_path",
        type=str,
        help="Path to the project root (containing mkdocs.yml)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path (default: docs/feature-checklist.md)"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Print to stdout instead of writing file"
    )
    parser.add_argument(
        "--save-json", "-j",
        type=str,
        default=None,
        help="Also save detection results as JSON"
    )

    args = parser.parse_args()
    project_path = Path(args.project_path).resolve()

    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}", file=sys.stderr)
        sys.exit(1)

    if not (project_path / "mkdocs.yml").exists():
        print(f"Error: No mkdocs.yml found in {project_path}", file=sys.stderr)
        sys.exit(1)

    # Generate the checklist
    content, results = generate_checklist(project_path)

    # Output
    if args.dry_run:
        print(content)
    else:
        output_path = Path(args.output) if args.output else project_path / "docs" / "feature-checklist.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Feature checklist written to: {output_path}")

        # Summary statistics
        print(f"\nDetection Summary:")
        print(f"  - Chapters: {results['chapter_count']}")
        print(f"  - MicroSims: {results['microsim_count']}")
        print(f"  - Glossary terms: {results['glossary_term_count']}")
        print(f"  - FAQ questions: {results['faq_question_count']}")
        print(f"  - Quiz files: {results['quiz_file_count']}")

    # Save JSON if requested
    if args.save_json:
        json_path = Path(args.save_json)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Detection results saved to: {json_path}")


if __name__ == "__main__":
    main()
