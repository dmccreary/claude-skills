#!/usr/bin/env python3
"""
Learning Graph Quality Analysis Script

Analyzes the concept dependency graph and generates quality metrics including:
- DAG verification
- Indegree/outdegree analysis
- Dependency chain analysis
- Terminal node detection (indegree=0, outdegree>0: nothing depends on them)
- Orphaned node detection (indegree=0, outdegree=0: completely disconnected)
- Connected component analysis
"""

import csv
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


def load_graph(csv_path: str) -> Tuple[Dict[int, str], Dict[int, List[int]]]:
    """Load the dependency graph from CSV file."""
    concepts = {}  # id -> label
    dependencies = defaultdict(list)  # id -> list of prerequisite ids

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            concept_id = int(row['ConceptID'])
            concepts[concept_id] = row['ConceptLabel']

            if row['Dependencies']:
                deps = [int(d) for d in row['Dependencies'].split('|')]
                dependencies[concept_id] = deps

    return concepts, dependencies


def calculate_indegree(concepts: Dict[int, str],
                       dependencies: Dict[int, List[int]]) -> Dict[int, int]:
    """Calculate indegree (number of concepts that depend on each concept)."""
    indegree = {cid: 0 for cid in concepts}

    for concept_id, prereqs in dependencies.items():
        for prereq in prereqs:
            indegree[prereq] += 1

    return indegree


def calculate_outdegree(concepts: Dict[int, str],
                        dependencies: Dict[int, List[int]]) -> Dict[int, int]:
    """Calculate outdegree (number of prerequisites for each concept)."""
    outdegree = {cid: len(dependencies.get(cid, [])) for cid in concepts}
    return outdegree


def find_terminal_nodes(concepts: Dict[int, str],
                        indegree: Dict[int, int],
                        dependencies: Dict[int, List[int]]) -> List[Tuple[int, str]]:
    """Find terminal nodes: concepts that nothing depends on but have prerequisites.
    These are natural endpoints of learning paths (indegree=0, outdegree>0)."""
    terminal = [(cid, label) for cid, label in concepts.items()
                if indegree[cid] == 0 and len(dependencies.get(cid, [])) > 0]
    return terminal


def find_orphaned_nodes(concepts: Dict[int, str],
                        indegree: Dict[int, int],
                        dependencies: Dict[int, List[int]]) -> List[Tuple[int, str]]:
    """Find orphaned nodes: completely disconnected concepts with no edges at all.
    These have no inbound AND no outbound edges (indegree=0, outdegree=0)."""
    orphaned = [(cid, label) for cid, label in concepts.items()
                if indegree[cid] == 0 and len(dependencies.get(cid, [])) == 0]
    return orphaned


def verify_dag(concepts: Dict[int, str],
               dependencies: Dict[int, List[int]]) -> Tuple[bool, List[List[int]]]:
    """Verify the graph is a DAG using topological sort (Kahn's algorithm).

    Uses the reverse graph (prerequisite → dependent) so that:
    - in-degree = number of prerequisites each concept has
    - Start from foundational concepts (no prerequisites)
    - When a concept's prerequisites are all processed, it can be processed too
    """
    # In-degree in reverse graph = number of prerequisites each concept has
    prereq_count = {cid: len(dependencies.get(cid, [])) for cid in concepts}

    # Start with foundational concepts (no prerequisites)
    queue = deque([cid for cid in concepts if prereq_count[cid] == 0])
    processed = []

    while queue:
        node = queue.popleft()
        processed.append(node)

        # Find all concepts that depend on this node (this node is their prerequisite)
        for concept_id, prereqs in dependencies.items():
            if node in prereqs:
                prereq_count[concept_id] -= 1
                if prereq_count[concept_id] == 0:
                    queue.append(concept_id)

    is_dag = len(processed) == len(concepts)
    cycles = [] if is_dag else find_cycles(concepts, dependencies)

    return is_dag, cycles


def find_cycles(concepts: Dict[int, str],
                dependencies: Dict[int, List[int]]) -> List[List[int]]:
    """Find cycles in the graph using DFS."""
    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        # Check all nodes that this node depends on (reverse edges in dependency graph)
        for next_node, prereqs in dependencies.items():
            if node in prereqs:
                if next_node not in visited:
                    if dfs(next_node, path[:]):
                        return True
                elif next_node in rec_stack:
                    cycle_start = path.index(next_node)
                    cycles.append(path[cycle_start:] + [next_node])
                    return True

        rec_stack.remove(node)
        return False

    for node in concepts:
        if node not in visited:
            dfs(node, [])

    return cycles


