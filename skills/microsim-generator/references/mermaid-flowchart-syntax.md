# Mermaid Flowchart Syntax Reference

Syntax details for Mermaid v11 flowcharts, used by the mermaid-generator workflow
(`references/mermaid-guide.md`). This file covers node/edge syntax and the named color
palettes; layout rules, tooltips, and the 2/3+1/3 panel pattern are covered in the guide itself.

## Node Shapes

| Syntax | Shape | Typical use |
|--------|-------|-------------|
| `id("Label")` | Rounded rectangle (stadium-ish) | Start / end |
| `id["Label"]` | Rectangle | Process step |
| `id{"Label"}` | Diamond | Decision point |
| `id(("Label"))` | Circle | Connector / junction |
| `id(["Label"])` | Stadium (fully rounded) | Start / end (alternate) |
| `id[["Label"]]` | Subroutine (double-bordered rect) | Call to a separate process |
| `id[("Label")]` | Cylinder | Data store / database |
| `id[/"Label"/]` | Parallelogram (leaning right) | Input |
| `id[\"Label"\]` | Parallelogram (leaning left) | Output |
| `id{{"Label"}}` | Hexagon | Preparation step |

Wrap every label in double quotes (`"Label"`) — required whenever the label contains spaces,
punctuation, or any of the characters in the "Avoid" table in mermaid-guide.md.

## Edges / Arrows

| Syntax | Meaning |
|--------|---------|
| `A --> B` | Solid arrow (standard flow) |
| `A -.-> B` | Dotted arrow (optional / conditional path) |
| `A ==> B` | Thick arrow (emphasized / primary path) |
| `A --- B` | Solid line, no arrowhead |
| `A -->|Label| B` | Labeled arrow (e.g. decision branch: `Yes`/`No`) |
| `A --> B & C` | Fan-out: A points to both B and C |
| `A & B --> C` | Fan-in: both A and B point to C |

## Directions

Set once at the top of the diagram, right after `flowchart`:

- `TD` / `TB` — top-down (default; use unless the user asks for a different layout)
- `LR` — left-to-right (good for narrow, wide-format panels)
- `RL` — right-to-left
- `BT` — bottom-to-top

## Comments

```
%% This line is a comment and is not rendered
```

Use sparingly — comments help maintainers reading the raw Mermaid source, not the rendered
diagram, and add no value to students viewing the output.

## Subgraphs (Grouping Nodes)

```
subgraph Phase1 ["Planning Phase"]
    direction TD
    A["Gather Requirements"]
    B["Define Scope"]
end
```

- The bracketed string after the subgraph ID is its display title.
- Always pair a titled subgraph with `subGraphTitleMargin` in `mermaid.initialize()` — see the
  mandatory rule in mermaid-guide.md Step 2, item 7.
- A subgraph can set its own `direction`, independent of the outer flowchart's direction.

## Named Color Palettes

Hex values for the four palette options mentioned in mermaid-guide.md Step 2, item 2:

**Vibrant** (purple/blue/pink — engaging, general-audience diagrams):
```
classDef startNode    fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef processNode  fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef decisionNode fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
classDef endNode      fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
```

**Professional** (turquoise/mint/coral — formal or business content):
```
classDef startNode    fill:#0f9b8e,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef processNode  fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#333,font-size:16px
classDef decisionNode fill:#ff6f61,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef endNode      fill:#95e1d3,stroke:#333,stroke-width:2px,color:#333,font-size:16px
```

**Ocean** (blue spectrum — technical/scientific content):
```
classDef startNode    fill:#0083b0,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef processNode  fill:#00b4d8,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
classDef decisionNode fill:#90e0ef,stroke:#333,stroke-width:2px,color:#333,font-size:16px
classDef endNode      fill:#48cae4,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
```

Always add an `errorNode` class when a diagram has failure/retry branches — pick a warm red
that contrasts with the palette's other classes (e.g. `#fa709a` for Vibrant, `#e63946` for
Professional, `#0077b6` for Ocean is too close to the palette — use `#ef476f` instead for Ocean).

## Styling a Single Node (Without classDef)

For a one-off style that doesn't warrant a reusable class:

```
style NodeId fill:#f9f,stroke:#333,stroke-width:4px
```

Prefer `classDef` + `:::className` for anything reused across 2+ nodes — `style` does not
scale to a full diagram's color scheme.

## External Resources

- Mermaid.js Syntax Reference: https://mermaid.js.org/syntax/flowchart.html
- Mermaid Theming: https://mermaid.js.org/config/theming.html
