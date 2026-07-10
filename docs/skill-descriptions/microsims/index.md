# Educational MicroSim Skills

!!! warning "Legacy snapshot"
    These per-skill pages describe the skills as they existed **before the
    2026-07 consolidation** into meta-skills. They are kept so existing links
    keep working. For the current 14-skill architecture and routing tables,
    see the [Skill Descriptions overview](../index.md).

Educational MicroSims are lightweight, interactive educational simulations designed for browser-based learning.
MicroSims are designed to run in a rectangular `iframe` placed within a page of a textbook.
The default height of a MicroSim is 500px and they are designed to be width-responsive so they
will adapt to various screen sizes and window resize events.

## Meta-Skill Architecture

MicroSim creation is organized into two meta-skills that consolidate related functionality:

| Meta-Skill | Purpose | Sub-Skills |
|------------|---------|------------|
| **microsim-generator** | Creates MicroSims using various JS libraries | 12 generator guides |
| **microsim-utils** | Utilities for MicroSim maintenance | 4 utility guides |

This architecture allows Claude Code to stay under the 30-skill limit while providing comprehensive MicroSim support. When you invoke a MicroSim skill, the meta-skill routes to the appropriate specialized guide.

## MicroSim Generator List

The **microsim-generator** meta-skill routes to the appropriate generator based on your request. Listed from most general to most specialized:

| # | Generator | Library | Best For |
|---|-----------|---------|----------|
| 1 | [MicroSim P5](./microsim-p5.md) | p5.js | Custom simulations, physics, animations |
| 2 | [Chart Generator](./chartjs-generator.md) | Chart.js | Bar, line, pie, doughnut, radar charts |
| 3 | [Comparison Table](./comparison-table-generator.md) | Custom | Side-by-side comparisons with ratings |
| 4 | [Concept Classifier](./concept-classifier.md) | p5.js | Classification quizzes with scenarios |
| 5 | [Mermaid Generator](./mermaid-generator.md) | Mermaid.js | Flowcharts, workflows, UML diagrams |
| 6 | [Vis-Network](./vis-network.md) | vis-network | Network graphs, concept maps |
| 7 | [Causal Loop](./causal-loop-microsim-generator.md) | vis-network | Systems thinking, feedback loops |
| 8 | [Math Function Plotter](./math-function-plotter-plotly.md) | Plotly.js | Mathematical function plots |
| 9 | [Timeline Generator](./timeline-generator.md) | vis-timeline | Chronological events, history |
| 10 | [Map Generator](./map-generator.md) | Leaflet.js | Geographic data, locations |
| 11 | [Venn Diagram](./venn-diagram-generator.md) | Custom | Set relationships (2-4 sets) |
| 12 | [Bubble Chart](./bubble-chart-generator.md) | Chart.js | Priority matrices, quadrants |
| 13 | [Celebration Animation](./celebration-generator.md) | p5.js | Particle effects, visual feedback |

## Common Elements to All MicroSims

All MicroSims are designed to run in a non-scrolling iframe that contains width-responsive drawing elements.

Sample `iframe`:

```html
<iframe src="http://example.com/microsims/my-microsim/main.html" height="500px" width="100%" scrolling="no">
```

MicroSims are packaged in a directory with the following files:

1. **main.html** - holds the main HTML code with possible inline CSS, JavaScript and data
2. **index.md** - documentation and `iframe` reference to a local `main.html`
3. **style.css** - optional CSS file
4. **script.js** - optional JavaScript file
5. **data.json** - optional JSON data file
6. **metadata.json** - optional Dublin Core metadata

Each generator follows templates located in `skills/microsim-generator/assets/templates/`.

All MicroSims should be designed to be width-responsive meaning that the components recenter and stretch if the containing window is resized.

---

## Generator Descriptions

### MicroSim P5 Generator

**Route Trigger:** simulation, animation, physics, bouncing, interactive, custom, p5.js

This is the most general-purpose skill that generates any p5.js application. It is ideal for simulations and animations where the user controls behavior through a set of controls at the bottom of the drawing area.

See the [MicroSim P5 Description](./microsim-p5.md)

### Chart Generator (ChartJS)

**Route Trigger:** chart, bar, line, pie, doughnut, radar, statistics, data

Creates general charts including bar, bubble, doughnut, line, pie, polar plot, radar, and scatter charts. The default is 500px high and fills 100% of the enclosing container width.

See the [ChartJS Generator](./chartjs-generator.md) skill description.

### Comparison Table Generator

**Route Trigger:** comparison, table, ratings, stars, side-by-side, features

Creates interactive comparison tables with color-coded star ratings (1-5 scale), difficulty badges (Easy/Medium/Hard), logos, and hover tooltips. Ideal for side-by-side comparisons of technologies, tools, frameworks, or any items with multiple evaluation criteria.

See the [Comparison Table Generator](./comparison-table-generator.md) skill description.

### Concept Classifier Quiz

**Route Trigger:** classify, quiz, categories, scenarios, identification

Creates interactive classification quiz MicroSims where students read scenarios and must identify the correct category from multiple choice options. All quiz content is stored in a separate `data.json` file.

Ideal for: identifying cognitive biases, logical fallacies, literary devices, taxonomic groups, design patterns, or matching scenarios to concepts.

See the [Concept Classifier](./concept-classifier.md) skill description.

### Mermaid Generator

**Route Trigger:** flowchart, workflow, process, state machine, UML, sequence diagram

The Mermaid.js library is ideal for specifying diagram content through text-based syntax. Supports:

- **Flowchart/Graph** - General-purpose flowcharts with decision points
- **State Diagram** - Models state transitions and lifecycles
- **Sequence Diagram** - Shows interactions between entities over time
- **User Journey** - Maps user experiences across stages
- **Class Diagram** - Object-oriented design showing classes and relationships
- **Entity Relationship (ER) Diagram** - Database schemas
- **C4 Diagram** - Software architecture views
- **Block Diagram** - High-level system components

See the [Mermaid Generator](./mermaid-generator.md)

### Vis-Network Generator

**Route Trigger:** network, nodes, edges, graph, dependencies, concept map, knowledge graph

Creates graph network diagrams using the vis-network JavaScript library. The user provides a list of nodes and edges as well as an optional list of groups.

See the [Vis Network](./vis-network.md) skill description.

### Causal Loop Diagram Generator

**Route Trigger:** causal, feedback, loop, systems thinking, reinforcing, balancing

Creates interactive Causal Loop Diagram (CLD) MicroSims for systems thinking education. Visualizes cause-and-effect relationships, feedback loops (reinforcing and balancing), and system dynamics.

Key features:

- **Polarity indicators**: Green (+) for positive, Red (-) for negative relationships
- **Loop markers**: R (reinforcing) and B (balancing) loop indicators
- **Interactive details**: Click nodes, edges, or loops for descriptions
- **Systems archetypes**: Support for common patterns (limits to growth, tragedy of the commons)

See the [Causal Loop MicroSim Generator](./causal-loop-microsim-generator.md) skill description.

### Math Function Plotter (Plotly)

**Route Trigger:** function, f(x), equation, plot, calculus, sine, cosine, polynomial

Creates professional, interactive mathematical function plots using Plotly.js. Features hover tooltips with precise coordinates, interactive sliders for exploring points along curves, and responsive design optimized for narrow textbook layouts.

See the [Math Function Plotter Plotly](./math-function-plotter-plotly.md) skill description.

### Timeline Generator

**Route Trigger:** timeline, dates, chronological, events, history, schedule, milestones

Takes an input of events and generates a timeline using the vis-timeline JavaScript library. Events should specify start dates, headlines, and optional descriptions.

See the [Timeline Generator](./timeline-generator.md) skill description.

### Map Generator

**Route Trigger:** map, geographic, coordinates, latitude, longitude, locations, markers

Generates interactive maps using the Leaflet JavaScript library. Creates geographic visualizations with markers, popups, and various map layers.

See the [Map Generator](./map-generator.md) skill description.

### Venn Diagram Generator

**Route Trigger:** venn, sets, overlap, intersection, union, categories

Creates Venn diagrams showing set relationships and overlaps (2-4 sets).

**Note:** Uses a custom implementation as Venn.js has not been maintained for several years.

See the [Venn Diagram Generator](./venn-diagram-generator.md) skill description.

### Bubble Chart Generator

**Route Trigger:** bubble, priority, matrix, quadrant, impact vs effort, risk vs value

A specialization of ChartJS for creating priority matrices, 2x2 quadrant visualizations, and multi-dimensional data displays where bubble size represents a third variable.

See the [Bubble Chart](./bubble-chart-generator.md) skill description.

### Celebration Animation Generator

**Route Trigger:** animation, celebration, particles, confetti, effects, reward

Creates self-contained p5.js celebration animation modules for visual feedback when students complete tasks correctly. Supports various motion patterns (burst, float, fall, explode, zoom, bounce) with a consistent API.

See the [Celebration Generator](./celebration-generator.md) skill description.

---

## MicroSim Utility Skills

The **microsim-utils** meta-skill provides maintenance and quality utilities:

### MicroSim Standardization

Validates MicroSim directories against a comprehensive quality checklist including structure, metadata, documentation, and required components. Generates quality scores and ensures consistency.

See the [MicroSim Standardization](./microsim-standardization.md) skill description.

### MicroSim Screen Capture

Automates the capture of high-quality screenshots for MicroSim visualizations using Chrome headless mode. Handles JavaScript-heavy visualizations that require proper rendering time.

See the [MicroSim Screen Capture](./microsim-screen-capture.md) skill description.

### MicroSim Add Icons

Adds clickable Creative Commons license and fullscreen navigation icons to the control region of an existing p5.js MicroSim.

See the [MicroSim Add Icons](./microsim-add-icons.md) skill description.

### MicroSim Index Generator

Generates index pages that list all MicroSims in a directory with thumbnails, descriptions, and links.

---

## Routing Logic

When you request a MicroSim, the **microsim-generator** meta-skill analyzes your request using keyword matching:

```
Has dates/timeline/chronological events?
  → timeline-guide.md

Has geographic coordinates/locations?
  → map-guide.md

Mathematical function f(x) or equation?
  → plotly-guide.md

Nodes and edges/network relationships?
  → vis-network-guide.md (or causal-loop-guide.md if systems thinking)

Flowchart/workflow/process diagram?
  → mermaid-guide.md

Sets with overlaps (2-4 categories)?
  → venn-guide.md

Priority matrix/2x2 quadrant?
  → bubble-guide.md

Standard chart (bar/line/pie/radar)?
  → chartjs-guide.md

Comparison table with ratings?
  → comparison-table-guide.md

Celebration/particles/visual feedback?
  → celebration-guide.md

Custom simulation/animation/physics?
  → p5-guide.md
```

For ambiguous requests, the skill presents options with scores and reasoning.

## Quality Standards

All MicroSims follow these standards:

- **Width-responsive** design (320px-1200px)
- **Non-scrolling** iframe container
- **Standard height**: 500px (adjustable)
- **Accessible** color schemes
- **Documentation** with lesson plans
- **Dublin Core** metadata for discoverability
