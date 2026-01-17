# Content Element Types for Textbook Chapters

This reference describes the various non-pure-text content elements that can be used to break up textbook content and enhance learning. Each element type should be specified in `<details markdown="1">` blocks when generating chapter content.
The content of the details blocks should be to describe what the learning objective is and
how a non-pure-text element can be used to promote learning.

## Driven By An Learning Objective

Behind the strategy for every diagram is to help the student learn. A unit of learning
is called a Learning Objective and diagrams are a wonderful way to teach visually.

By understanding the `Bloom Levels` and `Bloom Verbs` of learning objective we encounter, we can map the objective to a specific type of interactive diagram, chart, infographic or even a MicroSim.

Here are the six Bloom Levels of learning objectives

1. Remember (L1) - Recall facts and basic concepts
2. Understand (L2) - Explain ideas or concepts
3. Apply (L3) - Use knowledge to solve problems
4. Analyze (L4) - Examine relationships, connect concepts
5. Evaluate (L5) - Judge value, make decisions
6. Create (L6) - Design new solutions, produce original work

Here are the Bloom Verbs associated with each Bloom Level.When
you generate a diagram specification within a details block, use both the Bloom Level and Bloom Verb to describe a MicroSim.

### Remember (L1)
list, define, recall, identify, name, recognize, locate, describe

### Understand (L2)
explain, summarize, interpret, classify, compare, contrast, exemplify, infer

### Apply (L3)
use, execute, implement, solve, demonstrate, calculate, apply, practice

### Analyze (L4)
differentiate, organize, attribute, compare, contrast, examine, deconstruct, distinguish

### Evaluate (L5)
judge, critique, assess, justify, prioritize, recommend, validate, defend

### Create (L6)
design, construct, develop, formulate, compose, produce, invent, generate

## Examples of MicroSims for each Bloom Level

### Remember (L1) — Recall facts, terms, and basic concepts 

1. Flash Card MicroSims — Flip cards to reveal definitions or answers 
2. Term Sorter MicroSims — Drag terms into correct category bins
3. Label the Diagram — Click or drag labels onto parts of an image
4. Matching Pairs — Connect terms to their definitions with lines 
5. Sequence Ordering — Arrange steps or events in chronological order 

### Understand (L2) — Explain ideas and demonstrate comprehension 

1. Concept Matcher — Match concepts to their explanations or examples 
2. Paraphrase Checker — Select the best restatement of a concept
3. Analogy Builder — Complete "A is to B as C is to ___" relationships
4. Translation Converter — Convert between representations (e.g., equation
↔ graph)
5. Predict the Output — Given inputs, predict what a system will produce

### Apply (L3) — Use knowledge to solve problems

1. Interactive Calculator — Adjust sliders to solve equations or formulas
2. Parameter Explorer — Modify variables and observe simulation changes
3. Step-by-Step Solver — Work through problems with guided scaffolding
4. Code Tracer — Execute code mentally and predict variable states
5. Scenario Simulator — Apply rules to new situations and see outcomes

### Analyze (L4) — Identify patterns, relationships, and structure

1. Network Graph Explorer — Identify connections between nodes
2. Data Pattern Finder — Spot trends and outliers in visualizations 
3. Cause-Effect Mapper — Draw arrows between causes and their effects 
4. Component Breakdown — Decompose systems into constituent parts 
5. Compare-Contrast Matrix — Fill in similarities and differences between 
items 

### Evaluate (L5) — Make judgments and assess quality 

1. Classification Sorter — Categorize examples as valid/invalid or by quality
2. Error Detector — Find and flag mistakes in code, proofs, or arguments
3. Ranking Ladder — Order items by effectiveness, quality, or priority
4. Decision Tree Navigator — Evaluate criteria to reach justified conclusions 
5. Rubric Rater — Score examples against defined criteria 

### Create (L6) — Design, construct, and produce original work

1. Model Editor — Build custom models with draggable components 
2. Diagram Builder — Construct flowcharts, circuits, or concept maps
3. Equation Composer — Assemble formulas from mathematical building blocks
4. Algorithm Designer — Arrange code blocks to create working programs
5. Synthesis Canvas — Combine elements to design novel solutions or systems 

## Element Types Overview

The goal is to have not have more than four paragraphs of pure text without incorporating one of these elements. Students don't like to see large blocks of pure text scrolling in their intelligent textbook. They want to interact with the content.

## 1. Markdown Lists

**Type identifier:** `markdown-list`

