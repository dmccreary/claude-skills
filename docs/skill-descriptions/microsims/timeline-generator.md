# Timeline Generator

## Overview

The timeline-generator skill creates professional, interactive timeline visualizations using vis-timeline.js library. It generates complete MicroSim packages with HTML, CSS, JSON data, and documentation suitable for displaying chronological events with rich context including descriptions, notes, and category filtering.

## Purpose

This skill automates the creation of interactive timelines for historical events, project schedules, course timelines, or any chronological data visualization with optional category-based filtering capabilities.

## Key Features

- **Interactive Timelines**: Zoom, pan, click events for details
- **Category Filtering**: Optional filter buttons to view specific event types
- **Hover Tooltips**: Show contextual notes on event hover
- **Event Details Panel**: Display full event information on selection
- **Color-Coded Categories**: Visual distinction for different event types
- **Responsive Design**: Works on desktop, tablet, and mobile
- **TimelineJS Format**: Standard JSON data structure

## When to Use

Use this skill when users request:
- Historical timelines (family histories, organizational milestones, historical periods)
- Project timelines (development phases, product roadmaps, release schedules)
- Event sequences (course schedules, curriculum timelines, process flows)
- Category-based timelines (multi-track timelines with filtering)
- Interactive visualizations (hover tooltips, clickable events, zoom/pan navigation)

## Common Trigger Phrases

- "Create a timeline showing..."
- "Visualize the history of..."
- "Build an interactive timeline for..."
- "Show chronological events for..."

## Workflow Steps

### Step 1: Gather Timeline Requirements
Collect information about:
- Timeline subject/title and time period covered
- Specific events to display with dates
- Event data (headline, date, description, category, context notes)
- Category filtering preference
- Integration context (standalone or embedded)

### Step 2: Create Directory Structure
```
docs/sims/<timeline-name>/
├── main.html         # Main visualization file
├── timeline.json     # Event data in TimelineJS format
└── index.md          # Documentation (if part of MkDocs)
```

Naming: Use kebab-case (e.g., `project-history-timeline`, `course-schedule`)

### Step 3: Create timeline.json Data File

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

**Key data structure notes:**
- `year` is required in `start_date`
- `month` and `day` are optional (default to 1)
- `display_date` is optional for custom formatting
- `group` is the category used for filtering
- `notes` provides tooltip/hover text
- All text fields support basic HTML

### Step 4: Create main.html with vis-timeline

Generate HTML with:
1. vis-timeline CDN imports (JS and CSS)
2. Styled header with title and subtitle
3. Category filter controls (if requested)
4. Timeline container div
5. Info panel with legend and event details
6. JavaScript implementation

**Key vis-timeline configuration:**

```javascript
// Color scheme for categories
const categoryColors = {
    'Category 1': '#color1',
    'Category 2': '#color2'
};

// Convert JSON events to vis-timeline format
allItems = data.events.map((event, index) => {
    const year = event.start_date.year;
    const month = event.start_date.month || 1;
    const day = event.start_date.day || 1;
    const startDate = new Date(parseInt(year), month - 1, day);

    return {
        id: `event-${index}`,
        content: event.text.headline,
        start: startDate,
        title: event.notes || event.text.headline,
        style: `background-color: ${categoryColors[event.group]}; color: white;`,
        category: event.group,
        eventData: event
    };
});

// Timeline options
const options = {
    width: '100%',
    height: '600px',
    margin: { item: 20, axis: 40 },
    orientation: 'top',
    zoomMin: 1000 * 60 * 60 * 24 * 365 * 10,  // 10 years
    zoomMax: 1000 * 60 * 60 * 24 * 365 * 1200, // 1200 years
    selectable: true,
    stack: true
};
```

### Step 5: Create index.md Documentation

Include:
- Brief description of timeline
- Links to main.html and timeline.json
- Overview of content and coverage
- Features list (interactive elements, visual design)
- Data structure example
- Customization guide
- Technical details
- Use cases

### Step 6: Integrate into Navigation (MkDocs)

Add to `mkdocs.yml`:

```yaml
nav:
  - MicroSims:
      - Timeline Name: sims/[timeline-name]/index.md
```

### Step 7: Test and Validate

1. **Data validation**: Verify JSON, check dates parse correctly
2. **Visual testing**: Open main.html, test with mkdocs serve
3. **Interactive testing**: Zoom, pan, hover, click, filter
4. **Content review**: Proofread text, verify historical accuracy
5. **Browser compatibility**: Test on Chrome, Firefox, Safari, Edge

## Timeline Components

### Category Filter Implementation

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

### Event Detail Display

```javascript
timeline.on('select', function(properties) {
    if (properties.items.length > 0) {
        showEventDetails(properties.items[0]);
    }
});
```

### Features

- **Color-coded events**: Apply category colors
- **Responsive tooltips**: Show context notes on hover
- **Legend display**: Visual guide for category colors

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

## Common Variations

### Simple Timeline (No Categories)
Omit category filtering UI and use a single color

### Vertical Timeline
Change orientation for vertical layout:
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

## Troubleshooting

### Timeline Not Displaying
**Solution**: Check browser console for errors, verify timeline.json loads, ensure CDN resources accessible

### Events Overlapping
**Solution**: Increase `margin.item` value or enable `stack: true`

### Zoom Too Fast/Slow
**Solution**: Adjust `zoomMin` and `zoomMax` values based on date range

### Filter Buttons Not Working
**Solution**: Verify category names match exactly, check JavaScript console

### Dates Parsing Incorrectly
**Solution**: Ensure month values are 1-12, not 0-11

## Output Structure

Generated timeline package includes:
- `main.html`: Standalone interactive timeline
- `timeline.json`: Event data in TimelineJS-compatible format
- `index.md`: MkDocs integration page with documentation

## Technical Details

- **Timeline Library**: vis-timeline 7.7.3
- **Data Format**: TimelineJS-compatible JSON
- **Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: vis-timeline.js loaded from CDN

## Use Cases

- Historical education
- Project planning and tracking
- Course schedules and curricula
- Organizational history
- Personal timelines and biographies
- Event sequences and process flows

## Integration with Other Skills

- **learning-graph-generator**: Visualize concept development over time
- **chapter-content-generator**: Embed timelines in chapter content
- **microsim-p5**: Use timelines for static chronology, p5.js for dynamic simulations
- **quiz-generator**: Create questions about historical sequences
- **glossary-generator**: Define terms used in event descriptions

## CDN Resources

- **vis-timeline JS**: `https://cdnjs.cloudflare.com/ajax/libs/vis-timeline/7.7.3/vis-timeline-graph2d.min.js`
- **vis-timeline CSS**: `https://cdnjs.cloudflare.com/ajax/libs/vis-timeline/7.7.3/vis-timeline-graph2d.min.css`

## References

- [vis-timeline Documentation](https://visjs.github.io/vis-timeline/docs/timeline/)
- [TimelineJS3 Data Format](https://timeline.knightlab.com/docs/json-format.html)
- [vis-timeline GitHub Repository](https://github.com/visjs/vis-timeline)
- Example: `/docs/sims/timeline/` for reference implementation
