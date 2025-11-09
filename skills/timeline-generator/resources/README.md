# Timeline Generator Resources

This directory contains generic template files for creating interactive timeline visualizations using vis-timeline.js.

## Template Files

### template-timeline.json
Generic event data file demonstrating the JSON structure for timeline events. This sample includes:
- 6 sample events spanning 2020-2021
- 4 categories (Planning, Development, Launch, Maintenance)
- Complete data structure with all optional fields

**Placeholders**: None (this is a complete working example)

### template-main.html
Generic HTML template for the timeline viewer. Contains placeholders that should be replaced:

- `{{TIMELINE_TITLE}}` - The main title of the timeline (e.g., "Project History Timeline")
- `{{TIMELINE_SUBTITLE}}` - Subtitle or tagline (e.g., "Major milestones from 2020-2021")
- `{{FILTER_CONTROLS}}` - Either an empty string or the filter controls HTML block
- `{{TIMELINE_DESCRIPTION}}` - Brief description of the timeline's purpose
- `{{LEGEND}}` - Either an empty string or the legend HTML block
- `{{CATEGORY_COLORS}}` - JavaScript object defining category colors

#### Filter Controls Block
If the user wants category filtering, use this structure:

```html
<div class="controls">
    <div class="filter-group">
        <label>Filter:</label>
        <button class="filter-btn active" onclick="filterCategory('all')">All Events</button>
        <button class="filter-btn" onclick="filterCategory('Category1')">Category1</button>
        <button class="filter-btn" onclick="filterCategory('Category2')">Category2</button>
        <!-- Add more buttons as needed -->
    </div>
</div>
```

If no filtering is wanted, replace `{{FILTER_CONTROLS}}` with an empty string.

#### Legend Block
If the user wants category filtering, include a legend:

```html
<div class="legend">
    <div class="legend-item">
        <div class="legend-color" style="background-color: #8b0000;"></div>
        <span>Category1</span>
    </div>
    <div class="legend-item">
        <div class="legend-color" style="background-color: #1e3a8a;"></div>
        <span>Category2</span>
    </div>
    <!-- Add more legend items as needed -->
</div>
```

If no filtering, this can be omitted or replaced with an empty string.

#### Category Colors Object
Example JavaScript object:

```javascript
{
    'Planning': '#8b0000',
    'Development': '#1e3a8a',
    'Launch': '#1e5631',
    'Maintenance': '#7c2d12'
}
```

Recommended color palette for up to 6 categories:
- `#8b0000` (dark red)
- `#1e3a8a` (dark blue)
- `#1e5631` (dark green)
- `#7c2d12` (dark brown)
- `#6b21a8` (purple)
- `#b45309` (orange)

### template-index.md
Generic documentation template for MkDocs integration. Contains placeholders:

- `{{TIMELINE_TITLE}}` - The main title
- `{{TIMELINE_OVERVIEW_TEXT}}` - One-sentence overview
- `{{DETAILED_DESCRIPTION}}` - 2-3 paragraph detailed description
- `{{CATEGORY_FILTERING_FEATURE}}` - Either the filtering feature description or empty string

If category filtering is enabled, use:
```markdown
- **Category Filtering**: Use filter buttons to view specific event categories
```

## Usage Instructions

When generating a timeline:

1. **Gather requirements** from the user (see SKILL.md Step 1)
2. **Create directory structure**: `docs/sims/<timeline-name>/`
3. **Generate timeline.json** with user's event data
4. **Generate main.html** by replacing placeholders in template-main.html
5. **Generate index.md** by replacing placeholders in template-index.md
6. **Test** the timeline by opening main.html in a browser

## Example Workflow

```markdown
User wants: "Create a timeline of company milestones from 2015-2023"

1. Ask for events, categories, whether they want filtering
2. Create: docs/sims/company-milestones-timeline/
3. Generate timeline.json with their events
4. Replace placeholders:
   - {{TIMELINE_TITLE}} → "Company Milestones Timeline"
   - {{TIMELINE_SUBTITLE}} → "Major achievements from 2015-2023"
   - {{CATEGORY_COLORS}} → Object with their categories
   - etc.
5. Save as main.html and index.md
6. Test and validate
```

## Color Selection Guidelines

Choose colors that:
- Have sufficient contrast (dark colors work best with white text)
- Are visually distinct from each other
- Follow a logical scheme (e.g., chronological progression, thematic grouping)
- Are accessible (avoid red-green combinations for colorblind users)

## Common Customizations

### No Category Filtering
- Set `{{FILTER_CONTROLS}}` to empty string
- Set `{{LEGEND}}` to empty string
- Use single color in `{{CATEGORY_COLORS}}`
- In template-index.md, remove filtering feature text

### Few Events (< 10)
- Adjust timeline height to 400px instead of 600px
- Reduce zoomMin to show shorter time spans

### Many Events (> 50)
- Increase timeline height to 800px
- Consider grouping related events
- Use clearer category distinctions

### Long Time Spans (> 100 years)
- Increase zoomMax value appropriately
- Consider showing only decades on initial load

## Reference Implementation

See `/docs/sims/timeline/` for a complete working example (McCreary Family Heritage Timeline) that demonstrates:
- 60+ events spanning 1500+ years
- 4 distinct categories with filtering
- Rich historical context in notes
- Full documentation integration
