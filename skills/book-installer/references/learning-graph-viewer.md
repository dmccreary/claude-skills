---
name: install-learning-graph-viewer
description: This skill installs an interactive learning graph viewer application into an intelligent textbook project. Use this skill when working with a textbook that has a learning-graph.json file and needs a visual, interactive graph exploration tool with search, filtering, and statistics capabilities.
---
# Install Learning Graph Viewer

## Overview

This skill installs a complete interactive graph visualization application into the `/docs/sims/graph-viewer/` directory of an intelligent textbook project. The viewer provides an interactive way to explore learning graphs with features like node search, category filtering, and real-time statistics.

## When to Use This Skill

Use this skill when:

- A learning graph has been generated (learning-graph.json exists in /docs/learning-graph/)
- The textbook needs an interactive visualization tool for exploring concept dependencies
- Students or instructors need to filter, search, and analyze the learning graph structure

**Prerequisites:**

- `/docs/learning-graph/learning-graph.json` must exist
- The JSON file must have metadata with a `title` field
- The JSON file must have proper `classifierName` values in groups (see Step 3.5)
- MkDocs project structure must be in place

## Installation Workflow

### Step 1: Verify Prerequisites

Before installation, verify that the learning graph JSON file exists:

```bash
ls docs/learning-graph/learning-graph.json
```

If the file doesn't exist, use the `learning-graph-generator` skill first to create the learning graph.

### Step 2: Create Directory Structure

Create the graph-viewer directory:

```bash
mkdir -p docs/sims/graph-viewer
```

### Step 3: Create main.html

Create `docs/sims/graph-viewer/main.html` with the following structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Graph Viewer for TITLE</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link rel="stylesheet" href="local.css">
</head>
<body>
    <div class="container">
        <div class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h4>Learning Graph for TITLE</h4>
                <button id="toggle-sidebar" class="toggle-btn" title="Toggle Sidebar">&#9776;</button>
            </div>

            <div class="sidebar-content" id="sidebar-content">
                <div class="search-container">
                    <label for="search">Search Concepts:</label>
                    <input type="text" id="search" placeholder="Type to search...">
                    <div id="search-results" class="search-results"></div>
                </div>

                <div class="legend-container">
                    <h5>Categories</h5>
                    <div class="legend-controls">
                        <button id="check-all" class="legend-btn">Check All</button>
                        <button id="uncheck-all" class="legend-btn">Uncheck All</button>
                    </div>
                    <div id="legend"></div>
                </div>

                <div class="stats-container">
                    <h5>Statistics</h5>
                    <div id="stats">
                        <p>Visible Nodes: <span id="visible-nodes">0</span></p>
                        <p>Visible Edges: <span id="visible-edges">0</span></p>
                        <p>Foundational: <span id="foundational-nodes">0</span></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="graph-container" id="graph-container">
            <div id="network"></div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

Replace "TITLE" with the course title from learning-graph.json metadata.

### Step 4: Create local.css

Create `docs/sims/graph-viewer/local.css` with all sidebar and layout styling:

