# Chart.js Generator Assets

This directory contains template files for creating various types of Chart.js visualizations. Each template is ready to use and includes TODO markers for easy customization.

## Available Templates

### Chart Type Templates

1. **template-line.html** - Line chart for trends and time series data
2. **template-bar.html** - Bar chart for categorical comparisons
3. **template-pie.html** - Pie chart for proportions and percentages
4. **template-doughnut.html** - Doughnut chart (pie with center hole)
5. **template-radar.html** - Radar/spider chart for multi-dimensional data
6. **template-polar.html** - Polar area chart for proportional data with emphasis
7. **template-bubble.html** - Bubble chart for three-dimensional data
8. **template-scatter.html** - Scatter plot for correlations and distributions

### Supporting Templates

- **template-style.css** - Professional CSS styling for all chart types
- **template-index.md** - MkDocs documentation template

## Template Features

All HTML templates include:

- Complete HTML5 boilerplate with proper meta tags
- Chart.js 4.4.0 CDN import
- Canvas element for chart rendering
- Sample data with clear structure
- Comprehensive Chart.js configuration
- TODO markers for easy customization
- Commented code explaining key sections
- Responsive design settings
- Professional styling

## Quick Start Guide

### 1. Choose Your Chart Type

Select the template that best fits your data:

| Template | Best For | Not Suitable For |
|----------|----------|------------------|
| **Line** | Trends over time, continuous data | Categorical comparisons |
| **Bar** | Comparing categories, discrete data | Trends, continuous data |
| **Pie/Doughnut** | Part-to-whole (≤6 categories) | Precise comparisons, many categories |
| **Radar** | Multi-variable comparisons | Single variable data |
| **Polar** | Proportions with emphasis | Precise comparisons |
| **Bubble** | Three dimensions (x, y, size) | Simple 1D or 2D data |
| **Scatter** | Correlations, distributions | Categorical data |

### 2. Create Chart Directory

```bash
mkdir -p docs/sims/my-chart-name
cd docs/sims/my-chart-name
```

### 3. Copy Templates

```bash
# Copy the chart template
cp /path/to/skills/chartjs-generator/assets/template-[type].html main.html

# Copy the style template
cp /path/to/skills/chartjs-generator/assets/template-style.css style.css

# Copy the documentation template (optional)
cp /path/to/skills/chartjs-generator/assets/template-index.md index.md
```

### 4. Customize Your Chart

Edit `main.html` and replace the TODO sections:

1. **Chart title** - Update the page title and chart title
2. **Data** - Replace sample data with your actual data
3. **Colors** - Customize the color scheme
4. **Labels** - Update axis labels and legend text
5. **Options** - Adjust chart-specific options

### 5. Test Your Chart

Open `main.html` in a web browser to view your chart. If using MkDocs:

```bash
mkdocs serve
```

Then navigate to your chart page.

## Customization Examples

### Line Chart - Time Series Data

```javascript
const data = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
        label: 'Sales ($1000s)',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
    }]
};
```

### Bar Chart - Category Comparison

```javascript
const data = {
    labels: ['Product A', 'Product B', 'Product C', 'Product D'],
    datasets: [{
        label: 'Units Sold',
        data: [65, 59, 80, 81],
        backgroundColor: 'rgba(54, 162, 235, 0.8)'
    }]
};
```

### Pie/Doughnut - Proportions

```javascript
const data = {
    labels: ['Chrome', 'Firefox', 'Safari', 'Edge', 'Other'],
    datasets: [{
        data: [65, 15, 10, 7, 3],
        backgroundColor: [
            'rgba(255, 99, 132, 0.8)',
            'rgba(54, 162, 235, 0.8)',
            'rgba(255, 206, 86, 0.8)',
            'rgba(75, 192, 192, 0.8)',
            'rgba(201, 203, 207, 0.8)'
        ]
    }]
};
```

### Radar - Multi-Dimensional Comparison

```javascript
const data = {
    labels: ['Speed', 'Strength', 'Intelligence', 'Agility', 'Stamina'],
    datasets: [{
        label: 'Character A',
        data: [80, 70, 60, 85, 75],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)'
    }]
};
```

### Bubble - Three Dimensions

```javascript
const data = {
    datasets: [{
        label: 'Projects',
        data: [
            { x: 20, y: 30, r: 15 },  // x = effort, y = impact, r = cost
            { x: 40, y: 10, r: 10 }
        ],
        backgroundColor: 'rgba(255, 99, 132, 0.8)'
    }]
};
```

## Color Schemes

### Professional Color Palette

