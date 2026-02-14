# Learning Graph Quality and Validation

## Summary

This chapter focuses on validating and assessing the quality of your learning graph. You'll learn techniques for detecting circular dependencies and validating that your graph is a proper Directed Acyclic Graph (DAG). The chapter covers self-dependency checking and introduces comprehensive quality metrics including orphaned nodes, disconnected subgraphs, and linear chain detection.

You'll learn to analyze your graph using indegree and outdegree metrics, calculate average dependencies per concept, and determine the maximum dependency chain length. The chapter culminates with learning how to generate an overall learning graph quality score. Additionally, you'll explore taxonomy distribution metrics to ensure balanced category representation and avoid over-representation of any single topic area.

## Concepts Covered

This chapter covers the following 16 concepts from the learning graph:

1. Circular Dependency Detection
2. DAG Validation
3. Self-Dependency Checking
4. Quality Metrics for Graphs
5. Orphaned Nodes
6. Disconnected Subgraphs
7. Linear Chain Detection
8. Indegree Analysis
9. Outdegree Analysis
10. Average Dependencies Per Concept
11. Maximum Dependency Chain Length
12. Learning Graph Quality Score
13. Taxonomy Categories
14. TaxonomyID Abbreviations
15. Category Distribution
16. Avoiding Over-Representation

## Prerequisites

This chapter builds on concepts from:

- [Chapter 4: Introduction to Learning Graphs](../04-intro-learning-graphs/index.md)
- [Chapter 5: Concept Enumeration and Dependencies](../05-concept-enumeration-dependencies/index.md)

---

## Introduction to Learning Graph Quality Validation

Creating a learning graph is a significant achievement, but ensuring its quality is equally important for effective educational outcomes. A well-constructed learning graph serves as the foundation for your intelligent textbook, guiding students through concepts in a logical, dependency-aware sequence. Poor quality graphs—those with circular dependencies, orphaned concepts, or imbalanced taxonomy distributions—can confuse learners and undermine the pedagogical value of your materials.

This chapter introduces systematic approaches for validating and assessing the quality of your learning graph. You'll learn both structural validation techniques that ensure your graph is mathematically sound as a Directed Acyclic Graph (DAG), and quality metrics that measure pedagogical effectiveness. These validation techniques are essential for identifying and correcting issues before generating chapter content, as structural problems in your graph will propagate throughout your entire textbook.

The validation process combines automated analysis through Python scripts with manual review of quality reports. By the end of this chapter, you'll be able to generate comprehensive quality assessments for your learning graphs and make data-driven improvements to enhance their educational value.

## Directed Acyclic Graphs and Educational Dependencies

Learning graphs must be structured as **Directed Acyclic Graphs (DAGs)** to represent prerequisite relationships correctly. In a DAG, directed edges point from prerequisite concepts to dependent concepts, and the graph contains no cycles—you cannot follow the dependency arrows and return to your starting concept.

This DAG structure ensures that students can learn concepts in a valid sequence. If your graph contains a cycle (Concept A depends on B, B depends on C, and C depends on A), there is no valid starting point for learning—a logical impossibility that must be detected and corrected.

### DAG Validation

Validating that your learning graph is a proper DAG involves checking two critical properties:

1. **Acyclicity:** No circular dependency chains exist in the graph
2. **Connectivity:** All concepts are reachable from foundational nodes

The `analyze-graph.py` Python script performs DAG validation automatically by implementing a depth-first search (DFS) algorithm with cycle detection. During traversal, the algorithm maintains three node states:

- **White (unvisited):** Node has not been explored
- **Gray (in progress):** Node is being explored, currently on the recursion stack
- **Black (completed):** Node and all its descendants have been fully explored

If the algorithm encounters a gray node during traversal, it has detected a back edge indicating a cycle. This validation runs in O(V + E) time complexity, where V is the number of vertices (concepts) and E is the number of edges (dependencies).

#### Diagram: DAG Validation Algorithm Visualization

<iframe src="../../sims/three-color-dfs/main.html" width="100%" height="700px" scrolling="no"></iframe>