```css
/* Learning Graph Viewer Styles */

/* ================================
   RESET AND BASE STYLES
   ================================ */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    background-color: #f5f5f5;
    overflow: hidden;
}

/* ================================
   MAIN LAYOUT CONTAINER
   Uses flexbox for sidebar + graph layout
   ================================ */
.container {
    display: flex;
    height: 100vh;
    width: 100vw;
}

/* ================================
   SIDEBAR STYLES
   Collapsible sidebar with search, legend, and stats
   ================================ */
.sidebar {
    /* Width settings - adjust for label wrapping */
    width: 200px;
    min-width: 200px;
    /* Visual styling */
    background-color: #fff;
    border-right: 1px solid #ddd;
    /* Flexbox for internal layout */
    display: flex;
    flex-direction: column;
    /* Smooth collapse animation */
    transition: width 0.3s ease, min-width 0.3s ease;
    overflow: hidden;
}

/* Collapsed state - narrow width shows only toggle button */
.sidebar.collapsed {
    width: 50px;
    min-width: 50px;
}

/* ================================
   SIDEBAR HEADER
   Contains title and toggle button
   ================================ */
.sidebar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
    background-color: #2196F3;    /* Blue header bar */
    color: white;
}

.sidebar-header h4 {
    font-size: 14px;
    font-weight: 600;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;      /* Truncate long titles */
}

/* Hide title when collapsed */
.sidebar.collapsed .sidebar-header h4 {
    display: none;
}

/* ================================
   TOGGLE BUTTON
   Hamburger menu icon for collapse/expand
   ================================ */
.toggle-btn {
    background: none;
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    padding: 5px;
    border-radius: 4px;
}

.toggle-btn:hover {
    background-color: rgba(255,255,255,0.2);
}

/* ================================
   SIDEBAR CONTENT
   Scrollable area containing search, legend, stats
   ================================ */
.sidebar-content {
    flex: 1;
    overflow-y: auto;
    padding: 15px;
}

/* ================================
   SEARCH CONTAINER STYLES
   Type-ahead search for finding concepts
   ================================ */
.search-container {
    margin-bottom: 20px;
}

.search-container label {
    display: block;
    font-weight: 600;
    margin-bottom: 8px;
    color: #333;
}

.search-container input {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
    transition: border-color 0.2s;
}

.search-container input:focus {
    outline: none;
    border-color: #2196F3;
    box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.1);  /* Blue focus ring */
}

/* ================================
   SEARCH RESULTS DROPDOWN
   Positioned absolutely below search input
   ================================ */
.search-results {
    display: none;                    /* Hidden by default */
    position: absolute;
    width: calc(100% - 30px);         /* Account for sidebar padding */
    background: white;
    border: 1px solid #ddd;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    max-height: 300px;
    overflow-y: auto;
    z-index: 100;                     /* Above other content */
    margin-top: 4px;
}

.search-result-item {
    padding: 10px 12px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #eee;
}

.search-result-item:last-child {
    border-bottom: none;
}

.search-result-item:hover {
    background-color: #f5f5f5;
}

.result-label {
    font-weight: 500;
    color: #333;
}

/* Category badge in search results */
.result-category {
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 12px;
    color: #333;
}

/* ================================
   LEGEND CONTAINER STYLES
   Category filtering with checkboxes
   ================================ */
.legend-container {
    margin-bottom: 20px;
}

.legend-container h5 {
    font-weight: 600;
    margin-bottom: 10px;
    color: #333;
}

/* Check All / Uncheck All buttons */
.legend-controls {
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
}

.legend-btn {
    flex: 1;
    padding: 6px 10px;
    font-size: 12px;
    border: 1px solid #ddd;
    background: #fff;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
}

.legend-btn:hover {
    background: #f0f0f0;
    border-color: #bbb;
}

/* Legend items container - scrollable for many categories */
#legend {
    max-height: 400px;
    overflow-y: auto;
}

/* Individual legend item (checkbox + color + label) */
.legend-item {
    display: flex;
    align-items: center;
    padding: 6px 0;
    gap: 8px;
}

.legend-item input[type="checkbox"] {
    width: 16px;
    height: 16px;
    cursor: pointer;
}

/* Color swatch box */
.color-box {
    width: 20px;
    height: 20px;
    border-radius: 4px;
    border: 1px solid rgba(0,0,0,0.1);
    flex-shrink: 0;                   /* Don't shrink color box */
}

.legend-item label {
    font-size: 13px;
    color: #555;
    cursor: pointer;
    flex: 1;
}

/* ================================
   STATISTICS CONTAINER STYLES
   Shows counts of visible nodes, edges, foundational
   ================================ */
.stats-container {
    background-color: #f9f9f9;
    padding: 12px;
    border-radius: 6px;
}

.stats-container h5 {
    font-weight: 600;
    margin-bottom: 10px;
    color: #333;
}

#stats p {
    font-size: 13px;
    color: #666;
    margin-bottom: 6px;
}

#stats span {
    font-weight: 600;
    color: #2196F3;                   /* Blue accent for numbers */
}

/* ================================
   GRAPH CONTAINER STYLES
   Main visualization area
   ================================ */
.graph-container {
    flex: 1;                          /* Take remaining space */
    position: relative;
    background-color: aliceblue;      /* Light blue background */
}

#network {
    width: 100%;
    height: 100%;
}

/* ================================
   RESPONSIVE ADJUSTMENTS
   Mobile-friendly sidebar widths
   ================================ */
@media (max-width: 768px) {
    .sidebar {
        width: 250px;
        min-width: 250px;
    }

    .sidebar.collapsed {
        width: 40px;
        min-width: 40px;
    }
}
```

