# Average Dependencies Distribution Bar Chart

**Chapter:** 06 - Learning Graph Quality Validation
**Generator:** chartjs-generator
**Match Score:** 98/100
**Difficulty:** Medium

## Specification

<summary>Average Dependencies Distribution Bar Chart</summary>
    Type: chart

    Chart type: Histogram (bar chart)

    Purpose: Show distribution of prerequisite counts across all concepts in the learning graph

    X-axis: Number of prerequisites (0, 1, 2, 3, 4, 5, 6, 7, 8+)
    Y-axis: Number of concepts

    Data (example for 200-concept graph):
    - 0 prerequisites: 12 concepts (foundational)
    - 1 prerequisite: 45 concepts
    - 2 prerequisites: 58 concepts
    - 3 prerequisites: 42 concepts
    - 4 prerequisites: 25 concepts
    - 5 prerequisites: 12 concepts
    - 6 prerequisites: 4 concepts
    - 7 prerequisites: 2 concepts
    - 8+ prerequisites: 0 concepts

    Title: "Prerequisite Distribution Across Learning Graph"

    Calculated metrics displayed below chart:
    - Total concepts: 200
    - Total dependencies: 620
    - Average dependencies: 3.1 per concept
    - Median: 2
    - Mode: 2

    Annotations:
    - Shaded region (2-4 prerequisites) in light green labeled "Optimal Range"
    - Average line (vertical) at 3.1 in blue
    - Callout: "84% of concepts in optimal range (1-5 prerequisites)"

    Color scheme: Gold bars with green shading for optimal range

    Implementation: Chart.js bar chart with annotations