<details markdown="1">
    <summary>DAG Validation Algorithm Visualization</summary>
    Type: diagram

    Purpose: Illustrate the three-color DFS algorithm used for cycle detection in learning graphs

    Components to show:
    - A sample learning graph with 8 nodes arranged in a network
    - Color-coded nodes showing White (gray), Gray (yellow), Black (green)
    - Directed edges showing dependencies
    - One back edge highlighted in red creating a cycle
    - DFS traversal stack shown on the right side
    - Traversal order numbered 1-8

    Layout: Network graph on left (70%), DFS stack visualization on right (30%)

    Example nodes:
    - Node 1: "Variables" (Black - completed)
    - Node 2: "Functions" (Black - completed)
    - Node 3: "Loops" (Gray - in progress)
    - Node 4: "Recursion" (Gray - in progress)
    - Node 5: "Data Structures" (White - unvisited)
    - Node 6: "Algorithms" (White - unvisited)

    Edges:
    - Black arrows: Valid forward edges
    - Red arrow: Back edge from "Recursion" to "Loops" (cycle detected!)

    Annotations:
    - Arrow pointing to red edge: "Cycle detected: Loops ← Recursion ← Loops"
    - Stack showing: [Loops, Recursion]

    Style: Network diagram with color-coded nodes and directional arrows

    Implementation: SVG diagram with color-coded circles and arrows

---
**MicroSim Generator Recommendations:**

1. vis-network (98/100) - Network graph visualization ideal for displaying DAG validation algorithm with colored nodes
2. mermaid-generator (85/100) - Flowchart capabilities support algorithm visualization with decision points
3. microsim-p5 (75/100) - Custom interactive visualization possible but requires more development effort

</details>

[Run the Three Color DFS Fullscreen](../../sims/three-color-dfs/main.html)


### Circular Dependency Detection

Circular dependencies represent the most critical structural flaw in a learning graph. They create logical impossibilities in the learning sequence and must be identified and eliminated before proceeding with content generation.

Common sources of circular dependencies include:

- **Bidirectional prerequisites:** Concept A requires B, and B requires A
- **Multi-hop cycles:** A requires B, B requires C, C requires A
- **Self-dependencies:** A concept incorrectly lists itself as a prerequisite

The `analyze-graph.py` script reports all cycles found, displaying the complete dependency chain for each cycle. This detailed output allows you to identify which dependency link to remove to break the cycle.

Here's an example of cycle detection output:

```
CYCLE DETECTED:
  Graph Databases (ID: 45)
  → Query Performance (ID: 52)
  → Index Selection (ID: 48)
  → Database Design (ID: 44)
  → Graph Databases (ID: 45)

Recommendation: Remove dependency "Database Design → Graph Databases"
```

### Self-Dependency Checking

Self-dependencies occur when a concept incorrectly lists its own ConceptID in its dependencies column. While technically a special case of circular dependencies, self-dependencies are so common—often resulting from copy-paste errors in CSV editing—that the validation script checks for them explicitly before running the general cycle detection algorithm.

The self-dependency check is trivial but essential:

```python
for concept in learning_graph:
    if concept.id in concept.dependencies:
        report_error(f"Concept {concept.id} depends on itself")
```

Any self-dependencies detected indicate data entry errors that should be corrected immediately in your `learning-graph.csv` file.

## Quality Metrics for Learning Graphs

Beyond structural validation, effective learning graphs exhibit certain quality characteristics that enhance their pedagogical value. Quality metrics quantify these characteristics, providing objective measures for assessing and comparing learning graphs.

The following metrics help identify potential issues that, while not structurally invalid, may indicate pedagogical problems or opportunities for improvement.

### Orphaned Nodes

An **orphaned node** is a concept that no other concept depends upon—it has an outdegree of zero. While terminal concepts (endpoints in the learning journey) naturally have no dependents, excessive orphaned nodes suggest concepts that may be:

- Too specialized or advanced for the course scope
- Improperly isolated from the main learning progression
- Missing their dependent concepts due to incomplete graph construction

A well-designed learning graph typically has 5-10% orphaned nodes, representing culminating concepts and specialized topics. If more than 20% of your concepts are orphaned, review them to determine whether they should be connected to later material or removed from the graph entirely.
#### Diagram: Orphaned Nodes Identification Chart