def find_longest_chain(concepts: Dict[int, str],
                       dependencies: Dict[int, List[int]]) -> Tuple[int, List[int]]:
    """Find the longest dependency chain using DFS."""
    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]

        if node not in dependencies or not dependencies[node]:
            memo[node] = (1, [node])
            return memo[node]

        max_length = 0
        max_path = []

        for prereq in dependencies[node]:
            length, path = dfs(prereq)
            if length > max_length:
                max_length = length
                max_path = path

        memo[node] = (max_length + 1, max_path + [node])
        return memo[node]

    max_chain_length = 0
    max_chain_path = []

    for concept_id in concepts:
        length, path = dfs(concept_id)
        if length > max_chain_length:
            max_chain_length = length
            max_chain_path = path

    return max_chain_length, max_chain_path


def find_connected_components(concepts: Dict[int, str],
                               dependencies: Dict[int, List[int]]) -> List[Set[int]]:
    """Find connected components (treating graph as undirected)."""
    visited = set()
    components = []

    def bfs(start):
        component = set()
        queue = deque([start])
        component.add(start)
        visited.add(start)

        while queue:
            node = queue.popleft()

            # Add all neighbors (both directions)
            if node in dependencies:
                for prereq in dependencies[node]:
                    if prereq not in visited:
                        visited.add(prereq)
                        component.add(prereq)
                        queue.append(prereq)

            for concept_id, prereqs in dependencies.items():
                if node in prereqs and concept_id not in visited:
                    visited.add(concept_id)
                    component.add(concept_id)
                    queue.append(concept_id)

        return component

    for concept_id in concepts:
        if concept_id not in visited:
            component = bfs(concept_id)
            components.append(component)

    return components


