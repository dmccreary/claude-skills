---
title: {{TITLE}}
description: {{DESCRIPTION}}
quality_score: 85
image: /sims/{{MICROSIM_NAME}}/{{MICROSIM_NAME}}.png
og:image: /sims/{{MICROSIM_NAME}}/{{MICROSIM_NAME}}.png
---

# {{TITLE}}

## Interactive Visualization

<iframe src="main.html" width="100%" height="500px"></iframe>

[View the {{TITLE}} MicroSim Fullscreen](main.html){:target="_blank" .md-button}

## Copy-Paste Embed Code

To embed this visualization in your own page, use the following HTML code:

```html
<iframe src="https://{{GITHUB_USERNAME}}.github.io/{{REPO_NAME}}/sims/{{MICROSIM_NAME}}/main.html" width="100%" height="500px"></iframe>
```

## Overview

{{OVERVIEW}}

This interactive MicroSim demonstrates the mathematical function **{{FUNCTION_LABEL}}** using Plotly.js. The visualization includes:

- **Smooth function curve** - Plotted with {{NUM_POINTS}} points for visual clarity
- **Interactive point marker** - Red point that moves along the curve
- **Hover tooltips** - Show precise (x, y) coordinates at any point
- **Responsive design** - Adapts to different screen sizes
- **Slider control** - Adjust the x-coordinate to see the corresponding y-value

## How to Use

1. **View the plot** - The blue curve shows the function over the domain [{{X_MIN}}, {{X_MAX}}]
2. **Move the slider** - Drag the slider below the plot to change the x-coordinate
3. **Observe the point** - Watch the red point move along the curve
4. **Hover for details** - Hover over any part of the curve to see exact coordinates
5. **Export image** - Use the camera icon in the toolbar to save as PNG

## Educational Applications

This visualization is ideal for:

- **Calculus courses** - Understanding function behavior, continuity, limits
- **Precalculus** - Exploring trigonometric, polynomial, and exponential functions
- **Physics** - Visualizing wave functions, trajectories, and periodic motion
- **Engineering** - Analyzing signal processing, control systems
- **Self-study** - Interactive exploration of mathematical concepts

## Customization Guide

To create your own function plot, modify the following parameters in `script.js`:

### Function Definition

```javascript
function f(x) {
    return {{FUNCTION_EXPRESSION}};  // Replace with your function
}
```

### Domain and Range

```javascript
const config = {
    xMin: {{X_MIN}},     // Minimum x value
    xMax: {{X_MAX}},     // Maximum x value
    yMin: {{Y_MIN}},     // Minimum y value (for display)
    yMax: {{Y_MAX}},     // Maximum y value (for display)
    numPoints: 500,      // Number of points (higher = smoother)
    initialX: {{INITIAL_X}}  // Initial slider position
};
```

### Styling Options

Edit `style.css` to customize:

- **Colors** - Change background, curve, point colors
- **Font sizes** - Adjust title, labels, axis text
- **Plot height** - Modify `#plot { height: 400px; }`
- **Margins** - Adjust spacing for different layouts

## Technical Details

- **Library**: [Plotly.js v2.27.0](https://plotly.com/javascript/)
- **Function sampling**: {{NUM_POINTS}} evenly-spaced points
- **Responsive**: Uses Plotly's built-in responsive mode
- **Interactivity**: Range slider with real-time updates
- **Tooltips**: Automatic hover labels with 3 decimal precision
- **Export**: Built-in PNG export functionality

## Lesson Plan Suggestions

### Learning Objectives

Students will be able to:

1. Visualize the relationship between x and y in {{FUNCTION_TYPE}} functions
2. Understand how changing input values affects output values
3. Identify key features ({{KEY_FEATURES}})
4. Make predictions about function behavior in different domains

### Classroom Activities

**Activity 1: Function Exploration (15 minutes)**

- Have students use the slider to find specific points
- Ask: "What is f({{SAMPLE_X1}})? Use the slider to find out."
- Discuss: "What happens as x approaches {{CRITICAL_POINT}}?"

**Activity 2: Pattern Recognition (20 minutes)**

- Students observe the function over the entire domain
- Identify: {{PATTERN_QUESTIONS}}
- Compare with other functions in the same family

**Activity 3: Prediction Challenge (15 minutes)**

- Given x-values outside the visible range, predict y-values
- Verify predictions by adjusting the domain
- Discuss extrapolation vs. interpolation

### Assessment Questions

1. What is the approximate value of f({{SAMPLE_X2}})?
2. {{ASSESSMENT_Q1}}
3. {{ASSESSMENT_Q2}}
4. How would the graph change if we {{MODIFICATION}}?

## References

- [Plotly.js Documentation](https://plotly.com/javascript/)
- [Plotly.js Line Charts](https://plotly.com/javascript/line-charts/)
- [Plotly.js Hover Text](https://plotly.com/javascript/hover-text-and-formatting/)
- [Mathematical Functions Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
- {{ADDITIONAL_REFERENCES}}