<iframe src="../../sims/orphaned-nodes-identification/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Orphaned Nodes Identification Chart</summary>
    Type: chart

    Chart type: Scatter plot

    Purpose: Visualize concept connectivity by showing indegree vs outdegree for all concepts, highlighting orphaned nodes

    X-axis: Indegree (number of prerequisites, 0-8)
    Y-axis: Outdegree (number of dependents, 0-12)

    Data series:
    1. Foundational concepts (green dots, indegree = 0, outdegree > 0)
       - Example: "Introduction to Learning Graphs" (0, 8)
       - Example: "What is a Concept?" (0, 6)

    2. Intermediate concepts (blue dots, indegree > 0, outdegree > 0)
       - Scatter of 150+ points representing well-connected concepts
       - Example: "DAG Validation" (2, 4)

    3. Orphaned concepts (red dots, indegree > 0, outdegree = 0)
       - Example: "Advanced Quality Metrics" (5, 0)
       - Example: "Future of Learning Graphs" (3, 0)
       - Show approximately 15-20 red dots

    Title: "Concept Connectivity Analysis: Indegree vs Outdegree"

    Annotations:
    - Vertical line at outdegree=0 labeled "Orphaned Zone"
    - Horizontal line at indegree=0 labeled "Foundation Zone"
    - Callout: "12% orphaned (healthy range: 5-15%)"

    Legend: Position top-right with color coding explanation

    Implementation: Chart.js scatter plot with color-coded point categories

---
**MicroSim Generator Recommendations:**

1. chartjs-generator (97/100) - Scatter plot chart type directly supports indegree vs outdegree visualization
2. bubble-chart-generator (80/100) - Could add third dimension (concept importance) via bubble size
3. microsim-p5 (72/100) - Custom scatter plot possible with manual axis and point rendering

</details>

### Disconnected Subgraphs

A **disconnected subgraph** is a cluster of concepts isolated from the main learning graph—they have no dependency paths connecting them to foundational concepts. This indicates a serious structural problem: students cannot reach these concepts through the normal learning progression.

Disconnected subgraphs typically result from:

- Copy-pasting concept blocks without establishing connections
- Incomplete dependency mapping during graph construction
- Accidental deletion of bridging concepts

The `analyze-graph.py` script uses a connectivity analysis algorithm to identify all disconnected components. In a valid learning graph, there should be exactly one connected component containing all concepts. Any additional components indicate isolated concept clusters that need to be integrated into the main graph.

### Linear Chain Detection

A **linear chain** is a sequence of concepts where each concept depends on exactly one predecessor and is depended upon by exactly one successor, forming a single-file progression. While some linear sequences are natural (basic → intermediate → advanced), excessive linear chains indicate missed opportunities for:

- Parallel learning paths that students could explore in different orders
- Cross-concept connections that reinforce understanding
- Flexible curriculum that accommodates different learning styles

Linear chains are identified by checking each concept's indegree and outdegree:

```python
def is_linear_chain_node(concept):
    return concept.indegree == 1 and concept.outdegree == 1
```

Quality learning graphs typically have 20-40% of concepts in linear chains, with the remainder providing branching paths and concept integration points. If more than 60% of concepts form linear chains, consider adding cross-dependencies to create a richer learning network.
#### Diagram: Linear Chain vs Network Structure Comparison

<iframe src="../../sims/linear-chain-vs-network/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
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

---
**MicroSim Generator Recommendations:**

1. vis-network (95/100) - Network visualization perfectly suited for comparing linear vs networked graph structures
2. mermaid-generator (82/100) - Can create side-by-side graph diagrams with different layouts
3. microsim-p5 (78/100) - Force-directed graph layout possible but requires physics simulation coding

</details>

## Graph Analysis Metrics

Quantitative metrics provide objective measures of graph structure and complexity. These metrics help you understand your learning graph's characteristics and compare it to best practices for educational graph design.

### Indegree and Outdegree Analysis

**Indegree** (number of prerequisites) and **outdegree** (number of dependents) are fundamental graph metrics that reveal concept roles within the learning progression:

- **High indegree:** Advanced concepts requiring substantial prior knowledge
- **Low indegree (0):** Foundational concepts accessible without prerequisites
- **High outdegree:** Core concepts that enable many subsequent topics
- **Low outdegree (0):** Specialized or terminal concepts

Distribution of indegree values across your learning graph indicates its prerequisite structure:

