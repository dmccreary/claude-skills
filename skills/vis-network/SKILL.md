---
name: vis-network
description: Create an educational MicroSim using the vis-network JavaScript library.  Each MicroSim is a directory located in the /docs/sims folder.  It has a main.html file that can be referenced with an iframe.  The main.html file imports the main JavaScript code to run the educational MicroSim.
---
# Educational MicroSim Creation Skill for Vis-Network

## Overview

This skill contains the rules for generating a Educational MicroSim using the vis.network JavaScript library.
MicroSims are lightweight, interactive educational simulations designed for browser-based learning.
MicroSims occupy a unique position at the intersection of

1. **Simplicity** (focused scope, transparent code)
2. **Accessibility** (browser-native, universal embedding)
3. **AI Generation** (standardized patterns, prompt-compatible design).

## Purpose

Educational MicroSims transform abstract concepts into visual interactive, manipulable experiences that enable students to learn through exploration and experimentation. Each MicroSim addresses specific learning objectives while maintaining the pedagogical rigor and technical quality necessary for educational deployment.

## Default Layout: vis-network-tutorial

The **vis-network-tutorial** layout is the standard template for all vis-network MicroSims embedded in intelligent textbooks. This layout features:

- **Graph on the left** - Network visualization occupies the left portion of the canvas
- **Controls on the right** - Interactive controls, status panels, and legends in the right panel
- **Title at top center** - Clear identification of the visualization
- **Legend in upper left** - Color/symbol key for understanding the visualization
- **Responsive design** - Works across different screen sizes

**Reference Implementation**: See `/docs/sims/three-color-dfs/` for a complete working example.

## Development Process

### Step 1: Educational Requirements Specification

Before generating code, articulate the educational purpose:

1. **Subject Area and Topic**: What specific concept does this simulation teach?
2. **Grade Level**: Elementary (K-5), Middle School (6-8), High School (9-12), or Undergraduate
3. **Learning Objectives**: What should students understand after using this simulation? (Align with Bloom's Taxonomy: Remember, Understand, Apply, Analyze, Evaluate, Create)
4. **Duration**: Typical engagement time (5-15 minutes recommended)
5. **Prerequisites**: What knowledge must students have before using this?
6. **Assessment Opportunities**: How can educators verify learning?

### Step 2: MicroSim Implementation with Vis-Network

Generate a self-contained, interactive vis-network.js simulation following the standardized MicroSim architecture.  The program is width responsive.

#### Folder Structure
Each Vis-Network MicroSim is contained in a folder within the /docs/sims directory.  The folder name is $MICROSIM_NAME

```
/docs/sims/$MICROSIM_NAME
/docs/sims/$MICROSIM_NAME/index.md      # Documentation with iframe embed
/docs/sims/$MICROSIM_NAME/main.html     # HTML5 file with vis-network CDN link
/docs/sims/$MICROSIM_NAME/style.css     # All CSS styles (extracted from HTML)
/docs/sims/$MICROSIM_NAME/$MICROSIM_NAME.js  # All vis-network JavaScript
/docs/sims/$MICROSIM_NAME/metadata.json # Dublin core metadata
```

### Step 3: Default Interaction Settings

**IMPORTANT**: All vis-network MicroSims embedded in textbooks via iframe MUST disable mouse-based zoom and pan, and enable navigation buttons instead.

#### Required Interaction Options

```javascript
const options = {
    // ... other options ...
    interaction: {
        zoomView: false,        // Disable mouse wheel zoom
        dragView: false,        // Disable mouse drag to pan
        navigationButtons: true // Enable built-in navigation buttons
    }
};
```

#### Rationale

These settings are mandatory for textbook embedding because:

1. **Scroll Interference**: When a vis-network diagram is embedded in a textbook page via iframe, mouse wheel zoom captures scroll events. This prevents users from scrolling through the textbook content, creating a frustrating user experience.

2. **Touch Device Conflicts**: On tablets and phones, pinch-to-zoom and drag gestures conflict with page navigation and scrolling.

3. **Accessibility**: Navigation buttons provide a consistent, discoverable interface for all users, including those using assistive technologies.

4. **Predictable Behavior**: Students expect scrolling to move through content, not zoom into diagrams.

#### Exception: Fullscreen Mode

The ONLY exception to this rule is when a diagram is displayed in fullscreen mode (not embedded in an iframe). In fullscreen mode, mouse zoom and pan may be enabled since there is no surrounding content to scroll.

#### Detecting Iframe vs Fullscreen Context

Use these utility functions to detect the execution context and conditionally enable mouse interactions:

```javascript
// ===========================================
// ENVIRONMENT DETECTION
// ===========================================

/**
 * Detect if the MicroSim is running inside an iframe
 * Returns true if embedded in an iframe, false if standalone/fullscreen
 */
function isInIframe() {
    try {
        return window.self !== window.top;
    } catch (e) {
        return true; // If access denied, we're in a cross-origin iframe
    }
}

/**
 * Detect if the browser is in fullscreen mode
 */
function isFullscreen() {
    return !!(document.fullscreenElement ||
              document.webkitFullscreenElement ||
              document.mozFullScreenElement);
}
```

#### Conditional Interaction Options

Use the environment detection to set appropriate interaction options:

```javascript
function initializeNetwork() {
    // Enable mouse pan/zoom only when NOT in an iframe (i.e., fullscreen/standalone)
    const enableMouseInteraction = !isInIframe();

    const options = {
        layout: { improvedLayout: false },
        physics: { enabled: false },
        interaction: {
            selectConnectedEdges: false,
            dragView: enableMouseInteraction,   // Enable pan in fullscreen only
            zoomView: enableMouseInteraction,   // Enable zoom in fullscreen only
            navigationButtons: true,            // Always show nav buttons
            keyboard: {
                enabled: true,
                bindToWindow: false,
                speed: { x: 2, y: 2, zoom: 0.01 }  // Reduce keyboard nav speed
            }
        },
        // ... other options
    };

    const container = document.getElementById('network');
    network = new vis.Network(container, data, options);
}
```

#### Editor Mode with Save Functionality

For MicroSims that need manual node positioning, implement an editor mode using URL parameters:

```javascript
/**
 * Check if editor/save mode is enabled via URL parameter
 * Usage: main.html?enable-save=true
 */
function isSaveEnabled() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('enable-save') === 'true';
}

function initializeNetwork() {
    const saveEnabled = isSaveEnabled();

    const options = {
        interaction: {
            dragNodes: saveEnabled,                      // Only allow node dragging in save mode
            dragView: saveEnabled || !isInIframe(),      // Enable pan in save mode or fullscreen
            zoomView: saveEnabled || !isInIframe(),      // Enable zoom in save mode or fullscreen
            navigationButtons: true
        }
    };

    // Show/hide save controls based on mode
    const saveControls = document.getElementById('save-controls');
    if (saveControls) {
        saveControls.style.display = saveEnabled ? 'flex' : 'none';
    }
}
```

#### Save Node Positions to JSON

When editor mode is enabled, provide functionality to save updated node positions:

```javascript
function saveNodePositions() {
    // Get current positions from the network
    const positions = network.getPositions();

    // Update graphData with new positions
    graphData.nodes.forEach(node => {
        if (positions[node.id]) {
            node.x = Math.round(positions[node.id].x);
            node.y = Math.round(positions[node.id].y);
        }
    });

    // Update metadata
    graphData.metadata.lastUpdated = new Date().toISOString().split('T')[0];

    // Create JSON string with nice formatting
    const jsonString = JSON.stringify(graphData, null, 2);

    // Trigger download
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
```

#### Summary: Interaction Mode Matrix

| Context | dragView | zoomView | dragNodes | Use Case |
|---------|----------|----------|-----------|----------|
| Iframe (default) | `false` | `false` | `false` | Normal textbook embedding |
| Fullscreen/Standalone | `true` | `true` | `true` | User opened main.html directly |
| Editor Mode | `true` | `true` | `true` | Developer positioning nodes |

### Step 4: Standard vis-network Options Template

Use this template for all new vis-network MicroSims:

```javascript
const options = {
    layout: {
        improvedLayout: false
    },
    physics: {
        enabled: false  // Use fixed positions for educational clarity
    },
    interaction: {
        selectConnectedEdges: false,
        zoomView: false,
        dragView: false,
        navigationButtons: true
    },
    nodes: {
        shape: 'box',
        margin: 12,
        font: {
            size: 16,
            face: 'Arial'
        },
        borderWidth: 3,
        shadow: {
            enabled: true,
            color: 'rgba(0,0,0,0.2)',
            size: 5,
            x: 2,
            y: 2
        }
    },
    edges: {
        arrows: {
            to: { enabled: true, scaleFactor: 1.2 }
        },
        width: 2,
        smooth: {
            type: 'curvedCW',
            roundness: 0.15
        }
    }
};
```

## Complete Template Files

### main.html Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$MICROSIM_TITLE</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div id="network"></div>

        <!-- Title at top center -->
        <div class="title">$MICROSIM_TITLE</div>

        <!-- Legend in upper left -->
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color color-1"></div>
                <span><strong>Label 1</strong> - Description</span>
            </div>
            <div class="legend-item">
                <div class="legend-color color-2"></div>
                <span><strong>Label 2</strong> - Description</span>
            </div>
            <!-- Add more legend items as needed -->
        </div>

        <!-- Right panel with controls and status -->
        <div class="right-panel">
            <div class="controls">
                <div class="step-counter" id="step-counter">Step 0 / N</div>
                <button class="btn btn-primary" id="next-btn">Next Step</button>
                <button class="btn btn-secondary" id="reset-btn">Reset</button>
            </div>

            <div class="status-info" id="status-info">
                <div class="status-title">Current Action:</div>
                <div class="status-text" id="status-text">
                    Click "Next Step" to begin.
                </div>
            </div>
        </div>
    </div>

    <script src="$MICROSIM_NAME.js"></script>
</body>
</html>
```

### style.css Template

```css
/* vis-network-tutorial Layout Stylesheet
 * =======================================
 *
 * GRAPH POSITIONING NOTES:
 * ------------------------
 * The graph network position is controlled by TWO areas in the JavaScript file:
 *
 * 1. NODE POSITIONS (nodeData array):
 *    Each node has x, y coordinates that determine its position relative to
 *    the canvas center (0,0). Negative x values move nodes left, negative y
 *    values move nodes up.
 *
 *    Example: { id: 1, label: 'Node Name', x: -350, y: -150 }
 *
 * 2. CAMERA/VIEW POSITION (positionView function):
 *    The moveTo() call sets where the camera looks at the graph:
 *
 *    position: { x: -90, y: 60 }
 *
 *    - Lower x value = moves the view RIGHT (shows more of left side of graph)
 *    - Higher y value = moves the view UP (shows more of bottom of graph)
 *    - scale: 1 = default zoom level
 *
 *    Adjust these values if the graph appears cut off or poorly centered.
 */

/* ===========================================
   RESET & BASE STYLES
   =========================================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: aliceblue;
}

/* ===========================================
   MAIN CONTAINER & NETWORK CANVAS
   =========================================== */
.container {
    position: relative;
    width: 100%;
    height: 100vh;
}

#network {
    width: 100%;
    height: 100%;
    background-color: aliceblue;
}

