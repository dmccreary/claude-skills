# Diagram Reports Generator

> **Legacy snapshot.** The active route is
> `microsim-utils/references/diagram-reports.md`. It inventories only legacy
> `#### Diagram:` specification blocks and must not be used as a rendered-visual
> inventory or instructional-quality gate.

The diagram-reports-generator skill automatically generates comprehensive reports
of all diagrams and MicroSims in an intelligent textbook by analyzing chapter
markdown files. It creates both table and detailed views organized by chapter.

## Key Capabilities

This skill produces two report files:

1. **diagram-table.md** - Quick reference table view of all diagrams
2. **diagram-details.md** - Detailed view organized by chapter

## Information Tracked

For each diagram or MicroSim, the reports include:

- **Status**: Planned, In Progress, Complete
- **Planning Heuristic**: keyword-derived Easy, Medium, Hard, or Very Hard; not a quality score or measured estimate
- **Bloom's Taxonomy Level**: Remember through Create
- **UI Keyword Mentions**: text occurrences in the source specification, not implemented controls
- **Implementation Type**: Static diagram, Interactive MicroSim

## When to Use

Use this skill when:

- Auditing all diagrams and MicroSims across chapters
- Tracking implementation status of visual elements
- Analyzing complexity and Bloom's distribution
- Updating documentation after adding new content
- Generating reports for instructors or content creators

## Workflow

The skill follows these steps:

1. Install the diagram report generator script if not present
2. Verify project structure (chapters directory, learning-graph directory)
3. Run the Python script to analyze markdown files
4. Generate both table and detail report formats
5. Update mkdocs.yml navigation if needed

## Prerequisites

The textbook project should have:

- Chapter directories in `docs/chapters/` with numbered naming
- Diagram specifications in chapter markdown files
- Output directory at `docs/learning-graph/`

## Integration

This skill works best after chapters have been created with diagram specifications.
It helps track progress on converting specifications into actual implementations
and provides visibility into the visual element coverage across the textbook.
