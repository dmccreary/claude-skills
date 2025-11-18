# MicroSim File Relationship Diagram

**Chapter:** 12 - Interactive Elements Microsims
**Generator:** mermaid-generator
**Match Score:** 93/100
**Difficulty:** Easy

## Specification

<summary>MicroSim File Relationship Diagram</summary>
    Type: diagram

    Purpose: Show how the three core MicroSim files relate to each other and integrate into the MkDocs textbook

    Components to show:
    - MkDocs Navigation (top level, light gray box)
    - index.md (blue document icon, within MkDocs)
    - iframe element (orange rounded box, within index.md)
    - main.html (green document icon, pointed to by iframe)
    - p5.js simulation (red canvas, within main.html)
    - metadata.json (purple document icon, separate)
    - Learning Management System (optional, dotted line from metadata.json)

    Connections:
    - MkDocs Navigation → index.md (solid arrow, "includes")
    - index.md → iframe element (solid arrow, "contains")
    - iframe element → main.html (solid arrow, "embeds")
    - main.html → p5.js simulation (solid arrow, "renders")
    - metadata.json → Learning Management System (dotted arrow, "can export to")
    - metadata.json → index.md (dotted arrow, "describes")

    Style: Block diagram with document icons and containers

    Labels:
    - "Student navigates here" near index.md
    - "Sandbox isolation" near iframe
    - "Self-contained, interactive" near main.html
    - "Discovery & cataloging" near metadata.json

    Annotations:
    - Note near iframe: "Provides security boundary"
    - Note near main.html: "Loads p5.js from CDN"

    Color scheme: Blue for documentation, green for code, purple for metadata, orange for integration

    Implementation: Block diagram with icons