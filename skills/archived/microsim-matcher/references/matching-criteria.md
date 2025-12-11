# MicroSim Generator Matching Criteria

This reference document provides detailed matching criteria for all available MicroSim generator skills. Use this to score and rank which generator best matches a given diagram specification.

## Recent Updates

**Version Check:** This file is version-controlled on GitHub. Use `scripts/check-version.py` to verify you have the latest version.

- **2025-11-17**: Initial release with 9 MicroSim generators
  - Added: microsim-p5, chartjs-generator, math-function-plotter-plotly
  - Added: mermaid-generator, vis-network, timeline-generator
  - Added: map-generator, venn-diagram-generator, bubble-chart-generator
  - Included comprehensive scoring guidelines for each generator
  - Added decision tree and matching strategy sections

## Scoring Scale

- **90-100**: Perfect match - Primary use case for this generator
- **70-89**: Strong match - Well-suited, minor limitations
- **50-69**: Moderate match - Could work but not optimal
- **30-49**: Weak match - Significant limitations or workarounds needed
- **0-29**: Poor match - Not recommended, use different generator

## General Matching Factors

When scoring, consider:

1. **Data Type Match**: Does the specification's data structure align with what the generator expects?
2. **Interactivity Requirements**: Does the needed interactivity match the generator's capabilities?
3. **Visual Style**: Does the desired visual output match the generator's strengths?
4. **Complexity**: Is the specification within the generator's complexity range?
5. **Trigger Words**: Does the specification contain keywords strongly associated with this generator?

## MicroSim Generator Profiles

### 1. microsim-p5

**Skill Location**: `skills/microsim-p5/SKILL.md`

**Primary Use Cases:**
- Custom animations and simulations
- Interactive educational visualizations
- Physics simulations
- Generative art and creative coding
- Unique visualizations not served by standard libraries

**Data Types:**
- Any data type (most flexible)
- Real-time/dynamic data
- Procedural/algorithmic visualizations

**Interactivity Level:**
- Very High
- Sliders, buttons, mouse tracking
- Real-time parameter changes
- Custom interaction models

**Trigger Words/Phrases:**
- "animation", "simulation", "interactive"
- "custom visualization", "p5.js", "creative"
- "physics", "movement", "bouncing", "particles"
- "generative", "procedural", "algorithmic"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification requires custom animations, physics simulations, unique interactions not available in standard libraries, real-time updates, or mentions p5.js
- **Score 70-89 if**: Needs high interactivity with custom controls, visual effects, or creative visual style
- **Score 50-69 if**: Standard visualization with some custom styling needs
- **Score 30-49 if**: Could be done with p5 but standard library would be simpler
- **Score 0-29 if**: Pure data visualization better served by specialized libraries (charts, plots, diagrams)

**Strengths:**
- Complete flexibility and customization
- Complex animations and physics
- Real-time interactivity
- Creative visual effects

**Limitations:**
- Requires more development time
- Not optimized for standard charts/diagrams
- Steeper learning curve for users

---

### 2. chartjs-generator

**Skill Location**: `skills/chartjs-generator/SKILL.md`

**Primary Use Cases:**
- Standard statistical charts
- Data comparison visualizations
- Business intelligence dashboards
- Survey results and analytics

**Data Types:**
- Numerical data (continuous or discrete)
- Categorical data
- Time-series data (for line charts)
- Percentage/proportion data

**Chart Types Supported:**
1. Bar charts (vertical/horizontal)
2. Line charts
3. Pie charts
4. Doughnut charts
5. Radar charts
6. Polar area charts
7. Scatter plots
8. Bubble charts (also has dedicated bubble-chart-generator)

**Interactivity Level:**
- Medium
- Hover tooltips
- Legend toggling
- Responsive resizing

