# Taxonomy and Data Formats

## Summary

This chapter explores how to add taxonomy information to your learning graph and convert it to various formats for visualization and processing. You'll learn about the TaxonomyID field in CSV files and the process of adding taxonomy categorization to existing concept graphs. The chapter provides comprehensive coverage of the vis-network JSON format, including its schema structure with metadata, groups, nodes, and edges sections.

You'll learn about Dublin Core metadata standards and how to properly populate metadata fields including title, description, creator, date, version, format, and license. The chapter also covers color coding strategies for visualizations and font color selection for readability. Finally, you'll be introduced to Python scripting for learning graph processing, including key scripts like analyze-graph.py and csv-to-json.py.

## Concepts Covered

This chapter covers the following 22 concepts from the learning graph:

1. TaxonomyID Field in CSV
2. Adding Taxonomy to Graph
3. vis-network JSON Format
4. JSON Schema for Learning Graphs
5. Metadata Section in JSON
6. Groups Section in JSON
7. Nodes Section in JSON
8. Edges Section in JSON
9. Dublin Core Metadata
10. Title Metadata Field
11. Description Metadata Field
12. Creator Metadata Field
13. Date Metadata Field
14. Version Metadata Field
15. Format Metadata Field
16. License Metadata Field
17. Color Coding in Visualizations
18. Font Colors for Readability
19. Python
20. Python Scripts for Processing
21. analyze-graph.py Script
22. csv-to-json.py Script

## Prerequisites

This chapter builds on concepts from:

- [Chapter 5: Concept Enumeration and Dependencies](../05-concept-enumeration-dependencies/index.md)
- [Chapter 6: Learning Graph Quality and Validation](../06-learning-graph-quality-validation/index.md)

---

## Introduction to Data Formats for Learning Graphs

Learning graphs exist as data structures that must be stored, processed, and visualized effectively. While the conceptual model of a learning graph—concepts connected by dependency relationships—is straightforward, implementing that model requires careful attention to data formats and transformation pipelines. This chapter explores the complete data workflow from CSV-based graph authoring through JSON conversion to interactive visualization.

You'll learn how taxonomy information enriches your learning graph with categorical structure, enabling color-coded visualizations and category-based filtering. The chapter provides comprehensive coverage of the vis-network JSON format, which serves as the intermediate representation for browser-based graph visualization. Understanding JSON schema design, metadata standards, and color coding strategies will enable you to create professional, accessible learning graph visualizations.

The chapter culminates with practical Python scripting for learning graph processing. You'll explore the implementation details of scripts that validate, transform, and analyze your learning graph data, empowering you to customize the toolchain for your specific needs.

## The TaxonomyID Field in CSV Format

The learning graph CSV format introduced in Chapter 5 includes four essential columns: ConceptID, ConceptLabel, Dependencies, and **TaxonomyID**. While the first three columns define graph structure, the TaxonomyID column provides categorical metadata that enhances both organization and visualization.

A TaxonomyID is a short (3-5 letter) abbreviation representing a conceptual category or domain. Examples include:

- **FOUND**: Foundational concepts
- **TOOL**: Tools and technologies
- **IMPL**: Implementation techniques
- **ARCH**: Architecture and design
- **EVAL**: Evaluation and assessment

The TaxonomyID field serves multiple purposes in the learning graph ecosystem:

1. **Visual grouping**: Concepts with the same TaxonomyID display in the same color in visualizations
2. **Filtering**: Users can filter graph views to show only specific categories
3. **Balance analysis**: Distribution reports identify over- or under-represented categories
4. **Conceptual organization**: Related concepts cluster naturally during authoring

In the CSV format, TaxonomyID appears as the fourth column:

```csv
ConceptID,ConceptLabel,Dependencies,TaxonomyID
1,Introduction to Learning Graphs,,FOUND
2,What is a Concept?,1,FOUND
3,Concept Dependencies,1|2,BASIC
4,Graph Data Structures,3,ARCH
```

### Adding Taxonomy to Existing Graphs

If you created a learning graph without TaxonomyID information, you can add it retroactively using a multi-step process:

1. **Identify natural categories**: Review your concept list and identify 5-10 logical groupings based on topic similarity, complexity level, or knowledge domain
2. **Design TaxonomyID abbreviations**: Create distinctive, memorable 3-5 letter codes for each category
3. **Add TaxonomyID column to CSV**: Insert a new column header "TaxonomyID" as the fourth column
4. **Categorize concepts**: Assign each concept to its most appropriate category
5. **Validate distribution**: Run `taxonomy-distribution.py` to check for balanced categorization

