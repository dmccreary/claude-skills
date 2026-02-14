/* vis-network MicroSim Script Template
 * =====================================
 * Provides core functionality for vis-network graph visualizations:
 * - Loads graph data from data.json
 * - Creates and configures vis-network
 * - Handles node interactions (click, hover)
 * - Positions view for optimal display
 * - Optional: Save node positions for editing
 *
 * CUSTOMIZATION POINTS (marked with TODO):
 * - Node colors and styles
 * - Network options (physics, interaction)
 * - Event handlers (click, hover behavior)
 * - View positioning
 *
 * Scroll Hijacking Rule:
 * - When embedded in chapter iframes, do NOT capture mouse-wheel scroll by default.
 * - Keep zoom/pan disabled unless explicitly enabled for editor mode.
 */

// ===========================================
// CONFIGURATION - Customize these values
// ===========================================

// TODO: Define node colors for different states/categories
const colors = {
    default: {
        background: '#97c2fc',
        border: '#2b7ce9',
        font: '#333333'
    },
    selected: {
        background: '#ffeb3b',
        border: '#fbc02d',
        font: '#333333'
    },
    highlighted: {
        background: '#4caf50',
        border: '#2e7d32',
        font: 'white'
    }
    // Add more color states as needed
};

// ===========================================
// STATE VARIABLES
// ===========================================
let graphData = null;
let nodeData = [];
let edgeData = [];
let nodes, edges, network;
let selectedNode = null;

// ===========================================
// INTERACTION POLICY
// ===========================================
// Prevent iframe scroll hijacking in normal viewing mode.
// Enable wheel zoom/pan only when explicitly editing positions.
const interactionPolicy = {
    allowZoomInEditorOnly: true
};

// ===========================================
// UTILITY FUNCTIONS
// ===========================================

// Check if save mode is enabled via URL parameter (?enable-save=true)
function isSaveEnabled() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('enable-save') === 'true';
}

// ===========================================
// DATA LOADING
// ===========================================

// Load graph data from data.json
async function loadGraphData() {
    try {
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        graphData = await response.json();
        nodeData = graphData.nodes;
        edgeData = graphData.edges;
        return true;
    } catch (error) {
        console.error('Error loading graph data:', error);
        nodeData = [];
        edgeData = [];
        return false;
    }
}

// ===========================================
// VIEW POSITIONING
// ===========================================

/* Position the view to show graph optimally
 * Adjust these values based on your graph layout:
 * - Lower x = moves view RIGHT (shows more of left side)
 * - Higher y = moves view UP (shows more of bottom)
 */
function positionView() {
    if (network) {
        network.moveTo({
            position: { x: 0, y: 0 },  // TODO: Adjust based on graph layout
            scale: 1.0,                  // TODO: Adjust zoom level
            animation: false
        });
    }
}

// ===========================================
// NETWORK INITIALIZATION
// ===========================================

function initializeNetwork() {
    // Reset state
    selectedNode = null;

    // Transform nodes for vis-network
    const visNodes = nodeData.map(node => ({
        id: node.id,
        label: node.label,
        x: node.x,
        y: node.y,
        color: {
            background: colors.default.background,
            border: colors.default.border
        },
        font: { color: colors.default.font, size: 14 }
    }));

    // Transform edges for vis-network
    const visEdges = edgeData.map((edge, index) => ({
        id: index,
        from: edge.from,
        to: edge.to,
        color: { color: '#666666' },
        width: 2
    }));

    nodes = new vis.DataSet(visNodes);
    edges = new vis.DataSet(visEdges);

    // Configure vis-network options
    const saveEnabled = isSaveEnabled();

    const options = {
        layout: {
            improvedLayout: false  // Use fixed positions from data.json
        },
        physics: {
            enabled: false  // Disable physics for fixed layout
        },
        interaction: {
            selectConnectedEdges: false,
            // Scroll hijacking prevention: keep wheel zoom off in normal mode.
            zoomView: saveEnabled && interactionPolicy.allowZoomInEditorOnly,
            dragView: saveEnabled,       // Enable pan only in save mode
            dragNodes: saveEnabled,      // Enable node drag only in save mode
            navigationButtons: saveEnabled,
            keyboard: saveEnabled,
            hover: true
        },
        nodes: {
            shape: 'ellipse',
            margin: 10,
            font: {
                size: 14,
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
                to: { enabled: true, scaleFactor: 1 }
            },
            width: 2,
            smooth: {
                type: 'curvedCW',
                roundness: 0.15
            }
        }
    };

    // Create the network
    const container = document.getElementById('network');
    const data = { nodes: nodes, edges: edges };
    network = new vis.Network(container, data, options);

    // Set up event handlers
    network.on('click', handleNodeClick);
    network.on('hoverNode', handleNodeHover);
    network.on('blurNode', handleNodeBlur);

    // Track node position changes for save functionality
    if (saveEnabled) {
        network.on('dragEnd', handleDragEnd);
    }

    // Position the view after a short delay
    setTimeout(positionView, 200);

    // Update UI
    updateStats();
}