**Trigger Words/Phrases:**
- "chart", "bar chart", "line chart", "pie chart"
- "graph", "plot data", "visualize data"
- "compare", "statistics", "percentages"
- "dashboard", "analytics", "metrics"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification explicitly requests one of the supported chart types with numerical/categorical data
- **Score 70-89 if**: Data visualization needs that closely align with standard chart types
- **Score 50-69 if**: Could be represented as a chart but might benefit from more specialized tools
- **Score 30-49 if**: Chart representation possible but not optimal (e.g., timeline data, network data)
- **Score 0-29 if**: Non-chart visualization (diagrams, maps, networks, mathematical functions)

**Strengths:**
- Well-established library
- Clean, professional appearance
- Fast implementation
- Wide variety of chart types

**Limitations:**
- Limited to standard chart types
- Less suitable for custom visualizations
- Not designed for diagrams or workflows

---

### 3. math-function-plotter-plotly

**Skill Location**: `skills/math-function-plotter-plotly/SKILL.md`

**Primary Use Cases:**
- Mathematical function plots
- Calculus visualizations
- Physics equations and wave functions
- Engineering transfer functions
- Scientific function analysis

**Data Types:**
- Mathematical expressions (f(x) = ...)
- Continuous functions
- Parametric equations
- Numerical function data

**Function Categories:**
- Trigonometric (sin, cos, tan)
- Polynomial (quadratic, cubic, etc.)
- Exponential and logarithmic
- Physics/engineering functions
- Custom mathematical expressions

**Interactivity Level:**
- High
- Interactive sliders to move points along curves
- Hover tooltips showing coordinates
- Zoom and pan
- PNG export

**Trigger Words/Phrases:**
- "function", "plot", "f(x)", "equation"
- "graph", "mathematical", "calculus"
- "sine", "cosine", "polynomial", "exponential"
- "plotly", "interactive function"
- "domain", "range", "continuous"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification describes plotting a mathematical function with domain/range, mentions f(x) notation, or requests function exploration with sliders
- **Score 70-89 if**: Scientific/physics plot that can be expressed as a function
- **Score 50-69 if**: Numerical data that could be approximated as a function
- **Score 30-49 if**: Plot needs but not specifically functions (discrete data, categorical)
- **Score 0-29 if**: Non-plot visualizations (diagrams, charts, timelines, networks)

**Strengths:**
- Powerful Plotly.js library
- Smooth continuous curves (500+ points)
- Interactive exploration with sliders
- Educational lesson plans included
- Professional mathematical notation

**Limitations:**
- Focused on functions, not discrete data points
- Not suitable for diagrams or structural visualizations
- Requires function expression in JavaScript Math format

---

### 4. mermaid-generator

**Skill Location**: `skills/mermaid-generator/SKILL.md`

**Primary Use Cases:**
- Flowcharts and process diagrams
- State machines and state diagrams
- Sequence diagrams (interactions over time)
- Entity-relationship diagrams
- Class diagrams (UML)
- User journey maps

**Data Types:**
- Structural/hierarchical relationships
- Sequential processes
- State transitions
- Entity relationships
- Workflow steps

**Diagram Types Supported:**
1. Flowchart/Graph - Decision trees, workflows
2. State Diagram - State machines, lifecycle
3. Sequence Diagram - Interactions, API calls
4. ER Diagram - Database schemas
5. Class Diagram - Object-oriented design
6. User Journey - UX flows
7. Block Diagram - System components

**Interactivity Level:**
- Low to Medium
- Primarily static diagrams
- Some hover effects
- Limited interactivity compared to other generators

**Trigger Words/Phrases:**
- "flowchart", "flow chart", "diagram"
- "workflow", "process", "procedure"
- "state machine", "state diagram"
- "sequence diagram", "interaction"
- "ER diagram", "entity relationship"
- "class diagram", "UML"
- "decision tree", "logic flow"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification describes flowcharts, state machines, sequence diagrams, or other standard diagram types supported by Mermaid
- **Score 70-89 if**: Process or structural visualization that fits Mermaid's diagram types
- **Score 50-69 if**: Could be represented as a diagram but might need customization
- **Score 30-49 if**: Diagram needs but with heavy interactivity requirements
- **Score 0-29 if**: Data-driven visualizations (charts, plots, timelines) or highly interactive needs