**When to use:**
- Enumerating key points, features, or characteristics
- Presenting step-by-step procedures
- Listing examples or categories

**Implementation:** Embed directly in markdown content (no `<details markdown="1">` block needed)

**Requirements:**
- ALWAYS place a blank line before the list
- Use numbered lists for sequences or ordered items
- Use bullet lists for unordered collections

**Example:**
```markdown
The following are key characteristics of graph databases:

- Native graph storage
- Constant-time traversals
- Flexible schema
```

## 2. Markdown Tables

**Type identifier:** `markdown-table`

**When to use:**
- Comparing features across multiple dimensions
- Presenting structured data
- Showing before/after comparisons

**Implementation:** Embed directly in markdown content (no `<details markdown="1">` block needed)

**Requirements:**
- ALWAYS place a blank line before the table
- Use clear, concise column headers
- Keep cell content brief
- Ensure proper markdown table syntax

**Example:**
```markdown
Here is a comparison of database types:

| Feature | RDBMS | Graph Database |
|---------|-------|----------------|
| Schema | Rigid | Flexible |
| Joins | Required | Native traversal |
| Query Speed (multi-hop) | Slow | Fast |
```

## 3. Admonitions

An admonition is another way to break up a wall of text.
They should be used only occasionally. Try to not have
more than one per page.

Our intelligent textbooks use the MkDocs Material theme
which supports admonitions.

Here are the admonition types supported by MkDocs Material:

```markdown
!!! note
 This is a note admonition.

!!! abstract
 This is an abstract/summary/tldr admonition.

!!! info
 This is an info/todo admonition.

!!! tip
 This is a tip/hint/important admonition.

!!! success
 This is a success/check/done admonition.

!!! question
 This is a question/help/faq admonition.

!!! warning
 This is a warning/caution/attention admonition.

!!! failure
 This is a failure/fail/missing admonition.

!!! danger
 This is a danger/error admonition.

!!! bug
 This is a bug admonition.

!!! example
 This is an example admonition.

!!! quote
 This is a quote/cite admonition.

With custom titles:

!!! note "Custom Title Here"
 Content with a custom title.

Collapsible (requires pymdownx.details):

??? note "Click to expand"
 This content is hidden by default.

???+ note "Expanded by default"
 This content is visible but can be collapsed.

Inline admonitions (Material theme):

!!! info inline
 Inline left admonition.

!!! info inline end
 Inline right admonition.
```

The Collapsible admonition that uses `???` is a fun way to challenge students
test their knowledge.It can be used at the end of a chapter to present
a question and then reveal an answer.

```markdown
??? note "What are the first six digits of Pi? - Click to expand"
 3.14159
```

## 4. Diagrams and Drawings

In this section, you will create a detailed specification for a diagram, drawing, chart, flowchart, workflow, infographic or interactive MicroSim.

**Type identifier:** `diagram`

**When to use:**
- Illustrating system architectures
- Showing relationships between components
- Explaining abstract concepts visually
- Depicting data flows or processes
- Defining an infographic that has items in a diagram or workflow with hover-triggered information boxes

**Implementation:** 

Add a level 4 header that indicates we are placing a diagram in the content and leave
a template for an iframe that displays the diagram or microsim

```markdown
#### Diagram: {{DIAGRAM_NAME}}
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>
```

Note that the {MICROSIM_NAME} in the src path must be a string kebab-case (lowercase letters and dashes)

Use `<details markdown="1">` block with a detailed specification

**Required information in description:**

- Diagram Name - A title-case name of the diagram that is unique in the chapter
- Bloom Taxonomy - one of six levels of the 2001 Bloom Taxonomy: Remember, Understand, Analyze, Create
- Bloom Taxonomy Verb - one of the verbs from the bloom-taxonomy-verbs.md in the references
- Learning Objective - what concepts are we trying to teach
- What components/elements should be shown
- How elements are connected or related
- Suggested visual style (flowchart, network diagram, block diagram, etc.)
- Key labels and annotations
- Color scheme if relevant

**Example specification:**
```xml
#### Diagram: CMDB Architecture Diagram
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>
<details markdown="1">
<summary>CMDB Architecture Diagram</summary>
Type: diagram

Purpose: Show the traditional CMDB architecture with RDBMS foundation

Components to show:
- CMDB Application Layer (top)
- Business Logic Layer (middle)
- RDBMS Storage Layer (bottom)
- Multiple "CI Tables" within RDBMS layer
- Relationship tables connecting CI tables

Connections:
- Vertical arrows showing data flow from app to storage
- Horizontal arrows between relationship tables and CI tables

Style: Block diagram with layered architecture

Labels:
- "Configuration Items (CIs)" on tables
- "Relationships" on junction tables
- "Foreign Keys" on connection arrows

Color scheme: Blue for application layers, orange for database layer
</details>
```

