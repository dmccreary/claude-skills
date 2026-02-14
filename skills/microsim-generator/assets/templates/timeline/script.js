// Timeline Configuration
const categoryColors = {
    'Category1': '#2563eb',
    'Category2': '#16a34a',
    'Category3': '#d97706'
};

// Timeline state
let timeline;
let timelineData;
let allItems = [];

// Scroll Hijacking Rule:
// Keep wheel/drag timeline navigation disabled when embedded in chapter iframes.
// Enable only when explicitly requested via ?enable-interaction=true.
function isInteractionEnabled() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('enable-interaction') === 'true';
}

// Initialize timeline on page load
document.addEventListener('DOMContentLoaded', function() {
    loadTimelineData();
});

// Load data and initialize timeline
function loadTimelineData() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            // Convert JSON data to vis-timeline format
            allItems = data.events.map((event, index) => {
                const year = parseInt(event.start_date.year);
                const month = event.start_date.month ? parseInt(event.start_date.month) - 1 : 0;
                const day = event.start_date.day ? parseInt(event.start_date.day) : 1;

                return {
                    id: index,
                    content: event.text.headline,
                    start: new Date(year, month, day),
                    title: event.notes || event.text.text,
                    category: event.group,
                    description: event.text.text,
                    context: event.notes,
                    style: `background-color: ${categoryColors[event.group]}; color: white; border-color: ${categoryColors[event.group]};`
                };
            });

            // Create DataSet
            timelineData = new vis.DataSet(allItems);

            // Timeline options
            const interactionEnabled = isInteractionEnabled();
            const options = {
                width: '100%',
                height: '400px',
                margin: {
                    item: { horizontal: 50, vertical: 10 },
                    axis: 40
                },
                orientation: 'top',
                zoomMin: 1000 * 60 * 60 * 24 * 365 * 5,     // 5 years
                zoomMax: 1000 * 60 * 60 * 24 * 365 * 100,   // 100 years
                min: new Date(1900, 0, 1),
                max: new Date(2030, 0, 1),
                tooltip: {
                    followMouse: true
                },
                stack: true,
                selectable: true,
                showCurrentTime: false,
                moveable: interactionEnabled,
                zoomable: interactionEnabled,
                align: 'center'
            };

            // Create timeline
            const container = document.getElementById('timeline');
            timeline = new vis.Timeline(container, timelineData, options);

            // Set initial window with padding
            setWindowWithPadding(allItems);

            // Event selection handler
            timeline.on('select', function(properties) {
                if (properties.items.length > 0) {
                    showEventDetails(properties.items[0]);
                }
            });
        })
        .catch(error => {
            console.error('Error loading timeline data:', error);
            document.getElementById('timeline').innerHTML =
                '<p style="color: #dc2626; padding: 40px; text-align: center;">Error loading timeline data.</p>';
        });
}

// Set timeline window with padding around events
function setWindowWithPadding(items) {
    if (items.length === 0) return;

    const dates = items.map(item => item.start.getTime());
    const minDate = Math.min(...dates);
    const maxDate = Math.max(...dates);

    // Add 3 years padding on each side
    const threeYears = 3 * 365 * 24 * 60 * 60 * 1000;
    timeline.setWindow(
        new Date(minDate - threeYears),
        new Date(maxDate + threeYears),
        { animation: false }
    );
}

// Filter events by category
function filterCategory(category) {
    if (category === 'all') {
        timelineData.clear();
        timelineData.add(allItems);
        setWindowWithPadding(allItems);
    } else {
        const filtered = allItems.filter(item => item.category === category);
        timelineData.clear();
        timelineData.add(filtered);
        setWindowWithPadding(filtered);
    }
    document.getElementById('event-details').innerHTML = 'Click an event on the timeline to see details here.';
}

// Display event details in the details panel
function showEventDetails(itemId) {
    const item = allItems.find(i => i.id === itemId);
    if (!item) return;

    const dateStr = item.start.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: item.start.getDate() !== 1 ? 'numeric' : undefined
    });

    let html = `
        <div class="event-title">${item.content}</div>
        <div class="event-date">${dateStr}</div>
        <div class="event-description">${item.description}</div>
    `;

    if (item.context) {
        html += `<div class="event-context">${item.context}</div>`;
    }

    document.getElementById('event-details').innerHTML = html;
}

// Navigation functions
function panLeft() {
    const range = timeline.getWindow();
    const interval = (range.end - range.start) * 0.3;
    timeline.setWindow(range.start - interval, range.end - interval);
}

function panRight() {
    const range = timeline.getWindow();
    const interval = (range.end - range.start) * 0.3;
    timeline.setWindow(range.start + interval, range.end + interval);
}

function zoomIn() {
    const range = timeline.getWindow();
    const center = (range.start.getTime() + range.end.getTime()) / 2;
    const newInterval = (range.end - range.start) * 0.5;
    timeline.setWindow(center - newInterval / 2, center + newInterval / 2);
}

function zoomOut() {
    const range = timeline.getWindow();
    const center = (range.start.getTime() + range.end.getTime()) / 2;
    const newInterval = (range.end - range.start) * 2;
    timeline.setWindow(center - newInterval / 2, center + newInterval / 2);
}

function fitAll() {
    const currentItems = timelineData.get();
    setWindowWithPadding(currentItems);
}
