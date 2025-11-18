# Adding Taxonomy to CSV Workflow Diagram

**Chapter:** 07 - Taxonomy Data Formats
**Generator:** mermaid-generator
**Match Score:** 94/100
**Difficulty:** Medium

## Specification

<summary>Adding Taxonomy to CSV Workflow Diagram</summary>
    Type: workflow

    Purpose: Show the step-by-step process of adding taxonomy information to an existing learning graph CSV

    Visual style: Flowchart with process rectangles and decision diamonds

    Steps:
    1. Start: "Learning Graph CSV without TaxonomyID"
       Hover text: "Existing CSV with ConceptID, ConceptLabel, Dependencies columns only"

    2. Process: "Identify Natural Categories"
       Hover text: "Review all concept labels and group by topic, domain, or complexity"

    3. Process: "Design TaxonomyID Abbreviations"
       Hover text: "Create 3-5 letter codes (FOUND, BASIC, ARCH, etc.)"

    4. Decision: "Use automated categorization?"
       Hover text: "Choose between manual assignment or add-taxonomy.py script"

    5a. Process: "Run add-taxonomy.py" (if automated)
        Hover text: "Script uses keyword matching to suggest categories"

    5b. Process: "Manually add TaxonomyID column" (if manual)
        Hover text: "Insert column in spreadsheet, assign each concept"

    6. Process: "Review and adjust assignments"
       Hover text: "Check that categorization makes logical sense"

    7. Process: "Run taxonomy-distribution.py"
       Hover text: "Validate that no category exceeds 30% of concepts"

    8. Decision: "Distribution balanced?"
       Hover text: "Check quality report for over/under-representation"

    9a. Process: "Adjust categories" (if unbalanced)
        Hover text: "Merge over-represented categories or expand under-represented"
        → Loop back to step 6

    9b. End: "Learning Graph with Taxonomy" (if balanced)
        Hover text: "CSV ready for JSON conversion and visualization"

    Color coding:
    - Blue: Data processing steps
    - Yellow: Decision points
    - Green: Quality validation
    - Orange: Manual review steps

    Swimlanes: Not applicable (single-actor process)

    Implementation: SVG flowchart with hover tooltips