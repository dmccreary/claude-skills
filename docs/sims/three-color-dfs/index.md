---
title: Three-Color DFS Cycle Detection
description: Interactive vis-network visualization demonstrating the three-color DFS algorithm for detecting cycles in learning graphs
---

# Three-Color DFS Cycle Detection

<iframe src="main.html" width="100%" height="650px" scrolling="no"></iframe>

[Run Three-Color DFS MicroSim](main.html){ .md-button .md-button--primary }

This MicroSim illustrates the **three-color DFS algorithm** used to detect cycles in learning graph dependency structures. Understanding this algorithm is essential for validating that learning graphs maintain proper Directed Acyclic Graph (DAG) structure.

## The Three-Color Algorithm

The algorithm assigns one of three colors to each node during depth-first search traversal:

### Node Colors

| Color | Visual | State | Meaning |
|-------|--------|-------|---------|
| White | Gray circle | Unvisited | Node has not been explored yet |
| Gray | Yellow circle | In Progress | Node is currently on the DFS stack (being explored) |
| Black | Green circle | Completed | Node and all its descendants have been fully explored |

### Cycle Detection

A **cycle is detected** when we encounter an edge pointing to a **Gray** node. This means we've found a path back to a node that's currently being explored - a back edge that creates a cycle.

In the visualization above:

- **Recursion → Loops** is a back edge (shown in red)
- Both "Loops" and "Recursion" are Gray (in progress)
- This indicates a cycle: Loops → Recursion → Loops

## Algorithm Steps

1. Start with all nodes colored White (unvisited)
2. For each unvisited node, begin DFS:
   - Color the current node Gray (in progress)
   - Push it onto the DFS stack
   - For each neighbor:
     - If White: recurse
     - If Gray: **CYCLE DETECTED!** (back edge found)
     - If Black: skip (already processed)
   - Color the current node Black (completed)
   - Pop from stack

## Why This Matters for Learning Graphs

Learning graphs must be **Directed Acyclic Graphs (DAGs)** because:

- Concepts must be taught in a valid order
- Prerequisites must come before dependent concepts
- Cycles would create impossible learning sequences

For example, if "Recursion requires Loops" and "Loops requires Recursion", students could never begin learning either concept.

## Pseudocode

```python
def has_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY  # Mark as in-progress

        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True  # Back edge found - cycle!
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True

        color[node] = BLACK  # Mark as completed
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    return False
```

## Time Complexity

- **Time**: O(V + E) where V = vertices, E = edges
- **Space**: O(V) for the color array and recursion stack

This is optimal for cycle detection in directed graphs.

## Educational Applications

Use this visualization to:

- Understand DFS traversal order
- Visualize how the stack grows and shrinks
- Identify back edges that indicate cycles
- Learn why DAG structure is essential for learning graphs
- Debug cycle detection issues in learning graph validators

## Technical Notes

This MicroSim is built with:

- **vis-network.js** for graph visualization
- Custom CSS layout with 70/30 split view
- Responsive design for various screen sizes
- Navigation buttons enabled (mouse zoom/pan disabled for iframe embedding)
