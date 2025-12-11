# vis-network MicroSim Skill

A Claude Code skill for generating interactive network diagrams using the [vis-network](https://visjs.github.io/vis-network/docs/network/) JavaScript library, optimized for embedding in educational textbooks.

## Purpose

This skill creates vis-network diagrams designed specifically for **inline embedding within educational textbooks** using iframes. The diagrams are used to visualize:

- Causal loop diagrams (CLDs) for systems thinking
- Network relationships and dependencies
- Concept maps and knowledge graphs
- Workflow and process diagrams
- Organizational structures

## Key Design Principle: No Mouse Zoom/Pan

**All vis-network MicroSims created by this skill disable mouse-based zoom and pan by default.**

### Why?

When a vis-network diagram is embedded in a textbook page via iframe, users need to scroll through the surrounding content. If mouse wheel zoom is enabled on the diagram:

1. **Scroll hijacking**: The mouse wheel zooms the diagram instead of scrolling the page, trapping the user inside the iframe
2. **Touch conflicts**: Pinch-to-zoom and drag gestures interfere with mobile page navigation
3. **User frustration**: Students expect scrolling to move through content, not manipulate embedded diagrams

### The Solution

Instead of mouse controls, all diagrams use **vis-network's built-in navigation buttons**:

```javascript
interaction: {
    zoomView: false,        // Disable mouse wheel zoom
    dragView: false,        // Disable mouse drag to pan
    navigationButtons: true // Enable built-in navigation buttons
}
```

The navigation buttons appear in the corner of the diagram and provide:
- Zoom in (+)
- Zoom out (-)
- Fit to view
- Pan controls (arrow buttons)

### Exception: Fullscreen Mode

The **only** scenario where mouse zoom/pan may be enabled is when the diagram is displayed in fullscreen mode (standalone page, not embedded). In this case, there's no surrounding content to scroll through.

## Usage

This skill generates a complete MicroSim package:

```
/docs/sims/{microsim-name}/
├── index.md           # Documentation with iframe embed
├── main.html          # HTML wrapper with vis-network CDN
├── {microsim-name}.js # vis-network JavaScript code
└── metadata.json      # Dublin Core metadata
```

## Example Interaction Options

```javascript
const options = {
    layout: {
        improvedLayout: false
    },
    physics: {
        enabled: false  // Fixed positions for educational clarity
    },
    interaction: {
        selectConnectedEdges: false,
        zoomView: false,
        dragView: false,
        navigationButtons: true
    },
    nodes: {
        shape: 'box',
        font: { size: 20, face: 'Arial' },
        borderWidth: 2,
        shadow: true
    },
    edges: {
        arrows: { to: { enabled: true } },
        width: 2,
        smooth: { type: 'curvedCW', roundness: 0.4 }
    }
};
```

## Related Resources

- [vis-network Documentation](https://visjs.github.io/vis-network/docs/network/)
- [vis-network Interaction Options](https://visjs.github.io/vis-network/docs/network/interaction.html)
