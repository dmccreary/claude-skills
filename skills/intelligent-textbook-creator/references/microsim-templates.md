# MicroSim Templates and Implementation Guide

Complete templates and patterns for creating interactive p5.js simulations for educational content.

## What are MicroSims?

**MicroSims** (Micro-Simulations) are small, focused, interactive visualizations that demonstrate a single concept or principle. They:
- Make abstract concepts tangible through interaction
- Fit within the textbook page layout (~670px wide)
- Load quickly and run smoothly
- Work on mobile and desktop
- Require zero setup from the learner

## Complete Template Files

### Template 1: main.html (Standalone Page)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>MicroSim Title - Interactive Visualization</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
      body {
        padding: 0;
        margin: 0;
        overflow: hidden;
        font-family: Arial, Helvetica, sans-serif;
      }
      main {
        max-width: 670px;
        margin: 0 auto;
        padding: 20px;
      }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.1/p5.js"></script>
  </head>
  <body>
    <main>
      <!-- Canvas will be inserted here by p5.js -->
    </main>
    <script src="./your-sim-name.js"></script>
  </body>
</html>
```

**Key Elements:**
- **Minimal CSS**: Simple, clean styling
- **p5.js CDN**: Version 1.11.1 (update as needed)
- **main element**: Container for canvas
- **Viewport meta**: Ensures responsive behavior
- **External JS**: Separate file for simulation code

---

### Template 2: Basic p5.js Structure

**File:** `your-sim-name.js`

```javascript
// Basic MicroSim Template
// Description: [What this simulation demonstrates]

let canvas;
let containerWidth;
let canvasHeight = 500; // Adjust based on your content needs

// Add your simulation variables here
let myVariable = 0;

function setup() {
    // Get container dimensions
    updateCanvasSize();

    // Create canvas and attach to main element
    canvas = createCanvas(containerWidth, canvasHeight);
    const mainElement = document.querySelector('main');
    canvas.parent(mainElement);

    // Initialize your simulation here
    initSimulation();
}

function draw() {
    // Background - use aliceblue for consistency
    background('aliceblue');

    // Drawing region (top 70%)
    const drawHeight = height * 0.7;
    drawDrawingRegion(drawHeight);

    // Controls region (bottom 30%)
    const controlsY = drawHeight;
    const controlsHeight = height * 0.3;
    drawControlsRegion(controlsY, controlsHeight);
}

function drawDrawingRegion(regionHeight) {
    // Main visualization area
    push();
    fill('aliceblue');
    noStroke();
    rect(0, 0, width, regionHeight);

    // Add your visualization code here
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(16);
    text("Your visualization goes here", width/2, regionHeight/2);

    pop();
}

function drawControlsRegion(yStart, regionHeight) {
    // Controls and instructions area
    push();
    fill(255); // White background
    noStroke();
    rect(0, yStart, width, regionHeight);

    // Add controls, buttons, sliders, instructions
    fill(0);
    textAlign(CENTER, CENTER);
    textSize(14);
    text("Controls and instructions go here", width/2, yStart + regionHeight/2);

    pop();
}

function initSimulation() {
    // Initialize your simulation state
    myVariable = 0;
}

// Responsive design
function windowResized() {
    updateCanvasSize();
    resizeCanvas(containerWidth, canvasHeight);
    redraw();
}

function updateCanvasSize() {
    const container = document.querySelector('main');
    if (container) {
        containerWidth = Math.floor(container.getBoundingClientRect().width);
        containerWidth = Math.min(containerWidth, 670); // Max width
    } else {
        containerWidth = 670; // Fallback
    }
}

// Mouse interaction
function mousePressed() {
    // Handle mouse clicks
    return false; // Prevent default
}

function mouseMoved() {
    // Handle mouse movement
}

// Touch support for mobile
function touchStarted() {
    // Handle touch events
    return false; // Prevent default
}
```

---

### Template 3: Interactive Sim with Hover Effects

```javascript
// Interactive MicroSim with Hover Detection
// Example: Hovering over elements shows information

let canvas;
let containerWidth;
let canvasHeight = 500;

// Interactive elements
let elements = [];
let hoveredElement = -1;

