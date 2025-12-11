/*
    {{TITLE}} - Causal Loop Diagram

    This script uses the vis-network.js library to render the CLD.

    URL Parameters:
    - menu=true: Show header and details panel (default: hidden for iframe)
    - file=filename: Load a specific JSON file (without .json extension)
*/

// Global variables
let network = null;
let cldData = null;
let nodes, edges;

// Load the CLD data from JSON file
async function loadCLDData() {
    try {
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error(`Failed to load data.json: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error(`Error loading CLD data: ${error.message}`);
    }
}

// Initialize the vis-network
function initializeNetwork() {
    const container = document.getElementById('network');
    const options = {
        layout: {
            improvedLayout: false
        },
        physics: {
            enabled: false
        },
        interaction: {
            selectConnectedEdges: false
        },
        nodes: {
            shape: 'box',
            margin: 10,
            font: {
                size: 20,
                face: 'Arial'
            },
            borderWidth: 2,
            shadow: true,
            color: {
                background: 'white',
                border: 'dodgerblue',
                highlight: {
                    background: 'lightskyblue',
                    border: 'darkblue'
                }
            }
        },
        edges: {
            arrows: {
                to: { enabled: true, scaleFactor: 1.2 }
            },
            color: {
                color: 'gray',
                highlight: 'blue'
            },
            width: 2,
            smooth: {
                type: 'curvedCW',
                roundness: 0.4
            },
            font: {
                size: 48,
                strokeWidth: 3,
                strokeColor: 'white'
            }
        }
    };

    network = new vis.Network(container, {}, options);

    // Click event handlers
    network.on('click', function(params) {
        if (params.nodes.length > 0) {
            showNodeDetails(params.nodes[0]);
        } else if (params.edges.length > 0) {
            showEdgeDetails(params.edges[0]);
        } else {
            showDefaultDetails();
        }
    });
}

// Load and render the CLD
function loadCLD(data) {
    try {
        cldData = data;

        // Update title if element exists
        const titleEl = document.querySelector('.header h1');
        if (titleEl) {
            titleEl.textContent = data.metadata.title;
        }

        // Update description if element exists
        const descEl = document.getElementById('diagram-description');
        if (descEl) {
            descEl.textContent = data.metadata.description;
        }

        // Convert nodes to vis-network format
        const visNodes = data.nodes.map(node => ({
            id: node.id,
            label: wrapText(node.label, 20),
            x: node.position.x,
            y: node.position.y,
            title: node.description || `${node.label} (${node.type || 'variable'})`,
            originalData: node
        }));

        // Convert edges to vis-network format
        const visEdges = data.edges.map(edge => {
            const edgeConfig = {
                id: edge.id,
                from: edge.source,
                to: edge.target,
                label: edge.polarity === 'positive' ? '+' : '-',
                color: edge.polarity === 'positive' ? '#28a745' : '#dc3545',
                title: edge.description || `${edge.polarity === 'positive' ? 'Positive (+)' : 'Negative (-)'} relationship`,
                originalData: edge,
                font: {
                    size: 48,
                    strokeWidth: 2,
                    strokeColor: 'white'
                }
            };

            // Add custom curve if specified
            if (edge.curve) {
                edgeConfig.smooth = {
                    type: edge.curve.type || 'curvedCW',
                    roundness: edge.curve.roundness || 0.4
                };
            }

            return edgeConfig;
        });

        // Add loop indicators as special nodes
        if (data.loops) {
            data.loops.forEach(loop => {
                if (loop.position) {
                    visNodes.push({
                        id: 'loop_' + loop.id,
                        label: loop.type === 'reinforcing' ? 'R' : 'B',
                        x: loop.position.x,
                        y: loop.position.y,
                        shape: 'ellipse',
                        size: 30,
                        color: {
                            background: loop.type === 'reinforcing' ? '#dc3545' : '#28a745',
                            border: 'black'
                        },
                        font: {
                            color: 'white',
                            size: 16,
                            face: 'Arial'
                        },
                        title: `${loop.type === 'reinforcing' ? 'Reinforcing' : 'Balancing'} Loop: ${loop.label || loop.id}`,
                        originalData: loop,
                        isLoop: true
                    });
                }
            });
        }

        nodes = new vis.DataSet(visNodes);
        edges = new vis.DataSet(visEdges);

        network.setData({ nodes: nodes, edges: edges });

        // Center the diagram
        network.fit({
            animation: { duration: 500, easingFunction: "easeInOutQuad" }
        });

        showDefaultDetails();

    } catch (error) {
        showError('Error loading CLD data: ' + error.message);
    }
}

// Wrap long text for node labels
function wrapText(text, maxLength) {
    if (text.length <= maxLength) return text;

    const words = text.split(' ');
    const lines = [];
    let currentLine = '';

    for (const word of words) {
        if ((currentLine + ' ' + word).length <= maxLength) {
            currentLine += (currentLine ? ' ' : '') + word;
        } else {
            if (currentLine) lines.push(currentLine);
            currentLine = word;
        }
    }
    if (currentLine) lines.push(currentLine);

    return lines.join('\n');
}

// Show node details in panel
function showNodeDetails(nodeId) {
    const nodeData = nodes.get(nodeId);
    if (!nodeData) return;

    let content = '';

    if (nodeData.isLoop) {
        const loop = nodeData.originalData;
        content = `
            <div class="loop-info ${loop.type}">
                <h4>${loop.label || loop.id}</h4>
                <p><span class="label">Type:</span> ${loop.type === 'reinforcing' ? 'Reinforcing (R)' : 'Balancing (B)'}</p>
                <p><span class="label">Description:</span> ${loop.description || 'No description available'}</p>
                ${loop.behavior_pattern ? `<p><span class="label">Behavior Pattern:</span> ${loop.behavior_pattern}</p>` : ''}
                ${loop.path ? `<p><span class="label">Path:</span> ${loop.path.join(' → ')}</p>` : ''}
            </div>
        `;
    } else {
        const node = nodeData.originalData;
        content = `
            <h4>${node.label}</h4>
            <p><span class="label">Type:</span> ${node.type || 'variable'}</p>
            <p><span class="label">Description:</span> ${node.description || 'No description available'}</p>
            ${node.examples ? `<p><span class="label">Examples:</span> ${node.examples.join(', ')}</p>` : ''}
            ${node.measurement ? `<p><span class="label">Measurement:</span> ${node.measurement}</p>` : ''}
        `;
    }

    document.getElementById('details-content').innerHTML = content;
}

// Show edge details in panel
function showEdgeDetails(edgeId) {
    const edgeData = edges.get(edgeId);
    if (!edgeData) return;

    const edge = edgeData.originalData;
    const sourceNode = cldData.nodes.find(n => n.id === edge.source);
    const targetNode = cldData.nodes.find(n => n.id === edge.target);

    const content = `
        <h4>Causal Relationship</h4>
        <p><span class="label">From:</span> ${sourceNode ? sourceNode.label : edge.source}</p>
        <p><span class="label">To:</span> ${targetNode ? targetNode.label : edge.target}</p>
        <p><span class="label">Polarity:</span> ${edge.polarity === 'positive' ? 'Positive (+)' : 'Negative (-)'}</p>
        <p><span class="label">Description:</span> ${edge.description || 'No description available'}</p>
        ${edge.strength ? `<p><span class="label">Strength:</span> ${edge.strength}</p>` : ''}
        ${edge.delay && edge.delay.present ? `<p><span class="label">Delay:</span> ${edge.delay.duration || 'Present'}</p>` : ''}
    `;

    document.getElementById('details-content').innerHTML = content;
}

// Show default overview in panel
function showDefaultDetails() {
    let content = '<p>Click on a node, edge, or loop symbol to see details here.</p>';

    if (cldData) {
        content += `
            <h4>System Overview</h4>
            <p><span class="label">Title:</span> ${cldData.metadata.title}</p>
            ${cldData.metadata.archetype ? `<p><span class="label">Archetype:</span> ${cldData.metadata.archetype}</p>` : ''}
            <p><span class="label">Description:</span> ${cldData.metadata.description || 'No description available'}</p>
        `;

        if (cldData.loops && cldData.loops.length > 0) {
            content += '<h4>Feedback Loops</h4>';
            cldData.loops.forEach(loop => {
                content += `
                    <div class="loop-info ${loop.type}">
                        <strong>${loop.label || loop.id}</strong> (${loop.type === 'reinforcing' ? 'R' : 'B'})
                        <br>${loop.description || 'No description'}
                    </div>
                `;
            });
        }
    }

    document.getElementById('details-content').innerHTML = content;
}

// Show error message
function showError(message) {
    document.getElementById('details-content').innerHTML = `<div class="error">${message}</div>`;
}

// URL parameter handling
function getURLParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Check menu parameter for iframe embedding
function checkMenuParameter() {
    const menu = getURLParameter('menu');
    // Default to hidden menus for iframe embedding
    if (menu !== 'true') {
        document.body.classList.add('menu-hidden');
    }
}

// Initialize on page load
window.addEventListener('load', async function() {
    initializeNetwork();
    checkMenuParameter();

    try {
        const data = await loadCLDData();
        loadCLD(data);
    } catch (error) {
        showError(error.message);
    }
});