| Indegree | Interpretation | Typical % of Concepts |
|----------|----------------|----------------------|
| 0 | Foundational concepts | 5-10% |
| 1-2 | Early concepts with minimal prerequisites | 30-40% |
| 3-5 | Intermediate concepts requiring solid foundation | 40-50% |
| 6+ | Advanced concepts requiring extensive background | 5-15% |

If your graph has too many high-indegree concepts (>20% with indegree ≥ 6), consider whether some prerequisites are redundant or if the course scope is too advanced. Conversely, if most concepts have indegree 0-1, you may be missing important prerequisite relationships.

### Average Dependencies Per Concept

The **average dependencies per concept** metric indicates overall graph connectivity and curriculum density:

```
Average Dependencies = Total Edges / Total Nodes
```

For educational learning graphs, empirical research suggests optimal ranges:

- **2.0-3.0:** Appropriate for introductory courses with linear progressions
- **3.0-4.0:** Ideal for intermediate courses with moderate integration
- **4.0-5.0:** Suitable for advanced courses with high concept integration
- **>5.0:** May indicate over-specification of prerequisites

The `analyze-graph.py` script calculates this metric and flags values outside the recommended 2.0-4.5 range. Graphs with average dependencies below 2.0 may be too linear, while those above 5.0 may impose unrealistic prerequisite burdens on learners.
#### Diagram: Average Dependencies Distribution Bar Chart

<iframe src="../../sims/average-dependencies-distribution/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
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

---
**MicroSim Generator Recommendations:**

1. chartjs-generator (98/100) - Histogram/bar chart with annotations and shaded regions natively supported
2. microsim-p5 (70/100) - Custom bar chart rendering with manual annotation placement required
3. mermaid-generator (25/100) - Limited chart capabilities, not ideal for detailed histograms

</details>

### Maximum Dependency Chain Length

The **maximum dependency chain length** represents the longest sequence of prerequisite concepts from any foundational node to any terminal node. This metric indicates the depth of your curriculum and affects course duration planning.

For a 200-concept learning graph, typical maximum chain lengths are:

- **8-12 concepts:** Short course (4-6 weeks)
- **12-18 concepts:** Standard semester course (12-15 weeks)
- **18-25 concepts:** Extended course or multi-semester sequence
- **>25 concepts:** May indicate overly linear structure

The chain length affects student progress velocity. If your maximum chain is 20 concepts deep, students must complete at least 20 learning steps to reach the most advanced material—establishing a minimum time investment regardless of study intensity.

Critical path analysis identifies these longest chains, helping you understand pacing requirements and potential bottlenecks in the learning progression. Concepts on the critical path deserve extra attention in content development, as delays in mastering these concepts cascade through all dependent material.

## Learning Graph Quality Score

The overall **learning graph quality score** provides a single metric (0-100) that aggregates multiple quality dimensions into an interpretable assessment. While individual metrics reveal specific issues, the quality score enables quick comparison and tracking of improvements over time.

The quality scoring algorithm used by `analyze-graph.py` weights various factors:

**Structural Validity (40 points):**

- DAG validation passes (20 points)
- No self-dependencies (10 points)
- All concepts in single connected component (10 points)

**Connectivity Quality (30 points):**

- Orphaned nodes 5-15% of total (10 points, scaled for deviation)
- Average dependencies 2.5-4.0 per concept (10 points, scaled)
- Maximum chain length appropriate for scope (10 points)

**Distribution Quality (20 points):**

- No linear chains exceeding 20% of graph (10 points)
- Indegree distribution follows expected pattern (10 points)

**Taxonomy Balance (10 points):**

- No single taxonomy category exceeds 30% (5 points)
- At least 5 taxonomy categories represented (5 points)

Interpretation of quality scores:

| Score Range | Quality Level | Interpretation |
|-------------|--------------|----------------|
| 90-100 | Excellent | Publication-ready, well-structured graph |
| 75-89 | Good | Minor improvements recommended |
| 60-74 | Acceptable | Several issues to address before content generation |
| 40-59 | Poor | Significant structural or quality problems |
| 0-39 | Critical | Major revision required |

The quality score should be calculated after every significant graph revision. Track scores over time to ensure your changes improve rather than degrade graph quality.
#### Diagram: Learning Graph Quality Score Calculator MicroSim