function setup() {
    updateCanvasSize();
    canvas = createCanvas(containerWidth, canvasHeight);
    const mainElement = document.querySelector('main');
    canvas.parent(mainElement);

    // Create interactive elements
    createElements();
}

function createElements() {
    // Example: Create 5 clickable rectangles
    const elemWidth = 100;
    const elemHeight = 60;
    const spacing = 20;
    const startX = 50;
    const startY = 100;

    for (let i = 0; i < 5; i++) {
        elements.push({
            x: startX,
            y: startY + i * (elemHeight + spacing),
            w: elemWidth,
            h: elemHeight,
            label: `Element ${i + 1}`,
            description: `Description for element ${i + 1}`,
            color: color(100 + i * 30, 150, 200)
        });
    }
}

function draw() {
    background('aliceblue');

    // Title
    fill(0);
    textSize(20);
    textAlign(CENTER, TOP);
    text("Interactive MicroSim", width/2, 20);

    // Draw elements
    for (let i = 0; i < elements.length; i++) {
        const elem = elements[i];

        // Highlight if hovered
        if (i === hoveredElement) {
            stroke('blue');
            strokeWeight(4);
        } else {
            noStroke();
        }

        fill(elem.color);
        rect(elem.x, elem.y, elem.w, elem.h);

        // Label
        fill(255);
        noStroke();
        textAlign(CENTER, CENTER);
        textSize(14);
        text(elem.label, elem.x + elem.w/2, elem.y + elem.h/2);
    }

    // Show description for hovered element
    if (hoveredElement !== -1) {
        const elem = elements[hoveredElement];
        fill(255, 255, 255, 240);
        stroke(0);
        strokeWeight(2);
        rect(width/2 - 150, height - 120, 300, 100);

        fill(0);
        noStroke();
        textAlign(CENTER, CENTER);
        textSize(16);
        text(elem.description, width/2, height - 70, 280);
    } else {
        fill(0);
        textAlign(CENTER, CENTER);
        textSize(14);
        text("Hover over an element to see details", width/2, height - 70);
    }
}

function mouseMoved() {
    hoveredElement = -1;
    for (let i = 0; i < elements.length; i++) {
        const elem = elements[i];
        if (mouseX >= elem.x && mouseX <= elem.x + elem.w &&
            mouseY >= elem.y && mouseY <= elem.y + elem.h) {
            hoveredElement = i;
            break;
        }
    }
}

function touchStarted() {
    mouseMoved(); // Reuse hover detection for touch
    return false;
}

function windowResized() {
    updateCanvasSize();
    resizeCanvas(containerWidth, canvasHeight);
}

function updateCanvasSize() {
    const container = document.querySelector('main');
    if (container) {
        containerWidth = Math.floor(container.getBoundingClientRect().width);
        containerWidth = Math.min(containerWidth, 670);
    } else {
        containerWidth = 670;
    }
}
```

---

### Template 4: Sim with Sliders and Controls

```javascript
// MicroSim with Interactive Controls
// Uses p5.js DOM elements for sliders

let canvas;
let containerWidth;
let canvasHeight = 500;

// Simulation parameters
let paramA = 50;
let paramB = 100;
let paramC = 25;

// UI elements
let sliderA, sliderB, sliderC;
let resetButton;

function setup() {
    updateCanvasSize();
    canvas = createCanvas(containerWidth, canvasHeight);
    const mainElement = document.querySelector('main');
    canvas.parent(mainElement);

    // Create controls
    createControls();
}

function createControls() {
    // Position controls below canvas
    const controlsY = canvasHeight + 20;

    // Slider A
    createDiv('Parameter A: ').position(20, controlsY);
    sliderA = createSlider(0, 100, paramA);
    sliderA.position(120, controlsY);
    sliderA.style('width', '200px');

    // Slider B
    createDiv('Parameter B: ').position(20, controlsY + 30);
    sliderB = createSlider(0, 200, paramB);
    sliderB.position(120, controlsY + 30);
    sliderB.style('width', '200px');

    // Slider C
    createDiv('Parameter C: ').position(20, controlsY + 60);
    sliderC = createSlider(0, 50, paramC);
    sliderC.position(120, controlsY + 60);
    sliderC.style('width', '200px');

    // Reset button
    resetButton = createButton('Reset');
    resetButton.position(20, controlsY + 100);
    resetButton.mousePressed(resetSimulation);
}

