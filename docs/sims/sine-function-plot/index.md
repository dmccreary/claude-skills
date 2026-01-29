---
title: Sine Function Visualization
description: Interactive plot of the sine function with slider control to explore points along the curve
quality_score: 100
image: /sims/sine-function-plot/sine-function-plot.png
og:image: /sims/sine-function-plot/sine-function-plot.png
---
# Sine Function Visualization

## Interactive Visualization

<iframe src="main.html" width="100%" height="430"></iframe>

[View the Sine Function Visualization with Plotly.js Fullscreen](main.html){:target="_blank" .md-button}

## Copy-Paste Embed Code

To embed this visualization in your own page, use the following HTML code:

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/sine-function-plot/main.html" width="100%" height="430"></iframe>
```

## Overview

This interactive MicroSim demonstrates the **sine function** (y = sin(x)) using Plotly.js. The visualization includes:

- **Smooth function curve** - Plotted with 500 points for visual clarity
- **Interactive point marker** - Red point that moves along the curve
- **Hover tooltips** - Show precise (x, y) coordinates at any point
- **Responsive design** - Adapts to different screen sizes
- **Slider control** - Adjust the x-coordinate to see the corresponding y-value

The sine function is one of the fundamental trigonometric functions, representing periodic oscillation with amplitude 1 and period 2π. This visualization helps students understand the relationship between angle (in radians) and the vertical component of unit circle motion.

## How to Use

1. **View the plot** - The blue curve shows sin(x) over the domain [-2π, 2π]
2. **Move the slider** - Drag the slider below the plot to change the x-coordinate (in radians)
3. **Observe the point** - Watch the red point move along the curve
4. **Hover for details** - Hover over any part of the curve to see exact coordinates
5. **Export image** - Use the camera icon in the toolbar to save as PNG

## Educational Applications

This visualization is ideal for:

- **Trigonometry courses** - Understanding sine wave behavior and periodicity
- **Precalculus** - Exploring amplitude, period, and phase of trigonometric functions
- **Physics** - Visualizing simple harmonic motion and wave phenomena
- **Engineering** - Analyzing AC signals and periodic processes
- **Calculus** - Studying continuity, differentiability, and integration of sin(x)

## Customization Guide

To create your own function plot, modify the following parameters in `script.js`:

### Function Definition

```javascript
function f(x) {
    return Math.sin(x);  // Replace with your function
}
```

### Domain and Range

```javascript
const config = {
    xMin: -6.28,     // Approximately -2π
    xMax: 6.28,      // Approximately 2π
    yMin: -1.5,      // Minimum y value (for display)
    yMax: 1.5,       // Maximum y value (for display)
    numPoints: 500,  // Number of points (higher = smoother)
    initialX: 0      // Initial slider position
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
- **Function sampling**: 500 evenly-spaced points from -2π to 2π
- **Responsive**: Uses Plotly's built-in responsive mode
- **Interactivity**: Range slider with real-time updates
- **Tooltips**: Automatic hover labels with 3 decimal precision
- **Export**: Built-in PNG export functionality

## Lesson Plan Suggestions

### Learning Objectives

Students will be able to:

1. Visualize the periodic nature of the sine function
2. Understand how the sine function relates angle to height on the unit circle
3. Identify key features: amplitude (1), period (2π), zeros, and extrema
4. Make predictions about sine values for specific angles

### Classroom Activities

**Activity 1: Finding Special Angles (15 minutes)**

1. Use the slider to find sin(0). What value do you observe?
2. Find sin(π/2) ≈ 1.571. What is the maximum value of sin(x)?
3. Find sin(π) ≈ 3.142. Why is sin(π) = 0?
4. Find sin(3π/2) ≈ 4.712. What is the minimum value of sin(x)?
5. Find sin(2π) ≈ 6.283. How does this relate to sin(0)?

**Activity 2: Periodicity Exploration (20 minutes)**

1. Starting at x = 0, move the slider to complete one full period. What x-value returns to sin(x) = 0?
2. Find three different x-values where sin(x) = 0.5. What pattern do you notice?
3. How many times does the curve cross y = 0 in the visible domain?
4. Predict: What would sin(4π) equal? (Hint: Use periodicity)

**Activity 3: Symmetry Investigation (15 minutes)**

1. Compare sin(1) and sin(-1). What do you notice?
2. Is the sine function even, odd, or neither? (Test: Does f(-x) = f(x) or f(-x) = -f(x)?)
3. Find the line of symmetry for one complete wave cycle
4. How does this symmetry relate to the unit circle?

### Assessment Questions

1. What is the approximate value of sin(π/4)? (Use slider: ≈ 0.707)
2. Between what two values does sin(x) always remain? Why?
3. How many complete cycles of the sine wave appear in the domain [-2π, 2π]?
4. If sin(a) = 0.8, can you find another value b where sin(b) = 0.8? (Yes, use symmetry)
5. How would the graph change if we plotted y = 2sin(x)?

## Key Mathematical Concepts

### Properties of sin(x)

- **Domain**: All real numbers (-∞, ∞)
- **Range**: [-1, 1]
- **Period**: 2π (≈ 6.283 radians)
- **Amplitude**: 1
- **Zeros**: x = nπ where n is any integer
- **Maximum**: sin(π/2 + 2πn) = 1
- **Minimum**: sin(3π/2 + 2πn) = -1
- **Symmetry**: Odd function, sin(-x) = -sin(x)

### Relationship to Unit Circle

The sine function represents the y-coordinate of a point on the unit circle as it rotates counterclockwise from the positive x-axis. The angle (in radians) corresponds to the x-axis input, and the height of the point gives the y-axis output.

## References

- [Plotly.js Documentation](https://plotly.com/javascript/)
- [Plotly.js Line Charts](https://plotly.com/javascript/line-charts/)
- [Khan Academy - Unit Circle & Radians](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:trig/x2ec2f6f830c9fb89:unit-circle/v/unit-circle-definition-of-trig-functions-1)
- [Math is Fun - Sine Function](https://www.mathsisfun.com/sine-cosine-tangent.html)
- [Desmos Graphing Calculator](https://www.desmos.com/calculator)
