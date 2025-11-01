#!/usr/bin/env python3
"""
Generate Taxonomy Distribution Report

Analyzes the taxonomy distribution in the concept dependency CSV
and generates a detailed distribution report with recommendations.
"""

import csv
from collections import defaultdict
from typing import Dict, List, Tuple


def analyze_taxonomy_distribution(csv_path: str, output_path: str, taxonomy_names: dict = None):
    """
    Analyze taxonomy distribution and generate report.

    Args:
        csv_path: Path to input CSV file
        output_path: Path to output markdown report
        taxonomy_names: Optional dictionary mapping taxonomy IDs to full names
    """
    # Default taxonomy names
    default_names = {
        'FOUND': 'Foundation Concepts - Prerequisites',
        'DEF': 'Definitional Concepts',
        'CORE': 'Core Concepts',
        'INTER': 'Intermediate Topics',
        'ADV': 'Advanced Topics',
        'APPLIED': 'Applied Concepts',
        'SPEC': 'Specialized Topics',
        'PROJ': 'Capstone Projects Ideas',
        'MISC': 'Miscellaneous',
    }

    names = taxonomy_names if taxonomy_names is not None else default_names

    # Read CSV and count by taxonomy
    taxonomy_counts = defaultdict(int)
    taxonomy_concepts = defaultdict(list)

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tax = row['TaxonomyID']
            taxonomy_counts[tax] += 1
            taxonomy_concepts[tax].append((int(row['ConceptID']), row['ConceptLabel']))

    total_concepts = sum(taxonomy_counts.values())

    # Calculate percentages
    taxonomy_data = []
    for tax, count in taxonomy_counts.items():
        percentage = (count / total_concepts) * 100
        name = names.get(tax, tax)
        taxonomy_data.append((tax, name, count, percentage))

    # Sort by count descending
    taxonomy_data.sort(key=lambda x: x[2], reverse=True)

    # Identify issues
    over_represented = [(tax, name, count, pct) for tax, name, count, pct in taxonomy_data if pct > 30]
    under_represented = [(tax, name, count, pct) for tax, name, count, pct in taxonomy_data if pct < 3]

    # Generate markdown report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Taxonomy Distribution Report\n\n")

        f.write("## Overview\n\n")
        f.write(f"- **Total Concepts**: {total_concepts}\n")
        f.write(f"- **Number of Taxonomies**: {len(taxonomy_counts)}\n")
        f.write(f"- **Average Concepts per Taxonomy**: {total_concepts / len(taxonomy_counts):.1f}\n\n")

        f.write("## Distribution Summary\n\n")
        f.write("| Category | TaxonomyID | Count | Percentage | Status |\n")
        f.write("|----------|-----------|-------|------------|--------|\n")

        for tax, name, count, pct in taxonomy_data:
            status = "✅"
            if pct > 30:
                status = "⚠️ Over"
            elif pct < 3:
                status = "ℹ️ Under"
            f.write(f"| {name} | {tax} | {count} | {pct:.1f}% | {status} |\n")

        f.write("\n")

        # Visual distribution
        f.write("## Visual Distribution\n\n")
        f.write("```\n")
        for tax, name, count, pct in taxonomy_data:
            bar_length = int(pct / 2)  # Scale to fit
            bar = "█" * bar_length
            f.write(f"{tax:6s} {bar} {count:3d} ({pct:5.1f}%)\n")
        f.write("```\n\n")

        # Balance analysis
        f.write("## Balance Analysis\n\n")

        if over_represented:
            f.write("### ⚠️ Over-Represented Categories (>30%)\n\n")
            for tax, name, count, pct in over_represented:
                f.write(f"- **{name}** ({tax}): {count} concepts ({pct:.1f}%)\n")
                f.write(f"  - *Recommendation*: Consider splitting into subcategories or moving some concepts to related categories\n")
            f.write("\n")
        else:
            f.write("### ✅ No Over-Represented Categories\n\n")
            f.write("All categories are under the 30% threshold. Good balance!\n\n")

        if under_represented:
            f.write("### ℹ️ Under-Represented Categories (<3%)\n\n")
            for tax, name, count, pct in under_represented:
                f.write(f"- **{name}** ({tax}): {count} concepts ({pct:.1f}%)\n")
                f.write(f"  - *Note*: Small categories are acceptable for specialized topics\n")
            f.write("\n")

        # Detailed category breakdowns
        f.write("## Category Details\n\n")

        for tax, name, count, pct in taxonomy_data:
            f.write(f"### {name} ({tax})\n\n")
            f.write(f"**Count**: {count} concepts ({pct:.1f}%)\n\n")

            concepts = taxonomy_concepts[tax]
            concepts.sort(key=lambda x: x[0])  # Sort by ID

            f.write("**Concepts**:\n\n")
            for concept_id, concept_label in concepts[:15]:  # Show first 15
                f.write(f"- {concept_id}. {concept_label}\n")

            if len(concepts) > 15:
                f.write(f"- *...and {len(concepts) - 15} more*\n")

            f.write("\n")

        # Recommendations
        f.write("## Recommendations\n\n")

        # Check balance
        max_pct = max(pct for _, _, _, pct in taxonomy_data)
        min_pct = min(pct for _, _, _, pct in taxonomy_data if pct > 0)
        spread = max_pct - min_pct

        if spread < 15:
            f.write("- ✅ **Excellent balance**: Categories are evenly distributed (spread: {:.1f}%)\n".format(spread))
        elif spread < 25:
            f.write("- ✅ **Good balance**: Categories are reasonably distributed (spread: {:.1f}%)\n".format(spread))
        else:
            f.write("- ⚠️ **Consider rebalancing**: Large spread between categories ({:.1f}%)\n".format(spread))

        # Check for MISC
        misc_count = taxonomy_counts.get('MISC', 0)
        misc_pct = (misc_count / total_concepts) * 100 if total_concepts > 0 else 0

        if misc_pct < 2:
            f.write("- ✅ **MISC category minimal**: Good categorization specificity\n")
        else:
            f.write(f"- ⚠️ **MISC category has {misc_count} concepts**: Review for better categorization\n")

        # Educational recommendations
        f.write("\n### Educational Use Recommendations\n\n")
        f.write("- Use taxonomy categories for color-coding in graph visualizations\n")
        f.write("- Design curriculum modules based on taxonomy groupings\n")
        f.write("- Create filtered views for focused learning paths\n")
        f.write("- Use categories for assessment organization\n")
        f.write("- Enable navigation by topic area in interactive tools\n")

        f.write("\n---\n\n")
        f.write("*Report generated by learning-graph-reports/taxonomy_distribution.py*\n")

    print(f"✅ Taxonomy distribution report generated: {output_path}")
    return taxonomy_data


if __name__ == "__main__":
    import sys
    import json

    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python taxonomy-distribution.py <input_csv> <output_report.md> [taxonomy_names.json]")
        print("\nExample:")
        print("  python taxonomy-distribution.py data/concept-dependencies.csv reports/taxonomy-distribution.md")
        print("\nOptional taxonomy_names.json format:")
        print(json.dumps({
            'FOUNDATION': 'Foundation Concepts',
            'CORE': 'Core Concepts',
            'ADVANCED': 'Advanced Topics'
        }, indent=2))
        sys.exit(1)

    csv_path = sys.argv[1]
    output_path = sys.argv[2]

    # Load taxonomy names if provided
    taxonomy_names = None
    if len(sys.argv) > 3:
        config_file = sys.argv[3]
        with open(config_file, 'r', encoding='utf-8') as f:
            taxonomy_names = json.load(f)
        print(f"📋 Loaded taxonomy names from: {config_file}")

    analyze_taxonomy_distribution(csv_path, output_path, taxonomy_names)