/* ===========================================
   TITLE (Top Center)
   =========================================== */
.title {
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 20px;
    font-weight: bold;
    color: black;
    background-color: aliceblue;
    z-index: 10;
}

/* ===========================================
   LEGEND (Upper Left)
   =========================================== */
.legend {
    position: absolute;
    top: 10px;
    left: 10px;
    padding: 6px 8px;
    background-color: rgba(255, 255, 255, 0.95);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    z-index: 10;
}

.legend-item {
    display: flex;
    align-items: center;
    margin: 3px 0;
    font-size: 12px;
}

.legend-color {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    margin-right: 4px;
    border: 2px solid #333;
}

/* Define legend colors to match your node colors */
.color-1 { background-color: #e0e0e0; }
.color-2 { background-color: #ffd700; }
.color-3 { background-color: #4caf50; }

/* ===========================================
   RIGHT PANEL (Controls & Status)
   =========================================== */
.right-panel {
    position: absolute;
    top: 50px;
    right: 10px;
    width: 280px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 10;
}

/* ===========================================
   STATUS INFO PANEL
   =========================================== */
.status-info {
    background-color: rgba(255, 255, 255, 0.95);
    border-radius: 8px;
    padding: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.status-title {
    font-weight: bold;
    margin-bottom: 6px;
    font-size: 13px;
}

.status-text {
    font-size: 12px;
    line-height: 1.5;
}

/* ===========================================
   CONTROL BUTTONS
   =========================================== */
.controls {
    display: flex;
    gap: 10px;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.95);
    padding: 10px 12px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.step-counter {
    font-size: 14px;
    color: #666;
    margin-right: 10px;
}

.btn {
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-primary {
    background-color: #2196f3;
    color: white;
}

.btn-primary:hover {
    background-color: #1976d2;
}

.btn-primary:disabled {
    background-color: #90caf9;
    cursor: not-allowed;
}

.btn-secondary {
    background-color: #757575;
    color: white;
}

.btn-secondary:hover {
    background-color: #616161;
}

/* ===========================================
   RESPONSIVE STYLES
   =========================================== */
@media (max-width: 600px) {
    .title {
        font-size: 16px;
    }

    .legend {
        padding: 8px 10px;
    }

    .legend-item {
        font-size: 10px;
    }

    .right-panel {
        width: 200px;
    }

    .controls {
        padding: 8px 12px;
    }

    .btn {
        padding: 8px 14px;
        font-size: 12px;
    }

    .step-counter {
        font-size: 12px;
    }
}
```

### JavaScript Template ($MICROSIM_NAME.js)

```javascript
// $MICROSIM_TITLE
// Educational vis-network visualization

// Define node colors for different states
const colors = {
    default: {
        background: '#e0e0e0',
        border: '#757575',
        font: '#333333'
    },
    active: {
        background: '#ffd700',
        border: '#ffa000',
        font: '#333333'
    },
    complete: {
        background: '#4caf50',
        border: '#2e7d32',
        font: '#ffffff'
    }
};

// Node definitions with fixed positions
// Position nodes on the LEFT side of canvas (negative x values)
// Canvas center is (0,0)
const nodeData = [
    { id: 1, label: 'Node 1', x: -300, y: -100 },
    { id: 2, label: 'Node 2', x: -100, y: -100 },
    { id: 3, label: 'Node 3', x: -300, y: 100 },
    { id: 4, label: 'Node 4', x: -100, y: 100 }
];

// Edge definitions (directed graph)
const edgeData = [
    { from: 1, to: 2 },
    { from: 1, to: 3 },
    { from: 2, to: 4 },
    { from: 3, to: 4 }
];

// Animation state
let currentStep = 0;
let nodeColors = {};

// Define animation steps
const steps = [
    { action: 'start', description: 'Click "Next Step" to begin the visualization.' },
    { action: 'visit', nodeId: 1, description: 'Step 1: Processing Node 1.' },
    { action: 'visit', nodeId: 2, description: 'Step 2: Processing Node 2.' },
    { action: 'finish', nodeId: 1, description: 'Step 3: Node 1 complete.' },
    { action: 'done', description: 'Visualization complete!' }
];

// Create vis.js DataSets
let nodes, edges, network;

// Position the view to show nodes on the left side of canvas
// ADJUST THESE VALUES to control initial graph position:
// - Lower x = moves view RIGHT (shows more of left side)
// - Higher y = moves view UP (shows more of bottom)
function positionView() {
    if (network) {
        network.moveTo({
            position: { x: -90, y: 60 },
            scale: 1,
            animation: false
        });
    }
}

function initializeNetwork() {
    currentStep = 0;
    nodeColors = {};

    // Initialize all nodes with default color
    const initialNodes = nodeData.map(node => {
        nodeColors[node.id] = 'default';
        return {
            id: node.id,
            label: node.label,
            x: node.x,
            y: node.y,
            color: {
                background: colors.default.background,
                border: colors.default.border
            },
            font: { color: colors.default.font, size: 16 }
        };
    });

    const initialEdges = edgeData.map((edge, index) => ({
        id: index,
        from: edge.from,
        to: edge.to,
        color: { color: '#333333' },
        width: 2
    }));

    nodes = new vis.DataSet(initialNodes);
    edges = new vis.DataSet(initialEdges);

    const options = {
        layout: { improvedLayout: false },
        physics: { enabled: false },
        interaction: {
            selectConnectedEdges: false,
            zoomView: false,
            dragView: false,
            navigationButtons: true
        },
        nodes: {
            shape: 'box',
            margin: 12,
            font: { size: 16, face: 'Arial' },
            borderWidth: 3,
            shadow: {
                enabled: true,
                color: 'rgba(0,0,0,0.2)',
                size: 5,
                x: 2,
                y: 2
            }
        },
        edges: {
            arrows: { to: { enabled: true, scaleFactor: 1.2 } },
            width: 2,
            smooth: { type: 'curvedCW', roundness: 0.15 }
        }
    };

    const container = document.getElementById('network');
    const data = { nodes: nodes, edges: edges };
    network = new vis.Network(container, data, options);

    setTimeout(positionView, 200);
    updateUI();
}

function setNodeColor(nodeId, colorName) {
    nodeColors[nodeId] = colorName;
    const colorSet = colors[colorName];
    nodes.update({
        id: nodeId,
        color: {
            background: colorSet.background,
            border: colorSet.border
        },
        font: { color: colorSet.font, size: 16 }
    });
}

function updateUI() {
    const stepCounter = document.getElementById('step-counter');
    const statusText = document.getElementById('status-text');
    const nextBtn = document.getElementById('next-btn');

    stepCounter.textContent = `Step ${currentStep} of ${steps.length - 1}`;

    if (currentStep < steps.length) {
        statusText.textContent = steps[currentStep].description;
    }

    nextBtn.disabled = currentStep >= steps.length - 1;
}

function executeStep() {
    if (currentStep >= steps.length - 1) return;

    currentStep++;
    const step = steps[currentStep];

    switch (step.action) {
        case 'visit':
            setNodeColor(step.nodeId, 'active');
            break;
        case 'finish':
            setNodeColor(step.nodeId, 'complete');
            break;
    }

    updateUI();
}

function reset() {
    initializeNetwork();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeNetwork();
    document.getElementById('next-btn').addEventListener('click', executeStep);
    document.getElementById('reset-btn').addEventListener('click', reset);
    window.addEventListener('resize', positionView);
});
```

## Graph Positioning Guide

When creating a new vis-network MicroSim, proper positioning requires adjusting two areas:

### 1. Node Positions (nodeData array)

Place nodes on the **left side** of the canvas using negative x values:

```javascript
const nodeData = [
    { id: 1, label: 'Node 1', x: -350, y: -150 },  // Upper left
    { id: 2, label: 'Node 2', x: -100, y: -150 },  // Upper center-left
    { id: 3, label: 'Node 3', x: -350, y: 150 },   // Lower left
    { id: 4, label: 'Node 4', x: -100, y: 150 }    // Lower center-left
];
```

**Coordinate System:**
- Canvas center is `(0, 0)`
- Negative x = left side of canvas
- Negative y = top of canvas
- Typical x range for left-side placement: `-400` to `-50`
- Typical y range: `-200` to `+400` depending on number of nodes

### 2. Camera/View Position (positionView function)

The `moveTo()` function controls the initial camera position:

```javascript
network.moveTo({
    position: { x: -90, y: 60 },
    scale: 1,
    animation: false
});
```

**Adjustment Guide:**
- **x value**: Lower = view shifts RIGHT (shows more of left-positioned nodes)
- **y value**: Higher = view shifts UP (shows more of bottom nodes)
- **scale**: `1` = default zoom, `0.8` = zoomed out, `1.2` = zoomed in

**Common adjustments:**
- Graph cut off on left? → Decrease x (e.g., `-120`)
- Graph cut off on bottom? → Increase y (e.g., `100`)
- Graph too small? → Increase scale (e.g., `1.1`)

### Testing Positioning

Test your MicroSim locally:
```
http://127.0.0.1:8000/[repo-name]/sims/[microsim-name]/main.html
```

Adjust node positions and camera position iteratively until the graph is well-centered on the left with the right panel visible on the right.