function draw() {
    background('aliceblue');

    // Update parameters from sliders
    paramA = sliderA.value();
    paramB = sliderB.value();
    paramC = sliderC.value();

    // Title
    fill(0);
    textSize(18);
    textAlign(CENTER, TOP);
    text("Interactive Simulation with Controls", width/2, 10);

    // Visualization using parameters
    drawVisualization();

    // Display current values
    fill(0);
    textSize(12);
    textAlign(LEFT, TOP);
    text(`A: ${paramA.toFixed(0)}`, 10, 40);
    text(`B: ${paramB.toFixed(0)}`, 10, 60);
    text(`C: ${paramC.toFixed(0)}`, 10, 80);
}

function drawVisualization() {
    // Use paramA, paramB, paramC to draw something
    push();
    translate(width/2, height/2);

    // Example: Draw circles based on parameters
    noFill();
    stroke(0);
    strokeWeight(2);
    circle(0, 0, paramA * 2);
    circle(0, 0, paramB * 2);

    fill(255, 0, 0, 100);
    noStroke();
    circle(0, 0, paramC * 2);

    pop();
}

function resetSimulation() {
    sliderA.value(50);
    sliderB.value(100);
    sliderC.value(25);
}

function windowResized() {
    updateCanvasSize();
    resizeCanvas(containerWidth, canvasHeight);
}

function updateCanvasSize() {
    const container = document.querySelector('main');
    if (container) {
        containerWidth = Math.floor(container.getBoundingClientRect().width);
        containerWidth = Math.min(containerWidth, 670);
    } else {
        containerWidth = 670;
    }
}
```

---

## Embedding in MkDocs Pages

### index.md Template

```markdown
---
title: "Concept Name - Interactive Visualization"
description: "Interactive MicroSim demonstrating [concept]"
---

# Concept Name

Brief introduction to the concept (2-3 sentences).

## Interactive Visualization

Interact with the simulation below to explore [concept]:

<iframe src="./main.html"
  width="100%"
  height="550px"
  style="border: 2px solid #ccc;"
  scrolling="no">
</iframe>

[View Fullscreen](./main.html){ .md-button .md-button--primary }

## How to Use

1. **Instruction 1**: Description
2. **Instruction 2**: Description
3. **Instruction 3**: Description

## What to Observe

- **Observation 1**: What this shows
- **Observation 2**: What this demonstrates
- **Observation 3**: Key insight

## Concepts Demonstrated

This MicroSim illustrates:

- **Concept A**: Explanation
- **Concept B**: Explanation
- **Concept C**: Explanation

## Try This

Challenge prompts to deepen understanding:

1. **Challenge 1**: Try changing [parameter] and observe...
2. **Challenge 2**: What happens when...
3. **Challenge 3**: Can you predict...

## Related Concepts

- [Prerequisite Concept](../prerequisite/)
- [Related Concept](../related/)
- [Advanced Topic](../advanced/)

## Further Reading

- Resource 1
- Resource 2
- Resource 3
```

---

## Design Patterns and Best Practices

### Layout Pattern: Two-Region Design

```javascript
function draw() {
    background('aliceblue');

    // Region 1: Visualization (70% of height)
    const viz_height = height * 0.7;
    push();
    // Drawing code here
    pop();

    // Divider line
    stroke(0);
    strokeWeight(2);
    line(0, viz_height, width, viz_height);

    // Region 2: Controls/Info (30% of height)
    const controls_y = viz_height;
    const controls_height = height * 0.3;
    push();
    fill(255);
    rect(0, controls_y, width, controls_height);
    // Controls code here
    pop();
}
```

### Responsive Text Sizing

```javascript
function draw() {
    // Scale text based on canvas width
    const titleSize = constrain(containerWidth * 0.04, 16, 28);
    const bodySize = constrain(containerWidth * 0.025, 12, 18);
    const labelSize = constrain(containerWidth * 0.02, 10, 14);

    textSize(titleSize);
    text("Title", x, y);

    textSize(bodySize);
    text("Body text", x, y);

    textSize(labelSize);
    text("Labels", x, y);
}
```

### Adaptive Layout for Small Screens

```javascript
function updateLayout() {
    if (containerWidth < 400) {
        // Mobile layout
        elementSize = 40;
        spacing = 10;
        fontSize = 12;
    } else if (containerWidth < 600) {
        // Tablet layout
        elementSize = 60;
        spacing = 15;
        fontSize = 14;
    } else {
        // Desktop layout
        elementSize = 80;
        spacing = 20;
        fontSize = 16;
    }
}
```

### Animation Pattern

```javascript
let animationProgress = 0;
let animationSpeed = 0.01;
let isAnimating = false;