### Step 5: Create script.js

Create `docs/sims/graph-viewer/script.js` with the visualization logic:

```javascript
// Learning Graph Viewer Script
// Loads and displays an interactive learning graph using vis-network

let network = null;
let allNodes = [];
let allEdges = [];
let groups = {};
let visibleGroups = new Set();

// Load the learning graph data
async function loadGraph() {
    try {
        const response = await fetch('../../learning-graph/learning-graph.json');
        const data = await response.json();

        allNodes = data.nodes || [];
        allEdges = data.edges || [];
        groups = data.groups || {};

        // Initialize all groups as visible
        Object.keys(groups).forEach(g => visibleGroups.add(g));

        initializeNetwork();
        buildLegend();
        updateStats();
        setupSearch();
        setupControls();

    } catch (error) {
        console.error('Error loading learning graph:', error);
        document.getElementById('network').innerHTML =
            '<p style="color: red; padding: 20px;">Error loading learning graph. Make sure learning-graph.json exists.</p>';
    }
}

// Initialize the vis-network visualization
function initializeNetwork() {
    const container = document.getElementById('network');

    // Create nodes DataSet - colors are handled by the groups option
    const nodes = new vis.DataSet(allNodes);

    // Create edges DataSet
    const edges = new vis.DataSet(allEdges.map(edge => ({
        ...edge,
        arrows: 'to',
        color: { color: '#888', opacity: 0.6 }
    })));

    const data = { nodes, edges };

    // Build vis-network groups configuration from JSON groups
    const visGroups = {};
    Object.entries(groups).forEach(([groupId, groupInfo]) => {
        visGroups[groupId] = {
            color: {
                background: groupInfo.color || 'lightgray',
                border: groupInfo.color || 'lightgray',
                highlight: {
                    background: groupInfo.color || 'lightgray',
                    border: '#333'
                },
                hover: {
                    background: groupInfo.color || 'lightgray',
                    border: '#666'
                }
            },
            font: {
                color: groupInfo.font?.color || 'black'
            }
        };
    });

    const options = {
        groups: visGroups,
        layout: {
            randomSeed: 42,
            improvedLayout: true
        },
        physics: {
            enabled: true,
            solver: 'forceAtlas2Based',
            forceAtlas2Based: {
                gravitationalConstant: -50,
                centralGravity: 0.01,
                springLength: 100,
                springConstant: 0.08,
                damping: 0.4,
                avoidOverlap: 0.5
            },
            stabilization: {
                enabled: true,
                iterations: 1000,
                updateInterval: 25
            }
        },
        nodes: {
            shape: 'box',
            margin: 4,
            font: {
                size: 14,
                face: 'Arial'
            },
            borderWidth: 2,
            shadow: true
        },
        edges: {
            smooth: {
                type: 'cubicBezier',
                forceDirection: 'horizontal',
                roundness: 0.4
            },
            width: 1.5
        },
        interaction: {
            hover: true,
            tooltipDelay: 200,
            zoomView: true,
            dragView: true
        }
    };

    network = new vis.Network(container, data, options);

    // Handle node selection
    network.on('selectNode', function(params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const node = allNodes.find(n => n.id === nodeId);
            if (node) {
                highlightNode(nodeId);
            }
        }
    });
}

// Build the category legend
function buildLegend() {
    const legendContainer = document.getElementById('legend');
    legendContainer.innerHTML = '';

    Object.entries(groups).forEach(([groupId, groupInfo]) => {
        const count = allNodes.filter(n => n.group === groupId).length;

        const item = document.createElement('div');
        item.className = 'legend-item';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `group-${groupId}`;
        checkbox.checked = true;
        checkbox.addEventListener('change', () => toggleGroup(groupId, checkbox.checked));

        const colorBox = document.createElement('span');
        colorBox.className = 'color-box';
        colorBox.style.backgroundColor = groupInfo.color || 'lightgray';

        const label = document.createElement('label');
        label.htmlFor = `group-${groupId}`;
        label.textContent = `${groupInfo.classifierName || groupId} (${count})`;

        item.appendChild(checkbox);
        item.appendChild(colorBox);
        item.appendChild(label);
        legendContainer.appendChild(item);
    });
}

// Toggle visibility of a category group
function toggleGroup(groupId, visible) {
    if (visible) {
        visibleGroups.add(groupId);
    } else {
        visibleGroups.delete(groupId);
    }
    updateVisibility();
}

// Update node and edge visibility based on selected groups
function updateVisibility() {
    const visibleNodeIds = new Set(
        allNodes.filter(n => visibleGroups.has(n.group)).map(n => n.id)
    );

    const nodes = network.body.data.nodes;
    const edges = network.body.data.edges;

    // Update node visibility
    allNodes.forEach(node => {
        const isVisible = visibleGroups.has(node.group);
        nodes.update({
            id: node.id,
            hidden: !isVisible
        });
    });

    // Update edge visibility (hide if either endpoint is hidden)
    allEdges.forEach(edge => {
        const isVisible = visibleNodeIds.has(edge.from) && visibleNodeIds.has(edge.to);
        edges.update({
            id: edge.id || `${edge.from}-${edge.to}`,
            hidden: !isVisible
        });
    });

    updateStats();
}

// Update statistics display
function updateStats() {
    const visibleNodeIds = new Set(
        allNodes.filter(n => visibleGroups.has(n.group)).map(n => n.id)
    );

    const visibleEdgeCount = allEdges.filter(
        e => visibleNodeIds.has(e.from) && visibleNodeIds.has(e.to)
    ).length;

    // Count foundational nodes (nodes with no outgoing dependencies)
    const nodesWithDeps = new Set(allEdges.map(e => e.from));
    const foundationalCount = allNodes.filter(
        n => !nodesWithDeps.has(n.id) && visibleGroups.has(n.group)
    ).length;

    document.getElementById('visible-nodes').textContent = visibleNodeIds.size;
    document.getElementById('visible-edges').textContent = visibleEdgeCount;
    document.getElementById('foundational-nodes').textContent = foundationalCount;
}

// Setup search functionality
function setupSearch() {
    const searchInput = document.getElementById('search');
    const resultsContainer = document.getElementById('search-results');

    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase().trim();
        resultsContainer.innerHTML = '';

        if (query.length < 2) {
            resultsContainer.style.display = 'none';
            return;
        }

        const matches = allNodes.filter(n =>
            n.label.toLowerCase().includes(query)
        ).slice(0, 10);

        if (matches.length === 0) {
            resultsContainer.style.display = 'none';
            return;
        }

        matches.forEach(node => {
            const item = document.createElement('div');
            item.className = 'search-result-item';

            const groupInfo = groups[node.group] || {};
            item.innerHTML = `
                <span class="result-label">${node.label}</span>
                <span class="result-category" style="background-color: ${groupInfo.color || 'lightgray'}">
                    ${groupInfo.classifierName || node.group}
                </span>
            `;

            item.addEventListener('click', () => {
                selectNode(node.id);
                searchInput.value = node.label;
                resultsContainer.style.display = 'none';
            });

            resultsContainer.appendChild(item);
        });

        resultsContainer.style.display = 'block';
    });

    // Hide results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
            resultsContainer.style.display = 'none';
        }
    });
}

// Select and focus on a node
function selectNode(nodeId) {
    network.selectNodes([nodeId]);
    network.focus(nodeId, {
        scale: 1.2,
        animation: {
            duration: 500,
            easingFunction: 'easeInOutQuad'
        }
    });
    highlightNode(nodeId);
}

// Highlight a node and its connections
function highlightNode(nodeId) {
    const connectedNodes = network.getConnectedNodes(nodeId);
    const allConnected = [nodeId, ...connectedNodes];

    // Reset all nodes to normal opacity
    const nodes = network.body.data.nodes;
    allNodes.forEach(node => {
        const isConnected = allConnected.includes(node.id);
        nodes.update({
            id: node.id,
            opacity: isConnected ? 1 : 0.3
        });
    });

    // Reset opacity after a delay
    setTimeout(() => {
        allNodes.forEach(node => {
            nodes.update({
                id: node.id,
                opacity: 1
            });
        });
    }, 3000);
}

// Setup control buttons
function setupControls() {
    // Toggle sidebar
    document.getElementById('toggle-sidebar').addEventListener('click', function() {
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('sidebar-content');
        sidebar.classList.toggle('collapsed');
        content.style.display = sidebar.classList.contains('collapsed') ? 'none' : 'block';
    });

    // Check all groups
    document.getElementById('check-all').addEventListener('click', function() {
        Object.keys(groups).forEach(groupId => {
            visibleGroups.add(groupId);
            document.getElementById(`group-${groupId}`).checked = true;
        });
        updateVisibility();
    });

    // Uncheck all groups
    document.getElementById('uncheck-all').addEventListener('click', function() {
        Object.keys(groups).forEach(groupId => {
            visibleGroups.delete(groupId);
            document.getElementById(`group-${groupId}`).checked = false;
        });
        updateVisibility();
    });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', loadGraph);
```

