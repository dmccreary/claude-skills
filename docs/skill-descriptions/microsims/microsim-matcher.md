# MicroSim Matcher

!!! warning "Deprecated - Functionality Integrated into microsim-generator"
    The MicroSim Matcher functionality has been integrated into the **microsim-generator** meta-skill. You no longer need to invoke a separate matching skill - simply describe your visualization needs and the microsim-generator will automatically route to the appropriate generator.

## Current Status

As of the meta-skill consolidation, MicroSim matching is now **automatic**. When you invoke `microsim-generator` or describe a visualization request, the skill:

1. Analyzes your request for trigger keywords
2. Matches against all 13 available generators
3. Routes to the best-fit generator automatically
4. For ambiguous requests, presents ranked options with scores

## How to Use (Updated Workflow)

Instead of:
```
1. Invoke microsim-matcher
2. Get recommendations
3. Invoke recommended generator
```

Simply:
```
1. Describe your visualization need
2. microsim-generator routes automatically
```

## Routing Decision Tree

The integrated routing logic uses this decision tree:

| Trigger Keywords | Routes To |
|------------------|-----------|
| timeline, dates, chronological, events, history | timeline-guide |
| map, geographic, coordinates, latitude, longitude | map-guide |
| function, f(x), equation, plot, calculus, sine | plotly-guide |
| network, nodes, edges, graph, dependencies, concept map | vis-network-guide |
| causal, feedback, loop, systems thinking, reinforcing | causal-loop-guide |
| flowchart, workflow, process, state machine, UML | mermaid-guide |
| venn, sets, overlap, intersection, union | venn-guide |
| bubble, priority, matrix, quadrant, impact vs effort | bubble-guide |
| chart, bar, line, pie, doughnut, radar, statistics | chartjs-guide |
| comparison, table, ratings, stars, side-by-side | comparison-table-guide |
| celebration, particles, confetti, effects, reward | celebration-guide |
| simulation, animation, physics, bouncing, custom, p5.js | p5-guide |

## Handling Ambiguous Requests

When a request matches multiple generators, microsim-generator:

1. Scores the top 3 candidates (0-100 scale)
2. Presents options with reasoning:
   ```
   Based on your request, I recommend:
   1. [Generator A] (Score: 85) - Best for [reason]
   2. [Generator B] (Score: 70) - Alternative if you need [feature]
   3. [Generator C] (Score: 55) - Possible if [condition]

   Which would you prefer?
   ```
3. Proceeds with user's selection

## Common Ambiguities Resolved

| Ambiguous Term | Clarification |
|----------------|---------------|
| "graph" | Chart (ChartJS) vs Network graph (vis-network) |
| "diagram" | Structural (Mermaid) vs Network (vis-network) vs Custom (p5) |
| "map" | Geographic (Leaflet) vs Concept map (vis-network) |
| "visualization" | Depends on data type and interaction needs |

## Available Generators (13 Total)

The routing logic evaluates matches against:

| Generator | Library | Best For |
|-----------|---------|----------|
| p5-guide | p5.js | Custom simulations, physics, animations |
| chartjs-guide | Chart.js | Bar, line, pie, doughnut, radar charts |
| comparison-table-guide | Custom | Side-by-side comparisons with ratings |
| mermaid-guide | Mermaid.js | Flowcharts, workflows, UML diagrams |
| vis-network-guide | vis-network | Network graphs, concept maps |
| causal-loop-guide | vis-network | Systems thinking, feedback loops |
| plotly-guide | Plotly.js | Mathematical function plots |
| timeline-guide | vis-timeline | Chronological events, history |
| map-guide | Leaflet.js | Geographic data, locations |
| venn-guide | Custom | Set relationships (2-4 sets) |
| bubble-guide | Chart.js | Priority matrices, quadrants |
| celebration-guide | p5.js | Particle effects, visual feedback |

## Scoring Criteria

The integrated matcher evaluates:

- **Data Type Match**: Categorical, numerical, temporal, spatial, relational
- **Interactivity Requirements**: Static, animated, user-controlled
- **Visual Complexity**: Simple shapes to complex multi-element visualizations
- **Layout Needs**: Fixed, responsive, zoomable, scrollable
- **Special Features**: Tooltips, legends, export, real-time updates

## See Also

- [MicroSim Generator Index](./index.md) - Overview of all MicroSim skills
- [microsim-generator SKILL.md](https://github.com/dmccreary/ibook-skills/blob/main/skills/microsim-generator/SKILL.md) - Full routing logic
- [routing-criteria.md](https://github.com/dmccreary/ibook-skills/blob/main/skills/microsim-generator/references/routing-criteria.md) - Detailed scoring methodology

## Historical Note

The standalone `microsim-matcher` skill existed prior to the meta-skill consolidation (November 2024). It was merged into `microsim-generator` to:

- Reduce the number of skills (staying under the 30-skill limit)
- Provide seamless routing without extra invocation steps
- Centralize MicroSim creation logic in one meta-skill