<iframe src="../../sims/learning-graph-quality-score-calculator-microsim/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Learning Graph Quality Score Calculator MicroSim</summary>
    Type: microsim

    Learning objective: Allow students to experiment with how different graph characteristics affect overall quality score

    Canvas layout (900x600px):
    - Left side (600x600): Quality score visualization
    - Right side (300x600): Interactive controls

    Visual elements (left panel):
    - Large circular gauge showing overall score (0-100)
    - Color-coded segments: Red (0-39), Orange (40-59), Yellow (60-74), Light Green (75-89), Dark Green (90-100)
    - Current score displayed in center in large font
    - Four horizontal bars below gauge showing component scores:
      * Structural Validity: 0-40 points (blue bar)
      * Connectivity Quality: 0-30 points (green bar)
      * Distribution Quality: 0-20 points (orange bar)
      * Taxonomy Balance: 0-10 points (purple bar)
    - Each bar shows points earned out of maximum

    Interactive controls (right panel):
    - Slider: "Number of Concepts" (50-300, default 200)
    - Slider: "Orphaned Nodes %" (0-40%, default 10%)
    - Slider: "Avg Dependencies" (1.0-6.0, default 3.2)
    - Slider: "Max Chain Length" (5-35, default 16)
    - Slider: "Linear Chain %" (10-80%, default 35%)
    - Slider: "Largest Taxonomy %" (10-60%, default 22%)
    - Checkbox: "Has Cycles" (default unchecked)
    - Checkbox: "Has Disconnected Subgraphs" (default unchecked)
    - Button: "Reset to Defaults"
    - Button: "Load Example: Poor Graph"
    - Button: "Load Example: Excellent Graph"

    Default parameters (Good Graph):
    - Concepts: 200
    - Orphaned: 10%
    - Avg Dependencies: 3.2
    - Max Chain: 16
    - Linear Chain %: 35%
    - Largest Taxonomy: 22%
    - No cycles, no disconnected subgraphs
    - **Expected Score: 82** (Good)

    Behavior:
    - Real-time recalculation as sliders move
    - Score gauge animates to new value
    - Component bars update proportionally
    - Color of gauge changes based on score range
    - Tooltip on hover shows calculation details for each component
    - "Poor Graph" example: cycles=true, orphaned=35%, score~28
    - "Excellent Graph" example: optimal all parameters, score~96

    Implementation notes:
    - Use p5.js for rendering gauge and bars
    - Implement scoring algorithm matching analyze-graph.py logic
    - Use DOM elements for sliders and checkboxes
    - Map() function to scale slider values to score components
    - Lerp() for smooth score animations

    Implementation: p5.js MicroSim with interactive controls

---
**MicroSim Generator Recommendations:**

1. microsim-p5 (92/100) - Interactive gauge and sliders are core p5.js strengths with DOM controls
2. chartjs-generator (65/100) - Can create gauge charts but limited interactivity compared to p5.js
3. vis-network (20/100) - Not designed for gauge visualizations or quality scoring interfaces

</details>

## Taxonomy Distribution and Balance

Beyond graph structure, the distribution of concepts across taxonomy categories affects curriculum balance and learning progression. A well-balanced taxonomy distribution ensures students encounter appropriate variety across knowledge domains without over-concentration in any single area.

### Taxonomy Categories

Learning graphs typically categorize concepts using a **TaxonomyID** field that groups related concepts into domains. Common taxonomy categories for technical courses include:

- **FOUND** - Foundational concepts and definitions
- **BASIC** - Basic principles and core ideas
- **ARCH** - Architecture and system design
- **IMPL** - Implementation and practical skills
- **TOOL** - Tools and technologies
- **SKILL** - Professional skills and practices
- **ADV** - Advanced topics and specializations

The number and specificity of taxonomy categories varies by subject matter. Introductory courses might use 5-8 broad categories, while specialized courses might employ 10-15 granular categories.

### TaxonomyID Abbreviations

TaxonomyIDs use 3-5 letter abbreviations for compactness in CSV files and visualization color-coding. When designing your taxonomy, choose abbreviations that are:

- **Distinctive:** No two categories should share the same first 3 letters
- **Mnemonic:** Abbreviation should suggest the full category name
- **Consistent:** Use similar grammatical forms (nouns vs. adjectives)

