---
name: timeline-generator
description: This skill generates interactive timeline visualizations using the vis-timeline JavaScript library. Use this skill when users need to create historical timelines, project timelines, event sequences, or any chronological data visualization with optional category filtering. The skill creates a complete MicroSim package with HTML, CSS, JSON data, and documentation.
---

# Timeline Generator

## Overview

This skill generates professional, interactive timeline visualizations using vis-timeline.js. Timelines are ideal for displaying chronological events with rich context including descriptions, notes, and category groupings. The skill creates a complete MicroSim package suitable for embedding in educational content or documentation sites built with MkDocs.

## When to Use This Skill

Use this skill when users request:

- **Historical timelines**: Family histories, organizational milestones, historical periods
- **Project timelines**: Development phases, product roadmaps, release schedules
- **Event sequences**: Course schedules, curriculum timelines, process flows
- **Category-based timelines**: Multi-track timelines with filtering capabilities
- **Interactive visualizations**: Need for hover tooltips, clickable events, zoom/pan navigation

Common trigger phrases:
- "Create a timeline showing..."
- "Visualize the history of..."
- "Build an interactive timeline for..."
- "Show chronological events for..."

## Workflow

### Step 1: Gather Timeline Requirements

Before generating the timeline, collect information about:

1. **Timeline content**:
   - What is the subject/title of the timeline?
   - What time period does it cover?
   - What are the specific events to display?

2. **Event data** (for each event):
   - Event headline/title (required)
   - Date (year, month, day - year is required)
   - Description text (required)
   - Category/group (optional, for filtering)
   - Historical context notes (optional, for tooltips)

3. **Category filtering**:
   - Ask: "Would you like category filter buttons in the viewer?"
   - If yes, gather category names and colors
   - If not provided, create logical categories from the event data

4. **Integration context**:
   - Standalone page
   - Embedded in MkDocs documentation
   - Part of educational content

**IMPORTANT**: If the user has not provided a specific event list, prompt them:
> "I'll create an interactive timeline for you. Please provide the events you'd like to include with:
> - Event title/headline
> - Date (at least the year)
> - Description
> - Category (optional)
> - Any additional context notes for tooltips (optional)
>
> Would you also like category filter buttons to allow viewing specific types of events?"

### Step 2: Create Directory Structure

Create a new directory for the MicroSim following this pattern:

```
docs/sims/<timeline-name>/
├── main.html         # Main visualization file
├── style.css         # External stylesheet
├── timeline.json     # Event data in TimelineJS format
└── index.md          # Documentation (if part of MkDocs)
```

**Naming convention**: Use kebab-case (lowercase with hyphens) for directory names that are descriptive and URL-friendly (e.g., `project-history-timeline`, `course-schedule`, `family-heritage-timeline`).

### Step 3: Create timeline.json Data File

Generate a JSON file following this structure:

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

**Key data structure notes**:
- `year` is required in `start_date`
- `month` and `day` are optional (default to 1 if omitted)
- `display_date` is optional (for custom date formatting)
- `group` is the category used for filtering
- `notes` provides tooltip/hover text with additional context
- All text fields support basic HTML formatting

**Data preparation guidelines**:
1. Sort events chronologically (oldest to newest)
2. Use consistent category names across related events
3. Keep headlines concise (5-10 words)
4. Provide substantive descriptions (2-4 sentences)
5. Add historical context in notes for educational value

### Step 4: Create style.css External Stylesheet

Create an external CSS file for styling. Use the template at `resources/template-style.css` as the base.

**Key CSS features**:
- Clean, minimal design with `aliceblue` background
- Responsive layout with grid-based info panel
- Category filter buttons with distinct colors
- Properly styled vis-timeline tooltips with text wrapping
- Event details panel with context highlighting

**Template placeholders in style.css**:
- `{{FILTER_BUTTON_STYLES}}`: CSS rules for category-specific filter button colors

**Critical tooltip styling** (ensures text wraps properly):

```css
.vis-tooltip {
    background: #2c3e50 !important;
    color: white !important;
    padding: 10px 15px !important;
    border-radius: 8px !important;
    font-size: 13px !important;
    max-width: 300px !important;
    line-height: 1.4 !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    white-space: normal !important;
    box-sizing: border-box !important;
}

.vis-tooltip div {
    max-width: 280px !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    white-space: normal !important;
}
```

### Step 5: Create main.html with vis-timeline

Generate the main HTML file using the template at `resources/template-main.html`.

