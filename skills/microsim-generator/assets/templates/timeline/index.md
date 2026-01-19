# Timeline Template

An interactive timeline visualization for displaying chronological events with category 
filtering and detailed event information accessible by hovering over an event.

<iframe src="./main.html" width="100%" height="500px" scrolling="no"></iframe>

[View the Timeline Fullscreen](./main.html){ .md-button .md-button--primary }

## Overview

This template creates an interactive vis-timeline visualization with:

- **Category Filtering**: Filter events by type using color-coded buttons
- **Navigation Controls**: Pan left/right, zoom in/out, and fit all events
- **Event Details Panel**: Click any event to see full description and context
- **Hover Tooltips**: Quick context notes on hover
- **Responsive Design**: Works on desktop and mobile devices

## Features

### Interactive Elements

- **Filter Buttons**: Show all events or filter by category
- **Navigation**: Zoom and pan through the timeline
- **Selection**: Click events for detailed information
- **Tooltips**: Hover for quick context

### Visual Design

- **Light Theme**: Aliceblue background with high contrast
- **Color-coded Categories**: Distinct colors for each event type
- **Legend Panel**: Reference for category colors
- **Clean Typography**: System fonts for readability

## Customization Guide

### 1. Update the Title and Categories

In `main.html`, update:

```html
<header class="header">
    <h1>Your Timeline Title</h1>
    <p>Your subtitle with date range</p>
</header>
```

Update filter buttons to match your categories:

```html
<button class="filter-btn category1" onclick="filterCategory('YourCategory1')">Your Category 1</button>
```

### 2. Configure Category Colors

In `script.js`, update the `categoryColors` object:

```javascript
const categoryColors = {
    'YourCategory1': '#2563eb',  // Blue
    'YourCategory2': '#16a34a',  // Green
    'YourCategory3': '#d97706'   // Amber
};
```

### 3. Update the Legend

In `main.html` and `style.css`, update legend items to match your categories.

### 4. Adjust Timeline Range

In `script.js`, modify the timeline options:

```javascript
min: new Date(1900, 0, 1),  // Start date
max: new Date(2030, 0, 1),  // End date
zoomMin: 1000 * 60 * 60 * 24 * 365 * 5,   // Minimum zoom (5 years)
zoomMax: 1000 * 60 * 60 * 24 * 365 * 100, // Maximum zoom (100 years)
```

### 5. Update CSS Colors

In `style.css`, update the category button and legend colors:

```css
.filter-btn.category1 { background: #2563eb; }
.legend-color.category1 { background: #2563eb; }
```

## Data Format

Events are stored in `data.json` with this structure:

```json
{
  "title": "Timeline Title",
  "events": [
    {
      "start_date": {
        "year": "1950",
        "month": "1",    // Optional (1-12)
        "day": "15"      // Optional (1-31)
      },
      "text": {
        "headline": "Event Title",
        "text": "Full description of the event."
      },
      "group": "Category1",  // Must match categoryColors key
      "notes": "Additional context for tooltips."
    }
  ]
}
```

### Date Handling

- **Year only**: Defaults to January 1st
- **Year + Month**: Defaults to 1st of that month
- **Full date**: Uses exact date specified

## Adding New Events

1. Open `data.json`
2. Add a new event object to the `events` array
3. Ensure `group` matches a key in `categoryColors`
4. Reload the page

## Technical Details

- **Library**: vis-timeline 7.7.3
- **Data Format**: Custom JSON loaded via fetch()
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

## File Structure

```
timeline/
├── main.html      # HTML structure
├── script.js      # JavaScript logic and configuration
├── style.css      # All styling and responsive design
├── data.json      # Timeline event data
└── index.md       # Documentation (this file)
```
