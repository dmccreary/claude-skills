/**
 * Mermaid Diagram Interactive Features
 *
 * This file provides additional interactive functionality for the Mermaid diagram.
 * Mermaid.js handles the core diagram rendering automatically.
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Mermaid diagram loaded successfully');

    // Add zoom controls if needed
    addZoomControls();

    // Add export functionality if needed
    addExportButton();

    // Track diagram interactions
    trackDiagramInteractions();
});

/**
 * Add zoom controls to the diagram
 */
function addZoomControls() {
    const diagramContainer = document.querySelector('.diagram-container');

    // Create zoom controls container
    const zoomControls = document.createElement('div');
    zoomControls.className = 'zoom-controls';
    zoomControls.innerHTML = `
        <button id="zoom-in" title="Zoom In">+</button>
        <button id="zoom-reset" title="Reset Zoom">⟲</button>
        <button id="zoom-out" title="Zoom Out">−</button>
    `;

    // Add minimal styling
    zoomControls.style.cssText = `
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        gap: 5px;
        z-index: 1000;
    `;

    const buttons = zoomControls.querySelectorAll('button');
    buttons.forEach(button => {
        button.style.cssText = `
            width: 32px;
            height: 32px;
            border: 1px solid #ddd;
            background: white;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px;
            transition: all 0.2s;
        `;
        button.addEventListener('mouseenter', () => {
            button.style.background = '#f0f0f0';
        });
        button.addEventListener('mouseleave', () => {
            button.style.background = 'white';
        });
    });

    // Make container relative for positioning
    if (diagramContainer) {
        diagramContainer.style.position = 'relative';
        diagramContainer.appendChild(zoomControls);

        let currentZoom = 1;
        const zoomStep = 0.1;

        document.getElementById('zoom-in')?.addEventListener('click', () => {
            currentZoom += zoomStep;
            applyZoom(currentZoom);
        });

        document.getElementById('zoom-out')?.addEventListener('click', () => {
            currentZoom = Math.max(0.5, currentZoom - zoomStep);
            applyZoom(currentZoom);
        });

        document.getElementById('zoom-reset')?.addEventListener('click', () => {
            currentZoom = 1;
            applyZoom(currentZoom);
        });

        function applyZoom(zoom) {
            const svg = document.querySelector('.mermaid svg');
            if (svg) {
                svg.style.transform = `scale(${zoom})`;
                svg.style.transformOrigin = 'center center';
                svg.style.transition = 'transform 0.2s';
            }
        }
    }
}

/**
 * Add export button to download diagram as SVG or PNG
 */
function addExportButton() {
    const diagramContainer = document.querySelector('.diagram-container');

    if (!diagramContainer) return;

    const exportButton = document.createElement('button');
    exportButton.textContent = 'Export SVG';
    exportButton.style.cssText = `
        position: absolute;
        bottom: 10px;
        right: 10px;
        padding: 8px 16px;
        background: #667eea;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        transition: background 0.2s;
        z-index: 1000;
    `;

    exportButton.addEventListener('mouseenter', () => {
        exportButton.style.background = '#764ba2';
    });

    exportButton.addEventListener('mouseleave', () => {
        exportButton.style.background = '#667eea';
    });

    exportButton.addEventListener('click', () => {
        const svg = document.querySelector('.mermaid svg');
        if (svg) {
            const svgData = new XMLSerializer().serializeToString(svg);
            const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
            const svgUrl = URL.createObjectURL(svgBlob);
            const downloadLink = document.createElement('a');
            downloadLink.href = svgUrl;
            downloadLink.download = 'diagram.svg';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
            URL.revokeObjectURL(svgUrl);
        }
    });

    diagramContainer.appendChild(exportButton);
}

/**
 * Track user interactions with the diagram
 */
function trackDiagramInteractions() {
    const diagram = document.querySelector('.mermaid');

    if (!diagram) return;

    // Track clicks on diagram nodes
    diagram.addEventListener('click', (event) => {
        const target = event.target;

        // Check if user clicked on a node
        if (target.closest('.node')) {
            const nodeText = target.textContent || target.innerText;
            console.log('Node clicked:', nodeText.trim());

            // Optional: Add visual feedback
            highlightNode(target);
        }
    });
}

/**
 * Highlight a node when clicked
 */
function highlightNode(element) {
    const nodeElement = element.closest('.node');
    if (!nodeElement) return;

    // Remove previous highlights
    document.querySelectorAll('.node-highlight').forEach(el => {
        el.classList.remove('node-highlight');
    });

    // Add highlight class
    nodeElement.classList.add('node-highlight');

    // Add temporary highlight styling
    const originalOpacity = nodeElement.style.opacity;
    nodeElement.style.transition = 'opacity 0.3s';
    nodeElement.style.opacity = '0.7';

    setTimeout(() => {
        nodeElement.style.opacity = originalOpacity;
    }, 300);
}
