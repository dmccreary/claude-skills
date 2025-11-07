# Mermaid Flowchart Syntax Reference

This reference guide covers Mermaid flowchart syntax for generating interactive workflow diagrams.

## Basic Structure

Every Mermaid flowchart starts with a direction declaration:

```mermaid
flowchart TD
    A --> B
```

## Direction Options

Control flowchart orientation:
- **TD** or **TB**: Top to bottom (default for this skill)
- **BT**: Bottom to top
- **LR**: Left to right
- **RL**: Right to left

## Node Shapes

Mermaid supports various node shapes for different purposes:

| Shape | Syntax | Best For |
|-------|--------|----------|
| Rectangle | `A["Label"]` | Process steps, actions |
| Rounded Rectangle | `A("Label")` | Start/end points |
| Diamond | `A{"Decision?"}` | Decision points |
| Circle | `A(("Label"))` | Connectors, junctions |
| Stadium | `A(["Label"])` | Subroutines |
| Hexagon | `A{{"Label"}}` | Preparation steps |
| Parallelogram | `A[/"Input/Output"/]` | Data input/output |
| Trapezoid | `A[\"Process"\]` | Manual operations |

**Examples:**

```mermaid
flowchart TD
    Start("Start Process")
    Process["Execute Task"]
    Decision{"Success?"}
    End("End Process")

    Start --> Process --> Decision
    Decision -->|Yes| End
    Decision -->|No| Process
```

## Edges and Arrows

Connect nodes with various edge types:

| Type | Syntax | Use Case |
|------|--------|----------|
| Arrow | `A --> B` | Standard flow |
| Line (no arrow) | `A --- B` | Connection without direction |
| Dotted arrow | `A -.-> B` | Optional or conditional flow |
| Thick arrow | `A ==> B` | Primary/emphasized flow |
| Arrow with text | `A -->|Label| B` | Labeled transition |

**Edge Label Syntax:**

```mermaid
flowchart TD
    A -->|16pt label| B
    C -.->|Optional| D
    E ==>|Primary Path| F
```

## Styling Nodes

Apply colors and formatting to individual nodes:

```mermaid
flowchart TD
    A["Node"]
    style A fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
```

**Common Style Properties:**
- `fill`: Background color (hex or CSS color name)
- `stroke`: Border color
- `stroke-width`: Border thickness (pixels)
- `color`: Text color
- `font-size`: Font size (16px recommended for this skill)

## Class-Based Styling

Define reusable style classes for consistent theming:

```mermaid
flowchart TD
    A["Start"]:::startStyle
    B["Process"]:::processStyle
    C{"Decision"}:::decisionStyle

    classDef startStyle fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef processStyle fill:#95e1d3,stroke:#333,stroke-width:2px,color:#333,font-size:16px
    classDef decisionStyle fill:#f38181,stroke:#333,stroke-width:2px,color:#fff,font-size:16px

    A --> B --> C
```

## Styling Edges

Style links (edges) by their index:

```mermaid
flowchart TD
    A --> B --> C

    linkStyle 0 stroke:#ff6b6b,stroke-width:3px,font-size:16px
    linkStyle 1 stroke:#4ecdc4,stroke-width:3px,font-size:16px
```

**Note:** Links are indexed starting from 0 in the order they appear.

## Subgraphs

Group related nodes into subgraphs:

```mermaid
flowchart TD
    subgraph SG1[Data Processing]
        direction LR
        A["Input"] --> B["Transform"] --> C["Output"]
    end

    Start("Start") --> SG1
    SG1 --> End("End")
```

## Colorful Workflow Example

Here's a complete example with colorful backgrounds and 16pt fonts:

```mermaid
flowchart TD
    Start("Start"):::startNode
    Input["Gather Input"]:::processNode
    Validate{"Valid?"}:::decisionNode
    Process["Execute Process"]:::processNode
    Success("Success"):::successNode
    Error("Error"):::errorNode

    Start --> Input --> Validate
    Validate -->|Yes| Process --> Success
    Validate -->|No| Error

    classDef startNode fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef processNode fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef decisionNode fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
    classDef successNode fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
    classDef errorNode fill:#fa709a,stroke:#333,stroke-width:2px,color:#fff,font-size:16px

    linkStyle default stroke:#999,stroke-width:2px,font-size:16px
```

## Recommended Color Palettes

**Vibrant Palette:**
- Start/End: `#667eea` (purple-blue)
- Process: `#764ba2` (deep purple)
- Decision: `#f093fb` (pink)
- Success: `#4facfe` (light blue)
- Error: `#fa709a` (coral pink)

**Professional Palette:**
- Start/End: `#4ecdc4` (turquoise)
- Process: `#95e1d3` (mint)
- Decision: `#f38181` (coral)
- Success: `#6c5ce7` (purple)
- Error: `#ff7675` (red)

**Ocean Palette:**
- Start/End: `#0083b0` (ocean blue)
- Process: `#00b4d8` (sky blue)
- Decision: `#90e0ef` (light blue)
- Success: `#48cae4` (cyan)
- Error: `#0077b6` (deep blue)

## Best Practices

1. **Font Size**: Always use 16px font size for labels and edges for optimal readability
2. **Color Contrast**: Ensure text color contrasts well with background (use `color:#fff` for dark backgrounds, `color:#333` for light backgrounds)
3. **Consistent Styling**: Use class definitions for consistent appearance across similar nodes
4. **Edge Labels**: Keep edge labels concise (1-3 words) at 16pt
5. **Node Labels**: Use Title Case for node labels
6. **Direction**: Default to TD (top-down) unless horizontal flow is more intuitive
7. **Stroke Width**: Use 2-3px stroke width for clear node borders

## Common Patterns

**Linear Workflow:**
```mermaid
flowchart TD
    A["Step 1"] --> B["Step 2"] --> C["Step 3"] --> D["Step 4"]
```

**Branching Decision:**
```mermaid
flowchart TD
    Start("Start") --> Decision{"Condition?"}
    Decision -->|True| PathA["Action A"]
    Decision -->|False| PathB["Action B"]
    PathA --> End("End")
    PathB --> End
```

**Loop Pattern:**
```mermaid
flowchart TD
    Start("Start") --> Process["Process Item"]
    Process --> Check{"More Items?"}
    Check -->|Yes| Process
    Check -->|No| End("End")
```

**Parallel Processing:**
```mermaid
flowchart TD
    Start("Start") --> Split["Split Data"]
    Split --> Process1["Process A"]
    Split --> Process2["Process B"]
    Split --> Process3["Process C"]
    Process1 --> Merge["Merge Results"]
    Process2 --> Merge
    Process3 --> Merge
    Merge --> End("End")
```

## Interactive Features

Add click handlers or hyperlinks to nodes:

```mermaid
flowchart TD
    A["Click Me"]
    click A "https://example.com" "Open Example"
```

## Comments

Add comments for documentation:

```mermaid
flowchart TD
    %% This is a comment explaining the workflow
    A["Start"] --> B["End"]
```

## Text Formatting

Use markdown within labels:

```mermaid
flowchart TD
    A["**Bold** text and *italic* text"]
```

## Special Characters

Escape special characters in labels using quotes:

```mermaid
flowchart TD
    A["Node with 'quotes' and #symbols"]
```