Example taxonomy abbreviations:

| TaxonomyID | Full Category Name | Color Code (visualization) |
|------------|-------------------|---------------------------|
| FOUND | Foundational Concepts | Red |
| BASIC | Basic Principles | Orange |
| ARCH | Architecture & Design | Yellow |
| IMPL | Implementation | Light Green |
| DATA | Data Management | Green |
| TOOL | Tools & Technologies | Light Blue |
| QUAL | Quality Assurance | Blue |
| ADV | Advanced Topics | Purple |

### Category Distribution Analysis

The **category distribution** metric shows what percentage of your total concepts fall into each taxonomy category. This distribution should reflect the emphasis and scope of your course.

Healthy category distributions typically exhibit:

- **No single category exceeds 30%:** Avoid over-concentration
- **Top 3 categories contain 50-70% of concepts:** Natural emphasis areas
- **At least 5 categories represented:** Adequate coverage breadth
- **Foundational category: 5-10% of concepts:** Appropriate base layer

The `taxonomy-distribution.py` script generates a detailed report showing both absolute counts and percentages for each category, enabling quick identification of imbalanced distributions.
#### Diagram: Taxonomy Distribution Pie Chart

<iframe src="../../sims/taxonomy-distribution-pie/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Taxonomy Distribution Pie Chart</summary>
    Type: chart

    Chart type: Pie chart with percentage labels

    Purpose: Visualize the distribution of 200 concepts across taxonomy categories

    Data:
    - FOUND (Foundational): 18 concepts (9%) - Red
    - BASIC (Basic Principles): 42 concepts (21%) - Orange
    - ARCH (Architecture): 38 concepts (19%) - Yellow
    - IMPL (Implementation): 35 concepts (17.5%) - Light Green
    - DATA (Data Management): 28 concepts (14%) - Green
    - TOOL (Tools): 22 concepts (11%) - Light Blue
    - QUAL (Quality): 12 concepts (6%) - Blue
    - ADV (Advanced): 5 concepts (2.5%) - Purple

    Title: "Learning Graph Taxonomy Distribution (200 Concepts)"

    Label format: "CATEGORY: N concepts (P%)"

    Annotations:
    - Callout for BASIC slice: "Largest category: 21% (healthy)"
    - Callout for ADV slice: "Smallest category: 2.5% (may need expansion)"
    - Legend positioned to right side

    Quality indicators:
    - Green checkmark: "No category exceeds 30% ✓"
    - Green checkmark: "8 categories represented ✓"
    - Green checkmark: "Top 3 categories = 59% ✓"

    Color scheme: Rainbow gradient (red → orange → yellow → green → blue → purple)

    Implementation: Chart.js pie chart with custom colors and labels

---
**MicroSim Generator Recommendations:**

1. chartjs-generator (98/100) - Pie chart with percentage labels and color coding is primary Chart.js use case
2. microsim-p5 (68/100) - Custom pie rendering possible but Chart.js provides better built-in features
3. venn-diagram-generator (15/100) - Designed for overlapping sets, not category distribution

</details>

### Avoiding Over-Representation

**Over-representation** occurs when a single taxonomy category dominates the learning graph, consuming more than 30% of total concepts. This imbalance can result from:

- **Scope creep:** Course expanded in one area without proportional breadth
- **Expert bias:** Instructor's specialization over-emphasized
- **Incomplete mapping:** Other categories insufficiently developed

Over-representation in foundational or basic categories suggests the course may be too introductory, while over-representation in advanced or specialized categories indicates potential accessibility issues for learners.

To correct over-representation:

1. **Review over-represented category:** Identify concepts that could be consolidated or removed
2. **Expand under-represented categories:** Add concepts to balance distribution
3. **Reclassify borderline concepts:** Move concepts to more appropriate categories
4. **Validate against learning outcomes:** Ensure distribution aligns with stated course objectives

The taxonomy distribution report generated by `taxonomy-distribution.py` flags any categories exceeding the 30% threshold, enabling quick identification of balance issues.

## Generating Quality Reports with Python Scripts

The learning graph quality validation process relies on three Python scripts located in the `docs/learning-graph/` directory. These scripts analyze your `learning-graph.csv` file and generate comprehensive quality reports in Markdown format.