**Key structure**:
1. **HTML boilerplate** with proper meta tags
2. **vis-timeline CDN imports** and external style.css link
3. **Styled header** with timeline title and subtitle
4. **Category filter controls** (if requested)
5. **Timeline container** div
6. **Instructions text** for user guidance
7. **Info panel** with legend and event details
8. **JavaScript implementation**

**Template placeholders in main.html**:
- `{{TIMELINE_TITLE}}`: The main title of the timeline
- `{{TIMELINE_SUBTITLE}}`: Descriptive subtitle with date range
- `{{FILTER_BUTTONS}}`: HTML for category filter buttons
- `{{LEGEND_ITEMS}}`: HTML for legend color/label pairs
- `{{CATEGORY_COLORS}}`: JavaScript object mapping categories to colors
- `{{ZOOM_MIN_YEARS}}`: Minimum zoom level in years (e.g., 10)
- `{{ZOOM_MAX_YEARS}}`: Maximum zoom level in years (e.g., 1000)
- `{{MIN_YEAR}}`: Earliest year the timeline can pan to
- `{{MAX_YEAR}}`: Latest year the timeline can pan to

**Key vis-timeline configuration**:

```javascript
// Timeline options - important settings
// Note: See "Event Text Clipped at Edges" in Troubleshooting for edge clipping fixes
const options = {
    width: '100%',
    height: '400px',
    margin: {
        item: { horizontal: 50, vertical: 10 },  // Explicit horizontal margin for edge padding
        axis: 40
    },
    orientation: 'top',
    zoomMin: 1000 * 60 * 60 * 24 * 365 * 5,    // 5 years minimum zoom
    zoomMax: 1000 * 60 * 60 * 24 * 365 * 50,   // 50 years maximum zoom
    min: new Date(1500, 0, 1),  // Earliest panning limit
    max: new Date(2030, 0, 1),  // Latest panning limit
    tooltip: {
        followMouse: true
    },
    stack: true,
    selectable: true,
    showCurrentTime: false,
    moveable: true,   // Enable click-and-drag panning
    zoomable: false,  // Disable scroll-wheel zoom (use buttons instead to avoid page scroll interference)
    align: 'center'   // Center items on their date point to reduce edge overflow
};
```

**Navigation controls**: Since scroll-wheel zoom is disabled to prevent interference with page scrolling, the template includes explicit zoom/pan buttons:
- **◀ / ▶**: Pan left/right by 30% of visible range
- **+ / −**: Zoom in/out by 50%/200%
- **Fit All**: Reset to show all events with 2-year padding

**Important implementation features**:

1. **Category filtering**: Filter button implementation
   ```javascript
   function filterCategory(category) {
       if (category === 'all') {
           timelineData.clear();
           timelineData.add(allItems);
       } else {
           const filtered = allItems.filter(item => item.category === category);
           timelineData.clear();
           timelineData.add(filtered);
       }
       timeline.fit();
   }
   ```

2. **Event detail display**: Show full event information on click
   ```javascript
   timeline.on('select', function(properties) {
       if (properties.items.length > 0) {
           showEventDetails(properties.items[0]);
       }
   });
   ```

3. **Color-coded events**: Apply category colors to timeline items
4. **Responsive tooltips**: Show context notes on hover
5. **Legend display**: Visual guide for category colors

**Design considerations**:
- Use a professional color scheme (distinct, accessible colors)
- Provide clear visual hierarchy
- Ensure text readability against colored backgrounds
- Include hover effects for interactivity
- Make the layout responsive for different screen sizes

### Step 6: Create index.md Documentation

If the timeline is part of a MkDocs site, create comprehensive documentation:

```markdown
# [Timeline Title]

[Brief description of what this timeline visualizes]

[Run the [Timeline Name]](./main.html)

[View the Raw Timeline Data](timeline.json)

## Overview

[Detailed explanation of the timeline's purpose, content, and coverage]

## Features

### Interactive Elements
- **Zoom and Pan**: Click and drag to pan, scroll to zoom in/out
- **Event Details**: Click any event to see full details below the timeline
- **Hover Tooltips**: Hover over events to see historical context notes
- **Category Filtering**: Use filter buttons to view specific event categories

### Visual Design
- **Color-coded categories**: Each event category has a distinct color
- **Responsive layout**: Works on desktop, tablet, and mobile devices
- **Legend**: Visual guide showing category colors and meanings

## Data Structure

The timeline data is stored in `timeline.json` following this format:

[Include JSON structure example]

## Customization Guide

### Adding New Events

1. Open `timeline.json`
2. Add a new event object to the `events` array
3. Reload the page to see your changes

### Changing Colors

To modify category colors, edit the `categoryColors` object in `main.html`:

[Code example]

### Adjusting Time Range

To change the zoom limits, modify the `zoomMin` and `zoomMax` options:

[Code example]

## Technical Details

- **Timeline Library**: vis-timeline 7.7.3
- **Data Format**: TimelineJS-compatible JSON
- **Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: vis-timeline.js (loaded from CDN)

## Use Cases

This timeline pattern can be adapted for:
- Historical education
- Project planning and tracking
- Course schedules and curricula
- Organizational history
- Personal timelines and biographies
```

**Documentation best practices**:
1. Provide clear usage instructions
2. Include code examples for common customizations
3. Explain the data format thoroughly
4. Link to external resources (vis-timeline docs)
5. Suggest related use cases

### Step 7: Integrate into Navigation (MkDocs)

If using MkDocs, add the timeline to the navigation in `mkdocs.yml`:

```yaml
nav:
  - MicroSims:
      - Introduction: sims/index.md
      - [Timeline Name]: sims/[timeline-name]/index.md
      - [Other sims...]: ...
```

Place the entry in a logical position based on:
- Related content (group similar visualizations)
- Alphabetical order
- Chronological order of creation

### Step 8: Test and Validate

Before considering the timeline complete:

1. **Data validation**:
   - Verify timeline.json is valid JSON
   - Check all dates parse correctly
   - Confirm all events have required fields
   - Validate category names are consistent

2. **Visual testing**:
   - Open `main.html` directly in browser
   - Test with `mkdocs serve` if applicable
   - Check timeline spans entire date range
   - Verify all events are visible and properly spaced
   - Test on different screen sizes

3. **Interactive testing**:
   - Zoom in/out to verify scale limits
   - Pan across the full timeline
   - Hover over events to check tooltips
   - Click events to verify detail display
   - Test category filter buttons (if present)
   - Check "All Events" filter restores full view

4. **Content review**:
   - Proofread all event text
   - Verify historical accuracy
   - Check that context notes provide value
   - Ensure descriptions are complete

5. **Browser compatibility**:
   - Test on Chrome, Firefox, Safari, Edge
   - Verify CDN resources load correctly
   - Check console for JavaScript errors

### Step 9: Get a Screen Image

Use the shell script bk-capture-screenshot
To use this you must pass a path to the microsim directory as the parameter:
Example `bk-capture-screenshot docs/sims/[timeline-name]`
This will create a png file in that directory with the file name of the directory:

`docs/sims/[timeline-name]/[timeline-name].png`

This is what will be references in the YML metadata in the index.md file

### Step 9: Update the Social Image Preview Metadata in the index.md

In the main microsim index.md file we will insert metadata required
for social media preview images.

docs/sims/[timeline-name]/index.md

```markdown
---
title: [Timeline Name]
description: [Timeline Description]
image: /sims/[timeline-name]/[timeline-name].png
og:image: /sims/[timeline-name]/[timeline-name].png
---
# [Timeline Name]:
```

## Best Practices

### Data Preparation

1. **Date accuracy**: Use precise dates when available
2. **Chronological order**: Sort events in JSON for easier maintenance
3. **Consistent categories**: Use standardized category names
4. **Rich context**: Provide substantive descriptions and notes
5. **Source validation**: Verify historical facts and dates

### Category Design

1. **Limit categories**: 3-6 categories works best for filtering
2. **Meaningful groupings**: Categories should reflect natural divisions
3. **Balanced distribution**: Aim for relatively even event distribution
4. **Clear naming**: Use descriptive, non-overlapping category names
5. **Color accessibility**: Choose colors with sufficient contrast

### Visual Design

1. **Color coding**: Use distinct, visually appealing colors
2. **Text readability**: Ensure white text on colored backgrounds is clear
3. **Legend placement**: Make the legend visible and understandable
4. **Responsive sizing**: Timeline should work on all screen sizes
5. **Loading states**: Consider showing a loading indicator

### Documentation

1. **Usage examples**: Show how to interact with the timeline
2. **Data format**: Clearly document the JSON structure
3. **Customization**: Provide code snippets for common changes
4. **Attribution**: Credit data sources when appropriate
5. **Educational context**: Explain why the timeline matters

