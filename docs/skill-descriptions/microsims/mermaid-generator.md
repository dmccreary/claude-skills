# Mermaid Diagram Generator

## Overview

The mermaid-generator skill creates interactive workflow diagrams using the Mermaid JavaScript library. It generates complete MicroSim packages with standalone HTML files featuring colorful backgrounds, 16-point fonts, and top-down rendering by default for educational textbooks.

## Purpose

This skill automates the creation of professional flowcharts, process diagrams, workflow visualizations, and decision trees that are immediately ready for embedding in MkDocs sites or standalone use.

## Key Features

- **Top-Down Flowcharts**: Default TD (top-down) direction for optimal readability
- **Colorful Node Backgrounds**: Vibrant, educational-friendly color schemes
- **16-Point Fonts**: Optimal readability from back of classroom
- **Interactive Controls**: Zoom and export functionality
- **Complete MicroSim Package**: HTML, CSS, JavaScript, documentation, and metadata
- **MkDocs Integration**: Ready for iframe embedding

## When to Use

Use this skill when users request:
- Workflow diagrams or process flows
- Decision trees with branching logic
- Algorithm visualizations
- System architecture flows
- Educational process diagrams
- Step-by-step procedure illustrations
- State transition diagrams
- Any flowchart-style visualization

## Common Trigger Phrases

- "Create a flowchart showing..."
- "Generate a workflow diagram for..."
- "Make a decision tree for..."
- "Visualize the process of..."

## Workflow Steps

### Step 1: Gather Requirements
- Diagram purpose and workflow being illustrated
- Key steps/nodes in the workflow
- Decision points (branching if/then logic)
- Flow direction (top-down, left-right)
- Start and end points

### Step 2: Design Mermaid Flowchart
- Choose node shapes (rectangles, diamonds, circles)
- Select color palette (vibrant, professional, ocean, custom)
- Define style classes for consistent theming
- Ensure 16pt fonts for all elements
- Use top-down direction by default

### Step 3: Create MicroSim Structure
```
docs/sims/[diagram-name]/
├── main.html         # Standalone visualization
├── style.css         # Responsive styling
├── script.js         # Interactive features
├── index.md          # Documentation
└── metadata.json     # Dublin Core metadata
```

### Step 4: Generate Files from Templates
- Replace placeholders with actual content
- Embed Mermaid code in main.html
- Configure zoom and export features
- Create comprehensive documentation

### Step 5: Validate and Test
- Syntax validation
- File structure verification
- Font size confirmation (16px)
- Color contrast check
- Responsive design testing

## Node Shapes and Purposes

- **Rounded rectangles** `("Label")`: Start/end points
- **Rectangles** `["Label"]`: Process steps
- **Diamonds** `{"Decision?"}`: Decision points
- **Circles** `(("Label"))`: Connectors

## Color Palettes

### Vibrant (Purple/Blue/Pink)
- Engaging diagrams for educational content
- High contrast for visibility

### Professional (Turquoise/Mint/Coral)
- Formal content
- Business process flows

### Ocean (Blue Spectrum)
- Technical content
- System architecture

### Custom
- Match textbook theme
- Brand colors

## Mermaid Syntax Example

```mermaid
flowchart TD
    Start("Start Process"):::startNode
    Step1["Gather Input"]:::processNode
    Decision{"Valid Input?"}:::decisionNode
    Step2["Process Data"]:::processNode
    Success("Success"):::successNode
    Error("Error - Retry"):::errorNode

    Start --> Step1 --> Decision
    Decision -->|Yes| Step2 --> Success
    Decision -->|No| Error --> Step1

    classDef startNode fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef processNode fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef decisionNode fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
    classDef successNode fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef errorNode fill:#fa709a,stroke:#333,stroke-width:2px,color:#fff,font-size:16px

    linkStyle default stroke:#999,stroke-width:2px,font-size:16px
```

## Interactive Features

- **Zoom Controls**: Zoom in/out for large diagrams
- **Export to SVG**: Save diagrams for presentations
- **Node Interaction Tracking**: Monitor student engagement
- **Accessibility Features**: Keyboard navigation support

## Output Structure

