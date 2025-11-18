// Zoom functionality
let currentZoom = 1;
const zoomStep = 0.2;
const minZoom = 0.5;
const maxZoom = 3;

function zoomIn() {
    if (currentZoom < maxZoom) {
        currentZoom += zoomStep;
        applyZoom();
    }
}

function zoomOut() {
    if (currentZoom > minZoom) {
        currentZoom -= zoomStep;
        applyZoom();
    }
}

function resetZoom() {
    currentZoom = 1;
    applyZoom();
}

function applyZoom() {
    const diagram = document.querySelector('.mermaid');
    if (diagram) {
        diagram.style.transform = `scale(${currentZoom})`;
    }
}

// Export to SVG
function exportSVG() {
    const svg = document.querySelector('.mermaid svg');
    if (!svg) {
        alert('Diagram not found. Please wait for it to load.');
        return;
    }

    // Clone the SVG to avoid modifying the original
    const svgClone = svg.cloneNode(true);

    // Get SVG string
    const serializer = new XMLSerializer();
    const svgString = serializer.serializeToString(svgClone);

    // Create blob and download
    const blob = new Blob([svgString], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.download = 'microsim-file-relationship-diagram.svg';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(url);
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Zoom in: Ctrl/Cmd + Plus
    if ((e.ctrlKey || e.metaKey) && (e.key === '=' || e.key === '+')) {
        e.preventDefault();
        zoomIn();
    }
    // Zoom out: Ctrl/Cmd + Minus
    else if ((e.ctrlKey || e.metaKey) && e.key === '-') {
        e.preventDefault();
        zoomOut();
    }
    // Reset: Ctrl/Cmd + 0
    else if ((e.ctrlKey || e.metaKey) && e.key === '0') {
        e.preventDefault();
        resetZoom();
    }
});

// Track diagram interactions (optional analytics)
function trackInteraction(action) {
    console.log(`MicroSim interaction: ${action}`);
    // Could send to analytics service if needed
}

// Add interaction tracking to buttons
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            trackInteraction(this.textContent);
        });
    });
});

// Accessibility: Announce zoom level to screen readers
function announceZoom() {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = `Zoom level: ${Math.round(currentZoom * 100)}%`;

    document.body.appendChild(announcement);

    setTimeout(() => {
        document.body.removeChild(announcement);
    }, 1000);
}

// Update applyZoom to include announcement
const originalApplyZoom = applyZoom;
applyZoom = function() {
    originalApplyZoom();
    announceZoom();
};