### MkDocs Integration

1. **Direct linking**: Provide links to both main.html and timeline.json
2. **Iframe embedding**: Can use iframe for inline display if desired
3. **Navigation placement**: Group with related content
4. **Cross-references**: Link to related pages or timelines

## Common Variations

### Simple Timeline (No Categories)

Omit the category filtering UI and use a single color:

```javascript
const categoryColors = {
    'Default': '#2d5016'
};
```

### Vertical Timeline

Change orientation for a vertical layout:

```javascript
options: {
    orientation: 'left'  // or 'right'
}
```

### Range Events

For events with duration, add an `end_date`:

```json
{
  "start_date": {"year": "2020", "month": "1"},
  "end_date": {"year": "2021", "month": "12"},
  "text": {"headline": "Multi-year Project"}
}
```

### Embedded Media

Add images or videos to events (requires additional configuration).

## Troubleshooting

### Timeline Not Displaying
**Solution**: Check browser console for errors, verify timeline.json loads correctly, ensure CDN resources are accessible.

### Events Overlapping
**Solution**: Increase `margin.item` value in options or enable `stack: true` for automatic vertical stacking.

### Zoom Too Fast/Slow
**Solution**: Adjust `zoomMin` and `zoomMax` values based on your date range.

### Filter Buttons Not Working
**Solution**: Verify category names match exactly between JSON data and filter buttons, check JavaScript console for errors.

### Dates Parsing Incorrectly
**Solution**: Ensure month values are 1-12, not 0-11. The conversion to JavaScript Date handles this in the code.

### Event Text Clipped at Edges (IMPORTANT)

**Problem**: vis-timeline clips event boxes when they extend beyond the visible date range. Events near the left or right edges appear cut off, especially when using `timeline.fit()`.

**Root Cause**: vis-timeline's default `overflow: hidden` behavior clips content at container boundaries.

**Solution**: Apply a three-part fix combining CSS and JavaScript:

**Part 1 - CSS Container Padding and Overflow (in style.css)**:
```css
/* Timeline Container - add padding for edge events */
#timeline {
    padding-left: 80px;
    padding-right: 80px;
    overflow: hidden;
}

/* Override vis-timeline's default clipping behavior */
.vis-timeline {
    overflow: visible !important;
}

.vis-panel.vis-center {
    overflow: visible !important;
}

.vis-item .vis-item-overflow {
    overflow: visible !important;
}
```

**Part 2 - JavaScript Options (in main.html)**:
```javascript
const options = {
    // ... other options ...
    margin: {
        item: { horizontal: 50, vertical: 10 },  // Explicit horizontal margin
        axis: 40
    },
    align: 'center',        // Center items on their date point
    zoomable: false         // Disable scroll-wheel zoom (use buttons instead)
};
```

**Part 3 - Window Padding Instead of fit() (in main.html)**:
```javascript
// DON'T use: timeline.fit();
// INSTEAD, calculate padded window manually:
const dates = allItems.map(item => item.start.getTime());
const minDate = Math.min(...dates);
const maxDate = Math.max(...dates);

// Add 2 years padding on each side
const twoYears = 2 * 365 * 24 * 60 * 60 * 1000;
timeline.setWindow(
    new Date(minDate - twoYears),
    new Date(maxDate + twoYears),
    { animation: false }
);
```

**Note**: The same padding logic must be applied in the `filterCategory()` and `fitAll()` functions to maintain consistency when filtering or resetting the view.

## References

This skill uses the following assets and references:

### Assets
- **vis-timeline CDN** (standalone build - the old graph2d build is deprecated):
  - JS: `https://unpkg.com/vis-timeline/standalone/umd/vis-timeline-graph2d.min.js`
  - CSS: `https://unpkg.com/vis-timeline/standalone/umd/vis-timeline-graph2d.min.css`
- No local assets required (vis-timeline loaded from CDN)

### References
- [vis-timeline Documentation](https://visjs.github.io/vis-timeline/docs/timeline/)
- [TimelineJS3 Data Format](https://timeline.knightlab.com/docs/json-format.html) (compatible structure)
- [vis-timeline GitHub Repository](https://github.com/visjs/vis-timeline)

### Example Implementation
See the timeline example at `/docs/sims/timeline/` for a complete reference implementation showcasing McCreary family heritage timeline.

## License

This skill is provided under the same license as the claude-skills repository. The vis-timeline library is licensed under Apache-2.0/MIT dual license.
