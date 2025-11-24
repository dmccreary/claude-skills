// Book Build Workflow - Interactive Features

// Initialize Mermaid
mermaid.initialize({
    startOnLoad: true,
    theme: 'default',
    flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
    }
});

// Create tooltip element
let tooltip = null;

function createTooltip() {
    tooltip = document.createElement('div');
    tooltip.className = 'custom-tooltip';
    document.body.appendChild(tooltip);
}

function showTooltip(text, targetElement) {
    if (!tooltip) createTooltip();

    tooltip.textContent = text;
    tooltip.classList.remove('flipped'); // Reset flip state
    tooltip.classList.add('visible');

    // Force layout recalculation to get accurate dimensions
    tooltip.offsetHeight;

    // Position tooltip to the right of the element
    const rect = targetElement.getBoundingClientRect();
    const tooltipRect = tooltip.getBoundingClientRect();

    // Always try to position to the right first with some spacing
    let left = rect.right + 20;
    let top = rect.top + (rect.height / 2) - (tooltipRect.height / 2);

    // Check if tooltip goes off-screen to the right
    const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
    const rightEdge = left + tooltipRect.width;

    // Only flip to left if it goes off-screen AND there's more room on the left
    if (rightEdge > viewportWidth - 20 && rect.left > tooltipRect.width + 40) {
        left = rect.left - tooltipRect.width - 20;
        tooltip.classList.add('flipped');
    }
    // If no room on either side, keep it to the right but adjust left position
    else if (rightEdge > viewportWidth - 20) {
        left = viewportWidth - tooltipRect.width - 20;
    }

    // Ensure left edge stays on screen
    if (left < 20) left = 20;

    // Adjust if tooltip goes off-screen vertically
    if (top < 20) top = 20;
    if (top + tooltipRect.height > window.innerHeight - 20) {
        top = window.innerHeight - tooltipRect.height - 20;
    }

    tooltip.style.left = left + 'px';
    tooltip.style.top = top + 'px';
}

function hideTooltip() {
    if (tooltip) {
        tooltip.classList.remove('visible');
    }
}

// Tooltip definitions for each node
const tooltips = {
    'Course Description': 'Run the course-description-analyzer skill to get a quality score',
    'Learning Graph': 'Run the learning-graph-generator skill to generate the learning graph',
    'Chapter Structure': 'Run the book-chapter-generator skill to partition the graph into chapters',
    'Chapter 1': 'Run the chapter-content-generator skill to generate content for chapter 1',
    'Chapter 2': 'Run the chapter-content-generator skill to generate content for chapter 2',
    'Content Complete': 'This is the state when all chapters have been generated',
    'Glossary': 'Run the glossary-generator skill',
    'FAQ': 'Run the faq-generator skill',
    'Quizzes': 'Run the quiz-generator skill',
    'References': 'Run the reference-generator skill',
    'Diagrams': 'Run microsim-matcher on each diagram details description and try the best match',
    'Book Metrics': 'Run the book-metrics-generator shell scripts'
};

// Add tooltips to nodes after Mermaid renders
document.addEventListener('DOMContentLoaded', () => {
    // Use MutationObserver to detect when Mermaid finishes rendering
    const observer = new MutationObserver((mutations, obs) => {
        const svgElement = document.querySelector('.mermaid svg');
        if (svgElement) {
            obs.disconnect(); // Stop observing once we find the SVG
            addTooltips();
        }
    });

    observer.observe(document.getElementById('diagram-container'), {
        childList: true,
        subtree: true
    });

    // Fallback timeout in case observer doesn't trigger
    setTimeout(addTooltips, 2000);
});

function addTooltips() {
    // Try multiple selectors for Mermaid nodes
    const nodes = document.querySelectorAll('.nodeLabel, .node, g.node, g[class*="flowchart"]');

    console.log(`Found ${nodes.length} potential nodes`);

    nodes.forEach(node => {
        // Try to find text in various ways
        let labelElement = node.querySelector('text');
        if (!labelElement) {
            labelElement = node.querySelector('.nodeLabel');
        }
        if (!labelElement && node.tagName === 'text') {
            labelElement = node;
        }

        if (labelElement) {
            const label = labelElement.textContent.trim();
            console.log(`Node label: "${label}"`);

            // Add tooltip if it exists for this label
            if (tooltips[label]) {
                // Find the parent group or rect to attach tooltip
                const targetElement = node.closest('g') || node;
                const rect = targetElement.querySelector('rect') || targetElement;

                // Add aria-label for accessibility
                targetElement.setAttribute('aria-label', `${label}: ${tooltips[label]}`);

                // Visual indicator that tooltip exists (add pointer cursor)
                rect.style.cursor = 'help';
                targetElement.style.cursor = 'help';

                // Add mouse events for custom tooltip
                targetElement.addEventListener('mouseenter', () => {
                    showTooltip(tooltips[label], targetElement);
                });

                targetElement.addEventListener('mouseleave', () => {
                    hideTooltip();
                });

                // Add keyboard navigation support
                targetElement.setAttribute('tabindex', '0');
                targetElement.addEventListener('focus', () => {
                    showTooltip(tooltips[label], targetElement);
                });

                targetElement.addEventListener('blur', () => {
                    hideTooltip();
                });

                targetElement.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                        console.log(`Node selected: ${label}`);
                    }
                });

                console.log(`Added tooltip for: ${label}`);
            }
        }
    });
}
