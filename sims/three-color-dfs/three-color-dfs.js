// Three-Color DFS Cycle Detection Visualization
// Step-by-step animation of the algorithm used to detect cycles in learning graphs

// Define node colors based on DFS states
const colors = {
    white: {
        background: '#e0e0e0',
        border: '#757575',
        font: '#333333'
    },
    gray: {
        background: '#ffd700',
        border: '#ffa000',
        font: '#333333'
    },
    black: {
        background: '#4caf50',
        border: '#2e7d32',
        font: '#ffffff'
    }
};

// Node definitions with labels - positioned on left half of canvas
const nodeData = [
    { id: 1, label: 'Variables', x: -350, y: -150 },
    { id: 2, label: 'Functions', x: -100, y: -150 },
    { id: 3, label: 'Loops', x: -350, y: 10 },
    { id: 4, label: 'Recursion', x: -100, y: 10 },
    { id: 5, label: 'Data Structures', x: -350, y: 150 },
    { id: 6, label: 'Algorithms', x: -100, y: 150 },
    { id: 7, label: 'Arrays', x: -225, y: 250 },
    { id: 8, label: 'Sorting', x: -225, y: 350 }
];

// Edge definitions (adjacency list style)
const edgeData = [
    { from: 1, to: 2 },
    { from: 1, to: 3 },
    { from: 2, to: 4 },
    { from: 3, to: 4 },
    { from: 3, to: 5 },
    { from: 4, to: 3 },  // BACK EDGE - creates cycle!
    { from: 4, to: 6 },
    { from: 5, to: 7 },
    { from: 6, to: 7 },
    { from: 7, to: 8 }
];

// Animation state
let currentStep = 0;
let nodeColors = {};  // Track color state for each node
let dfsStack = [];    // Current DFS stack
let cycleDetected = false;
let backEdgeId = null;