The `add-taxonomy.py` helper script can semi-automate this process by suggesting categories based on concept labels using keyword matching:

```bash
cd docs/learning-graph
python add-taxonomy.py learning-graph.csv learning-graph-with-taxonomy.csv
```

The script prompts for taxonomy rules (keyword → TaxonomyID mappings) and applies them systematically, flagging ambiguous cases for manual review.

#### Diagram: Adding Taxonomy to CSV Workflow Diagram

<details markdown="1">
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

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (94/100) - Flowchart with decision diamonds and process boxes is core Mermaid strength
2. microsim-p5 (75/100) - Custom flowchart rendering possible with manual layout and interaction
3. vis-network (45/100) - Can represent workflow as directed graph but less intuitive than flowchart

</details>

## vis-network JSON Format

The vis-network JavaScript library provides powerful, interactive graph visualization in web browsers. To leverage vis-network for learning graph visualization, you must convert your CSV data into the vis-network JSON format—a structured representation that defines nodes, edges, visual styling, and metadata.

The vis-network format organizes graph data into four primary sections:

1. **metadata**: Information about the graph itself (title, creator, date, etc.)
2. **groups**: Visual styling definitions for each TaxonomyID category
3. **nodes**: Array of concept objects with id, label, and group properties
4. **edges**: Array of dependency objects with from and to properties

This hierarchical structure separates content (what concepts exist) from presentation (how concepts should be displayed), following best practices for data interchange formats.

### JSON Schema for Learning Graphs

A JSON schema defines the expected structure, data types, and constraints for JSON documents. For learning graphs, the schema ensures that generated JSON files conform to vis-network requirements and include all necessary metadata.

The learning graph JSON schema specifies:

**Top-level structure:**
```json
{
  "metadata": { ... },
  "groups": { ... },
  "nodes": [ ... ],
  "edges": [ ... ]
}
```

**Data type constraints:**

- `metadata`: Object with string values for title, description, etc.
- `groups`: Object with group names as keys, styling objects as values
- `nodes`: Array of objects, each with required `id` (number), `label` (string), `group` (string)
- `edges`: Array of objects, each with required `from` (number), `to` (number)

**Validation rules:**

- All node IDs must be unique within the nodes array
- All edge `from` and `to` values must reference existing node IDs
- All node `group` values must have corresponding entries in the `groups` object
- Metadata fields should follow Dublin Core standards (covered in next section)

The `csv-to-json.py` script implements this schema validation automatically, rejecting CSV data that would produce invalid JSON and providing detailed error messages for corrections.

#### Diagram: Learning Graph JSON Schema Diagram

<details markdown="1">
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

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (92/100) - Tree/hierarchical diagrams with nested structures well-supported
2. microsim-p5 (70/100) - Custom tree layout requires recursive positioning algorithms
3. vis-network (65/100) - Can display hierarchical graphs with physics-based layouts

</details>

### Metadata Section in JSON

The **metadata section** contains descriptive information about the learning graph as a whole, following Dublin Core metadata standards. This section enables proper attribution, versioning, and documentation of your learning graph dataset.

Example metadata section:

```json
{
  "metadata": {
    "title": "Introduction to Graph Databases Learning Graph",
    "description": "Concept dependency graph for a 15-week course on graph database fundamentals, architecture, and implementation",
    "creator": "Dr. Jane Smith",
    "date": "2024-09-15",
    "version": "1.2.0",
    "format": "vis-network JSON",
    "license": "CC BY-NC-SA 4.0"
  }
}
```

While metadata doesn't affect graph visualization directly, it provides essential context for:

- **Attribution**: Identifying who created or maintains the learning graph
- **Versioning**: Tracking changes over time and ensuring correct versions are used
- **Documentation**: Describing the graph's purpose, scope, and educational context
- **Licensing**: Clarifying usage rights and redistribution terms

### Groups Section in JSON

The **groups section** defines visual styling for each TaxonomyID category, enabling consistent color-coded visualization across the learning graph. Each group specifies:

- **color**: Background color for nodes in this category
- **font**: Text color and size for labels
- **shape**: Node shape (circle, box, diamond, etc.)

Example groups section:

```json
{
  "groups": {
    "FOUND": {
      "color": {"background": "#FF6B6B", "border": "#C92A2A"},
      "font": {"color": "#000000", "size": 14},
      "shape": "circle"
    },
    "BASIC": {
      "color": {"background": "#FFA94D", "border": "#E67700"},
      "font": {"color": "#000000", "size": 14},
      "shape": "circle"
    },
    "ARCH": {
      "color": {"background": "#FFD43B", "border": "#F59F00"},
      "font": {"color": "#000000", "size": 14},
      "shape": "circle"
    }
  }
}
```

Consistent group styling creates visual coherence and aids comprehension by allowing users to quickly identify concept categories by color.

### Nodes Section in JSON

The **nodes section** contains an array of concept objects representing the vertices of your learning graph. Each node object requires three properties:

- **id**: Unique numeric identifier (matches ConceptID from CSV)
- **label**: Human-readable concept name (matches ConceptLabel from CSV)
- **group**: TaxonomyID category for visual styling

Example nodes section:

```json
{
  "nodes": [
    {
      "id": 1,
      "label": "Introduction to Learning Graphs",
      "group": "FOUND"
    },
    {
      "id": 2,
      "label": "Concept Dependencies",
      "group": "BASIC"
    },
    {
      "id": 3,
      "label": "Graph Data Structures",
      "group": "ARCH"
    }
  ]
}
```

The nodes array typically contains 150-250 objects for a comprehensive learning graph. vis-network uses this array to render graph vertices, applying styling from the groups section based on each node's group property.

### Edges Section in JSON

The **edges section** contains an array of dependency relationship objects representing the directed edges of your learning graph. Each edge object requires two properties:

- **from**: Node ID of the prerequisite concept
- **to**: Node ID of the dependent concept

Example edges section:

```json
{
  "edges": [
    {
      "from": 1,
      "to": 2
    },
    {
      "from": 1,
      "to": 3
    },
    {
      "from": 2,
      "to": 4
    }
  ]
}
```

The edges array defines the directed acyclic graph structure. vis-network renders these as arrows pointing from prerequisite to dependent concepts, creating the visual flow of the learning progression.

For a 200-concept learning graph with an average of 3 dependencies per concept, expect approximately 600 edge objects in this array.

#### Diagram: CSV to JSON Conversion Mapping Diagram

<details markdown="1">
    <summary>CSV to JSON Conversion Mapping Diagram</summary>
    Type: diagram

    Purpose: Show how CSV columns map to JSON structure during conversion

    Layout: Side-by-side comparison with mapping arrows

    Left side - "CSV Format":
    ```
    ConceptID | ConceptLabel | Dependencies | TaxonomyID
    ----------|--------------|--------------|------------
    1         | Intro        |              | FOUND
    2         | Dependencies | 1            | BASIC
    3         | DAG          | 1|2          | ARCH
    ```

    Right side - "JSON Format":
    - Nodes section showing objects with id, label, group
    - Edges section showing objects with from, to

    Mapping arrows:
    - ConceptID → nodes[].id
    - ConceptLabel → nodes[].label
    - TaxonomyID → nodes[].group
    - Dependencies (split by |) → multiple edges with from/to

    Example transformation:
    - Row 2 (ConceptID=2, Dependencies="1") creates:
      * Node: {id: 2, label: "Dependencies", group: "BASIC"}
      * Edge: {from: 1, to: 2}

    - Row 3 (ConceptID=3, Dependencies="1|2") creates:
      * Node: {id: 3, label: "DAG", group: "ARCH"}
      * Edge: {from: 1, to: 3}
      * Edge: {from: 2, to: 3}

    Color coding:
    - Orange arrows: Direct 1:1 mappings
    - Purple arrows: Transformation mappings (Dependencies → Edges)

    Annotations:
    - "csv-to-json.py performs this transformation"
    - "Empty Dependencies creates node but no edges (foundational concept)"
    - "Pipe-delimited Dependencies create multiple edges"

    Implementation: Diagram with data tables and connecting arrows

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (90/100) - Data flow diagrams with transformation steps supported via flowchart syntax
2. microsim-p5 (78/100) - Custom visualization with tables and arrows achievable with careful layout
3. chartjs-generator (20/100) - Not designed for data transformation diagrams

</details>

## Dublin Core Metadata Standard

Dublin Core is an internationally recognized metadata standard (ISO 15836) for describing digital resources. Originally developed for library catalog systems, Dublin Core provides a simple yet powerful vocabulary for resource description that translates well to learning graph documentation.

The core Dublin Core elements most relevant to learning graphs include:

| Element | Purpose | Example |
|---------|---------|---------|
| Title | Name of the resource | "Graph Databases Learning Graph" |
| Description | Summary of content and scope | "200-concept graph covering Neo4j..." |
| Creator | Primary author or maintainer | "Dr. Jane Smith" |
| Date | Creation or modification date | "2024-09-15" (ISO 8601) |
| Version | Version number | "1.2.0" (semantic versioning) |
| Format | File format specification | "vis-network JSON v9.1" |
| License | Usage rights | "CC-BY-4.0" or "MIT" |

Using Dublin Core metadata ensures your learning graphs are properly documented, discoverable, and interoperable with academic and educational resource repositories.

### Title Metadata Field

The **title** field provides the primary name for your learning graph. Effective titles are:

- **Descriptive**: Clearly indicate the subject matter
- **Specific**: Distinguish from other learning graphs
- **Concise**: Typically 5-10 words maximum

Examples of effective titles:

- "Introduction to Graph Databases Learning Graph"
- "Python Programming Fundamentals Concept Map"
- "ITIL Service Management Dependency Graph"

Avoid generic titles like "Learning Graph" or "Course Concepts" that provide no information about content.

### Description Metadata Field

The **description** field offers a 1-3 sentence summary of the learning graph's scope, audience, and purpose:

```json
{
  "description": "Comprehensive 200-concept learning graph for a 15-week undergraduate course on graph database fundamentals, covering Neo4j architecture, Cypher query language, and graph data modeling. Designed for computer science students with prerequisites in data structures and SQL."
}
```

Effective descriptions answer:

- **What**: Topic and scope
- **Who**: Target audience and prerequisites
- **How many**: Number of concepts
- **When/Where**: Course duration or context

### Creator Metadata Field

The **creator** field identifies the primary author or team responsible for developing the learning graph:

```json
{
  "creator": "Dr. Jane Smith, Computer Science Department, State University"
}
```

For multiple creators, use semicolon-separated list:

```json
{
  "creator": "Dr. Jane Smith; Dr. John Doe; Teaching Assistant Team"
}
```

Proper attribution ensures:

- Academic credit for intellectual work
- Contact information for questions or collaborations
- Provenance tracking in educational repositories

### Date Metadata Field

The **date** field records when the learning graph was created or last significantly updated. Use ISO 8601 format (YYYY-MM-DD) for unambiguous, machine-parseable dates:

```json
{
  "date": "2024-09-15"
}
```

For resources with multiple relevant dates, use qualified Dublin Core:

```json
{
  "dateCreated": "2024-01-10",
  "dateModified": "2024-09-15",
  "dateAvailable": "2024-09-20"
}
```

Accurate dating enables versioning, change tracking, and temporal queries in learning resource repositories.

### Version Metadata Field

The **version** field tracks revisions using semantic versioning (MAJOR.MINOR.PATCH):

```json
{
  "version": "1.2.0"
}
```

Version numbering conventions:

- **MAJOR**: Increment for incompatible changes (e.g., restructuring categories, removing concepts)
- **MINOR**: Increment for backwards-compatible additions (e.g., adding concepts, refining dependencies)
- **PATCH**: Increment for corrections (e.g., fixing typos, correcting metadata)

Examples:

- `1.0.0`: Initial release
- `1.1.0`: Added 15 new concepts on advanced topics
- `1.1.1`: Fixed typo in concept label
- `2.0.0`: Restructured taxonomy from 8 to 12 categories (breaking change)

### Format Metadata Field

The **format** field specifies the file format and version:

```json
{
  "format": "vis-network JSON v9.1"
}
```

For learning graphs, useful format specifications include:

- Technical format: "vis-network JSON v9.1"
- MIME type: "application/json"
- Schema version: "Learning Graph Schema v2.0"

Explicit format declaration enables:

- Validation against correct schemas
- Compatibility checking with visualization tools
- Automated format conversion pipelines

### License Metadata Field

The **license** field clarifies usage rights using standard license identifiers:

```json
{
  "license": "CC BY-NC-SA 4.0"
}
```

Common licenses for educational resources:

| License | Meaning | Usage Rights |
|---------|---------|-------------|
| CC-BY-4.0 | Attribution required | Commercial and derivative works allowed |
| CC-BY-SA-4.0 | Attribution + Share-Alike | Derivatives must use same license |
| CC-BY-NC-4.0 | Attribution + Non-Commercial | No commercial use |
| MIT | Permissive open source | Minimal restrictions |
| All Rights Reserved | Traditional copyright | No use without permission |