### Step 6: Create index.md

Create `docs/sims/graph-viewer/index.md` with documentation:

```markdown
# Learning Graph Viewer

This interactive viewer allows you to explore the learning graph for the course.

## Features

- **Search**: Type in the search box to find specific concepts
- **Category Filtering**: Use checkboxes to show/hide concept categories
- **Interactive Navigation**: Click and drag to explore, scroll to zoom
- **Statistics**: View real-time counts of visible nodes and edges

## Using the Viewer

1. **Search for Concepts**: Start typing in the search box to find concepts. Click on a result to focus on that node.

2. **Filter by Category**: Use the category checkboxes in the sidebar to show or hide groups of related concepts. Use "Check All" or "Uncheck All" for bulk operations.

3. **Navigate the Graph**:
   - Drag to pan around the graph
   - Scroll to zoom in and out
   - Click on a node to select it and highlight its connections

4. **View Statistics**: The sidebar shows counts of visible nodes, edges, and foundational concepts.

## Graph Structure

- **Foundational Concepts** (left side): Prerequisites with no dependencies
- **Advanced Concepts** (right side): Topics that build on multiple prerequisites
- **Edges**: Arrows point from a concept to its prerequisites

## Launch the Viewer

[Open Learning Graph Viewer](./main.html){ .md-button .md-button--primary }

<iframe src="./main.html" width="100%" height="600px" frameborder="0"></iframe>
```

