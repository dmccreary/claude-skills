---
title: Taxonomy Distribution Pie Chart
description: Interactive Chart.js visualization showing taxonomy distribution pie chart
image: /sims/taxonomy-distribution-pie/taxonomy-distribution-pie.png
og:image: /sims/taxonomy-distribution-pie/taxonomy-distribution-pie.png
quality_score: 100
---
# Taxonomy Distribution Pie Chart

<iframe src="main.html" width="100%" height="620px"></iframe>

**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/ibook-skills/sims/taxonomy-distribution-pie/main.html" width="100%" height="600px"></iframe>
```

[Run Taxonomy Distribution Pie Chart in Fullscreen](main.html){ .md-button .md-button--primary }


An interactive pie chart visualizing how 200 concepts are distributed across 8 taxonomy categories in a learning graph, helping assess balanced coverage and appropriate categorization.


[View Fullscreen](main.html){:target="_blank"}

## Overview

This pie chart displays the percentage breakdown of concepts across taxonomy categories in a 200-concept learning graph. The rainbow color gradient (red through purple) visually distinguishes each category, while percentage labels show the exact distribution.

The visualization helps educators evaluate whether their learning graph provides balanced coverage across different concept types and complexity levels.

## Features

### Interactive Elements

- **Hover tooltips** - Display concept count, percentage, and category description
- **Data labels** - Percentage values displayed directly on chart segments
- **Click legend** - Toggle categories on/off by clicking legend items
- **Hover effects** - Segments expand slightly on hover for emphasis
- **Smooth animations** - Animated rotation and scaling on page load

### Visual Design

- **Rainbow gradient** - Color progression from red (foundational) to purple (advanced)
- **Side legend** - Right-side legend with full category labels and percentages
- **Quality indicators** - Three green checkmarks showing health metrics
- **Category cards** - Detailed descriptions for each taxonomy category
- **Badge annotations** - Largest and smallest categories highlighted

## Interpretation Guide

### Taxonomy Categories

**FOUND (Foundational) - 9%**
- Entry-level concepts requiring no prerequisites
- Examples: "Introduction to Learning Graphs", "What is a Concept?"
- Target range: 5-10%

**BASIC (Basic Principles) - 21%**
- Core concepts that build directly on foundations
- Examples: "DAG Structure", "Prerequisite Relationships"
- Target range: 15-25%

**ARCH (Architecture) - 19%**
- Structural and design concepts
- Examples: "Graph Quality Metrics", "Taxonomy Design"
- Target range: 15-25%

**IMPL (Implementation) - 17.5%**
- Practical application and implementation concepts
- Examples: "CSV File Format", "JSON Conversion"
- Target range: 12-20%

**DATA (Data Management) - 14%**
- Data structures, formats, and management
- Examples: "Data Validation", "File Formats"
- Target range: 10-18%

**TOOL (Tools) - 11%**
- Software tools and development utilities
- Examples: "MkDocs", "Python Scripts", "Git"
- Target range: 8-15%

**QUAL (Quality) - 6%**
- Quality assurance and validation
- Examples: "Quality Metrics", "Validation Rules"
- Target range: 5-10%

**ADV (Advanced) - 2.5%**
- Advanced topics and cutting-edge concepts
- Examples: "Research Applications", "Future Directions"
- Target range: 2-8%

### Quality Indicators

**No category exceeds 30%**: Ensures no single taxonomy dominates, preventing curriculum imbalance.

**8 categories represented**: Comprehensive coverage across all concept types from foundational to advanced.

**Top 3 categories = 59%**: BASIC, ARCH, and IMPL represent the core curriculum focus while maintaining breadth.

## Analysis

**Balanced Distribution:** The largest category (BASIC at 21%) is within healthy range, ensuring no single taxonomy dominates the learning graph.

**Comprehensive Coverage:** All 8 taxonomy categories are represented, providing diverse learning pathways through foundational, intermediate, and advanced concepts.

**Appropriate Specialization:** Advanced concepts comprise 2.5% of the graph, suggesting appropriate depth without overwhelming learners.

**Quality Assessment:** The top 3 categories (BASIC, ARCH, IMPL) represent 59% of concepts, indicating strong focus on core curriculum while maintaining breadth.

### Healthy Distribution Characteristics

- **Gradual progression**: Higher percentages for basic/intermediate, lower for advanced
- **No gaps**: All taxonomy categories have at least some concepts
- **Balanced core**: Top 3 categories represent 50-70% of total
- **Limited dominance**: No single category exceeds 30%
- **Appropriate specialization**: Advanced categories comprise 5-15% combined

## Customization Guide

### Adding Your Own Data

Replace the data arrays in `main.html` with your taxonomy distribution:

```javascript
const data = {
    labels: [
        'FOUND: 18 concepts (9%)',    // Update with your data
        'BASIC: 42 concepts (21%)',
        'ARCH: 38 concepts (19%)',
        'IMPL: 35 concepts (17.5%)',
        'DATA: 28 concepts (14%)',
        'TOOL: 22 concepts (11%)',
        'QUAL: 12 concepts (6%)',
        'ADV: 5 concepts (2.5%)'
    ],
    datasets: [{
        data: [18, 42, 38, 35, 28, 22, 12, 5],  // Update counts
        // ... colors remain the same
    }]
};
```

### Calculating Distribution from Learning Graph

Use this Python code to generate taxonomy distribution:

```python
import pandas as pd

