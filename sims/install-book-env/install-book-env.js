// Install Book Environment - Dependency Graph
// Shows the dependencies required to build an intelligent textbook

// Define nodes with fixed x,y positions
// X ranges from 100 (left - Permissions) to 1100 (right - Build Book)
const nodes = new vis.DataSet([
    // Foundation Layer (far left) - x: 100
    { id: 1, label: 'Permissions', x: 100, y: 280, fixed: true,
      group: 'foundation', title: 'User permissions to install software and create directories' },

    // System Layer - x: 200
    { id: 2, label: 'Unix Shell', x: 200, y: 180,
      group: 'system', title: 'Bash or Zsh terminal for running commands' },
    { id: 3, label: 'File System', x: 200, y: 380,
      group: 'system', title: 'Access to create and modify files' },

    // Runtime Layer - x: 350
    { id: 4, label: 'Python 3.10+', x: 350, y: 180,
      group: 'runtime', title: 'Python interpreter version 3.10 or higher' },
    { id: 5, label: 'Node.js', x: 350, y: 330,
      group: 'runtime', title: 'Node.js runtime for Claude Code CLI' },
    { id: 6, label: 'Git', x: 350, y: 480,
      group: 'runtime', title: 'Version control system' },

    // Package Manager Layer - x: 500
    { id: 7, label: 'pip', x: 500, y: 180,
      group: 'package_manager', title: 'Python package installer' },

    // Python Packages Layer - x: 650
    { id: 9, label: 'MkDocs', x: 650, y: 130,
      group: 'python_pkg', title: 'Static site generator for documentation' },
    { id: 10, label: 'MkDocs Material', x: 650, y: 230,
      group: 'python_pkg', title: 'Material design theme for MkDocs' },
    { id: 11, label: 'PyMdown\nExtensions', x: 650, y: 330,
      group: 'python_pkg', title: 'Markdown extensions for admonitions, tabs, etc.' },

    // Claude Tools Layer - x: 700
    { id: 12, label: 'Claude Code', x: 650, y: 405,
      group: 'claude', title: 'Claude AI coding assistant CLI' },
    { id: 13, label: 'GitHub Repo', x: 670, y: 490,
      group: 'claude', title: 'GitHub repository for textbook project' },

    // Skills Layer - x: 900
    { id: 14, label: 'Claude Skills', x: 900, y: 380,
      group: 'claude', title: 'Skill definitions for textbook generation' },

    // Goal (far right) - x: 1050
    { id: 15, label: 'Build Book', x: 1050, y: 280, fixed: true,
      group: 'goal', title: 'Generate and deploy intelligent textbook' }
]);

// Define edges with DEPENDS_ON labels
const edges = new vis.DataSet([
    // From Permissions
    { from: 2, to: 1, label: 'DEPENDS_ON' },  // Unix Shell -> Permissions
    { from: 3, to: 1, label: 'DEPENDS_ON' },  // File System -> Permissions

    // From Unix Shell
    { from: 4, to: 2, label: 'DEPENDS_ON' },  // Python -> Unix Shell
    { from: 5, to: 2, label: 'DEPENDS_ON' },  // Node.js -> Unix Shell
    { from: 6, to: 2, label: 'DEPENDS_ON' },  // Git -> Unix Shell

    // From File System
    { from: 4, to: 3, label: 'DEPENDS_ON' },  // Python -> File System
    { from: 6, to: 3, label: 'DEPENDS_ON' },  // Git -> File System

    // From Python
    { from: 7, to: 4, label: 'DEPENDS_ON' },  // pip -> Python


    // From pip
    { from: 9, to: 7, label: 'DEPENDS_ON' },   // MkDocs -> pip
    { from: 10, to: 7, label: 'DEPENDS_ON' },  // MkDocs Material -> pip
    { from: 11, to: 7, label: 'DEPENDS_ON' },  // PyMdown -> pip

    // MkDocs Material depends on MkDocs
    { from: 10, to: 9, label: 'DEPENDS_ON' },  // Material -> MkDocs

    // From Node.js
    { from: 12, to: 5, label: 'DEPENDS_ON' },  // Claude Code -> Node.js

    // From Git
    { from: 13, to: 6, label: 'DEPENDS_ON' },  // GitHub Repo -> Git

    // Claude Skills dependencies
    { from: 14, to: 12, label: 'DEPENDS_ON' }, // Skills -> Claude Code
    { from: 14, to: 13, label: 'DEPENDS_ON' }, // Skills -> GitHub Repo

    // Build Book dependencies
    { from: 15, to: 14, label: 'DEPENDS_ON' }, // Build Book -> Claude Skills
    { from: 15, to: 9, label: 'DEPENDS_ON' },  // Build Book -> MkDocs
    { from: 15, to: 10, label: 'DEPENDS_ON' }, // Build Book -> MkDocs Material
    { from: 15, to: 11, label: 'DEPENDS_ON' }  // Build Book -> PyMdown Extensions
]);

// Define group colors
const groups = {
    foundation: {
        color: { background: '#95a5a6', border: '#7f8c8d' },
        font: { color: '#fff' }
    },
    system: {
        color: { background: '#1abc9c', border: '#16a085' },
        font: { color: '#fff' }
    },
    runtime: {
        color: { background: '#f39c12', border: '#d68910' },
        font: { color: '#fff' }
    },
    package_manager: {
        color: { background: '#9b59b6', border: '#8e44ad' },
        font: { color: '#fff' }
    },
    python_pkg: {
        color: { background: '#2ecc71', border: '#27ae60' },
        font: { color: '#fff' }
    },
    claude: {
        color: { background: '#3498db', border: '#2980b9' },
        font: { color: '#fff' }
    },
    goal: {
        color: { background: '#e74c3c', border: '#c0392b' },
        font: { color: '#fff', size: 18 }
    }
};

// Network options
const options = {
    layout: {
        improvedLayout: false
    },
    physics: {
        enabled: false  // Use fixed positions
    },
    interaction: {
        selectConnectedEdges: true,
        hover: true,
        tooltipDelay: 100,
        zoomView: false,       // Disable mouse wheel zoom for iframe embedding
        dragView: false,       // Disable mouse drag to pan
        navigationButtons: true // Enable navigation buttons
    },
    nodes: {
        shape: 'box',
        margin: 12,
        font: {
            size: 14,
            face: 'Arial',
            multi: true
        },
        borderWidth: 2,
        shadow: {
            enabled: true,
            color: 'rgba(0,0,0,0.2)',
            size: 5
        }
    },
    edges: {
        arrows: {
            to: { enabled: true, scaleFactor: 0.8 }
        },
        width: 2,
        color: {
            color: '#666',
            highlight: '#e74c3c',
            hover: '#3498db'
        },
        font: {
            size: 14,
            color: '#666',
            strokeWidth: 3,
            strokeColor: '#fff'
            // if you remove the align middle you avoid the bug
            // https://github.com/visjs/vis-network/issues/2278 reported by me on sept 9th 2025
            // align: 'middle'
        },
        smooth: {
            type: 'curvedCW',
            roundness: 0.2
        }
    },
    groups: groups
};

// Create the network
const container = document.getElementById('network');
const data = { nodes: nodes, edges: edges };
const network = new vis.Network(container, data, options);

// Fit the network once after initial render, then shift view up
setTimeout(function() {
    network.fit();
    // Get current view position and shift up by 40 pixels
    var viewPosition = network.getViewPosition();
    network.moveTo({
        position: { x: viewPosition.x, y: viewPosition.y + 20 },
        animation: false
    });
}, 100);
