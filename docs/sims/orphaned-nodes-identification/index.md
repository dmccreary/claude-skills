---
title: Terminal Nodes Identification Chart
description: Interactive Chart.js visualization showing terminal nodes identification chart
image: /sims/orphaned-nodes-identification/orphaned-nodes-identification.png
og:image: /sims/orphaned-nodes-identification/orphaned-nodes-identification.png
quality_score: 100
---


# Terminal Nodes Identification Chart


**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/orphaned-nodes-identification/main.html" width="100%" height="600px"></iframe>
```


[Run Terminal Nodes Identification Chart in Fullscreen](main.html){ .md-button .md-button--primary }


An interactive scatter plot visualizing concept connectivity patterns by showing indegree (prerequisites) vs outdegree (dependents), helping identify foundational, intermediate, and terminal concepts in a learning graph.

## Interactive Chart



[View Fullscreen](main.html){:target="_blank"}

## Overview

This scatter plot maps all concepts in a 200-concept learning graph based on two dimensions:

- **X-axis (Indegree)**: Number of prerequisites a concept has
- **Y-axis (Outdegree)**: Number of other concepts that depend on this concept

The visualization reveals three critical categories of concepts through color coding, helping assess the structural health and connectivity of the learning graph.

## Features

### Interactive Elements

- **Hover tooltips** - Display concept name and exact indegree/outdegree values
- **Color-coded categories** - Green (foundational), Blue (intermediate), Red (terminal)
- **Named concepts** - Specific labels for foundational and terminal concepts
- **Zone annotations** - Visual indicators for foundation and terminal zones
- **Smooth animations** - Animated point rendering on page load

### Visual Design

- **Foundation Zone** - Green vertical line at indegree=0 marking foundational concepts
- **Terminal Zone** - Red horizontal line at outdegree=0 marking terminal concepts
- **Category legend** - Top legend with point style indicators
- **Detailed descriptions** - Expandable legend explaining each category

## Interpretation Guide

### Node Categories

**Foundational Concepts (Green)**
- **Location**: Left edge (indegree = 0)
- **Characteristics**: No prerequisites, but other concepts depend on them
- **Examples**: "Introduction to Learning Graphs", "Bloom's Taxonomy", "Graph Theory Basics"
- **Healthy range**: 5-10% of total concepts
- **Purpose**: Entry points for learners with no prior knowledge

**Intermediate Concepts (Blue)**
- **Location**: Center cluster (indegree > 0, outdegree > 0)
- **Characteristics**: Have both prerequisites and dependents
- **Healthy range**: 75-90% of total concepts
- **Purpose**: Core curriculum building blocks that connect foundational to advanced topics

**Terminal Concepts (Red)**
- **Location**: Bottom edge (outdegree = 0)
- **Characteristics**: Have prerequisites but no other concepts depend on them
- **Examples**: "Advanced Quality Metrics", "Future of Learning Graphs", "Machine Learning Integration"
- **Healthy range**: 5-15% of total concepts
- **Purpose**: Leaf nodes representing advanced topics, specializations, or applications

### Health Indicators

**Healthy Graph Characteristics:**
- 5-10% foundational concepts (clear entry points)
- 75-90% intermediate concepts (strong connectivity)
- 5-15% terminal concepts (appropriate depth)
- Even distribution across indegree values (gradual complexity)
- Higher outdegree for foundational concepts (many dependents)

**Warning Signs:**
- Too few foundational concepts (<5%): Unclear entry points
- Too many foundational concepts (>15%): Concepts may be too granular
- Too few terminal concepts (<5%): Graph may lack depth or specialization
- Too many terminal concepts (>20%): Poor connectivity, concepts may be isolated
- Clusters with high indegree but low outdegree: Unnecessarily complex prerequisites

## Customization Guide

### Adding Your Own Data

Replace the data generation code in `main.html` with your actual learning graph data:

```javascript
// Foundational concepts (indegree=0, outdegree>0)
const foundationalData = [
    { x: 0, y: 8, label: 'Your Foundational Concept 1' },
    { x: 0, y: 6, label: 'Your Foundational Concept 2' },
    // ... add all foundational concepts
];

// Intermediate concepts (indegree>0, outdegree>0)
const intermediateData = [
    { x: 2, y: 4, label: 'Your Intermediate Concept 1' },  // Optional labels
    { x: 3, y: 5 },  // Can omit labels for generic points
    // ... add all intermediate concepts
];

