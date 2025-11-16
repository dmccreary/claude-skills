# Venn Diagram Generator

## Overview

The venn-diagram-generator skill creates interactive Venn diagram visualizations using the venn.js JavaScript library. It generates complete MicroSim packages with standalone HTML files featuring colorful circles, clear labels, interactive tooltips with educational definitions, and follows the MicroSim pattern for seamless integration into educational textbooks.

## Purpose

This skill automates the creation of professional Venn diagrams for educational content, emphasizing educational tooltips that teach concepts through interaction rather than displaying meaningless size values.

## Key Features

- **Interactive Venn Diagrams**: 2-4 circle diagrams with hover tooltips
- **Educational Tooltips**: Definitions instead of size values (CRITICAL INNOVATION)
- **Glossary Integration**: Automatically uses definitions from `/docs/glossary.md` when available
- **Customizable Colors**: Educational-friendly color palettes
- **Responsive Design**: Works on all screen sizes
- **Complete MicroSim Package**: HTML, CSS, JavaScript, documentation, metadata
- **ISO 11179 Compliant**: Uses existing glossary definitions for consistency

## When to Use

Use this skill when users request:
- Venn diagrams showing set relationships
- Comparison diagrams between 2-4 categories
- Visual representations of overlapping concepts
- Set theory illustrations
- Intersection and union visualizations
- Categorical relationship diagrams
- Euler diagrams

## Common Trigger Phrases

- "Create a Venn diagram comparing..."
- "Make a 2-circle Venn diagram showing..."
- "Generate a diagram showing the overlap between..."
- "Visualize the relationship between sets..."

## Workflow Steps

### Step 1: Gather Diagram Requirements

Collect information about:
- Title for the diagram
- 2-4 distinct categories/sets to compare
- Relationships (which sets overlap and how)
- Educational purpose or subject area

**IMPORTANT - Check Glossary First:**
Before asking the user for definitions, check if `/docs/glossary.md` exists:
1. Read the glossary file if it exists
2. Extract relevant definitions for each set/term
3. Use glossary definitions if available (ensures consistency)
4. Only ask the user if definitions are missing

**Priority for Definitions:**
1. First: Check `/docs/glossary.md`
2. Second: Use definitions provided by user
3. Third: Create concise, educational definitions

### Step 2: Design Venn Diagram Data

Determine:
- Set count (2, 3, or 4 circles)
- Set sizes (proportional values)
- Color palette (primary, cool tones, pastels, or custom)
- Data structure in venn.js format

**Example 2-Circle:**
```javascript
var sets = [
  {sets: ['Python'], size: 100},
  {sets: ['JavaScript'], size: 100},
  {sets: ['Python', 'JavaScript'], size: 40}
];
```

**Example 3-Circle:**
```javascript
var sets = [
  {sets: ['AI'], size: 100},
  {sets: ['ML'], size: 80},
  {sets: ['Data Science'], size: 90},
  {sets: ['AI', 'ML'], size: 60},
  {sets: ['AI', 'Data Science'], size: 50},
  {sets: ['ML', 'Data Science'], size: 55},
  {sets: ['AI', 'ML', 'Data Science'], size: 40}
];
```

### Step 3: Create MicroSim Directory Structure

```
docs/sims/[diagram-name]/
├── main.html         # Standalone HTML with D3.js and venn.js
├── style.css         # Responsive styling
├── script.js         # Venn diagram data and interactions
├── index.md          # MkDocs integration
└── metadata.json     # Dublin Core metadata
```

Naming: Use kebab-case (e.g., `programming-languages`, `ml-ai-overlap`)

### Step 4: Generate Files from Templates

Use templates from `assets/template/` and replace placeholders:

**script.js** - The most important file:
- `{{VENN_DATA}}`: Sets array with sizes
- `{{COLOR_SCHEME}}`: Color configuration
- **`{{DEFINITIONS}}`**: Educational definitions object ⭐