### analyze-graph.py Script

The `analyze-graph.py` script performs comprehensive graph validation and quality analysis:

**Usage:**
```bash
cd docs/learning-graph
python analyze-graph.py learning-graph.csv quality-metrics.md
```

**Checks performed:**

1. CSV format validation
2. Self-dependency detection
3. Cycle detection (DAG validation)
4. Connectivity analysis
5. Orphaned node identification
6. Linear chain detection
7. Indegree/outdegree statistics
8. Maximum dependency chain calculation
9. Overall quality score computation

**Output:** Generates `quality-metrics.md` report file containing all findings, metrics, and a final quality score. Any critical issues (cycles, disconnected subgraphs) are highlighted at the top of the report.

### csv-to-json.py Script

The `csv-to-json.py` script converts your learning graph CSV to vis-network JSON format for visualization:

**Usage:**
```bash
cd docs/learning-graph
python csv-to-json.py learning-graph.csv learning-graph.json
```

**Functionality:**

- Parses CSV with ConceptID, ConceptLabel, Dependencies, TaxonomyID columns
- Generates nodes array with id, label, and group (taxonomy) fields
- Generates edges array with from and to fields (dependency arrows)
- Adds metadata section with graph statistics
- Validates JSON output format

**Output:** Creates `learning-graph.json` file that can be loaded by vis-network visualization tools to display your learning graph interactively.

### taxonomy-distribution.py Script

The `taxonomy-distribution.py` script analyzes the distribution of concepts across taxonomy categories:

**Usage:**
```bash
cd docs/learning-graph
python taxonomy-distribution.py learning-graph.csv taxonomy-distribution.md
```

**Analysis performed:**

- Counts concepts per taxonomy category
- Calculates percentage distribution
- Identifies over-represented categories (>30%)
- Identifies under-represented categories (<3%)
- Generates distribution table and summary statistics

**Output:** Creates `taxonomy-distribution.md` report with a table showing each category's count and percentage, plus recommendations for rebalancing if needed.

All three scripts should be run after any changes to your learning graph CSV file. Incorporate the generated reports into your MkDocs navigation to make quality metrics visible to reviewers and collaborators.

## Summary and Best Practices

Validating learning graph quality ensures your intelligent textbook rests on a sound pedagogical foundation. This chapter covered both structural validation (DAG properties, connectivity) and quality metrics (orphaned nodes, dependency distribution, taxonomy balance) that collectively determine graph effectiveness.

Key takeaways for maintaining high-quality learning graphs:

- **Always validate DAG structure first:** Circular dependencies and disconnected subgraphs are critical errors that must be fixed before proceeding
- **Target quality scores above 75:** Scores in this range indicate graphs ready for content generation
- **Monitor taxonomy distribution:** Keep any single category below 30% and ensure at least 5 categories represented
- **Aim for 2.5-4.0 average dependencies:** This range balances prerequisite completeness with learner accessibility
- **Accept 5-15% orphaned nodes:** Terminal and specialized concepts naturally have no dependents
- **Run all three Python scripts after edits:** Complete quality assessment requires structural validation, format conversion, and taxonomy analysis

Learning graph validation is iterative. Your first quality score may be low, but systematic application of the techniques in this chapter will guide improvements. Track your quality scores over time, targeting incremental increases until you achieve publication-ready scores above 85.

With a validated, high-quality learning graph in hand, you're ready to proceed to the next phase: converting your graph data to visualization formats and generating the rich content that will bring your intelligent textbook to life.

## References

1. [Topological Sorting](https://www.geeksforgeeks.org/dsa/topological-sorting/) - 2024 - GeeksforGeeks - Comprehensive tutorial on topological sorting algorithms including both DFS and BFS (Kahn's Algorithm) approaches for ordering DAG vertices, essential for understanding how to validate learning graph structure and generate valid prerequisite-respecting learning sequences.

2. [Introduction to Directed Acyclic Graph](https://www.geeksforgeeks.org/dsa/introduction-to-directed-acyclic-graph/) - 2024 - GeeksforGeeks - Educational resource explaining DAG properties, cycle detection algorithms, and common applications in scheduling and prerequisite management, providing theoretical foundation for learning graph quality validation techniques.
