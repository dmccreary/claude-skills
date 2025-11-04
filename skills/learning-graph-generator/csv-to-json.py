#!/usr/bin/env python3
"""
Convert CSV Learning Graph to JSON for vis-network.js
Converts the concept dependency CSV into the JSON format
used by the existing graph viewer (vis.js network format).
"""

import csv
import json
from typing import Dict, List
from datetime import datetime


def csv_to_json(csv_path: str, json_path: str, color_config: dict = None, metadata: dict = None):
    """
    Convert CSV dependency graph to vis.js JSON format with metadata and groups.

    Args:
        csv_path: Path to input CSV file with columns: ConceptID, ConceptLabel, Dependencies, TaxonomyID
        json_path: Path to output JSON file
        color_config: Optional dictionary mapping taxonomy IDs to colors.
                     If not provided, uses default color scheme.
        metadata: Optional dictionary with metadata fields (title, description, creator, etc.)
                 If not provided, creates minimal metadata.
    """
    # Default taxonomy group colors for visualization
    # Supports both text codes (FOUND, DEF, etc.) and numeric IDs (1, 2, etc.)
    default_colors = {
        # Text codes
        'FOUND': 'red',
        'DEF': 'orange',
        'CORE': 'gold',
        'INTER': 'green',
        'ADV': 'blue',
        'APPL': 'cyan',
        'SPEC': 'indigo',
        'PROJ': 'violet',
        'CAP': 'gray',
        'MISC': 'indigo',
        # Numeric IDs (same mapping)
        '1': 'red',
        '2': 'orange',
        '3': 'gold',
        '4': 'green',
        '5': 'blue',
        '6': 'cyan',
        '7': 'indigo',
        '8': 'violet',
        '9': 'gray',
        '10': 'brown',
    }

    taxonomy_colors = color_config if color_config is not None else default_colors

    # Taxonomy ID to classifier name mapping
    # Supports both text codes (FOUND, DEF, etc.) and numeric IDs (1, 2, etc.)
    # These are the display names (classifierName in schema) for each taxonomy
    taxonomy_names = {
        # Text codes
        'FOUND': 'Foundation Concepts',
        'DEF': 'Definitions',
        'CORE': 'Core Concepts',
        'INTER': 'Intermediate',
        'ADV': 'Advanced',
        'APPL': 'Applied',
        'SPEC': 'Specialized',
        'CAP': 'Capstone Projects',
        'PROJ': 'Project Ideas',
        'MISC': 'Miscellaneous Concepts',
        # Numeric IDs (common mapping)
        '1': 'Foundation Concepts',
        '2': 'Definitions',
        '3': 'Core Concepts',
        '4': 'Intermediate',
        '5': 'Advanced',
        '6': 'Applied',
        '7': 'Specialized',
        '8': 'Capstone Projects',
        '9': 'Miscellaneous Concepts',
        '10': 'Extended Topics',
    }

    # Read CSV
    nodes = []
    edges = []
    foundational_ids = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            concept_id = int(row['ConceptID'])
            # Support both ConceptLabel and ConceptName column names
            label = row.get('ConceptLabel') or row.get('ConceptName', '')
            taxonomy = row['TaxonomyID']
            dependencies_str = row['Dependencies']

            # Determine if foundational (no dependencies)
            is_foundational = (dependencies_str == '')
            if is_foundational:
                foundational_ids.append(concept_id)

            # Create node - use taxonomy ID directly as group reference
            node = {
                'id': concept_id,
                'label': label,
                'group': taxonomy
            }

            # Special styling for foundational concepts
            if is_foundational:
                node['shape'] = 'box'

            nodes.append(node)

            # Create edges (from concept to its prerequisites)
            if dependencies_str:
                prereq_ids = [int(pid) for pid in dependencies_str.split('|')]
                for prereq_id in prereq_ids:
                    edge = {
                        'from': concept_id,
                        'to': prereq_id
                    }
                    edges.append(edge)

    # Create metadata section
    default_metadata = {
        'title': 'Learning Graph',
        'description': f'Learning graph with {len(nodes)} concepts generated from CSV',
        'creator': 'CSV to JSON Converter',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'version': '1.0',
        'format': 'Learning Graph JSON v1.0',
        'schema': 'https://raw.githubusercontent.com/dmccreary/learning-graphs/refs/heads/main/src/schema/learning-graph-schema.json',
        'license': 'CC BY-NC-SA 4.0 DEED'
    }

    # Merge user-provided metadata with defaults
    if metadata:
        default_metadata.update(metadata)

    # Create groups section from taxonomy colors
    groups = {}

    # Determine which taxonomy IDs are actually used
    used_taxonomies = set(node['group'] for node in nodes)

    for tax_id, color in taxonomy_colors.items():
        # Only include groups that are actually used
        if tax_id in used_taxonomies:
            # Get the classifier name for this taxonomy
            classifier_name = taxonomy_names.get(tax_id, tax_id)

            # Determine font color based on background color
            # Dark colors need white text
            dark_colors = ['red', 'blue', 'indigo', 'violet', 'cyan']
            font_color = 'white' if color in dark_colors else 'black'

            groups[tax_id] = {
                'classifierName': classifier_name,
                'color': color,
                'font': {
                    'color': font_color
                }
            }

    # Create final JSON structure
    graph_data = {
        'metadata': default_metadata,
        'groups': groups,
        'nodes': nodes,
        'edges': edges
    }

    # Write JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=2)

    print(f"✅ JSON graph created: {json_path}")
    print(f"   - Title: {default_metadata['title']}")
    print(f"   - {len(groups)} groups/taxonomies")
    print(f"   - {len(nodes)} nodes")
    print(f"   - {len(edges)} edges")
    print(f"   - {len(foundational_ids)} foundational concepts")
    print(f"\nFoundational concept IDs: {foundational_ids}")
    print(f"Groups: {list(groups.keys())}")

    return graph_data