### Step 7: Verify classifierName Values in JSON (IMPORTANT)

The learning-graph.json file must have human-readable `classifierName` values in the groups section. **This is critical for the legend to display correctly.**

Check the groups section of learning-graph.json:

```json
"groups": {
  "FOUND": {
    "classifierName": "Foundation Concepts",  // CORRECT - human readable
    "color": "LightCoral"
  },
  "BLOOM": {
    "classifierName": "BLOOM",  // WRONG - just the ID, not human readable
    "color": "PeachPuff"
  }
}
```

If any `classifierName` values are just the group ID (like "BLOOM", "VISUA"), update them to be human-readable (like "Bloom's Taxonomy", "Visualization Types").

Common taxonomy mappings:

| Group ID | classifierName |
|----------|----------------|
| FOUND | Foundation Concepts |
| BLOOM | Bloom's Taxonomy |
| VISUA | Visualization Types |
| LIBRA | Libraries & Tools |
| SPECI | Specification |
| COGNI | Cognitive Science |
| AUDIE | Audience Adaptation |
| EVALU | Evaluation & Testing |
| ITERA | Iteration & Workflow |
| ACCES | Accessibility |
| DEPLO | Deployment |
| CAPST | Capstone |

### Step 8: Update Title in main.html

Replace the "TITLE" placeholder in main.html with the course title:

1. Extract title from learning-graph.json metadata
2. In `docs/sims/graph-viewer/main.html`, replace all instances of "TITLE" with the actual course title
3. This appears in two locations:
   - The `<title>` tag: `<title>Learning Graph Viewer for TITLE</title>`
   - The page heading: `<h4>Learning Graph for TITLE</h4>`

### Step 9: Update MkDocs Navigation (Optional)

If the user wants the graph viewer in the site navigation, add it to `mkdocs.yml`:

```yaml
nav:
  - MicroSims:
    - Graph Viewer: sims/graph-viewer/index.md
```

### Step 10: Inform the User

Provide the user with instructions to test the installation:

1. Run `mkdocs serve` to start the local development server
2. Navigate to the appropriate URL based on their repository name:
   - Format: `http://localhost:8000/REPO_NAME/sims/graph-viewer/main.html`
3. Alternatively, access it through the MkDocs site menu if added to navigation

---

