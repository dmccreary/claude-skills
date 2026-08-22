---
title: Concept Label Length Histogram
description: Interactive Chart.js visualization showing concept label length histogram
image: /sims/concept-length-histogram/concept-length-histogram.png
og:image: /sims/concept-length-histogram/concept-length-histogram.png
quality_score: 80
---


# Concept Label Length Histogram


**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/ibook-skills/sims/concept-length-histogram/main.html" width="100%" height="600px"></iframe>
```


[Run Concept Label Length Histogram in Fullscreen](main.html){ .md-button .md-button--primary }


## Overview

This interactive visualization analyzes the length distribution of all 200 concept labels in the learning graph for "Using Claude Skills to Create Intelligent Textbooks."

## Key Statistics

- **Total Concepts:** 200
- **Average Length:** 23.77 characters
- **Median Length:** 24 characters
- **Range:** 11-36 characters
- **Standard Deviation:** 5.15 characters
- **Compliance:** 98.5% of labels are within the 32-character guideline

## Distribution Analysis

The histogram shows that concept labels follow a roughly normal distribution centered around 24-26 characters:

- **Peak:** 26 characters (20 concepts, 10%)
- **Most Common Range:** 21-27 characters (80 concepts, 40%)
- **Shortest Label:** "What is Git" (11 characters)
- **Longest Labels:** "Difference Between Skills & Commands" and "Five Levels of Textbook Intelligence" (36 characters each)

## Design Rationale

Concept labels in learning graphs should be:

1. **Concise:** Short enough to display clearly in graph visualizations
2. **Descriptive:** Long enough to convey meaning without context
3. **Scannable:** Easy to read at a glance in node labels
4. **Consistent:** Maintain similar length for visual balance

The 32-character guideline helps ensure labels remain readable in compact graph visualizations while providing sufficient context for learners.

## Interactive Features

- **Hover** over bars to see exact counts and percentages
- **Color-coded** visualization with gradient background
- **Statistics cards** showing key metrics at a glance
- **Example labels** showing shortest and longest concepts

## Observations

1. **Well-Distributed:** Labels show good variation without extreme outliers
2. **Guideline Compliance:** Only 3 labels exceed 32 characters (1.5%)
3. **Readability:** Average length of ~24 characters is optimal for graph nodes
4. **Title Case Convention:** All labels follow consistent formatting

## Try It



## Related Files

- [Concept List](../../learning-graph/concept-list.md) - Full list of all 200 concepts
- [Learning Graph](../../learning-graph/index.md) - Complete learning graph documentation
- [Graph Viewer](../graph-viewer/index.md) - Interactive graph visualization

---

**Generated:** 2025-11-08
**Analysis Tool:** Python with Chart.js visualization
**Data Source:** learning-graph/concept-list.md