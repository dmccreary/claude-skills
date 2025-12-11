# venn.js Reference Guide

## Overview

venn.js is a JavaScript library for laying out area-proportional Venn and Euler diagrams. It uses D3.js for rendering SVG visualizations.

## Dependencies

- **D3.js v7+** - Required for DOM manipulation and SVG rendering
- CDN: `https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js`

## CDN Links

- **venn.js**: `https://cdnjs.cloudflare.com/ajax/libs/venn.js/0.2.20/venn.min.js`
- **Latest version**: 0.2.20 (as of 2024)

## Basic Data Format

Venn diagrams require an array of objects where each object represents either:
1. A single set
2. An intersection of multiple sets

### Data Structure

```javascript
var sets = [
  {sets: ['A'], size: 12},           // Set A with 12 items
  {sets: ['B'], size: 12},           // Set B with 12 items
  {sets: ['A','B'], size: 2}         // Intersection of A and B with 2 items
];
```

**Key properties:**
- `sets`: Array of set names (strings)
- `size`: Numerical value representing area/count
- `label`: Optional custom label (defaults to set names)

## Creating Diagrams

### 2-Circle Venn Diagram

```javascript
var sets = [
  {sets: ['Set A'], size: 10},
  {sets: ['Set B'], size: 10},
  {sets: ['Set A', 'Set B'], size: 3}
];

var chart = venn.VennDiagram();
d3.select("#venn").datum(sets).call(chart);
```

### 3-Circle Venn Diagram

```javascript
var sets = [
  // Individual sets
  {sets: ['A'], size: 12},
  {sets: ['B'], size: 12},
  {sets: ['C'], size: 12},

  // Pairwise intersections
  {sets: ['A','B'], size: 2},
  {sets: ['A','C'], size: 2},
  {sets: ['B','C'], size: 2},

  // Triple intersection
  {sets: ['A','B','C'], size: 1}
];

var chart = venn.VennDiagram();
d3.select("#venn").datum(sets).call(chart);
```

### 4+ Circle Venn Diagrams

venn.js supports 4 or more sets, though visual clarity may decrease:

```javascript
var sets = [
  {sets: ['A'], size: 10},
  {sets: ['B'], size: 10},
  {sets: ['C'], size: 10},
  {sets: ['D'], size: 10},
  {sets: ['A','B'], size: 2},
  {sets: ['A','C'], size: 2},
  {sets: ['A','D'], size: 2},
  {sets: ['B','C'], size: 2},
  {sets: ['B','D'], size: 2},
  {sets: ['C','D'], size: 2},
  // Add triple and quadruple intersections as needed
];
```

## Configuration Options

### Basic Configuration

```javascript
var chart = venn.VennDiagram()
    .width(600)
    .height(450)
    .padding(10);  // Padding around diagram
```

### Advanced Options

```javascript
var chart = venn.VennDiagram()
    .width(600)
    .height(450)
    .fontSize("14px")
    .duration(1000)  // Animation duration in ms
    .styled(true)    // Apply default styling
    .orientationOrder(function(a, b) {
        // Custom ordering function
        return a.size - b.size;
    });
```

## Styling with D3

Apply custom styles after rendering using D3 selectors:

### Circle Fill Colors

```javascript
// Apply colors to individual sets
var colors = {
    'A': '#667eea',
    'B': '#764ba2',
    'C': '#f093fb'
};

d3.selectAll("#venn .venn-circle")
    .filter(function(d) { return d.sets.length === 1; })
    .select("path")
    .style("fill", function(d) { return colors[d.sets[0]]; });
```

### Opacity and Strokes

```javascript
// Adjust fill opacity
d3.selectAll("#venn .venn-circle path")
    .style("fill-opacity", 0.75)
    .style("stroke", "#333")
    .style("stroke-width", "2px");

// Style intersection areas differently
d3.selectAll("#venn .venn-intersection path")
    .style("fill-opacity", 0.85);
```

### Text Styling

```javascript
// Style set labels
d3.selectAll("#venn .venn-circle text")
    .style("fill", "#333")
    .style("font-size", "16px")
    .style("font-weight", "bold");

// Style intersection labels
d3.selectAll("#venn .venn-intersection text")
    .style("fill", "#333")
    .style("font-size", "14px");
```