def create_taxonomy_legend(color_config: dict = None, taxonomy_names: dict = None):
    """
    Generate a legend of taxonomy colors for documentation.

    Args:
        color_config: Dictionary mapping taxonomy IDs to colors
        taxonomy_names: Dictionary mapping taxonomy IDs to classifier names
    """
    default_colors = {
        'FOUND': 'red',
        'DEF': 'orange',
        'CORE': 'gold',
        'INTER': 'green',
        'ADV': 'blue',
        'APPL': 'cyan',
        'SPEC': 'indigo',
        'PROJ': 'violet',
        'CAP': 'gray',
        'MISC': 'indigo',
    }

    default_names = {
        'FOUND': 'Foundation Concepts',
        'DEF': 'Definitions',
        'CORE': 'Core Concepts',
        'INTER': 'Intermediate',
        'ADV': 'Advanced',
        'APPL': 'Applied',
        'SPEC': 'Specialized',
        'PROJ': 'Project Ideas',
        'CAP': 'Capstone Projects',
        'MISC': 'Miscellaneous Concepts',
    }

    colors = color_config if color_config is not None else default_colors
    names = taxonomy_names if taxonomy_names is not None else default_names

    print("\n## Taxonomy Color Legend\n")
    print("| TaxonomyID | Category | Color |")
    print("|------------|----------|-------|")
    for tax_id in sorted(colors.keys()):
        name = names.get(tax_id, tax_id)
        color = colors[tax_id]
        print(f"| {tax_id} | {name} | {color} |")


if __name__ == "__main__":
    import sys

    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python csv-to-json.py <input_csv> <output_json> [color_config.json] [metadata.json]")
        print("Looking for CSV column names: ConceptID, ConceptLabel, Dependencies, TaxonomyID")
        print("\nExample:")
        print("   python csv-to-json.py learning-graph.csv learning-graph.json")
        print("\nOptional color_config.json format:")
        print(json.dumps({
            'FOUND': 'red',
            'CORE': 'yellow',
            'ADV': 'blue'
        }, indent=2))
        print("\nOptional metadata.json format:")
        print(json.dumps({
            'title': 'My Learning Graph',
            'description': 'A comprehensive learning graph',
            'creator': 'Your Name',
            'license': 'CC BY 4.0'
        }, indent=2))
        sys.exit(1)

    csv_path = sys.argv[1]
    json_path = sys.argv[2]

    # Load color config if provided
    color_config = None
    if len(sys.argv) > 3:
        config_file = sys.argv[3]
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                color_config = json.load(f)
            print(f"📋 Loaded color config from: {config_file}")
        except FileNotFoundError:
            print(f"⚠️  Color config file not found: {config_file}, using defaults")

    # Load metadata config if provided
    metadata = None
    if len(sys.argv) > 4:
        metadata_file = sys.argv[4]
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            print(f"📋 Loaded metadata from: {metadata_file}")
        except FileNotFoundError:
            print(f"⚠️  Metadata file not found: {metadata_file}, using defaults")

    graph_data = csv_to_json(csv_path, json_path, color_config, metadata)
    create_taxonomy_legend(color_config)

    print("\n✅ CSV to JSON format complete.  Ready to use with graph-viewer!")
    print(f"   Validate with: ./src/schema/validate-learning-graph.sh {json_path}")