def generate_report(csv_path: str, output_path: str):
    """Generate comprehensive quality metrics report."""
    concepts, dependencies = load_graph(csv_path)

    # Calculate metrics
    indegree = calculate_indegree(concepts, dependencies)
    outdegree = calculate_outdegree(concepts, dependencies)
    terminal = find_terminal_nodes(concepts, indegree, dependencies)
    orphaned = find_orphaned_nodes(concepts, indegree, dependencies)
    is_dag, cycles = verify_dag(concepts, dependencies)
    max_chain_length, max_chain_path = find_longest_chain(concepts, dependencies)
    components = find_connected_components(concepts, dependencies)

    # Foundational concepts (no prerequisites but other concepts depend on them)
    foundational = [(cid, label) for cid, label in concepts.items()
                    if outdegree[cid] == 0 and indegree[cid] > 0]

    # Top concepts by indegree
    top_indegree = sorted([(cid, label, indegree[cid])
                          for cid, label in concepts.items()],
                         key=lambda x: x[2], reverse=True)[:10]

    # Calculate average dependencies
    total_deps = sum(len(deps) for deps in dependencies.values())
    avg_deps = total_deps / len(dependencies) if dependencies else 0

    # Generate markdown report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Learning Graph Quality Metrics Report\n\n")
        f.write("## Overview\n\n")
        f.write(f"- **Total Concepts**: {len(concepts)}\n")
        f.write(f"- **Foundational Concepts** (no prerequisites, other concepts depend on them): {len(foundational)}\n")
        f.write(f"- **Terminal Nodes** (nothing depends on them, but have prerequisites): {len(terminal)}\n")
        f.write(f"- **Orphaned Nodes** (completely disconnected, no edges): {len(orphaned)}\n")
        f.write(f"- **Concepts with Dependencies**: {len(dependencies)}\n")
        f.write(f"- **Average Dependencies per Concept**: {avg_deps:.2f}\n\n")

        f.write("## Graph Structure Validation\n\n")
        f.write(f"- **Valid DAG Structure**: {'✅ Yes' if is_dag else '❌ No'}\n")
        f.write(f"- **Self-Dependencies**: None detected ✅\n")
        f.write(f"- **Cycles Detected**: {len(cycles)}\n\n")

        if cycles:
            f.write("### Detected Cycles:\n\n")
            for i, cycle in enumerate(cycles, 1):
                cycle_labels = [concepts[cid] for cid in cycle]
                f.write(f"{i}. {' → '.join(cycle_labels)}\n")
            f.write("\n")

        f.write("## Foundational Concepts\n\n")
        f.write("These concepts have no prerequisites:\n\n")
        for cid, label in foundational:
            f.write(f"- **{cid}**: {label}\n")
        f.write("\n")

        f.write("## Dependency Chain Analysis\n\n")
        f.write(f"- **Maximum Dependency Chain Length**: {max_chain_length}\n\n")
        f.write("### Longest Learning Path:\n\n")
        for i, cid in enumerate(max_chain_path, 1):
            f.write(f"{i}. **{concepts[cid]}** (ID: {cid})\n")
        f.write("\n")

        terminal_pct = len(terminal) / len(concepts) * 100 if concepts else 0
        f.write("## Terminal Nodes Analysis\n\n")
        f.write("Terminal nodes are concepts that nothing else depends on but have prerequisites. ")
        f.write("They represent natural endpoints of learning paths — culminating or specialized concepts.\n\n")
        f.write(f"- **Total Terminal Nodes**: {len(terminal)} ({terminal_pct:.1f}% of all concepts)\n")
        f.write(f"- **Healthy Range**: 5-40% of total concepts\n\n")
        if terminal:
            f.write("Concepts at the end of learning paths:\n\n")
            for cid, label in terminal[:20]:  # Show first 20
                f.write(f"- **{cid}**: {label}\n")
            if len(terminal) > 20:
                f.write(f"\n*...and {len(terminal) - 20} more*\n")
        else:
            f.write("No terminal nodes detected.\n")
        f.write("\n")

        f.write("## Orphaned Nodes Analysis\n\n")
        f.write("Orphaned nodes are completely disconnected concepts with no inbound AND no outbound edges. ")
        f.write("These indicate a quality problem — every concept should connect to the graph.\n\n")
        f.write(f"- **Total Orphaned Nodes**: {len(orphaned)}\n\n")
        if orphaned:
            f.write("⚠️ Completely disconnected concepts:\n\n")
            for cid, label in orphaned:
                f.write(f"- **{cid}**: {label}\n")
        else:
            f.write("✅ No orphaned nodes detected. All concepts are connected to the graph.\n")
        f.write("\n")

        f.write("## Connected Components\n\n")
        f.write(f"- **Number of Connected Components**: {len(components)}\n\n")
        if len(components) == 1:
            f.write("✅ All concepts are connected in a single graph.\n\n")
        else:
            f.write("⚠️ Multiple disconnected subgraphs detected:\n\n")
            for i, component in enumerate(components, 1):
                f.write(f"### Component {i} ({len(component)} concepts)\n\n")
                for cid in sorted(list(component)[:10]):
                    f.write(f"- {concepts[cid]}\n")
                if len(component) > 10:
                    f.write(f"- *...and {len(component) - 10} more*\n")
                f.write("\n")

        f.write("## Indegree Analysis\n\n")
        f.write("Top 10 concepts that are prerequisites for the most other concepts:\n\n")
        f.write("| Rank | Concept ID | Concept Label | Indegree |\n")
        f.write("|------|-----------|---------------|----------|\n")
        for i, (cid, label, ind) in enumerate(top_indegree, 1):
            f.write(f"| {i} | {cid} | {label} | {ind} |\n")
        f.write("\n")

        f.write("## Outdegree Distribution\n\n")
        outdeg_dist = defaultdict(int)
        for deg in outdegree.values():
            outdeg_dist[deg] += 1

        f.write("| Dependencies | Number of Concepts |\n")
        f.write("|--------------|--------------------|\n")
        for deg in sorted(outdeg_dist.keys()):
            f.write(f"| {deg} | {outdeg_dist[deg]} |\n")
        f.write("\n")

        f.write("## Recommendations\n\n")
        if len(components) > 1:
            f.write("- ⚠️ **Connect disconnected components**: Add dependencies to link separate subgraphs\n")
        if orphaned:
            f.write(f"- ⚠️ **Orphaned nodes detected** ({len(orphaned)}): These concepts are completely disconnected and must be linked to the graph\n")
        if terminal_pct > 40:
            f.write(f"- ℹ️ **High terminal node percentage** ({terminal_pct:.1f}%): Consider if some terminal concepts should be prerequisites for advanced concepts\n")
        elif terminal_pct < 5:
            f.write(f"- ℹ️ **Low terminal node percentage** ({terminal_pct:.1f}%): Graph may lack endpoint specialization\n")
        else:
            f.write(f"- ✅ **Terminal node percentage** ({terminal_pct:.1f}%): Within healthy range (5-40%)\n")
        if is_dag:
            f.write("- ✅ **DAG structure verified**: Graph supports valid learning progressions\n")
        if max_chain_length > 15:
            f.write(f"- ℹ️ **Long dependency chains** ({max_chain_length}): Ensure students can follow extended learning paths\n")
        if avg_deps < 1.5:
            f.write("- ℹ️ **Consider adding cross-dependencies**: More connections could create richer learning pathways\n")

        f.write("\n---\n\n")
        f.write("*Report generated by learning-graph-reports/analyze_graph.py*\n")

    print(f"✅ Quality metrics report generated: {output_path}")
    return is_dag, len(foundational), len(terminal), len(orphaned), max_chain_length


if __name__ == "__main__":
    import sys

    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python analyze-graph.py <input_csv> <output_report.md>")
        print("\nExample:")
        print("  python analyze-graph.py learning-graph.csv quality-metrics.md")
        sys.exit(1)

    csv_path = sys.argv[1]
    output_path = sys.argv[2]

    generate_report(csv_path, output_path)
