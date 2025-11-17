# Math Function Plotter with Plotly.js

## Overview

The math-function-plotter-plots skill creates professional, interactive mathematical function plots using the Plotly.js JavaScript library. It generates complete MicroSim packages optimized for iframe embedding in narrow textbook layouts, featuring hover tooltips with precise coordinates, interactive sliders for exploring points along curves, responsive design with minimal margins, and comprehensive educational documentation including lesson plans and assessment questions.

## Purpose

This skill automates the creation of interactive mathematical function visualizations for calculus, precalculus, physics, and engineering courses. It transforms mathematical expressions into engaging, explorable plots that help students understand function behavior, relationships between variables, and key mathematical concepts through interactive manipulation.

## Key Features

- **Interactive Sliders**: Move a point along the function curve to explore (x, y) relationships
- **Hover Tooltips**: Display precise coordinates with 3 decimal precision at any point on the curve
- **Smooth Curves**: 500-point sampling for visually appealing function plots
- **Responsive Design**: Optimized for narrow iframe widths (320px-1200px) with adaptive heights
- **Minimal Margins**: 2-5px padding optimized for efficient screen real estate in textbooks
- **Export Functionality**: Built-in PNG export via Plotly toolbar
- **Educational Documentation**: Complete lesson plans, activities, and assessment questions
- **Dublin Core Metadata**: Searchable, catalogable educational resources
- **Template-Based**: Consistent structure across all function plots
- **500px Height Standard**: Adjustable drawing region that scales responsively on mobile

## When to Use

Use this skill when users request:

- Plotting mathematical functions (trigonometric, polynomial, exponential, logarithmic)
- Graphing equations for educational purposes
- Visualizing function behavior over specific domains
- Creating interactive function explorers for textbooks
- Demonstrating calculus concepts (continuity, limits, derivatives)
- Physics visualizations (wave functions, trajectories, harmonic motion)
- Engineering plots (signals, control systems, transfer functions)
- Interactive mathematical demonstrations with sliders

## Common Trigger Phrases

- "Plot a mathematical function"
- "Graph the equation y = ..."
- "Visualize f(x) = ..."
- "Create an interactive function plotter"
- "Show me a graph of [function]"
- "Plot sin(x) / cos(x) / tan(x)"
- "Generate a calculus visualization"
- "Make a plot I can embed in my textbook"
- "Create an interactive [function type] graph"

## Workflow Steps

### Step 1: Gather Requirements

Collect information about the mathematical function and context:

**Required:**
- **Function expression**: The mathematical function to plot (e.g., "sin(x)", "x²", "e^(-x²)")
- **Title**: Descriptive name for the MicroSim (e.g., "Sine Function Visualization")
- **Domain**: Range of x-values to plot [xMin, xMax]

**Optional (with smart defaults):**
- **Range**: Y-axis limits [yMin, yMax] (auto-calculated if not provided)
- **Interactive point**: Initial x-position for the slider (default: midpoint of domain)
- **Slider step**: Increment for slider movement (default: (xMax - xMin) / 100)
- **Axis labels**: Custom labels for x and y axes (default: "x" and "y")
- **Subtitle**: Brief description (default: function expression)
- **Context**: Course/chapter where this will be used (for educational content)

**Example conversation:**
```
User: "Create a plot for the sine function"
Assistant: "I'll create an interactive sine function plot. Let me gather details:
- Title: 'Sine Function Visualization'
- Function: sin(x)
- Domain: -2π to 2π (approximately -6.28 to 6.28)?
- Is this for a specific course or chapter?"
```

Provide sensible defaults based on common mathematical conventions:
- Trigonometric functions: Domain [-2π, 2π], Range auto-calculated
- Polynomial functions: Domain showing all real roots if possible
- Exponential functions: Domain showing meaningful change (3-5 orders of magnitude)

### Step 2: Create Directory Structure

Create the MicroSim directory following the standardized pattern:

```
docs/sims/[microsim-name]/
├── main.html         # Standalone Plotly.js visualization
├── style.css         # Responsive styling with minimal margins
├── script.js         # Interactive logic (sliders, tooltips)
├── index.md          # MkDocs documentation page
└── metadata.json     # Dublin Core metadata
```

**Naming conventions:**
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- Examples: `sine-function`, `quadratic-parabola`, `exponential-decay`, `gaussian-bell-curve`

### Step 3: Convert Function Expression to JavaScript

Translate the mathematical expression to JavaScript Math functions:

**Common conversions:**

| Math Notation | JavaScript Code |
|--------------|----------------|
| sin(x) | Math.sin(x) |
| cos(x) | Math.cos(x) |
| tan(x) | Math.tan(x) |
| e^x | Math.exp(x) |
| x² | Math.pow(x, 2) or x**2 |
| √x | Math.sqrt(x) |
| ln(x) | Math.log(x) |
| log₁₀(x) | Math.log10(x) |
| \|x\| | Math.abs(x) |

