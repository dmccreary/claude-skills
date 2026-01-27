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
    // IMPORTANT: This ensures node colors match the legend colors
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
        // Pass groups configuration to vis-network for correct node coloring
        groups: visGroups,
        // Use physics-based layout (NOT hierarchical - it doesn't work well with DAGs)
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
            margin: 10,
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

    // Disable physics after stabilization to stop the graph from spinning
    network.on('stabilizationIterationsDone', function() {
        network.setOptions({ physics: { enabled: false } });
    });

    // Re-enable physics while dragging a node, disable when done
    // This allows manual node repositioning while keeping the graph stable
    network.on('dragStart', function() {
        network.setOptions({ physics: { enabled: true } });
    });
    network.on('dragEnd', function() {
        network.setOptions({ physics: { enabled: false } });
    });

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
// IMPORTANT: Uses classifierName from groups for human-readable labels
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
        // Use classifierName for human-readable label, fallback to groupId
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
