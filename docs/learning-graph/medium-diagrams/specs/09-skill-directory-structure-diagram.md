# Skill Directory Structure Diagram

**Chapter:** 09 - Claude Skills Architecture Development
**Generator:** mermaid-generator
**Match Score:** 93/100
**Difficulty:** Medium

## Specification

<summary>Skill Directory Structure Diagram</summary>
    Type: diagram

    Purpose: Illustrate the standard directory organization for a Claude Skill

    Components to show:
    - Root directory named "skill-name/" (blue folder icon)
    - SKILL.md file (primary file, highlighted in gold)
    - Subdirectories branching from root:
      - scripts/ (contains Python files)
      - templates/ (contains template files)
      - references/ (contains .md documentation)
      - examples/ (contains example files)
    - Files within subdirectories:
      - scripts/analyze-graph.py
      - scripts/csv-to-json.py
      - templates/report-template.md
      - references/reading-levels.md
      - examples/sample-output.json

    Connections:
    - SKILL.md references supporting files (dotted arrows)
    - Arrow from SKILL.md to scripts/ labeled "Executes"
    - Arrow from SKILL.md to references/ labeled "Loads"
    - Arrow from SKILL.md to templates/ labeled "Uses"

    Style: File system tree diagram with folder and file icons

    Labels:
    - "SKILL.md: Entry point & workflow"
    - "scripts/: Executable automation"
    - "templates/: Content patterns"
    - "references/: Context documents"
    - "examples/: Sample I/O"

    Color scheme:
    - Gold for SKILL.md (primary importance)
    - Blue for directories
    - Green for Python scripts
    - Purple for documentation files

    Implementation: Mermaid.js graph or custom SVG diagram