**Example JavaScript function:**
```javascript
function f(x) {
    return Math.sin(x);
}
```

**For complex functions:**
```javascript
// Damped oscillation
function f(x) {
    return Math.exp(-x/5) * Math.sin(x);
}

// Gaussian distribution
function f(x) {
    const mu = 0, sigma = 1;
    return Math.exp(-0.5 * ((x-mu)/sigma)**2) / (sigma * Math.sqrt(2*Math.PI));
}
```

### Step 4: Generate main.html from Template

Use `assets/template-iframe-main.html` and replace placeholders:

**Placeholder replacements:**
- `{{TITLE}}` → Full title (e.g., "Sine Function Visualization")
- `{{SUBTITLE}}` → Function expression (e.g., "y = sin(x)")
- `{{X_MIN}}` → Minimum x value (e.g., -6.28)
- `{{X_MAX}}` → Maximum x value (e.g., 6.28)
- `{{X_STEP}}` → Slider step size (e.g., 0.01)
- `{{INITIAL_X}}` → Initial slider position (e.g., 0)

**Critical features to preserve:**
- Plotly.js CDN link (v2.27.0 or latest stable)
- Minimal body margins: `margin: 0; padding: 0;`
- Links to external `style.css` and `script.js`
- Semantic HTML5 structure

### Step 5: Generate style.css with Minimal Margins

Use `assets/template-iframe-style.css` without modifications.

**Key styling requirements:**
- **Body margins**: MUST be `margin: 0; padding: 0;` for iframe embedding
- **Container padding**: Maximum 5px (reduces to 3px tablet, 2px mobile)
- **Header margins**: 5px top, 2px bottom (minimal spacing)
- **Background**: `aliceblue` (repository standard)
- **Plot height**: 400px desktop, 300px tablet, 250px mobile
- **Responsive breakpoints**: 768px (tablet), 480px (mobile)

**Testing**: Ensure visualization looks good at widths from 320px to 1200px.

### Step 6: Generate script.js with Plotly Configuration

Use `assets/template-script.js` and replace placeholders:

**Placeholder replacements:**
- `{{FUNCTION_JS}}` → JavaScript function definition (from Step 3)
- `{{X_MIN}}`, `{{X_MAX}}` → Domain limits
- `{{Y_MIN}}`, `{{Y_MAX}}` → Range limits (or auto-calculate)
- `{{FUNCTION_LABEL}}` → Legend label (e.g., "y = sin(x)")
- `{{X_LABEL}}` → X-axis label (default: "x")
- `{{Y_LABEL}}` → Y-axis label (default: "y")
- `{{FILENAME}}` → Export filename (e.g., "sine-function")

**Auto-calculate range** if not provided:
```javascript
// Sample the function to find y range
const samplePoints = 100;
const yValues = [];
for (let i = 0; i <= samplePoints; i++) {
    const x = xMin + (xMax - xMin) * i / samplePoints;
    yValues.push(f(x));
}
const yMin = Math.min(...yValues) * 1.1;  // Add 10% padding
const yMax = Math.max(...yValues) * 1.1;
```

**Plotly configuration includes:**
- Function curve trace (blue line, width 2)
- Interactive point trace (red marker, size 10)
- Hover tooltips with 3 decimal precision
- Responsive mode enabled
- Export toolbar with PNG option
- Grid lines and zero lines for reference

### Step 7: Create index.md Documentation

Use `assets/template-index.md` and customize:

**Required sections:**

1. **YAML frontmatter**
   ```yaml
   ---
   title: Sine Function Visualization
   description: Interactive plot of sine function with slider
   quality_score: 85
   image: /sims/sine-function/sine-function.png
   og:image: /sims/sine-function/sine-function.png
   ---
   ```

2. **Level 1 header** matching the title

3. **Interactive visualization** with iframe embed
   ```html
   <iframe src="main.html" width="100%" height="500px"></iframe>
   ```

4. **Fullscreen link button**

5. **Copy-paste embed code** in HTML code block

6. **Overview** - Purpose and features list

7. **How to Use** - Step-by-step user instructions

8. **Educational Applications** - Subject-specific use cases

9. **Customization Guide** - How to modify parameters

10. **Technical Details** - Library version, implementation

11. **Lesson Plan Suggestions** - Learning objectives, activities, assessments

12. **References** - Links to documentation

**Lesson plan quality**: Provide specific, actionable activities using the slider interactivity:

