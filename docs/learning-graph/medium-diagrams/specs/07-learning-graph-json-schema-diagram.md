# Learning Graph JSON Schema Diagram

**Chapter:** 07 - Taxonomy Data Formats
**Generator:** mermaid-generator
**Match Score:** 92/100
**Difficulty:** Medium

## Specification

<summary>Learning Graph JSON Schema Diagram</summary>
    Type: diagram

    Purpose: Visualize the hierarchical structure of the learning graph JSON format

    Layout: Tree diagram showing nested structure

    Components:
    - Root: "learning-graph.json" (gold rounded rectangle)
      ├─ "metadata" (blue rounded rectangle)
      │  ├─ title: string
      │  ├─ description: string
      │  ├─ creator: string
      │  ├─ date: string (ISO 8601)
      │  ├─ version: string
      │  ├─ format: string
      │  └─ license: string
      │
      ├─ "groups" (green rounded rectangle)
      │  ├─ FOUND: {color, font, shape}
      │  ├─ BASIC: {color, font, shape}
      │  └─ ... (other taxonomy groups)
      │
      ├─ "nodes" (purple rounded rectangle)
      │  ├─ [0]: {id: number, label: string, group: string}
      │  ├─ [1]: {id: number, label: string, group: string}
      │  └─ ... (array of 200 concept objects)
      │
      └─ "edges" (orange rounded rectangle)
         ├─ [0]: {from: number, to: number}
         ├─ [1]: {from: number, to: number}
         └─ ... (array of dependency relationships)

    Visual style: Tree diagram with connecting lines

    Color coding:
    - Gold: Root document
    - Blue: Metadata section
    - Green: Groups/styling section
    - Purple: Nodes/content section
    - Orange: Edges/relationships section

    Annotations:
    - "Required by vis-network" label pointing to nodes and edges
    - "Dublin Core metadata" label pointing to metadata section
    - "Visual styling" label pointing to groups section
    - "~200 objects" annotation on nodes array
    - "~600 objects" annotation on edges array (for 200-concept graph with avg 3 dependencies)

    Implementation: SVG tree diagram with labeled boxes and connecting lines