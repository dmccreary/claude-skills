# [Chart Title]

[Brief description of what this chart visualizes]

## Interactive Chart

<iframe src="main.html" width="100%" height="700" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}

## Overview

[Detailed explanation of what the chart shows and why it's useful]

## Features

### Interactive Elements

- **Hover tooltips** - Detailed data shown on hover
- **Clickable legend** - Show/hide datasets by clicking legend items
- **Smooth animations** - Chart animates on load and data updates
- **Responsive** - Adapts to different screen sizes

### Visual Design

- Color-coded categories for easy identification
- Clear axis labels and grid lines
- Professional styling with shadows and gradients
- Print-friendly layout

## Customization Guide

### Changing the Data

To modify the chart data, edit the `data` object in `main.html`:

```javascript
const data = {
    labels: ['Your', 'Labels', 'Here'],
    datasets: [{
        label: 'Your Dataset',
        data: [10, 20, 30, 40, 50]
    }]
};
```

### Adjusting Colors

Customize the color scheme by modifying the `backgroundColor` and `borderColor` properties:

```javascript
backgroundColor: [
    'rgba(255, 99, 132, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    'rgba(255, 206, 86, 0.8)',
    // Add more colors as needed
]
```

**Tip**: Use rgba() colors with alpha channel (0.0-1.0) for transparency.

### Chart Title and Labels

Update the chart title and axis labels:

```javascript
options: {
    plugins: {
        title: {
            display: true,
            text: 'Your Chart Title'
        }
    },
    scales: {
        x: {
            title: {
                display: true,
                text: 'X-Axis Label'
            }
        },
        y: {
            title: {
                display: true,
                text: 'Y-Axis Label'
            }
        }
    }
}
```

### Adjusting Chart Size

Modify the aspect ratio in the `options` object:

```javascript
options: {
    maintainAspectRatio: true,
    aspectRatio: 2  // Width:height ratio (2 = twice as wide as tall)
}
```

Or adjust the container height in `style.css`:

```css
.chart-container {
    height: 600px;  /* Adjust as needed */
}
```

### Legend Position

Change where the legend appears:

```javascript
options: {
    plugins: {
        legend: {
            position: 'top'  // Options: 'top', 'bottom', 'left', 'right'
        }
    }
}
```

## Technical Details

- **Library**: Chart.js 4.4.0
- **Chart Type**: [Line/Bar/Pie/etc.]
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Chart.js (loaded from CDN)
- **Responsive**: Yes, adapts to container width
- **Mobile Friendly**: Yes, optimized for touch devices

## File Structure

```
[chart-name]/
├── main.html       # Main chart implementation
├── style.css       # Styling and layout
└── index.md        # This documentation file
```

## Use Cases

This [chart type] is particularly useful for:

- [Use case 1]
- [Use case 2]
- [Use case 3]
- [Use case 4]

## References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Chart.js Chart Type Guide](https://www.chartjs.org/docs/latest/charts/[type].html)
- [Chart.js Configuration](https://www.chartjs.org/docs/latest/configuration/)
- [Chart.js Samples](https://www.chartjs.org/docs/latest/samples/)

## Related Charts

- [Link to related chart 1]
- [Link to related chart 2]

---

*Generated using the chartjs-generator skill*
