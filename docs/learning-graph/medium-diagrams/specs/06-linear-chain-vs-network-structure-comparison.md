# Linear Chain vs Network Structure Comparison

**Chapter:** 06 - Learning Graph Quality Validation
**Generator:** vis-network
**Match Score:** 95/100
**Difficulty:** Medium

## Specification

<summary>Linear Chain vs Network Structure Comparison</summary>
    Type: diagram

    Purpose: Compare linear chain structure (poor) with network structure (good) for learning graphs

    Layout: Two side-by-side network diagrams

    Left diagram - "Linear Chain Structure (Poor)":
    - 10 concepts arranged vertically
    - Single path: Concept 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10
    - All nodes colored orange
    - Title: "Linear Chain: 100% of concepts in single path"
    - Caption: "No flexibility, single learning route"

    Right diagram - "Network Structure (Good)":
    - Same 10 concepts arranged in a network
    - Multiple paths and connections:
      - Concept 1 (foundation) connects to 2, 3, 4
      - Concepts 2, 3, 4 are parallel (same level)
      - Concept 5 depends on 2 and 3
      - Concept 6 depends on 3 and 4
      - Concepts 7, 8 depend on various combinations
      - Concepts 9, 10 are terminal (culminating concepts)
    - Nodes colored by depth: green (foundation), blue (intermediate), purple (advanced)
    - Title: "Network Structure: 40% linear, 60% networked"
    - Caption: "Multiple paths, cross-concept integration"

    Visual style: Network diagrams with nodes as circles, directed arrows showing dependencies

    Annotations:
    - Left: Red "X" indicating poor structure
    - Right: Green checkmark indicating good structure
    - Arrow between diagrams showing "Refactor to add cross-dependencies"

    Color scheme: Orange for linear, green/blue/purple gradient for network depth

    Implementation: SVG network diagram with positioned nodes and edges