**main.html**:
- `{{TITLE}}`: Diagram title
- `{{SUBTITLE}}`: Brief subtitle
- `{{DESCRIPTION}}`: 2-3 sentence explanation

**index.md**:
- `{{TITLE}}`, `{{META_DESCRIPTION}}`, `{{OVERVIEW}}`
- `{{SET_RELATIONSHIPS}}`: Bulleted list of relationships
- `{{KEY_CONCEPTS}}`, `{{EDUCATIONAL_APPLICATIONS}}`

**metadata.json**:
- `{{TITLE}}`, `{{DESCRIPTION}}`, `{{SUBJECT}}`, `{{DATE}}`
- `{{SET_COUNT}}`, `{{INTERSECTION_COUNT}}`
- `{{CONCEPTS_LIST}}`, `{{BLOOM_LEVEL}}`

### Step 5: Validate and Test

1. **Data validation**: Verify intersection sizes don't exceed smallest containing set
2. **File structure**: All 5 files present
3. **Placeholder replacement**: No `{{PLACEHOLDERS}}` remain
4. **JavaScript syntax**: Valid JSON in sets array
5. **Responsive design**: Test on different screen sizes
6. **Browser test**: Open main.html, verify tooltips show definitions

### Step 6: Update MkDocs Navigation (Optional)

Suggest adding to `mkdocs.yml`:

```yaml
nav:
  - Visualizations:
    - Diagram Name: sims/[diagram-name]/index.md
```

### Step 7: Inform the User

Provide summary of what was created with file locations and features.

## Educational Tooltips - PRIMARY INNOVATION

**The Problem:**
Default venn.js examples display size values like "150" which provide no educational value.

**The Solution:**
Create a definitions object mapping each set and intersection to educational definitions:

```javascript
var definitions = {
    'AI': 'Systems that simulate human intelligence, reasoning, and decision-making',
    'ML': 'Algorithms that learn patterns from data without explicit programming',
    'Deep Learning': 'Neural networks with multiple layers that learn complex representations',
    'AI,ML': 'Machine Learning is a subset of AI that focuses on learning from data',
    'ML,Deep Learning': 'Deep Learning is a specialized form of ML using neural networks',
    'AI,ML,Deep Learning': 'Deep Learning represents the intersection of AI and ML approaches'
};

function getDefinition(sets) {
    var key = sets.sort().join(',');
    return definitions[key] || sets.join(" ∩ ");
}

// Use in tooltip (NOT d.size)
.on("mouseover", function(event, d) {
    tooltip.html(getDefinition(d.sets));  // Educational content
})
```

**Definition Guidelines:**
1. **Concise**: Keep under 100 characters (1 sentence ideal)
2. **Meaningful**: Focus on concepts, not numbers
3. **Educational**: Explain relationships for intersections
4. **Accessible**: Use language appropriate for target audience
5. **Consistent**: Maintain similar tone across all definitions

**Why This Matters:**
- Makes diagrams self-documenting
- Provides immediate context without external docs
- Reinforces learning through interaction
- Transforms every hover into a teaching moment
- Ensures consistency when using glossary definitions

## Color Palettes