**Strengths:**
- Wide variety of diagram types
- Clean, professional appearance
- Text-based specification (easy to modify)
- Good for documentation

**Limitations:**
- Limited interactivity
- Less suitable for data-heavy visualizations
- Shape sizes may not scale responsively
- Not ideal for network graphs with physics

---

### 5. vis-network

**Skill Location**: `skills/vis-network/SKILL.md`

**Primary Use Cases:**
- Network diagrams (nodes and edges)
- Concept dependency graphs
- Learning graphs showing prerequisite relationships
- Knowledge maps
- Social network visualizations
- System architecture diagrams with connections

**Data Types:**
- Nodes (entities) and edges (relationships)
- Graph structures
- Hierarchical data that can be graphed
- Network topologies

**Interactivity Level:**
- Very High
- Physics-based layout
- Drag nodes
- Click for details
- Zoom and pan
- Hover tooltips
- Dynamic clustering

**Trigger Words/Phrases:**
- "network", "graph", "nodes", "edges"
- "relationships", "connections", "dependencies"
- "concept map", "knowledge graph"
- "prerequisite", "dependency graph"
- "network diagram", "topology"
- "vis-network", "interactive graph"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification describes nodes and edges, network relationships, dependency graphs, or concept maps with connections
- **Score 70-89 if**: Hierarchical or relational data that naturally forms a network structure
- **Score 50-69 if**: Connected data but could also be shown as a tree or diagram
- **Score 30-49 if**: Relationships exist but not the primary focus
- **Score 0-29 if**: Non-network visualizations (charts, plots, timelines, workflows without connections)

**Strengths:**
- Physics-based automatic layout
- Highly interactive
- Excellent for complex relationships
- Scales well with many nodes
- Group/cluster support

**Limitations:**
- Can be overwhelming with too many nodes
- Not ideal for strict hierarchies (use Mermaid instead)
- Requires node and edge data structure

---

### 6. timeline-generator

**Skill Location**: `skills/timeline-generator/SKILL.md`

**Primary Use Cases:**
- Historical timelines
- Project timelines and schedules
- Product roadmaps and release plans
- Course schedules and curricula
- Event chronologies
- Organizational milestones

**Data Types:**
- Temporal/chronological data
- Events with specific dates
- Date ranges (start and end dates)
- Categorized events (optional groups)

**Interactivity Level:**
- High
- Zoom in/out on timeline
- Pan left/right
- Click events for detailed information
- Category filtering with buttons
- Hover for tooltips

**Trigger Words/Phrases:**
- "timeline", "chronological", "chronology"
- "events", "history", "historical"
- "schedule", "calendar", "dates"
- "roadmap", "milestones", "phases"
- "project timeline", "course timeline"
- "sequence of events", "over time"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification includes events with specific dates, mentions timeline/chronological order, or describes temporal sequences
- **Score 70-89 if**: Time-based data that would benefit from timeline visualization
- **Score 50-69 if**: Sequential data without specific dates (could use other methods)
- **Score 30-49 if**: Some temporal aspect but not the primary organizing principle
- **Score 0-29 if**: Non-temporal visualizations (charts, diagrams, networks, plots)

**Strengths:**
- Specialized for temporal data
- Excellent date handling and formatting
- Zoom and pan for long timelines
- Category filtering
- Event detail panels

**Limitations:**
- Requires date information
- Not suitable for non-temporal data
- Limited to linear time representation

---

### 7. map-generator

**Skill Location**: `skills/map-generator/SKILL.md`

**Primary Use Cases:**
- Geographic visualizations
- Location markers and points of interest
- Route visualization
- Regional data (GeoJSON)
- Campus maps, facility maps
- Travel itineraries

**Data Types:**
- Geographic coordinates (latitude, longitude)
- Location names (geocoded to coordinates)
- GeoJSON data for regions
- Marker data with descriptions
- Multiple map layers