# Load learning graph
df = pd.read_csv('learning-graph.csv')

# Count concepts by taxonomy
taxonomy_counts = df['TaxonomyID'].value_counts().sort_index()

# Calculate percentages
total_concepts = len(df)
for taxonomy, count in taxonomy_counts.items():
    percentage = (count / total_concepts) * 100
    print(f"{taxonomy}: {count} concepts ({percentage:.1f}%)")

# Generate chart data
print("\nChart data:")
print("data: [", end="")
print(", ".join([str(count) for count in taxonomy_counts.values()]), end="")
print("]")
```

### Customizing Colors

Modify the background colors for different taxonomy categories:

```javascript
backgroundColor: [
    'rgba(239, 83, 80, 0.9)',      // Red - FOUND
    'rgba(255, 112, 67, 0.9)',     // Orange - BASIC
    'rgba(255, 202, 40, 0.9)',     // Yellow - ARCH
    'rgba(156, 204, 101, 0.9)',    // Light Green - IMPL
    'rgba(102, 187, 106, 0.9)',    // Green - DATA
    'rgba(38, 198, 218, 0.9)',     // Light Blue - TOOL
    'rgba(66, 165, 245, 0.9)',     // Blue - QUAL
    'rgba(126, 87, 194, 0.9)'      // Purple - ADV
]
```

### Adding/Removing Categories

To add a new category:

1. Add to `labels` array: `'NEWCAT: X concepts (Y%)'`
2. Add count to `data` array
3. Add color to `backgroundColor` and `borderColor` arrays
4. Update category descriptions in tooltip callbacks
5. Add detail card in HTML

### Updating Quality Metrics

Update the quality indicator calculations in the HTML based on your data:

```html
<div class="indicator-item success">
    <span class="check-icon">✓</span>
    <span class="indicator-text">No category exceeds 30%</span>
</div>
```

Change to warning if condition not met:

```html
<div class="indicator-item warning">
    <span class="check-icon">⚠</span>
    <span class="indicator-text">WARNING: BASIC exceeds 30%</span>
</div>
```

## Technical Details

- **Library**: Chart.js 4.4.0
- **Plugins**: chartjs-plugin-datalabels 2.x (for percentage labels on slices)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Chart.js and Data Labels Plugin (both loaded from CDN)
- **Responsive**: Yes, with 1.2:1 aspect ratio
- **Total concepts**: 200 across 8 categories

## Analysis Metrics

### Balance Score

Calculate a balance score to assess distribution health:

```python
import numpy as np

# Expected even distribution
expected_pct = 100 / len(taxonomy_counts)

# Calculate variance from expected
variance = np.var([pct for pct in taxonomy_percentages])

# Balance score (0-100, higher is more balanced)
balance_score = max(0, 100 - variance)

print(f"Balance Score: {balance_score:.1f}/100")
```

### Coverage Assessment

Check for gaps and dominance:

```python
# Check for gaps (categories with < 5%)
gaps = [cat for cat, pct in taxonomy_pcts.items() if pct < 5]

# Check for dominance (categories with > 30%)
dominant = [cat for cat, pct in taxonomy_pcts.items() if pct > 30]

# Check for comprehensive coverage (all categories represented)
comprehensive = len(taxonomy_counts) >= 8

print(f"Gaps (< 5%): {gaps}")
print(f"Dominant (> 30%): {dominant}")
print(f"Comprehensive: {comprehensive}")
```

### Progression Analysis

Verify appropriate progression from basic to advanced:

```python
# Define expected progression (basic → advanced)
progression_order = ['FOUND', 'BASIC', 'ARCH', 'IMPL', 'DATA', 'TOOL', 'QUAL', 'ADV']

# Check if higher complexity categories have lower percentages
progression_valid = True
for i in range(len(progression_order) - 1):
    current = taxonomy_pcts[progression_order[i]]
    next_cat = taxonomy_pcts[progression_order[i + 1]]
    if next_cat > current + 10:  # Allow some flexibility
        progression_valid = False
        break