## Interactivity

### Tooltips

```javascript
// Create tooltip element
var tooltip = d3.select("body").append("div")
    .attr("class", "venntooltip")
    .style("position", "absolute")
    .style("opacity", 0);

// Add hover events
var div = d3.select("#venn");

div.selectAll("g")
    .on("mouseover", function(event, d) {
        // Ensure proper z-ordering
        venn.sortAreas(div, d);

        // Show tooltip
        tooltip.transition().duration(200).style("opacity", 0.9);
        tooltip.html(d.sets.join(" ∩ ") + ": " + d.size)
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 28) + "px");

        // Highlight area
        d3.select(this).select("path")
            .style("fill-opacity", 0.95);
    })
    .on("mouseout", function(event, d) {
        tooltip.transition().duration(200).style("opacity", 0);
        d3.select(this).select("path")
            .style("fill-opacity", 0.75);
    });
```

### Click Events

```javascript
div.selectAll("g")
    .on("click", function(event, d) {
        console.log("Clicked:", d.sets.join(", "));
        // Add custom click behavior
    });
```

## Educational Color Schemes

### Scheme 1: Primary Colors (Best for 3 sets)

```javascript
var colors = {
    'Set 1': '#FF6B6B',  // Red
    'Set 2': '#4ECDC4',  // Cyan
    'Set 3': '#FFE66D'   // Yellow
};
```

### Scheme 2: Cool Tones (Professional)

```javascript
var colors = {
    'Set 1': '#667eea',  // Blue-Purple
    'Set 2': '#764ba2',  // Purple
    'Set 3': '#4facfe'   // Sky Blue
};
```

### Scheme 3: Pastel (Gentle, Accessible)

```javascript
var colors = {
    'Set 1': '#a8dadc',  // Powder Blue
    'Set 2': '#f1faee',  // Mint Cream
    'Set 3': '#e63946'   // Imperial Red
};
```

### Scheme 4: Earth Tones

```javascript
var colors = {
    'Set 1': '#8ecae6',  // Sky
    'Set 2': '#219ebc',  // Ocean
    'Set 3': '#ffb703'   // Orange
};
```

## Common Patterns

### Two-Circle Comparison

Use for comparing two categories (e.g., "Cats vs Dogs", "Python vs JavaScript"):

```javascript
var sets = [
  {sets: ['Category A'], size: 100, label: 'Unique to A'},
  {sets: ['Category B'], size: 100, label: 'Unique to B'},
  {sets: ['Category A', 'Category B'], size: 50, label: 'Shared'}
];
```

### Three-Circle Knowledge Domains

Use for showing overlap between three fields (e.g., "Math, Computer Science, Engineering"):

```javascript
var sets = [
  {sets: ['Math'], size: 100},
  {sets: ['CS'], size: 100},
  {sets: ['Engineering'], size: 100},
  {sets: ['Math', 'CS'], size: 30},
  {sets: ['Math', 'Engineering'], size: 25},
  {sets: ['CS', 'Engineering'], size: 35},
  {sets: ['Math', 'CS', 'Engineering'], size: 15}
];
```

### Subset Representation

Show one set as a subset of another by making the intersection size equal to the smaller set:

```javascript
var sets = [
  {sets: ['All Animals'], size: 100},
  {sets: ['Mammals'], size: 30},
  {sets: ['All Animals', 'Mammals'], size: 30}  // Mammals ⊆ Animals
];
```

## Best Practices

### 1. Size Values

- Use proportional sizes that reflect actual relationships
- Ensure intersection sizes don't exceed the smallest containing set
- For purely symbolic diagrams, use consistent sizes (e.g., all 10)

### 2. Set Names

- Use clear, concise labels (2-4 words max)
- Avoid special characters in set names
- Use Title Case for professional appearance

### 3. Color Selection

- Choose high-contrast colors for accessibility
- Use colorblind-safe palettes when possible
- Apply consistent opacity (0.70-0.85) for visibility of overlaps

### 4. Layout

- Keep to 2-3 circles for optimal clarity
- Use 4+ circles only when necessary
- Consider multiple diagrams instead of one complex diagram

### 5. Responsive Design

Make diagrams responsive:

```javascript
var svg = d3.select("#venn svg");
var width = parseInt(svg.attr("width"));
var height = parseInt(svg.attr("height"));

svg.attr("viewBox", "0 0 " + width + " " + height)
   .attr("preserveAspectRatio", "xMidYMid meet")
   .attr("width", "100%")
   .attr("height", "100%");
```

## Troubleshooting

### Issue: Circles not appearing

**Solution:** Ensure D3.js is loaded before venn.js:
```html
<script src="d3.js"></script>
<script src="venn.js"></script>
```

### Issue: Layout looks wrong

**Solution:** Check that intersection sizes don't exceed individual set sizes:
```javascript
// BAD: Intersection larger than sets
{sets: ['A'], size: 5},
{sets: ['B'], size: 5},
{sets: ['A','B'], size: 10}  // Error!

// GOOD: Proportional sizes
{sets: ['A'], size: 10},
{sets: ['B'], size: 10},
{sets: ['A','B'], size: 3}
```

### Issue: Text labels cut off

**Solution:** Increase padding or adjust container size:
```javascript
var chart = venn.VennDiagram()
    .width(700)
    .height(500)
    .padding(20);  // Increase padding
```

### Issue: Colors not applying

**Solution:** Ensure you're selecting the correct elements:
```javascript
// Select path within circle, not the circle itself
d3.selectAll("#venn .venn-circle path")
    .style("fill", "red");
```

### Critical Rules for venn.js Hover Interactions

  1. Never Modify Fill Colors During Interactions

  - Set fill colors once during initialization
  - Never change fill property in mouseover/mouseout handlers
  - The venn.sortAreas() function can interfere with dynamic color changes

  2. Only Modify Opacity Values

  Use fill-opacity and stroke-opacity for hover effects:
  // CORRECT - Change opacity only
  .on("mouseover", function(event, d) {
      selection.select("path")
          .style("fill-opacity", d.sets.length == 1 ? 0.4 : 0.1)
          .style("stroke-opacity", 1);
  })

  // WRONG - Don't change fill color
  .on("mouseover", function(event, d) {
      selection.select("path")
          .style("fill", "#FF0000")  // ❌ Don't do this!
  })

  3. Use Low Opacity Values for Text Readability

  Follow the official venn.js example pattern:
  - Resting state: Single sets = 0.25, Intersections = 0.0
  - Hover state: Single sets = 0.4, Intersections = 0.1

  High opacity (0.75-0.85) makes text labels unreadable, especially on dark colors.

  4. Use Named Transitions

  Use .transition("tooltip") instead of .transition() to avoid conflicts:
  var selection = d3.select(this).transition("tooltip").duration(400);

  5. Don't Reapply Styles After sortAreas()

  - Calling venn.sortAreas(div, d) reorders DOM elements
  - Do not reapply fill colors or text styling after this call
  - The library handles this internally

  6. Reference Official Examples

  When in doubt, always check the official examples at:
  https://github.com/benfred/venn.js/tree/master/examples

  Especially intersection_tooltip.html for the canonical hover pattern.

  ### Complete Working Pattern:

  // Set colors once during initialization
  div.selectAll("g").select("path")
      .style("fill", function(d) { return getColor(d); });

  // Hover: change opacity only
  div.selectAll("g")
      .on("mouseover", function(event, d) {
          venn.sortAreas(div, d);
          var selection = d3.select(this).transition("tooltip").duration(400);
          selection.select("path")
              .style("fill-opacity", d.sets.length == 1 ? 0.4 : 0.1)
              .style("stroke-opacity", 1);
      })
      .on("mouseout", function(event, d) {
          var selection = d3.select(this).transition("tooltip").duration(400);
          selection.select("path")
              .style("fill-opacity", d.sets.length == 1 ? 0.25 : 0.0)
              .style("stroke-opacity", 0);
      });

## Resources

- **GitHub Repository**: https://github.com/benfred/venn.js
- **D3.js Documentation**: https://d3js.org/
- **Examples and Demos**: https://benfred.github.io/venn.js/
- **NPM Package**: https://www.npmjs.com/package/venn.js

## Version Notes

- **Current version**: 0.2.20
- **Breaking changes**: None reported between 0.2.x versions
- **Browser support**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Mobile support**: Responsive with proper viewport settings
