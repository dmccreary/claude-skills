# Terminal Nodes Identification Chart

**Chapter:** 06 - Learning Graph Quality Validation
**Generator:** chartjs-generator
**Match Score:** 97/100
**Difficulty:** Medium

## Specification

<summary>Terminal Nodes Identification Chart</summary>
    Type: chart

    Chart type: Scatter plot

    Purpose: Visualize concept connectivity by showing indegree vs outdegree for all concepts, highlighting terminal nodes

    X-axis: Indegree (number of prerequisites, 0-8)
    Y-axis: Outdegree (number of dependents, 0-12)

    Data series:
    1. Foundational concepts (green dots, indegree = 0, outdegree > 0)
       - Example: "Introduction to Learning Graphs" (0, 8)
       - Example: "What is a Concept?" (0, 6)

    2. Intermediate concepts (blue dots, indegree > 0, outdegree > 0)
       - Scatter of 150+ points representing well-connected concepts
       - Example: "DAG Validation" (2, 4)

    3. Terminal concepts (red dots, indegree > 0, outdegree = 0)
       - Example: "Advanced Quality Metrics" (5, 0)
       - Example: "Future of Learning Graphs" (3, 0)
       - Show approximately 15-20 red dots

    Title: "Concept Connectivity Analysis: Indegree vs Outdegree"

    Annotations:
    - Vertical line at outdegree=0 labeled "Terminal Zone"
    - Horizontal line at indegree=0 labeled "Foundation Zone"
    - Callout: "12% terminal (healthy range: 5-15%)"

    Legend: Position top-right with color coding explanation

    Implementation: Chart.js scatter plot with color-coded point categories