Each generated diagram includes:
- `main.html`: Standalone interactive diagram with Mermaid.js
- `style.css`: Responsive styling with 16px fonts and print-friendly rules
- `script.js`: Zoom controls, export functionality, interaction tracking
- `index.md`: MkDocs integration page with overview and usage guide
- `metadata.json`: Dublin Core metadata for searchability

## Metadata Fields

- Title and description
- Subject area
- Publication date
- Target audience
- Node and edge counts
- Concepts illustrated
- Bloom's Taxonomy level
- Version and dependencies

## MkDocs Integration

Add to navigation in `mkdocs.yml`:

```yaml
nav:
  - Visualizations:
    - Software Lifecycle: sims/software-lifecycle/index.md
```

Or integrate into chapter navigation:

```yaml
nav:
  - Chapter 3:
    - Introduction: chapters/03/index.md
    - Workflow Diagram: sims/workflow/index.md
```

## Best Practices

### Design Principles
1. **Clarity over Complexity**: Keep diagrams focused—break complex flows into multiple diagrams
2. **Consistent Styling**: Use same color palette across related diagrams
3. **Meaningful Labels**: Clear, concise labels (2-5 words max per node)
4. **Logical Flow**: Ensure arrows flow in expected reading direction
5. **Color Semantics**: Use colors consistently (green=success, red=errors)

### Accessibility
1. **Font Size**: Always 16px minimum for readability
2. **Color Contrast**: Ensure WCAG AA compliance (4.5:1)
3. **Text Alternatives**: Provide descriptive text in index.md
4. **Semantic HTML**: Use proper heading structure

### Educational Integration
1. **Align with Learning Goals**: Map to specific objectives
2. **Bloom's Taxonomy**: Tag with appropriate cognitive level
3. **Concept Dependencies**: Link to prerequisite concepts
4. **Practice Exercises**: Include comprehension questions

## Common Patterns

### Linear Process Flow
```
Start → Step 1 → Step 2 → Step 3 → End
```

### Decision Tree
```
Start → Decision 1 (Yes/No)
  ├─ Yes → Action A → End
  └─ No → Decision 2 (Yes/No)
      ├─ Yes → Action B → End
      └─ No → Action C → End
```

### Loop/Iteration
```
Start → Initialize → Process → Check Complete?
  ├─ No → Process (loop back)
  └─ Yes → End
```

### Error Handling
```
Start → Try Action → Success?
  ├─ Yes → Continue → End
  └─ No → Error Handler → Retry or Exit
```

## Troubleshooting

### Issue: Mermaid code doesn't render
**Solution**: Check for syntax errors (missing quotes/brackets), verify flowchart TD is first line

### Issue: Fonts not 16px
**Solution**: Verify `font-size:16px` in all classDef declarations and linkStyle

### Issue: Colors not showing
**Solution**: Confirm classDef declarations come after flowchart code and verify `:::className` syntax

### Issue: Diagram too large/small
**Solution**: Adjust node count (split if >15 nodes) or modify CSS max-width

### Issue: Labels cut off
**Solution**: Shorten text, use markdown strings for wrapping, increase container width

## Integration with Other Skills

- **learning-graph-generator**: Create diagrams for learning concepts
- **chapter-content-generator**: Embed diagrams in chapter content
- **microsim-p5**: Use Mermaid for static workflows, p5.js for dynamic simulations
- **quiz-generator**: Create questions about workflow understanding
- **glossary-generator**: Define terms used in diagram labels

## When to Use Mermaid vs. Chart.js, p5.js, and vis.js

Choose Mermaid When:

### 1\ **Text-Based Generation is Priority**

Mermaid excels when AI needs to generate diagrams from text descriptions because:

-   **Simple, declarative syntax** - LLMs can reliably output valid Mermaid code
-   **Low hallucination risk** - Structured syntax reduces errors compared to imperative code
-   **No computation required** - Pure markup, no need for data calculations or logic
-   **Version control friendly** - Text format works well in documentation and repositories

### 2. **Diagram Type Matches Mermaid Strengths**

Use Mermaid for:

-   Flowcharts and process diagrams
-   ER diagrams and database schemas
-   State machines and sequence diagrams
-   Git graphs and timelines
-   Architecture diagrams
-   Class diagrams
-   Gantt charts (simple project timelines)