Clear licensing enables:

- Legal sharing and remixing
- Inclusion in open educational resource repositories
- Compliance with institutional policies

#### Diagram: Dublin Core Metadata Field Reference Card

<details markdown="1">
    <summary>Dublin Core Metadata Field Reference Card</summary>
    Type: infographic

    Purpose: Create a visual reference guide for all Dublin Core metadata fields used in learning graphs

    Layout: Grid layout with 7 cards (one per metadata field)

    Each card contains:
    - Field name (large, bold)
    - Purpose (1 sentence)
    - Format/constraint
    - Example value
    - Icon representing the field

    Card details:

    1. Title
       Icon: 📚
       Purpose: "Primary name of the learning graph"
       Format: "String, 5-10 words"
       Example: "Graph Databases Learning Graph"

    2. Description
       Icon: 📝
       Purpose: "Detailed summary of scope and audience"
       Format: "String, 1-3 sentences"
       Example: "200-concept graph for undergraduate..."

    3. Creator
       Icon: 👤
       Purpose: "Primary author or maintainer"
       Format: "String, name and affiliation"
       Example: "Dr. Jane Smith, State University"

    4. Date
       Icon: 📅
       Purpose: "Creation or last update date"
       Format: "ISO 8601: YYYY-MM-DD"
       Example: "2024-09-15"

    5. Version
       Icon: 🔢
       Purpose: "Revision number for tracking changes"
       Format: "Semantic: MAJOR.MINOR.PATCH"
       Example: "1.2.0"

    6. Format
       Icon: 📄
       Purpose: "File format and version specification"
       Format: "String, format name + version"
       Example: "vis-network JSON v9.1"

    7. License
       Icon: ⚖️
       Purpose: "Usage rights and restrictions"
       Format: "License identifier"
       Example: "CC-BY-4.0"

    Visual style: Modern card-based grid with icons and color-coded borders

    Color scheme:
    - Title: Blue border
    - Description: Green border
    - Creator: Purple border
    - Date: Orange border
    - Version: Red border
    - Format: Teal border
    - License: Gold border

    Interactive elements:
    - Click card to expand with detailed guidelines
    - Hover to show validation rules

    Implementation: HTML/CSS grid with JavaScript for interactivity

---
**MicroSim Generator Recommendations:**

1. markdown table (best) - Static reference card doesn't require interactivity, markdown table is simplest
2. microsim-p5 (85/100) - If interactivity needed, p5.js with DOM elements supports card grid layout
3. chartjs-generator (15/100) - Not designed for reference card layouts or metadata display

</details>

## Color Coding in Visualizations

Color coding transforms abstract graph data into intuitive visual representations where patterns emerge naturally. For learning graphs, color serves as a primary visual variable encoding taxonomy categories, enabling users to identify concept domains at a glance.

Effective color coding schemes for learning graphs follow several design principles:

### Color Palette Selection

Choose colors that are:

1. **Distinctive**: Easily distinguished from one another
2. **Meaningful**: Associate naturally with category semantics when possible
3. **Accessible**: Visible to users with color vision deficiencies
4. **Consistent**: Use same colors across all visualizations

Recommended palette strategies:

**Rainbow gradient** (for sequential categories):