## vis-network Options Reference

The viewer uses these vis-network configuration options:

### Groups Configuration

**Purpose:** Maps learning graph taxonomy groups to vis-network colors so legend and nodes match.

```javascript
const visGroups = {};
Object.entries(groups).forEach(([groupId, groupInfo]) => {
    visGroups[groupId] = {
        color: {
            background: groupInfo.color || 'lightgray',  // Node fill color
            border: groupInfo.color || 'lightgray',      // Node border color
            highlight: {
                background: groupInfo.color || 'lightgray',
                border: '#333'                            // Dark border when selected
            },
            hover: {
                background: groupInfo.color || 'lightgray',
                border: '#666'                            // Medium border on hover
            }
        },
        font: {
            color: groupInfo.font?.color || 'black'       // Label text color
        }
    };
});
```

### Layout Options

**Purpose:** Controls initial node positioning. Uses physics-based layout (NOT hierarchical).

```javascript
layout: {
    randomSeed: 42,        // Consistent initial positions across reloads
    improvedLayout: true   // Better initial spread before physics kicks in
}
```

**Important:** Do NOT use hierarchical layout for learning graphs - it doesn't work well with complex DAGs.

### Physics Options

**Purpose:** Controls force-directed graph simulation for node positioning.

```javascript
physics: {
    enabled: true,
    solver: 'forceAtlas2Based',           // Best solver for large graphs
    forceAtlas2Based: {
        gravitationalConstant: -50,        // Repulsion force (negative = push apart)
        centralGravity: 0.01,              // Pull toward center (low = spread out)
        springLength: 100,                 // Ideal edge length in pixels
        springConstant: 0.08,              // Edge spring stiffness
        damping: 0.4,                      // Velocity damping (higher = slower settling)
        avoidOverlap: 0.5                  // Node overlap prevention (0-1)
    },
    stabilization: {
        enabled: true,
        iterations: 1000,                  // Stabilization iterations before render
        updateInterval: 25                 // Progress update frequency (ms)
    }
}
```

### Node Options

**Purpose:** Visual appearance of concept nodes.

```javascript
nodes: {
    shape: 'box',          // Rectangular nodes (good for text labels)
    margin: 4,             // Padding inside node box
    font: {
        size: 14,          // Label font size
        face: 'Arial'      // Font family
    },
    borderWidth: 2,        // Node border thickness
    shadow: true           // Drop shadow for depth
}
```

### Edge Options

**Purpose:** Visual appearance of dependency arrows.

```javascript
edges: {
    smooth: {
        type: 'cubicBezier',         // Curved edges
        forceDirection: 'horizontal', // Curves bend horizontally
        roundness: 0.4               // Curve intensity (0-1)
    },
    width: 1.5                       // Line thickness
}
```

**Note on edge creation:** Edges are created with arrows and muted color:

```javascript
edges = new vis.DataSet(allEdges.map(edge => ({
    ...edge,
    arrows: 'to',                         // Arrowhead at target
    color: { color: '#888', opacity: 0.6 } // Gray, semi-transparent
})));
```

### Interaction Options

**Purpose:** User interaction controls.

```javascript
interaction: {
    hover: true,           // Enable hover effects
    tooltipDelay: 200,     // Delay before tooltip appears (ms)
    zoomView: true,        // Allow scroll-to-zoom
    dragView: true         // Allow click-and-drag panning
}
```

---

## CSS Reference

### Layout Classes

| Class | Purpose |
|-------|---------|
| `.container` | Flex container holding sidebar + graph (100vw × 100vh) |
| `.sidebar` | Left sidebar (200px width, collapsible to 50px) |
| `.sidebar.collapsed` | Collapsed state styling |
| `.sidebar-content` | Scrollable content area inside sidebar |
| `.graph-container` | Main graph area (flex: 1, fills remaining space) |
| `#network` | vis-network canvas (100% × 100%) |

### Sidebar Header Classes