### 3. **Static Documentation Context**

-   Embedding in Markdown files (GitHub, GitLab, MkDocs)
-   Technical documentation sites
-   README files and wikis
-   Static site generators
-   Simple, read-only visualizations

### Choose Chart.js Over Mermaid When:

### 1. **Data-Driven Charts**

-   Bar charts, line graphs, scatter plots with actual data
-   Need precise control over scales, axes, and gridlines
-   Real-time data updates and animations
-   Statistical visualizations
-   Dashboard metrics

### 2. **Customization Requirements**

-   Complex styling and theming
-   Interactive tooltips and hover effects
-   Responsive design with specific breakpoints
-   Plugin ecosystem for specialized features

## Choose p5.js Over Mermaid When:

### 1. Creative or Custom Visualizations

-   Unique, non-standard diagram types
-   Generative art or creative data visualization
-   Custom animations and interactions
-   Physics simulations
-   Particle systems
-   Educational simulations (like you mentioned with microsims)

### 2. Full Control Required

-   Pixel-level drawing control
-   Complex animation sequences
-   Game-like interactions
-   Audio-visual synchronization

### Choose vis.js Over Mermaid When:

#### 1. **Complex Network Graphs**

-   Large node-edge networks (hundreds or thousands of nodes)
-   Interactive network exploration
-   Physics-based layout algorithms
-   Hierarchical networks
-   Dynamic graph updates

#### 2. **Advanced Timeline Visualizations**

-   Complex timelines with groups and nested items
-   Interactive time-based data exploration
-   Resource scheduling

## Decision Matrix for AI Generation

| Factor | Mermaid | Chart.js | p5.js | vis.js |
| --- |  --- |  --- |  --- |  --- |
| **AI Generation Ease** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| --- |  --- |  --- |  --- |  --- |
| **Syntax Simplicity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **No Runtime Logic** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ |
| **Data Visualization** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Custom Interactions** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Static Diagrams** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |

### Practical Guidelines for AI-Generated Diagrams

### **Use Mermaid as Default for:**

1.  Conceptual diagrams (workflows, architectures, relationships)
2.  Documentation that lives in Markdown
3.  Quick prototypes and mockups
4.  When the diagram structure is more important than pixel-perfect design
5.  When you need guaranteed rendering without JavaScript execution

### Switch to From Mermaid to Chart.js when:

1.  You have actual numerical data to plot
2.  Need standard chart types (bar, line, pie, radar)
3.  Interactive data exploration is required
4.  Precise statistical representation matters

### Switch from Mermaid to p5.js when:

1.  Creating educational simulations
2.  Need custom drawing logic AI can generate
3.  Building unique, non-standard visualizations
4.  Combining graphics with user interaction

### Switch to vis.js when:

1.  Dealing with network/graph data with many nodes
2.  Need physics-based layouts
3.  Interactive graph exploration is essential
4.  Mermaid's graph capabilities are insufficient

## AI Generation Considerations

### Why Mermaid is Often Best for AI:

-   **Predictable output** - Syntax is consistent and well-documented
-   **Error recovery** - Easier to debug text-based syntax
-   **Token efficiency** - Shorter code for same result
-   **No state management** - No need to track variables or state
-   **Rendering agnostic** - Works in multiple environments without modification

### When to Use Other Libraries for MicroSims

-   Chart.js: When you need to **process data** (calculations, aggregations)
-   p5.js: When you need **procedural generation** or custom logic
-   vis.js: When you need **complex interactivity** with large datasets

## Summary

1. **Default to Mermaid** for structural, conceptual, and process diagrams in documentation contexts. 
2. **Upgrade to Chart.js** when you need data-driven charts with standard formats. 
3. **Choose p5.js** for creative, educational, or highly custom visualizations. 
4. **Select vis.js** for complex network graphs that exceed Mermaid's capabilities.

For AI generation specifically, Mermaid's text-based, declarative syntax makes it the most reliable choice for ~80% of diagram use cases.

## References

- Mermaid.js Documentation: https://mermaid.js.org/
- MkDocs Material Theme: https://squidfunk.github.io/mkdocs-material/
- Flowchart Syntax: https://mermaid.js.org/syntax/flowchart.html
