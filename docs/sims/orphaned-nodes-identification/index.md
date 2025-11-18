# Orphaned Nodes Identification Chart

An interactive scatter plot visualizing concept connectivity patterns by showing indegree (prerequisites) vs outdegree (dependents), helping identify foundational, intermediate, and orphaned concepts in a learning graph.

## Interactive Chart

<iframe src="main.html" width="100%" height="900" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}

## Overview

This scatter plot maps all concepts in a 200-concept learning graph based on two dimensions:

- **X-axis (Indegree)**: Number of prerequisites a concept has
- **Y-axis (Outdegree)**: Number of other concepts that depend on this concept

The visualization reveals three critical categories of concepts through color coding, helping assess the structural health and connectivity of the learning graph.

## Features

### Interactive Elements

- **Hover tooltips** - Display concept name and exact indegree/outdegree values
- **Color-coded categories** - Green (foundational), Blue (intermediate), Red (orphaned)
- **Named concepts** - Specific labels for foundational and orphaned concepts
- **Zone annotations** - Visual indicators for foundation and orphaned zones
- **Smooth animations** - Animated point rendering on page load

### Visual Design

- **Foundation Zone** - Green vertical line at indegree=0 marking foundational concepts
- **Orphaned Zone** - Red horizontal line at outdegree=0 marking terminal concepts
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

**Orphaned Concepts (Red)**
- **Location**: Bottom edge (outdegree = 0)
- **Characteristics**: Have prerequisites but no other concepts depend on them
- **Examples**: "Advanced Quality Metrics", "Future of Learning Graphs", "Machine Learning Integration"
- **Healthy range**: 5-15% of total concepts
- **Purpose**: Terminal/leaf nodes representing advanced topics, specializations, or applications

### Health Indicators

**Healthy Graph Characteristics:**
- 5-10% foundational concepts (clear entry points)
- 75-90% intermediate concepts (strong connectivity)
- 5-15% orphaned concepts (appropriate depth)
- Even distribution across indegree values (gradual complexity)
- Higher outdegree for foundational concepts (many dependents)

**Warning Signs:**
- Too few foundational concepts (<5%): Unclear entry points
- Too many foundational concepts (>15%): Concepts may be too granular
- Too few orphaned concepts (<5%): Graph may lack depth or specialization
- Too many orphaned concepts (>20%): Poor connectivity, concepts may be isolated
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

// Orphaned concepts (indegree>0, outdegree=0)
const orphanedData = [
    { x: 5, y: 0, label: 'Your Orphaned Concept 1' },
    { x: 3, y: 0, label: 'Your Orphaned Concept 2' },
    // ... add all orphaned concepts
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
df.loc[(df['indegree'] > 0) & (df['outdegree'] == 0), 'category'] = 'orphaned'

# Export for JavaScript
for category in ['foundational', 'intermediate', 'orphaned']:
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
- **Data points**: 200 concepts (12 foundational, 164 intermediate, 24 orphaned)

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
orphaned_pct = (df['category'] == 'orphaned').sum() / total_concepts * 100

print(f"Foundational: {foundational_pct:.1f}% (target: 5-10%)")
print(f"Intermediate: {intermediate_pct:.1f}% (target: 75-90%)")
print(f"Orphaned: {orphaned_pct:.1f}% (target: 5-15%)")
```

## Use Cases

This visualization is useful for:

- **Learning graph quality assessment** - Identify connectivity issues
- **Curriculum gap analysis** - Find missing connections or isolated concepts
- **Entry point identification** - Locate foundational concepts for learners
- **Terminal concept review** - Evaluate whether orphaned concepts are appropriate
- **Graph refactoring** - Identify concepts that need to be split or merged
- **Pedagogical planning** - Understand concept relationships and dependencies
- **Comparative analysis** - Compare connectivity patterns across different graphs

## Common Patterns and Issues

### Healthy Pattern
- Small cluster of green dots on left edge (foundational)
- Large blue cluster in center (well-connected)
- Scattered red dots on bottom edge (specializations)

### Warning Pattern: Too Many Isolates
- Many single blue dots far from cluster
- **Fix**: Review whether these concepts belong in the graph or need better connections

### Warning Pattern: Hub-and-Spoke
- One concept with very high outdegree, others with low
- **Fix**: Consider breaking the hub concept into smaller components

### Warning Pattern: Linear Chain
- Diagonal line pattern (each concept depends on exactly one previous)
- **Fix**: Add lateral connections between concepts at similar levels

## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Scatter Plot Guide](https://www.chartjs.org/docs/latest/charts/scatter.html)
- [Chart.js Annotation Plugin](https://www.chartjs.org/chartjs-plugin-annotation/latest/)
- [Graph Theory: Degree Centrality](https://en.wikipedia.org/wiki/Degree_centrality)
- [Learning Graph Quality Metrics](../../chapters/06-learning-graph-quality-validation/)