function draw() {
    background('aliceblue');

    if (isAnimating) {
        animationProgress += animationSpeed;
        if (animationProgress >= 1) {
            animationProgress = 0; // Loop or stop
        }
    }

    // Use animationProgress (0.0 to 1.0) to interpolate
    const x = lerp(startX, endX, animationProgress);
    const y = lerp(startY, endY, animationProgress);

    circle(x, y, 20);
}

function mousePressed() {
    isAnimating = !isAnimating; // Toggle animation
}
```

---

## Common MicroSim Types

### 1. Concept Explorer

**Purpose**: Click elements to reveal information

**Pattern**:
- Array of clickable regions
- Click detection
- Info display on selection
- Clear visual feedback

### 2. Parameter Adjuster

**Purpose**: Sliders/controls modify visualization

**Pattern**:
- Sliders for parameters
- Real-time visual update
- Value displays
- Reset button

### 3. Process Animator

**Purpose**: Animated step-by-step process

**Pattern**:
- Play/pause controls
- Step-by-step progression
- Labels for each stage
- Optional speed control

### 4. Comparison Viewer

**Purpose**: Side-by-side comparison

**Pattern**:
- Split screen layout
- Independent controls for each side
- Highlighting differences
- Synchronized interactions

### 5. Graph/Chart Interactive

**Purpose**: Interactive data visualization

**Pattern**:
- Axes with labels
- Data points/lines
- Hover to show values
- Toggle data series

---

## Testing Checklist

Before deploying a MicroSim:

- [ ] Works on desktop (Chrome, Firefox, Safari)
- [ ] Works on mobile (iOS Safari, Android Chrome)
- [ ] Responsive to window resize
- [ ] Touch events work on mobile
- [ ] No console errors
- [ ] Loads in under 2 seconds
- [ ] Framerate is smooth (>30 FPS)
- [ ] Instructions are clear
- [ ] Accessible (keyboard navigation if applicable)
- [ ] Embedded iframe displays correctly in MkDocs
- [ ] Fullscreen link works

---

## Performance Optimization

### Reduce Draw Calls

```javascript
// Bad: Redrawing static elements every frame
function draw() {
    drawComplexBackground(); // Expensive!
    drawDynamicElements();
}

// Good: Use background layer
let bgGraphics;

function setup() {
    bgGraphics = createGraphics(width, height);
    drawComplexBackground(bgGraphics); // Draw once
}

function draw() {
    image(bgGraphics, 0, 0); // Fast blit
    drawDynamicElements();
}
```

### Limit Object Count

```javascript
// If you have many objects, consider:
// 1. Spatial hashing
// 2. Object pooling
// 3. Level of detail (LOD)

// Example: Only update visible objects
function draw() {
    for (let obj of objects) {
        if (isVisible(obj)) {
            obj.update();
            obj.display();
        }
    }
}
```

---

## Summary

Use these templates as starting points:
- **Basic Template**: Simple visualization without controls
- **Interactive Template**: Hover and click interactions
- **Controls Template**: Sliders and buttons
- **Custom**: Combine patterns as needed

Key principles:
- Responsive design (works 320px-670px width)
- Touch and mouse support
- Clear visual hierarchy
- Performance optimization
- Accessibility considerations

Refer to actual MicroSims in `/docs/sims/` for real-world examples.