!!! Note
 Do not over specify the positioning of items using absolute (x,y) coordinates.
 MicroSims are all width responsive and must adapt to windows that are resized.

## 5. Interactive Infographics

**Type identifier:** `infographic`

**When to use:**
- Presenting statistical information visually
- Creating clickable concept maps
- Building progressive disclosure interfaces
- Showing hierarchical information

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Purpose and main message
- Visual layout and organization
- Interactive elements (hovers, clicks, reveals)
- Data to be displayed
- Color coding or visual hierarchy
- Responsive behavior

**Example MicroSim Specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">

<summary>ITIL Framework Evolution Interactive Timeline</summary>
Type: infographic

Purpose: Show the evolution of ITIL from version 1 (1990) through current version, with clickable details

Layout: Horizontal timeline with major milestones

Milestones:
- 1990: ITIL v1 (31 books)
- 2001: ITIL v2 (7 books)
- 2007: ITIL v3 (5 books, lifecycle approach)
- 2011: ITIL 2011 (update to v3)
- 2019: ITIL 4 (value-driven service management)

Interactive elements:
- Hover over each milestone to see key changes
- Click to expand full details panel
- Hover over connecting lines to see transition challenges

Visual style: Modern timeline with circular nodes for milestones
Color scheme: Red gradient getting darker for newer versions

Implementation: HTML/CSS/JavaScript with SVG timeline
</details>
```

## 6. MicroSims (p5.js Simulations)

**Type identifier:** `microsim`

**When to use:**
- Demonstrating dynamic behavior
- Allowing students to experiment with parameters
- Visualizing algorithms or processes
- Showing cause-and-effect relationships

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Learning objective (what concept is being taught)
- Visual elements in the simulation
- Interactive controls (sliders, buttons, inputs)
- Default parameter values
- What happens when parameters change
- Canvas layout (drawing area + controls area)
- Animation or static visualization

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>Graph Traversal Visualization MicroSim</summary>
Type: microsim

Learning objective: Demonstrate the difference between depth-first search (DFS) and breadth-first search (BFS) in graph traversal

Canvas layout:
- Left side (450): Drawing area showing a graph network
- Right side (150): Control panel and infobox

Visual elements:

- 15 nodes arranged in a tree-like structure
- Edges connecting nodes
- Start node (green)
- Current node (yellow)
- Visited nodes (blue)
- Unvisited nodes (gray)

Interactive controls:
- Dropdown: Select algorithm (DFS or BFS)
- Button: "Start Traversal"
- Button: "Reset"
- Slider: Animation speed (50-1000ms per step)
- Display: Node visit order as a list

Default parameters:
- Algorithm: DFS
- Animation speed: 500ms
- Start node: Node 1

Behavior:
- When "Start Traversal" clicked, animate the selected algorithm
- Highlight current node in yellow
- Mark visited nodes in blue
- Display visit order in right panel
- Show queue/stack state for educational purposes

Implementation notes:
- Use p5.js for rendering
- Store graph as adjacency list
- Implement both DFS (recursive/stack) and BFS (queue)
- Use frameCount for animation timing
</details>
```

## 7. Charts (Bar, Line, Pie)

**Type identifier:** `chart`

**When to use:**
- Presenting quantitative data
- Showing trends over time
- Comparing values across categories
- Illustrating proportions or distributions

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Chart type (bar, line, pie, scatter, etc.)
- Data to be plotted (specific values or representative data)
- Axis labels and units
- Title and legend
- Color scheme
- Key insights to highlight

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>
<details markdown="1">
<summary>Query Performance Comparison: RDBMS vs Graph Database</summary>
Type: chart

Chart type: Bar chart

Purpose: Show performance degradation of RDBMS multi-hop queries compared to constant-time graph traversals

X-axis: Number of hops (1, 2, 3, 4, 5)
Y-axis: Query response time (milliseconds, logarithmic scale)

Data series:
1. RDBMS (orange bars):
 - 1 hop: 10ms
 - 2 hops: 150ms
 - 3 hops: 2,500ms
 - 4 hops: 45,000ms
 - 5 hops: 780,000ms (timed out)

