# Bubble Chart Generator Assets

This directory contains template files that can be used as starting points for creating bubble chart visualizations.

## Template Files

### template-main.html
A complete HTML template with Chart.js bubble chart implementation. Includes:
- HTML boilerplate with proper meta tags
- Chart.js CDN import
- Canvas element for rendering
- Quadrant analysis section
- Fully commented JavaScript with TODO markers for customization
- Data structure example
- Color scheme configuration
- Bubble size calculation
- Chart.js configuration with all options
- Custom plugin for quadrant backgrounds
- Quadrant population logic

**Usage**: Copy this file to your target directory (e.g., `docs/sims/my-chart/main.html`) and customize the TODO sections.

### template-style.css
Professional CSS styling for bubble chart visualizations. Includes:
- Reset and base styles
- Chart container styling
- Legend and quadrant section styling
- Interactive hover effects
- Responsive design media queries
- Print-friendly styles

**Usage**: Copy this file to your target directory (e.g., `docs/sims/my-chart/style.css`) and customize colors/dimensions as needed.

## Customization Guide

When using these templates:

1. **Replace TODO markers** in template-main.html:
   - Chart title
   - Data array
   - Color scheme
   - Axis labels
   - Quadrant colors

2. **Adjust styling** in template-style.css:
   - Chart container height (default: 600px)
   - Color scheme to match your data categories
   - Responsive breakpoints if needed

3. **Test thoroughly**:
   - Open main.html directly in browser
   - Verify all data points display correctly
   - Check tooltips and interactions
   - Test on different screen sizes

## Example Implementation

For a complete reference implementation, see:
`/docs/sims/skill-impact-chart/`

This demonstrates all features in action with real data.
