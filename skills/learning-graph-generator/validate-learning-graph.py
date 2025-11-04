#!/usr/bin/env python3
"""
validate-learning-graph.py
Validates a learning graph JSON file against the learning-graph-schema.json

Usage: python3 validate-learning-graph.py <data-file> <schema-file>
"""

import json
import sys
from pathlib import Path

# ANSI color codes
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color

def validate_learning_graph(data_path, schema_path):
    """Validate a learning graph JSON file against the schema."""

    # Try to import jsonschema
    try:
        import jsonschema
        from jsonschema import validate, ValidationError, SchemaError
    except ImportError:
        print(f"{RED}Error: jsonschema library not found{NC}")
        print("\nPlease install it with:")
        print("  pip install jsonschema")
        print("\nOr with conda:")
        print("  conda install -c conda-forge jsonschema")
        return False

    # Load schema
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{RED}✗ Schema file is not valid JSON: {e}{NC}")
        return False
    except Exception as e:
        print(f"{RED}✗ Error reading schema file: {e}{NC}")
        return False

    # Load data
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{RED}✗ Data file is not valid JSON: {e}{NC}")
        return False
    except Exception as e:
        print(f"{RED}✗ Error reading data file: {e}{NC}")
        return False

    # Validate
    try:
        validate(instance=data, schema=schema)
        print(f"{GREEN}✓ Validation successful!{NC}")
        print("")
        print("Summary:")
        print(f"  Title: {data.get('metadata', {}).get('title', 'N/A')}")
        print(f"  Creator: {data.get('metadata', {}).get('creator', 'N/A')}")
        print(f"  Version: {data.get('metadata', {}).get('version', 'N/A')}")
        print(f"  Date: {data.get('metadata', {}).get('date', 'N/A')}")
        print(f"  License: {data.get('metadata', {}).get('license', 'N/A')}")
        print(f"  Groups: {len(data.get('groups', {}))}")
        print(f"  Nodes: {len(data.get('nodes', []))}")
        print(f"  Edges: {len(data.get('edges', []))}")

        # Check for orphan nodes
        if 'nodes' in data and 'edges' in data:
            node_ids = {node['id'] for node in data['nodes']}
            connected_ids = set()
            for edge in data['edges']:
                connected_ids.add(edge['from'])
                connected_ids.add(edge['to'])
            orphans = node_ids - connected_ids
            if orphans:
                print(f"  {YELLOW}Orphan nodes: {len(orphans)} (nodes with no connections){NC}")
                if len(orphans) <= 10:
                    orphan_labels = [node['label'] for node in data['nodes'] if node['id'] in orphans]
                    print(f"    {', '.join(orphan_labels)}")
            else:
                print(f"  Orphan nodes: 0")

        # Check for duplicate node IDs
        node_ids_list = [node['id'] for node in data['nodes']]
        if len(node_ids_list) != len(set(node_ids_list)):
            duplicates = [id for id in node_ids_list if node_ids_list.count(id) > 1]
            print(f"  {RED}Warning: Duplicate node IDs found: {set(duplicates)}{NC}")

        # Check for edges referencing non-existent nodes
        if 'nodes' in data and 'edges' in data:
            node_ids = {node['id'] for node in data['nodes']}
            invalid_edges = []
            for edge in data['edges']:
                if edge['from'] not in node_ids:
                    invalid_edges.append(f"Edge from {edge['from']} -> {edge['to']}: source node {edge['from']} doesn't exist")
                if edge['to'] not in node_ids:
                    invalid_edges.append(f"Edge from {edge['from']} -> {edge['to']}: target node {edge['to']} doesn't exist")
            if invalid_edges:
                print(f"  {RED}Warning: Invalid edges found:{NC}")
                for invalid in invalid_edges[:5]:  # Show first 5
                    print(f"    - {invalid}")
                if len(invalid_edges) > 5:
                    print(f"    ... and {len(invalid_edges) - 5} more")

        return True

    except ValidationError as e:
        print(f"{RED}✗ Validation failed!{NC}")
        print("")
        print(f"Error path: {' -> '.join(str(p) for p in e.absolute_path)}")
        print(f"Error: {e.message}")
        if e.context:
            print("\nAdditional errors:")
            for suberror in e.context:
                print(f"  - {suberror.message}")
        return False

    except SchemaError as e:
        print(f"{RED}✗ Schema itself is invalid: {e}{NC}")
        return False

    except Exception as e:
        print(f"{RED}✗ Unexpected error during validation: {e}{NC}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print(f"{RED}Error: Wrong number of arguments{NC}")
        print(f"Usage: {sys.argv[0]} <data-file> <schema-file>")
        sys.exit(1)

    data_file = sys.argv[1]
    schema_file = sys.argv[2]

    # Validate the learning graph
    success = validate_learning_graph(data_file, schema_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