2. Graph Database (gold bars):
 - 1 hop: 5ms
 - 2 hops: 8ms
 - 3 hops: 12ms
 - 4 hops: 15ms
 - 5 hops: 18ms

Title: "Multi-Hop Query Performance: RDBMS vs Graph Database"
Legend: Position top-right

Annotations:
- Arrow pointing to RDBMS 5-hop bar: "Query timed out after 13 minutes"
- Arrow pointing to graph DB series: "Constant-time traversal"

Implementation: Chart.js or similar JavaScript library
</details>
```

## 8. Timeline

**Type identifier:** `timeline`

**When to use:**
- Showing historical progression
- Illustrating project phases
- Demonstrating evolution of concepts
- Presenting sequential events

Timelines are ideal for putting current events into context.
Timelines can be used at the begging of a textbook to show
the historical events that triggered an important based of knowledge.

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Time period covered
- Major events/milestones with dates
- Visual style (horizontal/vertical, linear/branching)
- Detail level for each event
- Color coding or visual grouping
- Interactive features if applicable

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>Evolution of Configuration Management Timeline</summary>
Type: timeline

Time period: 1980-2025

Orientation: Horizontal

Events:
- 1980: Military configuration management practices established
- 1990: ITIL v1 released (31 books including Configuration Management)
- 1995: First commercial CMDB implementations
- 2001: ITIL v2 consolidates CM practices
- 2005-2010: "CMDB crisis" - high failure rates reported
- 2012: Neo4j gains traction for IT dependency management
- 2015: Observability tools (Dynatrace, etc.) begin automated discovery
- 2018: Graph-based CMDB alternatives emerge
- 2020: COVID pandemic accelerates digital transformation
- 2023: AI-assisted IT management graphs
- 2025: Real-time graph-based IT management becomes standard

Visual style: Horizontal timeline with alternating above/below placement

Color coding:
- Red: ITIL/traditional CMDB era (1990-2010)
- Orange: Transition period (2010-2015)
- Gold: Graph database adoption (2015-2020)
- Green: Modern AI-enhanced approaches (2020+)

Interactive features:
- Hover to see detailed description
- Click to expand with images/screenshots from that era
</details>
```

## 9. Maps with Movement Arrows

**Type identifier:** `map`

**When to use:**
- Showing geographic distribution
- Illustrating data flows across regions
- Demonstrating adoption patterns
- Visualizing network topologies

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Geographic scope (world, region, country)
- Locations to mark
- Directional flows or connections
- Data being represented
- Legend and labels
- Color scheme
- Interactive features

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>GDPR Data Flow Compliance Map</summary>
Type: map

Geographic scope: World map focusing on EU and major trading partners

Purpose: Illustrate data flow restrictions under GDPR

Locations:
- European Union (highlighted in blue)
- United States (highlighted in orange)
- United Kingdom (highlighted in purple)
- Asia-Pacific data centers (marked with icons)

Data flows (arrows):
- Green arrows: Permitted flows (within EU)
- Yellow arrows: Conditional flows (EU to UK, adequacy decision)
- Red arrows: Restricted flows (EU to US, requires safeguards)
- Dotted arrows: Data center backup routes

Labels:
- "GDPR Protected Territory"
- "Adequacy Decision Required"
- "Standard Contractual Clauses (SCCs) Required"

Legend:
- Arrow colors and meanings
- Icon explanations (data center, user, cloud)

Interactive features:
- Hover over arrows to see data transfer requirements
- Click regions to see compliance details
</details>
```

## 10. Workflow Diagrams with Hover Text

**Type identifier:** `workflow`

**When to use:**
- Illustrating business processes
- Showing decision trees
- Explaining system interactions
- Demonstrating procedural steps

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Process name and purpose
- Steps in the workflow (with descriptions)
- Decision points and branches
- Start and end states
- Hover text content for each element
- Visual style (swimlanes, flowchart, BPMN)
- Roles or systems involved

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>Change Management Workflow with Impact Analysis</summary>
Type: workflow

Purpose: Show the change management process using graph-based impact analysis

Visual style: Flowchart with decision diamonds and process rectangles

Steps:
1. Start: "Change Request Submitted"
 Hover text: "Engineer submits change request for system update"

2. Process: "Query IT Management Graph"
 Hover text: "Run graph traversal to identify all downstream dependencies"

3. Process: "Calculate Blast Radius"
 Hover text: "Determine which services, applications, and business functions are affected"

4. Decision: "Risk Level?"
 Hover text: "Based on blast radius: Low (<10 services), Medium (10-50), High (>50)"

5a. Process: "Auto-Approve" (if Low risk)
Hover text: "Changes affecting fewer than 10 services are auto-approved"

5b. Process: "Manager Review" (if Medium risk)
Hover text: "Changes affecting 10-50 services require manager approval"

5c. Process: "CAB Review" (if High risk)
Hover text: "Changes affecting >50 services require Change Advisory Board review"

6. Process: "Notify Affected Teams"
 Hover text: "Automated notifications sent to all teams managing dependent services"

7. End: "Change Approved"
 Hover text: "Change ticket updated and implementation scheduled"

Color coding:
- Blue: Data/query steps
- Yellow: Decision points
- Green: Approval outcomes
- Orange: Communication steps

Swimlanes:
- Requester
- IT Management Graph System
- Approval Authority
- Affected Teams
</details>
```