// Define the sequence of steps for the DFS animation
// Each step: { action: 'visit'|'finish'|'cycle', nodeId, description }
const steps = [
    { action: 'start', description: 'Starting DFS from node 1 (Variables). All nodes begin as Gray (unvisited).' },
    { action: 'visit', nodeId: 1, description: 'Visit Variables: Color it Yellow (in progress) and push onto stack.' },
    { action: 'visit', nodeId: 2, description: 'Visit Functions (neighbor of Variables): Color it Yellow and push onto stack.' },
    { action: 'visit', nodeId: 4, description: 'Visit Recursion (neighbor of Functions): Color it Yellow and push onto stack.' },
    { action: 'visit', nodeId: 3, description: 'Visit Loops (neighbor of Recursion): Color it Yellow and push onto stack.' },
    { action: 'cycle', fromId: 4, toId: 3, description: 'CYCLE DETECTED! From Recursion, we check neighbor Loops which is already Yellow (on stack). Back edge found!' },
    { action: 'visit', nodeId: 5, description: 'Continue DFS: Visit Data Structures (neighbor of Loops): Color it Yellow and push onto stack.' },
    { action: 'visit', nodeId: 7, description: 'Visit Arrays (neighbor of Data Structures): Color it Yellow and push onto stack.' },
    { action: 'visit', nodeId: 8, description: 'Visit Sorting (neighbor of Arrays): Color it Yellow and push onto stack.' },
    { action: 'finish', nodeId: 8, description: 'Sorting has no unvisited neighbors. Color it Green (complete) and pop from stack.' },
    { action: 'finish', nodeId: 7, description: 'Arrays has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'finish', nodeId: 5, description: 'Data Structures has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'finish', nodeId: 3, description: 'Loops has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'visit', nodeId: 6, description: 'Back to Recursion: Visit Algorithms (neighbor of Recursion): Color it Yellow and push onto stack.' },
    { action: 'skipblack', nodeId: 7, fromId: 6, description: 'From Algorithms, neighbor Arrays is already Green (complete). Skip it.' },
    { action: 'finish', nodeId: 6, description: 'Algorithms has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'finish', nodeId: 4, description: 'Recursion has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'finish', nodeId: 2, description: 'Functions has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'finish', nodeId: 1, description: 'Variables has no more unvisited neighbors. Color it Green and pop from stack.' },
    { action: 'done', description: 'DFS complete! A cycle was detected: Loops ↔ Recursion. This graph is NOT a valid DAG.' }
];

// Create vis.js DataSets
let nodes, edges, network;

// Position the view to show nodes on the left side of canvas
function positionView() {
    if (network) {
        network.moveTo({
            // lower X to move nodes and arcs initial position further to the right
            // increase y to move nodes and arcs up
            position: { x: -90, y: 60 },
            scale: 1,
            animation: false
        });
    }
}

function initializeNetwork() {
    // Reset state
    currentStep = 0;
    nodeColors = {};
    dfsStack = [];
    cycleDetected = false;
    backEdgeId = null;

    // Initialize all nodes as white
    const initialNodes = nodeData.map(node => {
        nodeColors[node.id] = 'white';
        return {
            id: node.id,
            label: node.label,
            x: node.x,
            y: node.y,
            color: {
                background: colors.white.background,
                border: colors.white.border
            },
            font: { color: colors.white.font, size: 16 }
        };
    });

    // Initialize edges (without the back edge highlighted initially)
    const initialEdges = edgeData.map((edge, index) => ({
        id: index,
        from: edge.from,
        to: edge.to,
        color: { color: '#333333' },
        width: 2
    }));

    nodes = new vis.DataSet(initialNodes);
    edges = new vis.DataSet(initialEdges);

    // Configure vis-network options
    const options = {
        layout: {
            improvedLayout: false
        },
        physics: {
            enabled: false
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

    // Create/recreate the network
    const container = document.getElementById('network');
    const data = { nodes: nodes, edges: edges };
    network = new vis.Network(container, data, options);

    // Position the view to show nodes on the left side of canvas
    setTimeout(positionView, 200);

    // Update UI
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

function highlightBackEdge(fromId, toId) {
    // Find the edge from fromId to toId
    const allEdges = edges.get();
    for (let edge of allEdges) {
        if (edge.from === fromId && edge.to === toId) {
            backEdgeId = edge.id;
            edges.update({
                id: edge.id,
                color: { color: '#f44336' },
                width: 4,
                label: 'CYCLE!',
                font: {
                    color: '#f44336',
                    size: 14,
                    strokeWidth: 3,
                    strokeColor: '#ffffff'
                }
            });
            break;
        }
    }
}

function updateStackDisplay() {
    const stackEl = document.getElementById('dfs-stack');

    if (dfsStack.length === 0) {
        stackEl.innerHTML = '<div class="stack-empty">Empty</div>';
    } else {
        stackEl.innerHTML = dfsStack.map(nodeId => {
            const node = nodeData.find(n => n.id === nodeId);
            return `<div class="stack-item">${node.label}</div>`;
        }).join('');
    }
}

function updateUI() {
    const stepCounter = document.getElementById('step-counter');
    const statusText = document.getElementById('status-text');
    const cycleAlert = document.getElementById('cycle-alert');
    const nextBtn = document.getElementById('next-btn');
    const statusInfo = document.getElementById('status-info');

    stepCounter.textContent = `Step ${currentStep} of ${steps.length - 1}`;

    if (currentStep < steps.length) {
        statusText.textContent = steps[currentStep].description;
    }

    // Show/hide cycle alert
    if (cycleDetected) {
        cycleAlert.classList.add('visible');
    } else {
        cycleAlert.classList.remove('visible');
    }

    // Update status info styling
    if (currentStep >= steps.length - 1) {
        statusInfo.classList.add('complete');
        nextBtn.disabled = true;
    } else {
        statusInfo.classList.remove('complete');
        nextBtn.disabled = false;
    }

    updateStackDisplay();
}

function executeStep() {
    if (currentStep >= steps.length - 1) return;

    currentStep++;
    const step = steps[currentStep];

    switch (step.action) {
        case 'start':
            // Initial state - all white
            break;

        case 'visit':
            setNodeColor(step.nodeId, 'gray');
            dfsStack.push(step.nodeId);
            break;

        case 'finish':
            setNodeColor(step.nodeId, 'black');
            const idx = dfsStack.indexOf(step.nodeId);
            if (idx > -1) {
                dfsStack.splice(idx, 1);
            }
            break;

        case 'cycle':
            cycleDetected = true;
            highlightBackEdge(step.fromId, step.toId);
            break;

        case 'skipblack':
            // Just informational - node is already black
            break;

        case 'done':
            // Final state
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

    // Set up button handlers
    document.getElementById('next-btn').addEventListener('click', executeStep);
    document.getElementById('reset-btn').addEventListener('click', reset);

    // Handle window resize - maintain left-side positioning
    window.addEventListener('resize', positionView);
});