**Interactivity Level:**
- Very High
- Zoom in/out
- Pan across map
- Click markers for popups
- Toggle layers
- Marker clustering for dense data

**Trigger Words/Phrases:**
- "map", "geographic", "location"
- "coordinates", "latitude", "longitude"
- "markers", "pins", "points of interest"
- "route", "path", "journey"
- "GeoJSON", "regions", "boundaries"
- "leaflet", "interactive map"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification includes geographic coordinates, location names, map regions, or explicitly requests a map visualization
- **Score 70-89 if**: Location-based data that would benefit from spatial representation
- **Score 50-69 if**: Some geographic component but could use other representations
- **Score 30-49 if**: Location mentioned but not central to visualization
- **Score 0-29 if**: Non-geographic visualizations (charts, timelines, diagrams, plots)

**Strengths:**
- Full-featured mapping with Leaflet.js
- Multiple basemap options (street, satellite, terrain)
- Layer support for complex visualizations
- Marker customization
- GeoJSON support for regions

**Limitations:**
- Requires geographic data
- Not suitable for abstract spatial layouts
- May be overkill for simple location lists

---

### 8. venn-diagram-generator

**Skill Location**: `skills/venn-diagram-generator/SKILL.md`

**Primary Use Cases:**
- Set theory visualizations
- Category overlap comparisons
- Concept relationship diagrams (2-4 sets)
- Educational comparisons
- Feature comparison diagrams

**Data Types:**
- Sets (2-4 distinct categories)
- Set intersections and overlaps
- Educational definitions for each region
- Proportional or symbolic sizes

**Interactivity Level:**
- Medium
- Hover tooltips with educational definitions
- Static circular layout
- Definitions from glossary (preferred)

**Trigger Words/Phrases:**
- "venn", "venn diagram"
- "sets", "set theory", "overlap"
- "intersection", "union"
- "compare", "categories", "groups"
- "commonalities", "differences"
- "2 circles", "3 circles", "4 circles"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification explicitly requests Venn diagram or describes 2-4 sets with overlaps and intersections
- **Score 70-89 if**: Category comparison that would benefit from showing overlaps
- **Score 50-69 if**: Comparison of categories but overlaps not emphasized
- **Score 30-49 if**: Multiple categories but no clear overlap relationships
- **Score 0-29 if**: Not a set comparison (charts, timelines, networks, plots)

**Strengths:**
- Clear visualization of set relationships
- Educational tooltips with glossary integration
- Simple, clean appearance
- Supports 2-4 sets

**Limitations:**
- Limited to 2-4 sets
- Proportional sizing can be misleading
- Less suitable for complex relationships (use vis-network instead)
- Library not actively maintained (use with caution)

**Special Note**: Always check `/docs/glossary.md` for existing definitions before asking user for set definitions.

---

### 9. bubble-chart-generator

**Skill Location**: `skills/bubble-chart-generator/SKILL.md`

**Primary Use Cases:**
- Priority matrices (2x2 grids)
- Impact vs Effort analysis
- Risk vs Value assessment
- Portfolio analysis
- Multi-dimensional data comparison (x, y, size)

**Data Types:**
- Items with 2-3 dimensions
- X-axis value (e.g., Effort, Time, Cost)
- Y-axis value (e.g., Impact, Value, Priority)
- Size dimension (optional, e.g., Resource requirement)
- Quadrant categorization

**Interactivity Level:**
- Medium
- Hover tooltips
- Quadrant highlighting
- Click for details
- Legend toggling

**Trigger Words/Phrases:**
- "priority matrix", "prioritization"
- "bubble chart", "bubble plot"
- "impact vs effort", "effort vs impact"
- "risk vs value", "value vs complexity"
- "portfolio", "quadrant", "2x2"
- "multi-dimensional", "scatter with size"

