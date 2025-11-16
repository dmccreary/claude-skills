# Vis-Network MicroSim Generator

## Overview

The vis-network skill creates educational MicroSims using the vis-network JavaScript library for interactive network and graph visualizations. Each MicroSim is a directory in `/docs/sims/` with a main.html file that can be embedded via iframe in educational content.

## Purpose

This skill transforms abstract network and graph concepts into interactive, manipulable experiences that enable students to learn through visual exploration and experimentation. Ideal for visualizing learning graphs, concept dependencies, social networks, organizational structures, and any relationship-based data.

## Key Features

- **Interactive Network Graphs**: Node-link diagrams with physics simulations
- **Concept Dependency Visualization**: Learning graph exploration with search and filtering
- **Educational Focus**: Simplicity, accessibility, and AI-generation compatibility
- **MicroSim Architecture**: Standardized patterns for iframe embedding
- **Browser-Native**: No server-side requirements, universal embedding
- **Responsive Design**: Adapts to container width

## When to Use

Use this skill when users need to:
- Visualize learning graphs and concept dependencies
- Create network diagrams (social networks, organizational charts)
- Show graph structures (trees, DAGs, general graphs)
- Display relationship data (connections, dependencies, hierarchies)
- Build interactive explorable visualizations
- Demonstrate graph algorithms or network analysis

## Common Trigger Phrases

- "Create a network visualization for..."
- "Visualize the learning graph..."
- "Show the concept dependencies as..."
- "Build an interactive graph of..."
- "Display the network structure of..."

## MicroSim Architecture

Educational MicroSims occupy the intersection of:
1. **Simplicity**: Focused scope, transparent code
2. **Accessibility**: Browser-native, universal embedding
3. **AI Generation**: Standardized patterns, prompt-compatible design

## Folder Structure

Each vis-network MicroSim contains:

```
/docs/sims/$MICROSIM_NAME/
├── index.md                # Main documentation with iframe
├── main.html              # Standalone HTML5 file
├── $MICROSIM_NAME.js      # All vis-network JavaScript
└── metadata.json          # Dublin Core metadata
```

## Educational Requirements Specification

Before generating, articulate:

1. **Subject Area and Topic**: What specific concept does this visualization teach?
2. **Grade Level**: Elementary (K-5), Middle School (6-8), High School (9-12), Undergraduate
3. **Learning Objectives**: What should students understand? (Align with Bloom's Taxonomy)
4. **Duration**: Typical engagement time (5-15 minutes recommended)
5. **Prerequisites**: Required prior knowledge
6. **Assessment Opportunities**: How can educators verify learning?

## Network Types Supported

### Learning Graphs (Concept Dependencies)
- **Nodes**: Concepts (abstract units of knowledge)
- **Edges**: Prerequisites (directed dependencies)
- **Structure**: Directed Acyclic Graph (DAG)
- **Use Case**: Optimal teaching order, adaptive learning paths

### Social Networks
- **Nodes**: People, entities
- **Edges**: Relationships, connections
- **Structure**: Undirected or directed graph
- **Use Case**: Communication patterns, influence networks

### Organizational Structures
- **Nodes**: Departments, roles, people
- **Edges**: Reporting relationships, collaborations
- **Structure**: Tree or hierarchical graph
- **Use Case**: Org charts, team structures

### Process Flows
- **Nodes**: Steps, states, activities
- **Edges**: Transitions, dependencies
- **Structure**: Directed graph
- **Use Case**: Workflows, state machines

## vis-network Configuration

### Basic Network Setup

```javascript
var nodes = new vis.DataSet([
    {id: 1, label: 'Node 1', group: 'category1'},
    {id: 2, label: 'Node 2', group: 'category2'}
]);

var edges = new vis.DataSet([
    {from: 1, to: 2, arrows: 'to'}
]);

var container = document.getElementById('network');
var data = {nodes: nodes, edges: edges};

var options = {
    physics: {
        enabled: true,
        stabilization: {iterations: 100}
    },
    layout: {
        hierarchical: {
            enabled: false
        }
    }
};

var network = new vis.Network(container, data, options);
```

### Common Options

**Physics Simulation:**
```javascript
physics: {
    enabled: true,
    barnesHut: {
        gravitationalConstant: -2000,
        centralGravity: 0.3,
        springLength: 95
    }
}
```

**Hierarchical Layout:**
```javascript
layout: {
    hierarchical: {
        enabled: true,
        direction: 'UD',  // Up-Down
        sortMethod: 'directed'
    }
}
```

**Interactive Features:**
```javascript
interaction: {
    dragNodes: true,
    dragView: true,
    zoomView: true,
    selectable: true,
    hover: true
}
```

## Node and Edge Styling

### Node Configuration

```javascript
{
    id: 1,
    label: 'Concept Name',
    group: 'CATEGORY',
    title: 'Hover tooltip text',
    shape: 'dot',  // dot, box, diamond, star
    color: {
        background: '#97C2FC',
        border: '#2B7CE9',
        highlight: {
            background: '#D2E5FF',
            border: '#2B7CE9'
        }
    }
}
```

### Edge Configuration

```javascript
{
    from: 1,
    to: 2,
    arrows: 'to',  // from, to, middle
    color: {color: '#848484'},
    width: 2,
    dashes: false,  // true for dashed lines
    label: 'Edge label'
}
```

## Interactive Features

### Click Events

```javascript
network.on('click', function(params) {
    if (params.nodes.length > 0) {
        var nodeId = params.nodes[0];
        showNodeDetails(nodeId);
    }
});
```

### Hover Tooltips

```javascript
network.on('hoverNode', function(params) {
    var nodeId = params.node;
    // Show additional information
});
```

### Selection Management

```javascript
network.on('select', function(params) {
    var selectedNodes = params.nodes;
    var selectedEdges = params.edges;
    highlightPath(selectedNodes);
});
```

## Learning Graph Specific Features

For learning graphs, implement:

1. **Search Functionality**: Find concepts by name
2. **Filter by Category**: Show only specific concept types
3. **Highlight Dependencies**: Show prerequisite chains
4. **Statistics Display**: Count concepts, dependencies, categories
5. **Export Options**: Download graph data

### Example Search Implementation

```javascript
function searchConcepts(searchTerm) {
    var matchingNodes = nodes.get({
        filter: function(node) {
            return node.label.toLowerCase().includes(searchTerm.toLowerCase());
        }
    });

    network.selectNodes(matchingNodes.map(node => node.id));
    if (matchingNodes.length > 0) {
        network.focus(matchingNodes[0].id, {scale: 1.5, animation: true});
    }
}
```

## Metadata Requirements

`metadata.json` should include:

```json
{
    "title": "Learning Graph Visualization",
    "description": "Interactive network visualization of concept dependencies",
    "creator": "Claude AI with Vis-Network Skill",
    "date": "2025-11-09",
    "type": "Interactive Network Visualization",
    "format": "text/html",
    "subject": "Educational Technology",
    "audience": "Undergraduate",
    "node_count": "198",
    "edge_count": "287",
    "graph_type": "Directed Acyclic Graph",
    "concepts": ["Learning Graph", "Concept Dependencies", "Graph Visualization"],
    "bloom_taxonomy": "Analyze",
    "version": "1.0"
}
```

## Best Practices

### Network Design
1. **Limit Complexity**: Keep under 200 nodes for performance
2. **Use Categories**: Group related nodes with color coding
3. **Clear Labels**: Concise, readable node names
4. **Meaningful Edges**: Show only significant relationships
5. **Interactive Help**: Provide instructions for navigation

### Performance
1. **Physics Stabilization**: Let network stabilize before showing
2. **Clustering**: For large graphs, use vis-network clustering
3. **Level of Detail**: Show/hide details based on zoom level
4. **Lazy Loading**: Load additional data on demand

### Educational Value
1. **Guided Exploration**: Provide questions to focus investigation
2. **Progressive Disclosure**: Start simple, add complexity
3. **Context**: Explain what the network represents
4. **Assessment**: Include comprehension questions

### Accessibility
1. **Keyboard Navigation**: Support arrow keys and tab navigation
2. **Color**: Use color and shape/pattern for categories
3. **Labels**: Ensure readable text size (minimum 12px)
4. **Alternative**: Provide text-based alternative in index.md

## Troubleshooting

### Issue: Network not displaying
**Solution**: Check container has height set, verify data format is correct

### Issue: Nodes overlapping excessively
**Solution**: Adjust physics parameters, increase springLength, enable hierarchical layout

### Issue: Performance slow with many nodes
**Solution**: Disable physics after stabilization, implement clustering, use DataView filtering

### Issue: Layout not hierarchical
**Solution**: Verify graph is DAG (no cycles), enable hierarchical layout, set direction

## Output Files

1. **index.md**: Documentation with iframe embed and usage instructions
2. **main.html**: Standalone HTML5 file with vis-network CDN
3. **[sim-name].js**: All JavaScript code for the visualization
4. **metadata.json**: Dublin Core metadata for the MicroSim

## Integration with Other Skills

**Primary Integrations:**
- **learning-graph-generator**: Visualize the learning graph CSV as interactive network
- **book-chapter-generator**: Show chapter structure as network
- **glossary-generator**: Link nodes to glossary definitions

**Other Integrations:**
- **chapter-content-generator**: Embed network visualizations in content
- **quiz-generator**: Create questions about network structure
- **intelligent-textbook**: Core component for Level 2+ textbooks

## Technical Requirements

- **vis-network.js**: Loaded from CDN
- **Modern Browser**: Chrome, Firefox, Safari, Edge
- **No Server**: Runs entirely client-side
- **Responsive**: Container-based sizing

## Example Use Cases

1. **Learning Graph Viewer**: Interactive exploration of concept dependencies
2. **Course Structure**: Visualize relationships between course topics
3. **Prerequisite Chains**: Show what must be learned before advanced topics
4. **Taxonomy Visualization**: Network of concept categories
5. **Social Learning**: Student collaboration and communication networks

## References

- **vis-network Documentation**: https://visjs.github.io/vis-network/docs/network/
- **vis-network Examples**: https://visjs.github.io/vis-network/examples/
- **Graph Theory**: Basic concepts for network understanding
- **Learning Graphs**: Educational concept dependency frameworks
