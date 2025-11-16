# Bubble Chart Generator

## Overview

The bubble-chart-generator skill creates professional, interactive bubble chart visualizations using Chart.js for displaying three-dimensional data on a 2D plane with X-axis, Y-axis, and bubble size representations.

## Purpose

This skill generates complete MicroSim packages with bubble charts ideal for priority matrices (Impact vs Effort, Risk vs Value), portfolio analysis, and any visualization comparing items across two dimensions with a third dimension represented by size.

## Key Features

- **Priority Matrices**: Create 2x2 quadrant visualizations for strategic analysis
- **Interactive Charts**: Hover tooltips, clickable elements, dynamic data display
- **Quadrant Analysis**: Color-coded backgrounds with labeled sections
- **Customizable Colors**: Status-based color schemes for visual clarity
- **Responsive Design**: Works across desktop, tablet, and mobile devices
- **Complete Package**: Generates HTML, CSS, and documentation files

## When to Use

Use this skill when users need to:

- Visualize priority matrices (Impact vs Effort, Risk vs Value, Cost vs Benefit)
- Create portfolio visualizations comparing items across two dimensions
- Display multi-dimensional data with three key metrics
- Perform quadrant analysis categorizing items into four strategic zones
- Build interactive charts with hover tooltips and dynamic features

## Common Trigger Phrases

- "Create a bubble chart showing..."
- "Visualize the priority matrix for..."
- "Build an interactive scatter plot with..."
- "Show a 2x2 matrix with bubble sizes representing..."

## Technical Components

- **Chart.js**: Industry-standard charting library
- **Canvas Rendering**: High-performance visualization
- **Custom Plugins**: Quadrant backgrounds and labels
- **Bubble Scaling**: Automatic size calculation from data
- **Zoom Controls**: Pan and zoom capabilities

## Output Structure

```
docs/sims/<chart-name>/
├── main.html         # Standalone interactive chart
├── style.css         # Responsive styling
├── index.md          # MkDocs integration page
```

## Data Structure

Each data point includes:
- X-axis value (e.g., effort, cost)
- Y-axis value (e.g., impact, value)
- Size metric (e.g., count, frequency)
- Category/status for color coding
- Label for identification

## Customization Options

Users can customize:
- Chart margins and layout
- Bubble sizes (min/max scaling)
- Colors (status colors, quadrant backgrounds)
- Data structure and values
- Label positioning
- Tooltip content
- Quadrant thresholds

## Educational Applications

- **Business Strategy**: Effort/Impact matrices for prioritization
- **Project Management**: Risk assessment and task prioritization
- **Data Visualization**: Teaching multi-dimensional data representation
- **Decision Analysis**: Comparing options across multiple criteria

## Best Practices

1. Use 0-10 scales for comparability
2. Calculate derived metrics (priority scores, ratios)
3. Group items by meaningful status or type
4. Apply intuitive colors (green=good, red=caution)
5. Scale bubbles proportionally with clear bounds
6. Use subtle quadrant shading (5-10% opacity)
7. Prevent overlap with appropriate margins

## Integration

Works well with:
- **learning-graph-generator**: Visualize concept relationships
- **chapter-content-generator**: Embed charts in chapter content
- **quiz-generator**: Create questions about data interpretation

## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Bubble Chart Guide](https://www.chartjs.org/docs/latest/charts/bubble.html)
- Example: `/docs/sims/skill-impact-chart/`