// ===========================================
// EVENT HANDLERS
// ===========================================

function handleNodeClick(params) {
    if (params.nodes.length > 0) {
        selectedNode = params.nodes[0];
        const node = nodeData.find(n => n.id === selectedNode);
        // TODO: Customize click behavior
        console.log('Node clicked:', node);
        showNodeDetails(node);
    }
}

function handleNodeHover(params) {
    const nodeId = params.node;
    const node = nodeData.find(n => n.id === nodeId);

    // TODO: Customize hover display
    const infoPanel = document.getElementById('info-panel');
    const infoContent = document.getElementById('info-content');

    if (infoPanel && infoContent && node) {
        let html = `<strong>${node.label}</strong><br>`;
        html += `ID: ${node.id}<br>`;
        // Add more node details as needed
        infoContent.innerHTML = html;
        infoPanel.style.display = 'block';
    }
}

function handleNodeBlur(params) {
    const infoPanel = document.getElementById('info-panel');
    if (infoPanel) {
        infoPanel.style.display = 'none';
    }
}

function showNodeDetails(node) {
    // TODO: Implement detailed node view
    console.log('Show details for:', node);
}

// ===========================================
// NODE POSITION SAVING (Editor Mode)
// ===========================================

function handleDragEnd(params) {
    if (params.nodes.length > 0) {
        params.nodes.forEach(nodeId => {
            const position = network.getPositions([nodeId])[nodeId];
            const nodeIndex = nodeData.findIndex(n => n.id === nodeId);
            if (nodeIndex !== -1) {
                nodeData[nodeIndex].x = Math.round(position.x);
                nodeData[nodeIndex].y = Math.round(position.y);
            }
        });
    }
}

function saveNodePositions() {
    // Update graphData with current positions
    graphData.nodes = nodeData;

    // Create JSON string with nice formatting
    const jsonString = JSON.stringify(graphData, null, 2);

    // Create blob and download link
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'data.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    console.log('Node positions saved. Replace data.json with the downloaded file.');
}

// ===========================================
// UI UPDATES
// ===========================================

function updateStats() {
    const statsElement = document.getElementById('stats');
    if (statsElement) {
        statsElement.textContent = `Nodes: ${nodeData.length}`;
    }
}

function reset() {
    initializeNetwork();
}

// ===========================================
// INITIALIZATION
// ===========================================

document.addEventListener('DOMContentLoaded', async function() {
    // Load graph data first
    await loadGraphData();

    // Initialize the network
    initializeNetwork();

    // Set up button handlers
    const resetBtn = document.getElementById('reset-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', reset);
    }

    // Show save button if save mode is enabled
    if (isSaveEnabled()) {
        const saveBtn = document.getElementById('save-btn');
        if (saveBtn) {
            saveBtn.style.display = 'block';
            saveBtn.addEventListener('click', saveNodePositions);
        }
    }

    // Handle window resize
    window.addEventListener('resize', positionView);
});
