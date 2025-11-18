# Average Dependencies Distribution Bar Chart

An interactive histogram visualizing the distribution of prerequisite counts across all concepts in a learning graph, helping assess the quality and pedagogical structure of concept dependencies.

## Interactive Chart

<iframe src="main.html" width="100%" height="800" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}

## Overview

This bar chart displays how many concepts in a 200-concept learning graph have each number of prerequisites (0 through 8+). The visualization helps educators and instructional designers evaluate whether their learning graph has appropriate complexity distribution.

The chart highlights the **optimal range** (2-4 prerequisites) where most well-structured concepts should fall, and shows the **average** prerequisite count across all concepts.

## Features

### Interactive Elements

- **Hover tooltips** - Display exact concept count and percentage for each bar
- **Smooth animations** - Animated bars on page load
- **Color coding** - Green bars indicate optimal range (2-4), gold bars show other ranges
- **Annotations** - Visual indicators for optimal zone and average line

### Visual Design

- **Optimal Range Shading** - Light green background highlights the 2-4 prerequisite range
- **Average Line** - Blue dashed vertical line at 3.1 shows the mean
- **Metrics Panel** - Six key statistics displayed below the chart
- **Analysis Section** - Interpretation guidance for understanding the distribution

## Interpretation Guide

### Key Metrics

1. **Total Concepts (200)** - The complete size of the learning graph
2. **Total Dependencies (620)** - Sum of all prerequisite relationships
3. **Average Dependencies (3.1)** - Mean number of prerequisites per concept
4. **Median (2)** - Middle value when concepts are sorted by prerequisite count
5. **Mode (2)** - Most common number of prerequisites
6. **In Optimal Range (84%)** - Percentage of concepts with 1-5 prerequisites

### What Makes a Healthy Distribution

**Bell-Curve Shape**: The distribution should resemble a bell curve, with most concepts in the middle ranges (2-4 prerequisites) and fewer concepts at the extremes.

**Foundational Layer**: Having 5-10% of concepts with 0 prerequisites (foundational concepts) provides clear entry points.

**Optimal Range**: 70-90% of concepts should have 1-5 prerequisites, indicating appropriate granularity.

**Few Complex Concepts**: Less than 5% of concepts should have 6+ prerequisites to avoid overwhelming learners.

### Red Flags

- **Flat distribution**: Suggests inconsistent concept granularity
- **Too many foundational concepts** (>15%): May indicate concepts are too broad
- **Too many complex concepts** (>10% with 6+ prerequisites): Concepts may need to be broken down
- **Heavily skewed distribution**: Indicates structural issues in the learning graph

## Customization Guide

### Changing the Data

To modify the chart data for your own learning graph, edit the `data` array in `main.html`:

```javascript
const data = {
    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8+'],
    datasets: [{
        label: 'Number of Concepts',
        data: [12, 45, 58, 42, 25, 12, 4, 2, 0], // Replace with your counts
        // ... rest of configuration
    }]
};
```

### Updating Metrics

Update the calculated metrics in the HTML to match your data:

```html
<div class="metric-value">200</div>  <!-- Total concepts -->
<div class="metric-value">620</div>  <!-- Total dependencies -->
<div class="metric-value">3.1</div>  <!-- Average -->
<div class="metric-value">2</div>    <!-- Median -->
<div class="metric-value">2</div>    <!-- Mode -->
<div class="metric-value">84%</div>  <!-- Optimal range % -->
```

### Adjusting the Optimal Range

To change the optimal range shading (currently 2-4), modify the annotation configuration:

```javascript
optimalZone: {
    type: 'box',
    xMin: 1.5,  // Start at 2 (1.5 accounts for bar centering)
    xMax: 4.5,  // End at 4
    // ... styling
}
```

### Moving the Average Line

Update the average line position:

```javascript
averageLine: {
    type: 'line',
    xMin: 3.1,  // Your calculated average
    xMax: 3.1,
    label: {
        content: 'Average: 3.1',  // Update label text
        // ... styling
    }
}
```

### Customizing Colors

Modify the bar colors in the `backgroundColor` array:

```javascript
backgroundColor: [
    'rgba(255, 193, 7, 0.8)',  // Bar for 0 prerequisites
    'rgba(255, 193, 7, 0.8)',  // Bar for 1 prerequisite
    'rgba(76, 175, 80, 0.6)',  // Bar for 2 (optimal - green)
    'rgba(76, 175, 80, 0.6)',  // Bar for 3 (optimal - green)
    'rgba(76, 175, 80, 0.6)',  // Bar for 4 (optimal - green)
    'rgba(255, 193, 7, 0.8)',  // Bar for 5
    'rgba(255, 193, 7, 0.8)',  // Bar for 6
    'rgba(255, 193, 7, 0.8)',  // Bar for 7
    'rgba(255, 193, 7, 0.8)'   // Bar for 8+
],
```

## Technical Details

- **Library**: Chart.js 4.4.0
- **Plugins**: chartjs-plugin-annotation 3.0.1 (for shaded zones and lines)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Chart.js and Annotation Plugin (both loaded from CDN)
- **Responsive**: Yes, adapts to container width with 2:1 aspect ratio

## Calculating Your Own Metrics

To generate these metrics from your learning graph CSV:

```python
import pandas as pd

# Load learning graph
df = pd.read_csv('learning-graph.csv')

# Count prerequisites per concept
prerequisite_counts = df['Dependencies'].str.split('|').str.len()
prerequisite_counts = prerequisite_counts.fillna(0)  # Foundational concepts

# Calculate metrics
total_concepts = len(df)
total_dependencies = prerequisite_counts.sum()
average_dependencies = total_dependencies / total_concepts
median_dependencies = prerequisite_counts.median()
mode_dependencies = prerequisite_counts.mode()[0]

# Count concepts in optimal range (1-5)
optimal_count = ((prerequisite_counts >= 1) & (prerequisite_counts <= 5)).sum()
optimal_percentage = (optimal_count / total_concepts) * 100

# Create distribution
distribution = prerequisite_counts.value_counts().sort_index()
```

## Use Cases

This chart type is useful for:

- **Learning graph quality assessment** - Evaluate structural balance
- **Curriculum design validation** - Ensure appropriate complexity progression
- **Concept granularity analysis** - Identify over- or under-divided concepts
- **Pedagogical planning** - Plan teaching sequence based on dependency patterns
- **Comparative analysis** - Compare multiple learning graphs
- **Documentation** - Communicate graph structure to stakeholders

## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Bar Chart Guide](https://www.chartjs.org/docs/latest/charts/bar.html)
- [Chart.js Annotation Plugin](https://www.chartjs.org/chartjs-plugin-annotation/latest/)
- [Learning Graph Quality Metrics](../../chapters/06-learning-graph-quality-validation/)