// Terminal concepts (indegree>0, outdegree=0)
const terminalData = [
    { x: 5, y: 0, label: 'Your Terminal Concept 1' },
    { x: 3, y: 0, label: 'Your Terminal Concept 2' },
    // ... add all terminal concepts
];
```

### Extracting Data from Learning Graph CSV

Use this Python code to extract connectivity data:

```python
import pandas as pd
import csv

# Load learning graph
df = pd.read_csv('learning-graph.csv')

# Calculate indegree (number of prerequisites)
df['indegree'] = df['Dependencies'].str.count('\|') + 1
df.loc[df['Dependencies'].isna(), 'indegree'] = 0

# Calculate outdegree (number of dependents)
outdegree = {}
for idx, row in df.iterrows():
    concept_id = row['ConceptID']
    outdegree[concept_id] = 0

for idx, row in df.iterrows():
    if pd.notna(row['Dependencies']):
        deps = row['Dependencies'].split('|')
        for dep in deps:
            dep_id = int(dep)
            outdegree[dep_id] += 1

df['outdegree'] = df['ConceptID'].map(outdegree)

# Categorize concepts
df['category'] = 'intermediate'
df.loc[(df['indegree'] == 0) & (df['outdegree'] > 0), 'category'] = 'foundational'
df.loc[(df['indegree'] > 0) & (df['outdegree'] == 0), 'category'] = 'terminal'

# Export for JavaScript
for category in ['foundational', 'intermediate', 'terminal']:
    subset = df[df['category'] == category]
    print(f"\n// {category.capitalize()} concepts")
    print(f"const {category}Data = [")
    for _, row in subset.iterrows():
        print(f"    {{ x: {int(row['indegree'])}, y: {int(row['outdegree'])}, label: '{row['ConceptLabel']}' }},")
    print("];")
```

### Adjusting Axis Ranges

Modify the scale configuration to match your data range:

```javascript
scales: {
    x: {
        min: -0.5,
        max: 8,  // Adjust based on max indegree in your data
        // ...
    },
    y: {
        min: -0.5,
        max: 12,  // Adjust based on max outdegree in your data
        // ...
    }
}
```

### Customizing Point Appearance

Modify point sizes and colors:

```javascript
{
    label: 'Foundational Concepts',
    backgroundColor: 'rgba(76, 175, 80, 0.7)',  // Point fill color
    borderColor: 'rgba(76, 175, 80, 1)',  // Point border color
    pointRadius: 6,  // Normal size
    pointHoverRadius: 8  // Hover size
}
```

## Technical Details

- **Library**: Chart.js 4.4.0
- **Plugins**: chartjs-plugin-annotation 3.0.1 (for zone lines)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Chart.js and Annotation Plugin (both loaded from CDN)
- **Responsive**: Yes, with 1.3:1 aspect ratio
- **Data points**: 200 concepts (12 foundational, 164 intermediate, 24 terminal)

## Connectivity Analysis Metrics

### Centrality Measures

**Indegree Centrality**: Concepts with high indegree (many prerequisites) are advanced/complex concepts that require substantial prior knowledge.

**Outdegree Centrality**: Concepts with high outdegree (many dependents) are foundational/important concepts that support many other topics.

**Combined Analysis**: The ideal foundational concept has low indegree (easy to start with) and high outdegree (enables many other concepts).

### Graph Health Metrics

Calculate these metrics to assess graph quality:

```python
total_concepts = len(df)
foundational_pct = (df['category'] == 'foundational').sum() / total_concepts * 100
intermediate_pct = (df['category'] == 'intermediate').sum() / total_concepts * 100
terminal_pct = (df['category'] == 'terminal').sum() / total_concepts * 100