**Scoring Guidelines:**
- **Score 90-100 if**: Specification describes priority matrix, impact vs effort, 2x2 quadrant analysis, or bubble chart with 3 dimensions
- **Score 70-89 if**: Multi-dimensional comparison that would benefit from bubble visualization
- **Score 50-69 if**: 2D scatter plot without size dimension (could use chartjs instead)
- **Score 30-49 if**: Comparison data but not naturally 2D or quadrant-based
- **Score 0-29 if**: Non-comparative visualizations or single-dimension data

**Strengths:**
- Specialized for priority/portfolio analysis
- Quadrant labeling and highlighting
- Good for decision-making visualizations
- Clean Chart.js implementation

**Limitations:**
- Very specific use case
- Limited to 2-3 dimensions
- May be overkill for simple scatter plots
- Overlap can make bubbles hard to read with many items

---

## Matching Strategy

### Step-by-Step Matching Process

1. **Extract Key Characteristics**
   - Data type (temporal, geographic, relational, numerical, categorical, mathematical)
   - Visual style (chart, diagram, plot, map, timeline, network)
   - Interactivity needs (static, hover, click, drag, sliders, real-time)
   - Explicit mentions of tools/libraries

2. **Identify Primary Matches**
   - Look for trigger words specific to each generator
   - Match data type to generator specialization
   - Consider visual style requirements

3. **Score Each Generator**
   - Use the 0-100 scale defined for each generator above
   - Consider multiple factors (data, interaction, visual, trigger words)
   - Be honest about limitations

4. **Rank by Score**
   - Sort generators from highest to lowest score
   - Include top 3-5 recommendations minimum
   - Always include at least one score above 50 if possible

5. **Provide Reasoning**
   - Explain why the score is high/low
   - Mention specific features that match or don't match
   - Suggest alternatives if score is low
   - Note any caveats or considerations

### Decision Tree Examples

**Has dates/timeline?**
→ YES: timeline-generator (high score)
→ NO: Continue

**Has geographic coordinates?**
→ YES: map-generator (high score)
→ NO: Continue

**Mathematical function f(x)?**
→ YES: math-function-plotter-plotly (high score)
→ NO: Continue

**Nodes and edges?**
→ YES: vis-network (high score)
→ NO: Continue

**Flowchart/process/workflow?**
→ YES: mermaid-generator (high score)
→ NO: Continue

**Sets with overlaps?**
→ YES: venn-diagram-generator (high score)
→ NO: Continue

**Priority matrix / 2x2?**
→ YES: bubble-chart-generator (high score)
→ NO: Continue

**Standard chart type (bar, line, pie)?**
→ YES: chartjs-generator (high score)
→ NO: Continue

**Custom/animated/unique?**
→ YES: microsim-p5 (high score)
→ NO: Need more information

---

## Common Ambiguities and How to Resolve

### "Interactive visualization of data"
- **Clarify**: What type of data? What kind of interaction?
- **Consider**: chartjs-generator (if standard charts), microsim-p5 (if custom)

### "Graph showing..."
- **Clarify**: "Graph" can mean chart (ChartJS) or network graph (vis-network)
- **Look for**: Nodes/edges → vis-network; Data points → chartjs or function plot

### "Diagram of..."
- **Clarify**: Structural (Mermaid), Network (vis-network), or Custom (p5)?
- **Look for**: Process words → Mermaid; Relationship words → vis-network

### "Timeline with events"
- **Clear choice**: timeline-generator (high score)
- **Alternative**: chartjs line chart (lower score)

### "Map of concepts"
- **Clarify**: Geographic map or concept map?
- **Geographic** → map-generator
- **Conceptual** → vis-network or mermaid-generator

---

## Quality Assurance

When providing match scores, ensure:

1. **At least one score ≥ 70**: There should be a good match
2. **Diversity in scores**: Show range of options (don't score everything 50)
3. **Clear reasoning**: Explain scores with specific features
4. **Honesty about limitations**: Don't oversell poor matches
5. **Alternative suggestions**: If primary match has limitations, mention alternatives
6. **Complete ranking**: Include all relevant generators (usually 3-5 minimum)