## 11. Graph Data Models (vis-network)

**Type identifier:** `graph-model`

**When to use:**
- Showing entity relationships
- Demonstrating graph database schemas
- Illustrating dependency networks
- Visualizing knowledge graphs

**Implementation:** Use `<details markdown="1">` block with specification

**Required information in description:**
- Node types and their properties
- Edge types and their properties
- Sample data to display
- Layout algorithm (force-directed, hierarchical, circular)
- Visual styling (colors, shapes, sizes)
- Interactive features (zoom, drag, click, hover)
- Legend explaining node/edge types

**Example specification:**
```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>IT Management Graph Data Model</summary>
Type: graph-model

Purpose: Illustrate the node and relationship types in a typical IT management graph

Node types:
1. Business Service (pink circles)
 - Properties: name, owner, SLA_target
 - Example: "Customer Portal"

2. Application (light blue squares)
 - Properties: name, version, technology_stack
 - Example: "Web Server v2.1"

3. Infrastructure (gray diamonds)
 - Properties: name, type, location
 - Example: "Server-001 (VM)"

4. Data Store (orange cylinders)
 - Properties: name, type, size_gb
 - Example: "Customer DB"

Edge types:
1. DEPENDS_ON (solid black arrows)
 - Properties: criticality (high/medium/low)
 - Example: Business Service → Application

2. HOSTS (dashed blue arrows)
 - Properties: deployment_type
 - Example: Infrastructure → Application

3. CONNECTS_TO (dotted green arrows)
 - Properties: protocol, port
 - Example: Application → Data Store

Sample data:
- Customer Portal (Business Service)
├─ DEPENDS_ON → Web Application (Application)
│├─ HOSTS ← VM-Server-001 (Infrastructure)
│└─ CONNECTS_TO → Customer DB (Data Store)
└─ DEPENDS_ON → API Gateway (Application)
 └─ CONNECTS_TO → Auth Service DB (Data Store)

Layout: Hierarchical with business services at top

Interactive features:
- Hover node: Show properties
- Click node: Highlight all connected nodes
- Double-click: Expand/collapse dependencies
- Zoom: Mouse wheel
- Pan: Click and drag background

Visual styling:
- Node size based on number of connections (degree)
- Edge thickness based on criticality
- Highlight critical path in red when node selected

Legend:
- Node shapes and their meanings
- Edge styles and their meanings
- Color coding explanation

Implementation: vis-network JavaScript library
Canvas size: 800x600px
</details>
```

## General Guidelines for All Content Elements

1. **Progressive Complexity:** Place simpler elements earlier in the chapter, more complex ones later
2. **Concept Coverage:** Ensure elements connect back to concepts listed in "Concepts Covered"
3. **Learning Objectives:** Every element should serve a clear pedagogical purpose
4. **Accessibility:** Provide text alternatives for visual elements
5. **Consistency:** Use similar visual styles and color schemes throughout a chapter
6. **Interactivity:** Favor interactive elements (infographics, MicroSims) that enable student engagement tracking
7. **Balance:** Mix different types of elements rather than using the same type repeatedly

## Details Block Template

For any element requiring specification (types 3-10), use this template:

```xml
<iframe src="../../sims/{MICROSIM_NAME}/main.html" width="100%" height="500xp" scrolling="no"></iframe>

<details markdown="1">
<summary>Brief descriptive title</summary>
Type: [element-type]

Purpose: [What educational goal does this serve?]

[Element-specific details as outlined above]

Implementation: [Technology/approach to be used]
</details>
```

The specification should be detailed enough that another skill or developer can implement the element without additional context.