- FOUND: Red (#FF6B6B)
- BASIC: Orange (#FFA94D)
- ARCH: Yellow (#FFD43B)
- IMPL: Light Green (#8CE99A)
- DATA: Green (#51CF66)
- TOOL: Light Blue (#74C0FC)
- QUAL: Blue (#4C6EF5)
- ADV: Purple (#9775FA)

**Categorical palette** (for non-sequential categories):

Use palettes designed for categorical data with maximum perceptual distance:

- ColorBrewer qualitative schemes (Set1, Set2, Set3)
- Tableau categorical palettes
- Okabe-Ito colorblind-safe palette

### Font Colors for Readability

Node label text must be readable against the background color. The W3C Web Content Accessibility Guidelines (WCAG) specify minimum contrast ratios:

- **Normal text**: 4.5:1 contrast ratio (AA level)
- **Large text** (18pt+): 3:1 contrast ratio (AA level)
- **Enhanced** (AAA level): 7:1 for normal, 4.5:1 for large

General rules for font color selection:

| Background Lightness | Recommended Font Color | Hex Code |
|---------------------|----------------------|----------|
| Dark (L < 50%) | White or very light gray | #FFFFFF or #F8F9FA |
| Light (L > 50%) | Black or very dark gray | #000000 or #212529 |
| Medium (L ≈ 50%) | Test both; choose higher contrast | Depends on specific color |

The `csv-to-json.py` script can calculate optimal font colors automatically using the relative luminance formula:

```
Relative Luminance = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

If luminance > 0.5, use black text; otherwise, use white text.

#### Diagram: Color Accessibility Checker MicroSim

<details markdown="1">
    <summary>Color Accessibility Checker MicroSim</summary>
    Type: microsim

    Learning objective: Demonstrate WCAG contrast ratio requirements and help users select accessible color combinations

    Canvas layout (800x500px):
    - Left side (400x500): Color preview area
    - Right side (400x500): Controls and contrast analysis

    Visual elements (left panel):
    - Large preview box (350x250px) showing selected background color
    - Text samples in different sizes:
      * 14pt normal text: "The quick brown fox jumps over the lazy dog"
      * 18pt large text: "The quick brown fox jumps"
      * 24pt heading: "Sample Heading"
    - Text displayed in selected font color
    - Pass/Fail indicators (✓ or ✗) next to each text sample

    Interactive controls (right panel):
    - Color picker: "Background Color" (default: #FFA94D orange)
    - Color picker: "Font Color" (default: #000000 black)
    - Button: "Auto-Calculate Optimal Font Color"
    - Display: "Contrast Ratio: X.XX:1"
    - Display: "WCAG AA Compliance: ✓/✗"
    - Display: "WCAG AAA Compliance: ✓/✗"
    - Preset buttons:
      * "FOUND (Red bg)"
      * "BASIC (Orange bg)"
      * "ARCH (Yellow bg)"
      * "IMPL (Green bg)"
      * "TOOL (Blue bg)"
      * "ADV (Purple bg)"

    Default parameters:
    - Background: #FFA94D (orange)
    - Font: #000000 (black)
    - Contrast ratio: 5.2:1
    - AA: Pass, AAA: Fail

    Behavior:
    - Real-time contrast ratio calculation as colors change
    - "Auto-Calculate" button sets font to black or white for optimal contrast
    - Pass/Fail indicators update based on WCAG thresholds
    - Preset buttons load taxonomy category colors
    - Warning message if contrast ratio < 3.0 (severe accessibility issue)

    Implementation notes:
    - Use p5.js for rendering preview box and text
    - Calculate relative luminance: L = 0.2126*R + 0.7152*G + 0.0722*B
    - Contrast ratio = (L1 + 0.05) / (L2 + 0.05) where L1 > L2
    - Use DOM color pickers for easier color selection

    Implementation: p5.js MicroSim with color picker controls

---
**MicroSim Generator Recommendations:**

1. microsim-p5 (95/100) - Interactive color pickers, contrast calculation, and live preview are p5.js + DOM strengths
2. chartjs-generator (25/100) - Not designed for color accessibility checking tools
3. vis-network (10/100) - Not applicable to color contrast validation interfaces

</details>

## Python for Learning Graph Processing

Python serves as the primary scripting language for learning graph validation, transformation, and analysis. Its rich ecosystem of libraries for data processing (csv, json, pandas) and graph analysis (networkx) makes it ideal for implementing the learning graph toolchain.

The learning graph workflow uses Python for three main tasks:

1. **Validation**: Checking structural integrity and quality metrics
2. **Transformation**: Converting between formats (CSV → JSON)
3. **Analysis**: Generating quality reports and distribution statistics

Python scripts follow consistent patterns:

**Command-line interface:**
```python
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py input.csv output.md")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
```

**CSV reading with error handling:**
```python
import csv

try:
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
except FileNotFoundError:
    print(f"Error: {input_file} not found")
    sys.exit(1)
```

**JSON writing with formatting:**
```python
import json

with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)
```

### Python Scripts for Processing

The learning graph toolkit includes three core Python scripts, each focused on a specific processing task:

| Script | Input | Output | Purpose |
|--------|-------|--------|---------|
| analyze-graph.py | learning-graph.csv | quality-metrics.md | Validate structure, calculate quality score |
| csv-to-json.py | learning-graph.csv | learning-graph.json | Convert to vis-network format |
| taxonomy-distribution.py | learning-graph.csv | taxonomy-distribution.md | Analyze category balance |

All scripts follow similar architectural patterns:

1. **Argument parsing**: Accept input/output filenames via command line
2. **File reading**: Load CSV data with error handling
3. **Data validation**: Check format, detect errors
4. **Processing**: Perform core transformation or analysis
5. **Output generation**: Write results to file
6. **Status reporting**: Print summary to console

This consistency makes scripts easy to understand, maintain, and extend.

### analyze-graph.py Script Implementation

The `analyze-graph.py` script performs comprehensive learning graph validation and quality analysis. Its implementation illustrates key graph algorithms and quality metric calculations.

**Core functionality:**

1. **CSV parsing**: Reads four-column format, creates graph data structure
2. **Dependency parsing**: Splits pipe-delimited dependencies into integer lists
3. **Graph construction**: Builds adjacency list representation for traversal
4. **Cycle detection**: DFS-based algorithm with three-color marking
5. **Connectivity analysis**: Identifies disconnected components
6. **Metric calculation**: Computes indegree, outdegree, chain lengths
7. **Quality scoring**: Aggregates metrics into overall score
8. **Report generation**: Outputs formatted Markdown

**Key implementation details:**

Cycle detection using DFS:

```python
def detect_cycles(graph):
    color = {node: 'WHITE' for node in graph}
    cycles = []

    def dfs(node, path):
        color[node] = 'GRAY'
        path.append(node)

        for neighbor in graph[node]:
            if color[neighbor] == 'GRAY':
                # Cycle detected
                cycle_start = path.index(neighbor)
                cycles.append(path[cycle_start:])
            elif color[neighbor] == 'WHITE':
                dfs(neighbor, path[:])

        color[node] = 'BLACK'

    for node in graph:
        if color[node] == 'WHITE':
            dfs(node, [])

    return cycles
```

Quality score calculation:

```python
def calculate_quality_score(metrics):
    score = 0

    # Structural validity (40 points)
    if not metrics['has_cycles']:
        score += 20
    if not metrics['has_self_deps']:
        score += 10
    if metrics['num_components'] == 1:
        score += 10

    # Connectivity quality (30 points)
    orphaned_pct = metrics['orphaned_nodes'] / metrics['total_nodes']
    if 0.05 <= orphaned_pct <= 0.15:
        score += 10
    elif orphaned_pct < 0.25:
        score += 5

    # ... (additional metrics)

    return score
```

### csv-to-json.py Script Implementation

The `csv-to-json.py` script transforms CSV learning graphs into vis-network JSON format. Its implementation demonstrates data format conversion and JSON schema construction.

**Core functionality:**

1. **CSV reading**: Parses four-column format
2. **Nodes array construction**: Creates objects with id, label, group
3. **Edges array construction**: Parses dependencies, creates from/to objects
4. **Groups object construction**: Defines color schemes for each TaxonomyID
5. **Metadata population**: Adds Dublin Core fields
6. **JSON serialization**: Outputs formatted vis-network JSON

**Key implementation details:**

Node creation:

```python
nodes = []
for row in csv_data:
    node = {
        'id': int(row['ConceptID']),
        'label': row['ConceptLabel'],
        'group': row['TaxonomyID']
    }
    nodes.append(node)
```

Edge creation from dependencies:

```python
edges = []
for row in csv_data:
    concept_id = int(row['ConceptID'])
    deps = row['Dependencies']

    if deps:  # Not empty
        for dep in deps.split('|'):
            edge = {
                'from': int(dep),
                'to': concept_id
            }
            edges.append(edge)
```

Groups generation with color palette:

```python
taxonomy_colors = {
    'FOUND': '#FF6B6B',
    'BASIC': '#FFA94D',
    'ARCH': '#FFD43B',
    # ... more colors
}

groups = {}
for tax_id in set(row['TaxonomyID'] for row in csv_data):
    groups[tax_id] = {
        'color': {
            'background': taxonomy_colors.get(tax_id, '#CCCCCC'),
            'border': darken_color(taxonomy_colors.get(tax_id))
        },
        'font': {'color': '#000000', 'size': 14},
        'shape': 'circle'
    }
```

Complete JSON structure assembly:

```python
output = {
    'metadata': {
        'title': 'Learning Graph',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'format': 'vis-network JSON v9.1',
        # ... more fields
    },
    'groups': groups,
    'nodes': nodes,
    'edges': edges
}

with open(output_file, 'w') as f:
    json.dump(output, f, indent=2)
```

#### Diagram: Python Learning Graph Processing Pipeline

<details markdown="1">
    <summary>Python Learning Graph Processing Pipeline</summary>
    Type: diagram

    Purpose: Show the complete data flow from CSV creation through JSON visualization

    Layout: Horizontal pipeline with data transformations

    Pipeline stages:

    1. "Author CSV" (Human)
       - Tool: Spreadsheet editor
       - Output: learning-graph.csv
       - Format: ConceptID, ConceptLabel, Dependencies, TaxonomyID

    2. "Validate Structure" (analyze-graph.py)
       - Input: learning-graph.csv
       - Process: DAG validation, quality metrics
       - Output: quality-metrics.md
       - Decision: Pass → continue, Fail → return to stage 1

    3. "Analyze Distribution" (taxonomy-distribution.py)
       - Input: learning-graph.csv
       - Process: Category counting, balance checking
       - Output: taxonomy-distribution.md
       - Decision: Balanced → continue, Unbalanced → return to stage 1

    4. "Convert to JSON" (csv-to-json.py)
       - Input: learning-graph.csv
       - Process: Parse CSV, build nodes/edges, add metadata
       - Output: learning-graph.json
       - Format: vis-network JSON

    5. "Visualize Graph" (Browser)
       - Input: learning-graph.json
       - Tool: vis-network JavaScript library
       - Output: Interactive graph visualization
       - User can explore, zoom, filter by taxonomy

    Data flow arrows:
    - CSV file flows forward through pipeline
    - Quality reports feed back to stage 1 for corrections
    - JSON is final output for visualization

    Color coding:
    - Human steps: Blue
    - Python automation: Green
    - Decision points: Yellow
    - Browser visualization: Purple

    Annotations:
    - "Iterative refinement loop" showing feedback from stages 2-3 to stage 1
    - "Automated pipeline" showing stages 2-4 can run in sequence
    - "One-time setup" for initial CSV creation

    Implementation: Flowchart diagram with data flow arrows and decision diamonds

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (93/100) - Pipeline flowcharts with sequential stages and decision points well-supported
2. vis-network (70/100) - Can model pipeline as directed graph with custom node shapes
3. microsim-p5 (72/100) - Custom flowchart rendering with manual stage positioning and arrows

</details>

## Summary and Next Steps

This chapter provided comprehensive coverage of data formats and processing pipelines for learning graphs. You learned how the TaxonomyID field enables categorical organization and color-coded visualization, how the vis-network JSON format structures graph data for web-based visualization, and how Dublin Core metadata standards ensure proper documentation.

The Python scripting coverage demonstrated practical implementation patterns for graph validation, format conversion, and analysis. These scripts form a reusable toolkit that processes learning graph data from authoring through quality validation to visualization-ready JSON.

Key takeaways:

- **TaxonomyID is the fourth column** in learning graph CSV, providing categorical metadata
- **vis-network JSON has four sections**: metadata, groups, nodes, edges
- **Dublin Core metadata** ensures proper attribution, versioning, and licensing
- **Color accessibility matters**: Use WCAG contrast ratios for readable text
- **Python scripts automate processing**: Validation, conversion, and analysis in consistent pipelines
- **Data flows CSV → validation → JSON → visualization**: Each stage builds on the previous

With validated learning graphs converted to visualization-ready JSON format, you're prepared to deploy interactive graph viewers that enable students and instructors to explore concept dependencies visually. The next chapters will cover visualization implementation, chapter structure generation, and content creation workflows that transform your learning graph into a complete intelligent textbook.

## References

1. [vis-network documentation](https://visjs.github.io/vis-network/docs/) - 2024 - vis.js - Official documentation for the vis-network JavaScript library used to create interactive, customizable network visualizations in browsers, supporting thousands of nodes with clustering for larger datasets, essential for implementing learning graph viewers.

2. [DCMI: Using Dublin Core](https://www.dublincore.org/specifications/dublin-core/usageguide/) - 2024 - Dublin Core Metadata Initiative - Official usage guide for Dublin Core metadata standards, explaining how to create descriptive records for information resources with the fifteen core metadata elements, ensuring professional metadata quality in learning graph JSON files.

3. [Working with CSV and JSON Files in Python](https://dev.to/devasservice/working-with-csv-json-and-binary-files-in-python-2bge) - 2024-10-15 - DEV Community - Tutorial covering CSV and JSON file handling in Python using built-in libraries and pandas, with practical examples for data conversion workflows directly applicable to learning graph processing scripts.