### Primary Colors
- Red (#FF6B6B), Cyan (#4ECDC4), Yellow (#FFE66D)
- Engaging diagrams for educational content

### Cool Tones
- Blue-Purple (#667eea), Purple (#764ba2), Sky Blue (#4facfe)
- Professional appearance

### Pastels
- Powder Blue (#a8dadc), Mint (#f1faee), Coral (#e63946)
- Soft, accessible colors

### Custom
- Match textbook theme or brand colors

## Best Practices

### Educational Tooltips (Most Important)
- **ALWAYS** use educational definitions instead of size values
- Check glossary first for existing definitions
- Keep definitions concise (under 100 characters)
- Focus on meaning, not technical details
- Explain relationships for intersections

### Design Principles
1. **Clarity over Complexity**: Prefer 2-3 circles for readability
2. **Proportional Sizing**: Use actual proportions for data, symbolic sizes for concepts
3. **Color Selection**: High-contrast, colorblind-safe palettes
4. **Meaningful Labels**: Concise set names (1-3 words), Title Case
5. **Educational Context**: Align with learning objectives

### Accessibility
1. **Font Size**: Minimum 16px for readability
2. **Color Contrast**: WCAG AA compliance (4.5:1)
3. **Alternative Text**: Provide descriptive text in index.md
4. **Keyboard Navigation**: D3.js handles this automatically
5. **Screen Readers**: Semantic HTML structure

### Educational Integration
1. **Align with Learning Goals**: Map to specific objectives
2. **Bloom's Taxonomy**: Tag with appropriate cognitive level
3. **Prerequisites**: Document required prior knowledge
4. **Assessment**: Suggest comprehension questions

## Common Patterns

### Pattern 1: Simple Comparison (2 Circles)
```javascript
var sets = [
  {sets: ['Dogs'], size: 100},
  {sets: ['Cats'], size: 100},
  {sets: ['Dogs', 'Cats'], size: 40}
];
```

### Pattern 2: Triple Intersection (3 Circles)
```javascript
var sets = [
  {sets: ['Math'], size: 100},
  {sets: ['Physics'], size: 100},
  {sets: ['CS'], size: 100},
  {sets: ['Math', 'Physics'], size: 40},
  {sets: ['Math', 'CS'], size: 35},
  {sets: ['Physics', 'CS'], size: 30},
  {sets: ['Math', 'Physics', 'CS'], size: 15}
];
```

### Pattern 3: Subset Representation (Nested)
```javascript
var sets = [
  {sets: ['Animals'], size: 150},
  {sets: ['Mammals'], size: 50},
  {sets: ['Animals', 'Mammals'], size: 50}  // Mammals ⊆ Animals
];
```

### Pattern 4: Disjoint Sets (No Overlap)
```javascript
var sets = [
  {sets: ['Odd Numbers'], size: 100},
  {sets: ['Even Numbers'], size: 100}
  // No intersection - sets are disjoint
];
```

## Troubleshooting

### Issue: Sets data is invalid
**Solution**: Check intersection sizes don't exceed individual set sizes

### Issue: Colors not showing correctly
**Solution**: Verify set names in color scheme exactly match data (case-sensitive)

### Issue: Diagram too small/large
**Solution**: Adjust width/height in script.js `venn.VennDiagram()` call

### Issue: Labels cut off
**Solution**: Increase diagram padding, shorten labels, or increase container size

### Issue: Tooltips not appearing
**Solution**: Check tooltip CSS class exists and JavaScript handlers attached

### Issue: Diagram not responsive on mobile
**Solution**: Verify `makeResponsive()` function called and SVG has viewBox attribute

## Output Files

1. **main.html**: Standalone interactive diagram with D3.js and venn.js
2. **style.css**: Responsive styling with tooltips and print-friendly rules
3. **script.js**: Venn data, definitions, and interactive features
4. **index.md**: MkDocs integration page with documentation
5. **metadata.json**: Dublin Core metadata for searchability

## Integration with Other Skills

**PRIMARY INTEGRATION:**
- **glossary-generator**: Always check `/docs/glossary.md` first for ISO 11179-compliant definitions to use in tooltips for consistency

**Other Integrations:**
- **learning-graph-generator**: Visualize concept dependencies as Venn diagrams
- **chapter-content-generator**: Embed diagrams in chapter content
- **quiz-generator**: Create questions about set relationships
- **microsim-p5**: Use Venn for static sets, p5.js for dynamic simulations

## Technical Details

- **venn.js Library**: 0.2.20
- **D3.js Library**: 7.9.0
- **Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Loaded from CDN (no local files required)

## References

- **venn.js GitHub**: https://github.com/benfred/venn.js
- **venn.js Examples**: https://benfred.github.io/venn.js/
- **D3.js Documentation**: https://d3js.org/
- **Set Theory**: https://en.wikipedia.org/wiki/Venn_diagram
- **Example**: `ai-ml-dl-example.js` - Complete working example with educational tooltips