| Class | Purpose |
|-------|---------|
| `.sidebar-header` | Blue header bar with title and toggle |
| `.sidebar-header h4` | Title text (truncates with ellipsis) |
| `.toggle-btn` | Hamburger menu button (&#9776;) |

### Search Classes

| Class | Purpose |
|-------|---------|
| `.search-container` | Wrapper for search input and results |
| `.search-results` | Dropdown with matching concepts |
| `.search-result-item` | Individual search result row |
| `.result-label` | Concept name in search result |
| `.result-category` | Category badge in search result |

### Legend Classes

| Class | Purpose |
|-------|---------|
| `.legend-container` | Wrapper for category legend |
| `.legend-controls` | Check All / Uncheck All buttons |
| `.legend-btn` | Individual control button |
| `#legend` | Container for legend items (scrollable) |
| `.legend-item` | Single category row (checkbox + color + label) |
| `.color-box` | 20×20px color swatch |

### Statistics Classes

| Class | Purpose |
|-------|---------|
| `.stats-container` | Gray background box for stats |
| `#stats` | Container for stat paragraphs |
| `#visible-nodes` | Span for node count (blue text) |
| `#visible-edges` | Span for edge count (blue text) |
| `#foundational-nodes` | Span for foundational count (blue text) |

### Key CSS Variables/Colors

| Element | Color | Usage |
|---------|-------|-------|
| Sidebar header | `#2196F3` | Blue Material Design primary |
| Focus ring | `rgba(33, 150, 243, 0.1)` | Light blue focus glow |
| Stats numbers | `#2196F3` | Blue accent for statistics |
| Graph background | `aliceblue` | Light blue canvas background |
| Borders | `#ddd` | Light gray for borders |
| Text primary | `#333` | Dark gray for headings |
| Text secondary | `#555` / `#666` | Medium gray for labels |

---

## Common Issues and Fixes

### Issue 1: Legend colors don't match node colors

**Symptom:** When filtering by category, the visible nodes are a different color than the legend swatch.

**Cause:** The script must pass the groups configuration to vis-network's `groups` option.

**Fix:** Ensure script.js builds `visGroups` from JSON and passes to options:

```javascript
const options = {
    groups: visGroups,  // This is required!
    // ... other options
};
```

### Issue 2: Legend shows group IDs instead of readable names

**Symptom:** The legend shows "FOUND", "BLOOM" instead of "Foundation Concepts", "Bloom's Taxonomy".

**Cause:** The `classifierName` values in learning-graph.json are set to the group IDs.

**Fix:** Update the groups section in learning-graph.json to have proper classifierName values.

### Issue 3: Hierarchical layout doesn't work well

**Symptom:** The graph layout is messy or nodes overlap badly.

**Cause:** Hierarchical layout doesn't work well with DAGs that have complex dependency structures.

**Fix:** Use physics-based layout with `forceAtlas2Based` solver (as shown in script.js).

### Issue 4: Graph takes too long to stabilize

**Symptom:** The graph keeps moving for a long time before settling.

**Fix:** Adjust physics parameters:
- Increase `damping` (e.g., 0.4 → 0.6) for faster settling
- Decrease `stabilization.iterations` for quicker initial render
- Increase `springConstant` for stiffer edges

---

## Viewer Features

The installed graph viewer provides:

**Search Functionality:**

- Type-ahead search with dropdown results
- Shows category information for each node
- Focuses and selects matching nodes in the visualization

**Category Filtering:**

- Sidebar legend with color-coded categories
- Checkboxes to show/hide specific taxonomy groups
- "Check All" and "Uncheck All" bulk operations
- Collapsible sidebar for expanded viewing

**Real-time Statistics:**

- Visible node count
- Visible edge count
- Foundational node count (concepts with no dependencies)

**Interactive Visualization:**

- vis-network graph with physics simulation
- Color-coded nodes by taxonomy category
- Directed edges showing concept dependencies
- Zoomable and draggable interface
- Node highlight on selection (dims unconnected nodes)

---

## Technical Details

**File Structure:**

```
docs/sims/graph-viewer/
├── main.html      # Main application HTML
├── script.js      # JavaScript logic for visualization
├── local.css      # Styling for the viewer
└── index.md       # Documentation page with iframe embed
```

**Dependencies:**

- vis-network.js (loaded from CDN: `https://unpkg.com/vis-network/standalone/umd/vis-network.min.js`)
- learning-graph.json (loaded from `../../learning-graph/learning-graph.json`)

**Data Path:**
The script.js file loads the learning graph from a relative path: `../../learning-graph/learning-graph.json`. This assumes the standard intelligent textbook structure where `/docs/sims/` and `/docs/learning-graph/` are siblings.
