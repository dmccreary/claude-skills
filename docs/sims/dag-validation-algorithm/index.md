# DAG Validation Algorithm Visualization

This interactive visualization demonstrates the three-color DFS (Depth-First Search) algorithm used to detect cycles in learning graph dependencies.

## Interactive Diagram

<iframe src="main.html" width="100%" height="700px" style="border: 2px solid #ccc; border-radius: 8px;"></iframe>

## Overview

The visualization shows:
- **White nodes:** Unvisited concepts
- **Gray nodes:** Currently being explored (on the DFS stack)
- **Black nodes:** Fully explored
- **Red edge:** Indicates a cycle (back edge)

When an edge points to a gray node, a cycle is detected, invalidating the DAG structure.