```javascript
// Primary colors with transparency
const colors = {
    red: 'rgba(255, 99, 132, 0.8)',
    blue: 'rgba(54, 162, 235, 0.8)',
    yellow: 'rgba(255, 206, 86, 0.8)',
    green: 'rgba(75, 192, 192, 0.8)',
    purple: 'rgba(153, 102, 255, 0.8)',
    orange: 'rgba(255, 159, 64, 0.8)',
    gray: 'rgba(201, 203, 207, 0.8)'
};

// Solid border colors
const borderColors = {
    red: 'rgb(255, 99, 132)',
    blue: 'rgb(54, 162, 235)',
    yellow: 'rgb(255, 206, 86)',
    green: 'rgb(75, 192, 192)',
    purple: 'rgb(153, 102, 255)',
    orange: 'rgb(255, 159, 64)',
    gray: 'rgb(201, 203, 207)'
};
```

### Accessibility-Friendly Colors

Use color combinations with sufficient contrast:

```javascript
const accessibleColors = [
    'rgba(0, 114, 178, 0.8)',    // Blue
    'rgba(230, 159, 0, 0.8)',    // Orange
    'rgba(0, 158, 115, 0.8)',    // Green
    'rgba(204, 121, 167, 0.8)',  // Pink
    'rgba(86, 180, 233, 0.8)'    // Sky blue
];
```

## Common Customizations

### Change Chart Aspect Ratio

```javascript
options: {
    aspectRatio: 2  // Width:height (2 = twice as wide as tall)
}
```

### Disable Animations

```javascript
options: {
    animation: false
}
```

### Custom Tooltips

```javascript
options: {
    plugins: {
        tooltip: {
            callbacks: {
                label: function(context) {
                    return 'Value: ' + context.parsed.y + ' units';
                }
            }
        }
    }
}
```

### Stacked Bar/Line Charts

```javascript
options: {
    scales: {
        x: { stacked: true },
        y: { stacked: true }
    }
}
```

### Horizontal Bar Chart

```javascript
{
    type: 'bar',
    options: {
        indexAxis: 'y'  // Makes bars horizontal
    }
}
```

## Troubleshooting

### Chart Not Displaying

- Verify Chart.js CDN is loading (check browser console)
- Ensure canvas element has correct ID
- Check for JavaScript errors in console

### Data Not Showing Correctly

- Verify data array structure matches chart type
- Check that labels array length matches data array length
- Ensure numeric values are not strings

### Labels Overlapping

```javascript
scales: {
    x: {
        ticks: {
            maxRotation: 45,
            minRotation: 45
        }
    }
}
```

### Colors Not Appearing

- Ensure color arrays match data length
- Use proper rgba() or rgb() format
- Check alpha channel value (0.0-1.0)

## Advanced Features

### Data Labels Plugin

Add value labels directly on chart elements:

```html
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
```

```javascript
options: {
    plugins: {
        datalabels: {
            color: '#fff',
            font: { weight: 'bold' }
        }
    }
}
```

### Click Events

Handle clicks on chart elements:

```javascript
options: {
    onClick: (event, elements) => {
        if (elements.length > 0) {
            const index = elements[0].index;
            console.log('Clicked:', chart.data.labels[index]);
        }
    }
}
```

### Custom Plugins

Add background colors, watermarks, or other custom features:

```javascript
plugins: [{
    afterDraw: function(chart) {
        const ctx = chart.ctx;
        // Custom drawing code here
    }
}]
```

## Best Practices

### Data Preparation

1. **Validate data** - Ensure all values are numeric and complete
2. **Normalize scales** - Use consistent ranges for comparability
3. **Meaningful labels** - Use clear, descriptive labels
4. **Limit categories** - Keep pie charts to ≤6 slices for readability

### Visual Design

1. **Color accessibility** - Use high-contrast, colorblind-friendly colors
2. **Consistent styling** - Match colors to your brand or theme
3. **Clear labels** - Ensure all text is readable at different sizes
4. **Appropriate chart type** - Choose the right visualization for your data

### Performance

1. **Limit data points** - For line/scatter charts, avoid thousands of points
2. **Disable animations** - For large datasets or print views
3. **Use decimation** - Sample large datasets appropriately

### Documentation

1. **Explain the data** - Describe what the chart shows
2. **Provide context** - Explain why the visualization matters
3. **Include customization guide** - Help others modify the chart
4. **Link to references** - Cite Chart.js documentation

## File Organization

When creating charts for MkDocs sites:

```
docs/sims/
├── chart-name-1/
│   ├── main.html
│   ├── style.css
│   └── index.md
├── chart-name-2/
│   ├── main.html
│   ├── style.css
│   └── index.md
└── index.md  # Overview of all charts
```

## References

- [Chart.js Official Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Samples](https://www.chartjs.org/docs/latest/samples/)
- [Chart.js GitHub Repository](https://github.com/chartjs/Chart.js)
- [Chart.js Community Plugins](https://github.com/chartjs)
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/)

## Support

For issues or questions:

1. Check the [Chart.js documentation](https://www.chartjs.org/docs/latest/)
2. Search [Chart.js GitHub issues](https://github.com/chartjs/Chart.js/issues)
3. Review the SKILL.md file for workflow guidance
4. Examine example implementations in `/docs/sims/`

---

*Part of the chartjs-generator skill for creating interactive Chart.js visualizations*