```markdown
**Activity 1: Finding Special Values (10 minutes)**

1. Use the slider to find f(π/2). What value do you observe?
2. At what x-value does f(x) = 0.5? (Approximate using the slider)
3. Challenge: Find all x-values where f(x) = 0 in the visible range.
```

**Customize for function type:**
- **Trigonometric**: Mention periodicity, amplitude, phase shift
- **Polynomial**: Discuss degree, roots, turning points
- **Exponential**: Highlight growth/decay, asymptotes
- **Logarithmic**: Note domain restrictions, inverse relationships

### Step 8: Create metadata.json with Dublin Core

Use `assets/template-metadata.json` and replace:

**Required Dublin Core fields:**
```json
{
  "title": "Sine Function Visualization",
  "description": "Interactive plot of sine function...",
  "creator": "Your Name or Organization",
  "date": "2025-11-17",
  "subject": ["mathematics", "trigonometry", "calculus"],
  "type": "Interactive Simulation",
  "format": "text/html",
  "language": "en-US",
  "rights": "CC BY 4.0"
}
```

**Optional educational fields:**
- `audience` - "High school students", "College undergraduates"
- `educationalLevel` - "Grade 11-12", "Undergraduate"
- `learningResourceType` - "Interactive Plot"
- `interactivityType` - "active"
- `typicalLearningTime` - "PT10M" (ISO 8601 duration)

**Subject keyword selection** (choose 3-5 specific keywords):
- Mathematics: algebra, geometry, trigonometry, calculus, statistics
- Physics: kinematics, waves, thermodynamics
- Engineering: signals, control-systems, circuits

### Step 9: Test and Validate

Perform comprehensive testing:

**Visual Testing:**
1. Open `main.html` in a browser
2. Verify plot renders correctly
3. Check axes are labeled and readable
4. Confirm tooltips appear on hover
5. Test slider - point should move smoothly along curve
6. Resize browser window - verify responsive behavior

**Functional Testing:**
1. Slider range covers full x domain
2. Point position matches slider value
3. Tooltips show correct coordinates (3 decimal places)
4. PNG export functionality works
5. Mobile testing (320px width minimum)

**Documentation Review:**
1. Verify iframe embed works in `index.md`
2. Check all placeholders replaced
3. Ensure lesson plan is function-specific
4. Validate all markdown links work

**Metadata Validation:**
1. Confirm `metadata.json` is valid JSON
2. Check all required Dublin Core fields present
3. Verify subject keywords are relevant

## Common Function Configurations

### Trigonometric Functions

**Sine Function:**
```javascript
function f(x) { return Math.sin(x); }
// Domain: -2π to 2π (-6.28 to 6.28)
// Range: -1.5 to 1.5
```

**Cosine Function:**
```javascript
function f(x) { return Math.cos(x); }
// Domain: -2π to 2π
// Range: -1.5 to 1.5
```

**Tangent Function (with discontinuities):**
```javascript
function f(x) { return Math.tan(x); }
// Domain: -π to π (-3.14 to 3.14)
// Range: -10 to 10 (limited for visibility)
```

**Damped Sine Wave:**
```javascript
function f(x) { return Math.exp(-x/5) * Math.sin(x); }
// Domain: 0 to 20
// Range: Auto-calculate
```

### Polynomial Functions

**Quadratic:**
```javascript
function f(x) { return x**2; }
// Domain: -5 to 5
// Range: 0 to 25
```

**Cubic:**
```javascript
function f(x) { return x**3 - 3*x; }
// Domain: -3 to 3
// Range: Auto-calculate
```

**Quartic with Turning Points:**
```javascript
function f(x) { return x**4 - 4*x**2 + 1; }
// Domain: -3 to 3
// Range: Auto-calculate
```

### Exponential and Logarithmic

**Exponential Growth:**
```javascript
function f(x) { return Math.exp(x); }
// Domain: -2 to 2
// Range: 0 to 10
```

**Exponential Decay:**
```javascript
function f(x) { return Math.exp(-x); }
// Domain: 0 to 5
// Range: 0 to 1.2
```

**Natural Logarithm:**
```javascript
function f(x) { return Math.log(x); }
// Domain: 0.1 to 10 (must be positive)
// Range: Auto-calculate
```

**Gaussian (Normal Distribution):**
```javascript
function f(x) {
    const mu = 0, sigma = 1;
    return Math.exp(-0.5 * ((x-mu)/sigma)**2) / (sigma * Math.sqrt(2*Math.PI));
}
// Domain: -4 to 4
// Range: 0 to 0.5
```

### Physics and Engineering

**Projectile Motion:**
```javascript
function f(x) {
    const v0 = 20, angle = 45 * Math.PI/180, g = 9.8;
    return x * Math.tan(angle) - (g * x**2) / (2 * v0**2 * Math.cos(angle)**2);
}
// Domain: 0 to 40
// Range: Auto-calculate
```

