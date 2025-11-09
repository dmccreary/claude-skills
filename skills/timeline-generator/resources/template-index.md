# {{TIMELINE_TITLE}}

{{TIMELINE_OVERVIEW_TEXT}}

[Run the {{TIMELINE_TITLE}}](./main.html)

[View the Raw Timeline Data](timeline.json)

## Overview

{{DETAILED_DESCRIPTION}}

## Features

### Interactive Elements
- **Zoom and Pan**: Click and drag to pan, scroll to zoom in/out
- **Event Details**: Click any event to see full details below the timeline
- **Hover Tooltips**: Hover over events to see historical context notes
{{CATEGORY_FILTERING_FEATURE}}

### Visual Design
- **Color-coded categories**: Each event category has a distinct color
- **Responsive layout**: Works on desktop, tablet, and mobile devices
- **Legend**: Visual guide showing category colors and meanings

## Data Structure

The timeline data is stored in `timeline.json` following this format:

```json
{
  "title": "Timeline Title",
  "events": [
    {
      "start_date": {
        "year": "2024",
        "month": "1",
        "day": "15",
        "display_date": "January 15, 2024"
      },
      "text": {
        "headline": "Event Title",
        "text": "Detailed description of the event."
      },
      "group": "Category Name",
      "notes": "Additional context that appears in the tooltip."
    }
  ]
}
```

## Customization Guide

### Adding New Events

1. Open `timeline.json`
2. Add a new event object to the `events` array following the structure above
3. Ensure the `year` field is present in `start_date`
4. Assign the event to a category using the `group` field
5. Save and reload the page to see your changes

### Changing Colors

To modify category colors, edit the `categoryColors` object in `main.html`:

```javascript
const categoryColors = {
    'Category1': '#8b0000',
    'Category2': '#1e3a8a',
    'Category3': '#1e5631',
    // Add more categories as needed
};
```

### Adjusting Time Range

To change the zoom limits, modify the `zoomMin` and `zoomMax` options in `main.html`:

```javascript
zoomMin: 1000 * 60 * 60 * 24 * 365 * 10,  // 10 years minimum zoom
zoomMax: 1000 * 60 * 60 * 24 * 365 * 1200, // 1200 years maximum zoom
```

### Modifying Filter Buttons

To add or modify category filter buttons, update the controls section in `main.html`:

```html
<div class="filter-group">
    <label>Filter:</label>
    <button class="filter-btn active" onclick="filterCategory('all')">All Events</button>
    <button class="filter-btn" onclick="filterCategory('YourCategory')">Your Category</button>
</div>
```

## Technical Details

- **Timeline Library**: vis-timeline 7.7.3
- **Data Format**: TimelineJS-compatible JSON
- **Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**:
  - vis-timeline.js (loaded from CDN)
  - vis-timeline.css (loaded from CDN)

## Use Cases

This timeline pattern can be adapted for:
- Historical education and chronological learning
- Project planning and tracking
- Course schedules and curricula
- Organizational history and milestones
- Personal timelines and biographies
- Event sequences and process flows

## References

- [vis-timeline Documentation](https://visjs.github.io/vis-timeline/docs/timeline/)
- [TimelineJS3 Data Format](https://timeline.knightlab.com/docs/json-format.html)