print(f"Foundational: {foundational_pct:.1f}% (target: 5-10%)")
print(f"Intermediate: {intermediate_pct:.1f}% (target: 75-90%)")
print(f"Terminal: {terminal_pct:.1f}% (target: 5-15%)")
```

## Use Cases

This visualization is useful for:

- **Learning graph quality assessment** - Identify connectivity issues
- **Curriculum gap analysis** - Find missing connections or isolated concepts
- **Entry point identification** - Locate foundational concepts for learners
- **Terminal concept review** - Evaluate whether terminal concepts are appropriate
- **Graph refactoring** - Identify concepts that need to be split or merged
- **Pedagogical planning** - Understand concept relationships and dependencies
- **Comparative analysis** - Compare connectivity patterns across different graphs

## Common Patterns and Issues

### Healthy Pattern
- Small cluster of green dots on left edge (foundational)
- Large blue cluster in center (well-connected)
- Scattered red dots on bottom edge (terminal concepts/specializations)

### Warning Pattern: Too Many Isolates
- Many single blue dots far from cluster
- **Fix**: Review whether these concepts belong in the graph or need better connections

### Warning Pattern: Hub-and-Spoke
- One concept with very high outdegree, others with low
- **Fix**: Consider breaking the hub concept into smaller components

### Warning Pattern: Linear Chain
- Diagonal line pattern (each concept depends on exactly one previous)
- **Fix**: Add lateral connections between concepts at similar levels

## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Identify** (Remember) terminal nodes in directed graphs using visual analysis
- **Analyze** (Analyze) the pedagogical implications of concepts with no dependents
- **Evaluate** (Evaluate) whether terminal nodes represent valid endpoints or indicate quality issues
- **Apply** (Apply) graph analysis techniques to improve learning graph structure
- **Create** (Create) recommendations for resolving terminal node issues

### Target Audience

- **Primary**: Instructional designers working with learning graphs
- **Secondary**: Curriculum developers, educational data analysts
- **Level**: Graduate education programs or professional development
- **Prerequisites**: Understanding of directed graphs and learning graph concepts

### Activities

**Activity 1: Terminal Node Detection (15 minutes)**

1. Examine the chart showing terminal nodes vs. integrated concepts
2. Calculate what percentage of the 200-concept graph consists of terminal nodes
3. Identify the maximum in-degree for integrated concepts
4. Discuss: Is having 8 terminal nodes (4%) a problem for a 200-concept graph?

**Activity 2: Root Cause Analysis (25 minutes)**

For each identified terminal node, determine the likely cause:

1. **Too advanced**: Concept has no simpler concepts depending on it
2. **Too specific**: Niche topic not needed for other concepts
3. **Incorrectly placed**: Should be in a different domain/course
4. **Valid terminal**: Legitimate endpoint in the learning progression

Categorize the 8 terminal nodes using these criteria.

**Activity 3: Resolution Strategies (30 minutes)**

For 3 different terminal nodes, propose resolution strategies:

1. **Option 1**: Remove the terminal concept entirely (when appropriate?)
2. **Option 2**: Add dependent concepts that build on it
3. **Option 3**: Merge it with a related concept
4. **Option 4**: Keep as-is (justify why it's a valid terminal concept)

Write a 1-paragraph rationale for each chosen strategy.

**Activity 4: Graph Quality Improvement (40 minutes)**

Using a provided learning graph CSV:

1. Run a script to identify all terminal nodes (outdegree = 0)
2. Visualize terminal vs. integrated concepts using Chart.js
3. Propose 5 new concepts that could depend on terminal nodes
4. Update the CSV to add these dependencies and verify terminal nodes are resolved

### Assessment

**Formative Assessment:**
- During Activity 2: Can students correctly categorize terminal node types?
- During Activity 3: Do resolution strategies match the terminal node characteristics?

**Summative Assessment:**

Analyze and improve a learning graph with terminal nodes:

1. **Detection** (25 points): Correctly identify all terminal nodes in a 150-concept graph
2. **Analysis** (30 points): Categorize each terminal node by type with clear rationale
3. **Resolution Plan** (25 points): Propose specific, actionable fixes for each terminal node
4. **Implementation** (20 points): Update graph structure and verify improvement

**Success Criteria:**
- Terminal node percentage reduced to <3%
- All remaining terminal nodes justified as valid endpoints
- No new terminal nodes introduced during resolution
- Graph maintains DAG structure (no cycles)


## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Scatter Plot Guide](https://www.chartjs.org/docs/latest/charts/scatter.html)
- [Chart.js Annotation Plugin](https://www.chartjs.org/chartjs-plugin-annotation/latest/)
- [Graph Theory: Degree Centrality](https://en.wikipedia.org/wiki/Degree_centrality)
- [Learning Graph Quality Metrics](../../chapters/06-learning-graph-quality-validation/)