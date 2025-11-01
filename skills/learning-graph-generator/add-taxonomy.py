#!/usr/bin/env python3
"""
Add Taxonomy IDs to Concept Dependency CSV

Reads the concept dependency CSV and assigns appropriate taxonomy IDs
based on concept labels and position in the concept hierarchy.
"""

import csv
import re
from typing import Dict, List


def assign_taxonomy(concept_id: int, concept_label: str, taxonomy_config: dict = None) -> str:
    """
    Assign taxonomy ID based on concept ID and label.

    Args:
        concept_id: The concept identifier
        concept_label: The concept name/label
        taxonomy_config: Optional dictionary mapping taxonomy IDs to their configurations.
                        Each config contains 'range' (tuple) and 'keywords' (list).
                        If not provided, returns 'MISC' for all concepts.

    Returns:
        Taxonomy ID string

    Example taxonomy_config:
    {
        'MATH': {
            'range': (1, 20),
            'keywords': ['number', 'algebra', 'calculus', 'derivative']
        },
        'CORE': {
            'range': (21, 50),
            'keywords': ['fundamental', 'basic', 'foundation']
        }
    }
    """
    if taxonomy_config is None:
        return 'MISC'

    label_lower = concept_label.lower()

    # Check each taxonomy in order
    for tax_id, config in taxonomy_config.items():
        range_start, range_end = config.get('range', (0, 0))
        keywords = config.get('keywords', [])
        exclude_keywords = config.get('exclude', [])

        # Check if in range or matches keywords
        in_range = range_start <= concept_id <= range_end
        matches_keywords = any(kw in label_lower for kw in keywords)
        has_exclusions = any(kw in label_lower for kw in exclude_keywords)

        if (in_range or matches_keywords) and not has_exclusions:
            return tax_id

    # Default to MISC
    return 'MISC'


def add_taxonomy_to_csv(input_csv: str, output_csv: str, taxonomy_config: dict = None):
    """
    Read CSV, add taxonomy column, and write updated CSV.

    Args:
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file
        taxonomy_config: Optional taxonomy configuration dictionary

    Returns:
        Dictionary of taxonomy counts
    """
    rows = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            concept_id = int(row['ConceptID'])
            concept_label = row['ConceptLabel']
            taxonomy_id = assign_taxonomy(concept_id, concept_label, taxonomy_config)

            rows.append({
                'ConceptID': concept_id,
                'ConceptLabel': concept_label,
                'Dependencies': row['Dependencies'],
                'TaxonomyID': taxonomy_id
            })

    # Write updated CSV
    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['ConceptID', 'ConceptLabel', 'Dependencies', 'TaxonomyID']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Count concepts per taxonomy
    taxonomy_counts = {}
    for row in rows:
        tax = row['TaxonomyID']
        taxonomy_counts[tax] = taxonomy_counts.get(tax, 0) + 1

    print(f"✅ Taxonomy added to CSV: {output_csv}")
    print(f"\n📊 Taxonomy Distribution:")
    for tax in sorted(taxonomy_counts.keys()):
        count = taxonomy_counts[tax]
        percentage = (count / len(rows)) * 100
        print(f"  {tax:6s}: {count:3d} concepts ({percentage:5.1f}%)")

    return taxonomy_counts


if __name__ == "__main__":
    import sys
    import json

    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python add-taxonomy.py <input_csv> <output_csv> [taxonomy_config.json]")
        print("\nExample taxonomy_config.json format:")
        print(json.dumps({
            'FOUNDATION': {
                'range': [1, 20],
                'keywords': ['basic', 'fundamental', 'introduction'],
                'exclude': []
            },
            'ADVANCED': {
                'range': [21, 50],
                'keywords': ['advanced', 'complex', 'detailed'],
                'exclude': []
            }
        }, indent=2))
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    # Load taxonomy config if provided
    taxonomy_config = None
    if len(sys.argv) > 3:
        config_file = sys.argv[3]
        with open(config_file, 'r', encoding='utf-8') as f:
            taxonomy_config = json.load(f)
        print(f"📋 Loaded taxonomy config from: {config_file}")
    else:
        print("⚠️  No taxonomy config provided. All concepts will be marked as 'MISC'.")
        print("   Provide a taxonomy config JSON file as the third argument.")

    taxonomy_counts = add_taxonomy_to_csv(input_csv, output_csv, taxonomy_config)