print(f"Appropriate progression: {progression_valid}")
```

## Use Cases

This visualization is useful for:

- **Curriculum balance assessment** - Ensure even coverage across concept types
- **Taxonomy validation** - Verify concepts are categorized appropriately
- **Gap identification** - Find underrepresented taxonomy categories
- **Complexity distribution** - Assess ratio of basic to advanced concepts
- **Comparative analysis** - Compare taxonomy distributions across multiple graphs
- **Stakeholder communication** - Visually communicate curriculum scope
- **Planning** - Guide development of new concepts to fill gaps

## Common Distribution Patterns

### Healthy Pattern: Gradual Taper
- FOUND: 5-10%
- BASIC: 20-25%
- Intermediate categories: 15-20% each
- Advanced: 2-8%
- **Assessment**: Balanced, appropriate complexity progression

### Warning Pattern: Top-Heavy
- FOUND: 25%
- BASIC: 30%
- Intermediate: 10% each
- Advanced: <5%
- **Issue**: Concepts may be too granular or lack depth

### Warning Pattern: Bottom-Heavy
- FOUND: <5%
- BASIC: <10%
- Intermediate: 15% each
- Advanced: 25%
- **Issue**: May be too complex, lacking foundational support

### Warning Pattern: Single Dominant Category
- One category: >35%
- Others: <10% each
- **Issue**: Curriculum imbalance, consider reorganizing taxonomy

## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Interpret** (Understand) taxonomy distribution patterns in learning graphs
- **Analyze** (Analyze) whether concept categorization is balanced across domains
- **Evaluate** (Evaluate) the appropriateness of taxonomy category percentages
- **Apply** (Apply) Chart.js pie chart techniques to visualize categorical data
- **Create** (Create) custom taxonomy schemes for new subject domains

### Target Audience

- **Primary**: Instructional designers, curriculum developers
- **Secondary**: Data visualization specialists, educational researchers
- **Level**: Graduate education or professional development
- **Prerequisites**: Basic statistics, familiarity with learning graphs

### Activities

**Activity 1: Distribution Analysis (20 minutes)**

1. Identify the three largest taxonomy categories in the pie chart
2. Calculate what percentage of concepts fall outside the top 3 categories
3. Determine if any single category exceeds 30% (potential over-concentration)
4. Compare the largest and smallest categories - what's the ratio?

**Activity 2: Balance Evaluation (25 minutes)**

Using taxonomic distribution best practices:

1. Assess whether the distribution indicates good coverage across domains
2. Identify any categories that seem under-represented (<3%)
3. Evaluate if any categories could be merged due to semantic overlap
4. Propose an "ideal" distribution for a well-balanced course (percentages for each category)

**Activity 3: Interactive Chart Modification (30 minutes)**

1. Modify the Chart.js data array to represent your own course's concept distribution
2. Add a new taxonomy category and update colors appropriately
3. Implement hover tooltips showing concept count + percentage
4. Add a legend positioned to the right of the chart

**Activity 4: Create Custom Taxonomy (45 minutes)**

For a new course domain (e.g., "Introduction to Cybersecurity"):

1. Design 8-12 taxonomy categories that span the subject comprehensively
2. Assign 3-letter abbreviation codes to each category
3. Create a balanced target distribution (sum to 100%)
4. Generate a pie chart visualization with your taxonomy and target percentages
5. Write 2-3 sentences explaining your category choices

### Assessment

**Formative Assessment:**
- During Activity 1: Can students correctly calculate percentages from visual data?
- During Activity 4: Do custom taxonomy categories cover the domain comprehensively?

**Summative Assessment:**

Design and visualize a complete taxonomy system:

1. **Taxonomy Design** (30 points): Create 10-12 categories for a specified subject
   - Categories are mutually exclusive
   - Complete domain coverage
   - Clear, descriptive labels

2. **Distribution Planning** (25 points): Assign target percentages summing to 100%
   - No category exceeds 30%
   - Justification for distribution choices

3. **Visualization** (25 points): Create functional Chart.js pie chart
   - Accurate data representation
   - Appropriate color scheme
   - Readable labels and legend

4. **Documentation** (20 points): Write taxonomy usage guidelines
   - When to use each category
   - Example concepts for each
   - Decision criteria for edge cases

**Success Criteria:**
- Taxonomy categories are comprehensive and non-overlapping
- Distribution is balanced without over-concentration
- Visualization clearly communicates proportions
- Documentation enables consistent categorization


## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Pie Chart Guide](https://www.chartjs.org/docs/latest/charts/doughnut.html)
- [Chart.js Data Labels Plugin](https://chartjs-plugin-datalabels.netlify.app/)
- [Learning Graph Taxonomy Design](../../chapters/07-taxonomy-data-formats/)
- [ISO 11179 Metadata Standards](https://en.wikipedia.org/wiki/ISO/IEC_11179)