**Simple Harmonic Motion:**
```javascript
function f(x) {
    const A = 1, omega = 2, phi = 0;
    return A * Math.cos(omega * x + phi);
}
// Domain: 0 to 10
// Range: -1.5 to 1.5
```

## Best Practices

### Educational Design

1. **Slider Activities**: Design questions that promote exploration
   - "Find where f(x) = 0"
   - "What happens as x approaches infinity?"
   - "Locate the maximum value"

2. **Lesson Integration**: Reference specific textbook concepts
   - Link to chapter sections
   - Use consistent notation
   - Address common misconceptions

3. **Assessment Quality**: Provide measurable learning outcomes
   - Specific x-values to find
   - Pattern recognition questions
   - Prediction challenges

### Technical Design

1. **Function Sampling**: Use 500 points minimum for smooth curves

2. **Domain Selection**: Choose domains that show key features
   - Trigonometric: 1-3 complete periods
   - Polynomial: All real roots if possible
   - Exponential: 3-5 orders of magnitude

3. **Range Calculation**: Add 10% padding above/below extrema

4. **Responsive Testing**: Test at 320px, 480px, 768px, 1024px, 1200px

5. **Performance**: Keep total points under 2000 for smooth rendering

### Accessibility

1. **Color Contrast**: WCAG AA minimum (blue #007bff, red #dc3545)
2. **Font Sizes**: Minimum 12px, scale up to 16px on desktop
3. **Keyboard Navigation**: Slider is keyboard-accessible (HTML range input)
4. **Alt Text**: Provide text descriptions of function behavior

## Template Files

The skill includes five template files in `skills/math-function-plotter-plotly/assets/`:

1. **template-iframe-main.html** - HTML structure with Plotly.js CDN
2. **template-iframe-style.css** - Responsive CSS with minimal margins
3. **template-script.js** - Plotly configuration and slider interactivity
4. **template-index.md** - Documentation with lesson plans
5. **template-metadata.json** - Dublin Core metadata

All templates use `{{PLACEHOLDER}}` format for easy find-and-replace.

## Output Files

Each generated MicroSim includes:

- **main.html** - Standalone visualization (can open directly in browser)
- **style.css** - Responsive styling optimized for iframe embedding
- **script.js** - Interactive JavaScript with Plotly configuration
- **index.md** - Complete documentation with iframe embed
- **metadata.json** - Dublin Core metadata for searchability

## Technical Details

- **Library**: Plotly.js v2.27.0 (or latest stable version)
- **CDN**: https://cdn.plot.ly/plotly-2.27.0.min.js
- **Function Sampling**: 500 evenly-spaced points by default
- **Responsive Mode**: Plotly's built-in responsive layout
- **Interactivity**: HTML5 range input with event listeners
- **Tooltips**: Plotly hovertemplate with custom formatting
- **Export**: Built-in PNG export via toolbar
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## Integration with MkDocs

To add the MicroSim to your textbook navigation:

```yaml
# mkdocs.yml
nav:
  - MicroSims:
    - Sine Function: sims/sine-function-plot/index.md
```

The iframe will automatically embed within the page with proper responsive behavior.

## Example Use Cases

### Calculus Course
- Visualizing limits and continuity
- Exploring derivatives graphically
- Understanding integral areas under curves
- Demonstrating Mean Value Theorem

### Precalculus Course
- Exploring trigonometric functions
- Understanding polynomial behavior
- Analyzing exponential growth/decay
- Comparing function families

### Physics Course
- Wave functions and interference
- Projectile motion trajectories
- Simple harmonic motion
- Damped oscillations

### Engineering Course
- Signal processing functions
- Transfer function responses
- Control system behaviors
- Frequency domain analysis

## Troubleshooting

### Issue: Plot appears blank
**Solution**: Check browser console for JavaScript errors. Verify function doesn't return NaN for any x-values in the domain.

### Issue: Slider doesn't update point
**Solution**: Verify trace index is correct (curve=0, point=1) in `Plotly.restyle` call.

### Issue: Layout too cramped
**Solution**: Reduce container padding to 2-5px. Check margin settings in Plotly layout.

### Issue: Function looks jagged
**Solution**: Increase `numPoints` to 500-1000 for smoother curves.

## References

- [Plotly.js Official Documentation](https://plotly.com/javascript/)
- [Plotly.js Line Charts](https://plotly.com/javascript/line-charts/)
- [MDN Math Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
- [MicroSim Standardization](../microsim-standardization/SKILL.md)
- [Dublin Core Metadata](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)

## Skill Location

`skills/math-function-plotter-plotly/SKILL.md`
