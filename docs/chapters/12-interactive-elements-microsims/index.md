# Interactive Elements and MicroSims

## Summary

This chapter introduces MicroSims, interactive educational simulations built with the p5.js JavaScript library that bring concepts to life through visualization and interactivity. You'll learn about the MicroSim directory structure, including main.html files for simulations and index.md files for documentation. The chapter covers iframe embedding techniques for integrating simulations into your textbook pages.

You'll explore key simulation design principles including seeded randomness for reproducibility, and learn to create interactive controls using sliders and buttons that allow students to experiment with parameters. The chapter also covers MicroSim metadata and broader principles of educational simulation design that ensure your interactive elements effectively support learning objectives.

## Concepts Covered

This chapter covers the following 12 concepts from the learning graph:

1. MicroSim
2. p5.js JavaScript Library
3. Interactive Simulations
4. MicroSim Directory Structure
5. main.html in MicroSims
6. index.md for MicroSim Docs
7. Iframe Embedding
8. Seeded Randomness
9. Interactive Controls (Sliders)
10. Interactive Controls (Buttons)
11. MicroSim Metadata
12. Educational Simulation Design

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction to AI and Intelligent Textbooks](../01-intro-ai-intelligent-textbooks/index.md)
- [Chapter 8: MkDocs Platform and Documentation](../08-mkdocs-platform-documentation/index.md)

---

## Introduction to MicroSims

MicroSims represent a powerful approach to educational content delivery, bridging the gap between static text explanations and hands-on experimentation. A MicroSim (Micro Simulation) is a focused, interactive visualization that demonstrates a single concept or principle through direct manipulation and real-time feedback. Unlike traditional educational simulations that may attempt to model entire systems comprehensively, MicroSims are deliberately constrained in scope, allowing learners to develop intuition about specific phenomena without cognitive overload.

The pedagogical value of interactive simulations in education has been well-documented across multiple disciplines. When learners can adjust parameters and immediately observe the consequences, they develop deeper conceptual understanding than through passive reading alone. MicroSims leverage this insight by providing low-friction experimentation environments where mistakes are safe, reversible, and instructive. For intelligent textbook creators, MicroSims serve as engagement multipliers, transforming abstract concepts into tangible, explorable experiences that students can revisit repeatedly.

In the context of intelligent textbooks built with MkDocs Material, MicroSims function as embedded interactive elements that complement traditional text content. They enable learning analytics through interaction tracking, support personalized content recommendations based on exploration patterns, and provide formative assessment opportunities through challenge scenarios. The following table compares MicroSims to other educational content types:

| Content Type | Interactivity | Scope | Implementation Effort | Learning Analytics Potential |
|--------------|---------------|-------|----------------------|------------------------------|
| Static Text | None | Unlimited | Low | Minimal (time-on-page only) |
| Images/Diagrams | None | Moderate | Low-Moderate | Minimal |
| Video | Linear playback | Moderate | Moderate-High | Basic (completion tracking) |
| Quiz Questions | Limited | Narrow | Low | Good (correctness data) |
| MicroSims | High | Narrow | Moderate | Excellent (interaction patterns) |
| Full Simulations | Very High | Broad | High | Excellent but complex |

## The p5.js Foundation

MicroSims in this textbook framework are built using p5.js, a JavaScript library designed to make coding accessible for artists, designers, educators, and beginners. Created by Lauren McCarthy in 2013, p5.js is a modern interpretation of Processing, the influential creative coding framework originally developed by Ben Fry and Casey Reas. The library provides a gentle learning curve for educators who may not have extensive programming backgrounds, while still offering the power needed to create sophisticated visualizations.

The p5.js library excels in educational contexts for several key reasons. First, it uses an intuitive immediate-mode graphics paradigm where you simply call functions to draw shapes, eliminating the complexity of retained-mode graphics APIs. Second, it provides built-in animation loops through the `draw()` function that executes continuously, making it straightforward to create dynamic visualizations without managing timers or animation frameworks. Third, it includes extensive support for interactivity through mouse, keyboard, and touch events, allowing students to manipulate simulations naturally.

For MicroSim development, p5.js offers several technical advantages. The library handles canvas creation and management automatically, provides coordinate systems that are easy to reason about, includes mathematical utilities for common operations, and maintains a comprehensive ecosystem of contributed libraries for extended functionality. The simplicity of the basic p5.js template reduces the barrier to creating new MicroSims while maintaining professional visual quality.

Here's the fundamental structure every p5.js sketch follows:

- `setup()` function executes once when the program starts, used for initialization
- `draw()` function executes continuously (default 60 frames per second), used for animation
- Global variables store state that persists across draw cycles
- Event handlers respond to user interactions (mousePressed, keyPressed, etc.)

<details markdown="1">
    <summary>p5.js Architecture and Execution Model</summary>
    Type: diagram

    Purpose: Illustrate the execution flow of a p5.js sketch and how setup, draw, and event handlers interact

    Components to show:
    - "Program Start" at top (green circle)
    - "setup()" function box (blue)
    - "draw()" function box (orange) with circular arrow indicating loop
    - "Event Handlers" boxes on the side (purple): mousePressed(), keyPressed(), slider events
    - "Canvas Display" at bottom (gray rectangle)

    Connections:
    - Arrow from "Program Start" to "setup()"
    - Arrow from "setup()" to "draw()"
    - Circular arrow from "draw()" back to itself with label "60 FPS (default)"
    - Arrows from "draw()" to "Canvas Display"
    - Bidirectional arrows between "Event Handlers" and "draw()" labeled "state changes"

    Style: Flowchart with rounded rectangles for functions, circles for start/end states

    Labels:
    - "Runs once" near setup()
    - "Runs continuously" near draw()
    - "Triggered by user input" near Event Handlers
    - "Updates every frame" near Canvas Display

    Annotations:
    - Note: "Global variables accessible throughout"
    - Note: "Event handlers can modify state that draw() uses"

    Color scheme: Blue for initialization, orange for main loop, purple for events, gray for output

    Implementation: Flowchart diagram using Mermaid or similar tool
</details>

## MicroSim Directory Structure

Each MicroSim in an intelligent textbook follows a standardized directory structure that promotes consistency, maintainability, and ease of integration. This organizational pattern separates concerns between the interactive simulation itself, its documentation, and its metadata, following the architectural principle of loose coupling. Understanding this structure is essential for creating, modifying, and debugging MicroSims effectively.

The canonical MicroSim directory structure places each simulation in a dedicated folder within the `/docs/sims/` directory of your MkDocs project. The directory name should use kebab-case (lowercase with hyphens) and clearly indicate the concept being simulated. For example, a simulation demonstrating graph traversal algorithms would be located at `/docs/sims/graph-traversal-visualization/`. This naming convention ensures URLs remain readable and SEO-friendly when the site is deployed.

Within each MicroSim directory, three essential files work together to provide a complete interactive learning experience:

- **main.html** — A standalone HTML file containing the p5.js simulation code, including all JavaScript, CSS, and canvas elements. This file must be fully self-contained so it can be embedded via iframe without external dependencies beyond the p5.js library itself (loaded from CDN).

- **index.md** — A Markdown documentation file that explains what the simulation demonstrates, provides instructions for use, discusses the underlying concepts, and embeds the simulation using an iframe. This file integrates into the MkDocs navigation and serves as the primary learning context.

- **metadata.json** — A JSON file containing Dublin Core metadata about the simulation, including title, creator, subject, description, date, learning objectives, and technical specifications. This metadata supports discovery, cataloging, and potential integration with learning management systems.

The following shows a typical MicroSim file structure:

```
/docs/sims/graph-traversal-visualization/
├── main.html          # Self-contained p5.js simulation
├── index.md           # Documentation and embedding page
└── metadata.json      # Dublin Core metadata
```

Additional files may be present depending on the complexity of the simulation. Some MicroSims include separate CSS files for sophisticated styling, JSON data files for configuration, or supporting image assets. However, the three core files listed above are mandatory for all MicroSims in the intelligent textbook framework.

<details markdown="1">
    <summary>MicroSim File Relationship Diagram</summary>
    Type: diagram

    Purpose: Show how the three core MicroSim files relate to each other and integrate into the MkDocs textbook

    Components to show:
    - MkDocs Navigation (top level, light gray box)
    - index.md (blue document icon, within MkDocs)
    - iframe element (orange rounded box, within index.md)
    - main.html (green document icon, pointed to by iframe)
    - p5.js simulation (red canvas, within main.html)
    - metadata.json (purple document icon, separate)
    - Learning Management System (optional, dotted line from metadata.json)

    Connections:
    - MkDocs Navigation → index.md (solid arrow, "includes")
    - index.md → iframe element (solid arrow, "contains")
    - iframe element → main.html (solid arrow, "embeds")
    - main.html → p5.js simulation (solid arrow, "renders")
    - metadata.json → Learning Management System (dotted arrow, "can export to")
    - metadata.json → index.md (dotted arrow, "describes")

    Style: Block diagram with document icons and containers

    Labels:
    - "Student navigates here" near index.md
    - "Sandbox isolation" near iframe
    - "Self-contained, interactive" near main.html
    - "Discovery & cataloging" near metadata.json

    Annotations:
    - Note near iframe: "Provides security boundary"
    - Note near main.html: "Loads p5.js from CDN"

    Color scheme: Blue for documentation, green for code, purple for metadata, orange for integration

    Implementation: Block diagram with icons
</details>

## Creating the main.html File

The `main.html` file serves as the executable heart of a MicroSim, packaging the p5.js sketch into a standalone web page that can be embedded anywhere via iframe. This file must be entirely self-contained, with all JavaScript code, CSS styling, and HTML structure included in a single document. The only external dependency permitted is the p5.js library itself, which is loaded from a content delivery network (CDN) to ensure reliability and leverage browser caching.

A well-structured `main.html` file follows a consistent template that divides the page into two primary regions: the canvas area where p5.js renders visualizations, and the control panel where interactive elements like sliders, buttons, and dropdowns reside. This left-right or top-bottom split provides a clear visual hierarchy, separating the simulation display from the manipulation interface. For most educational purposes, an 800x600 pixel canvas with a 200-pixel-wide control panel provides adequate space without overwhelming smaller screens.

The HTML document begins with standard boilerplate including DOCTYPE declaration, meta tags for character encoding and viewport configuration, and a title that matches the MicroSim concept. The head section loads the p5.js library from the cdnjs or jsdelivr CDN, ensuring the latest stable version is available. Internal CSS defines the layout using flexbox or grid, establishes the visual styling for controls, and ensures responsive behavior for different viewport sizes.

Within the body, the JavaScript section contains the complete p5.js sketch. This includes global variable declarations, the `setup()` function for initialization, the `draw()` function for continuous rendering, event handler functions for interactivity, and any helper functions needed for calculations or algorithms. The code should be well-commented to support future modifications and serve as a learning resource for students interested in the implementation details.

Key requirements for the `main.html` structure:

- Load p5.js from CDN with integrity hash for security
- Define canvas and control panel regions with clear visual separation
- Use semantic HTML5 elements (canvas, aside, button, input, label)
- Include CSS for layout, styling, and responsive design
- Implement p5.js sketch with setup(), draw(), and event handlers
- Add comments explaining the simulation logic and algorithms
- Set default parameter values that produce interesting behavior
- Ensure the simulation starts in a meaningful state

<details markdown="1">
    <summary>Basic MicroSim Template Structure</summary>
    Type: diagram

    Purpose: Show the HTML structure and organization of a typical main.html file

    Visual style: Hierarchical tree diagram showing HTML element nesting

    Components to show:
    <!DOCTYPE html> (root, gray)
    └── <html> (light blue)
        └── <head> (yellow)
            ├── <meta charset="utf-8">
            ├── <meta viewport>
            ├── <title>
            ├── <script src="p5.js CDN">
            └── <style> (contains CSS for layout)
        └── <body> (light green)
            ├── <main> (flex container)
            │   ├── <div id="canvas-container"> (left/top region)
            │   │   └── <!-- p5.js creates canvas here -->
            │   └── <aside id="controls"> (right/bottom region)
            │       ├── <label> + <input type="range"> (sliders)
            │       ├── <button> (action buttons)
            │       └── <select> (dropdowns)
            └── <script> (contains p5.js code)
                ├── // Global variables
                ├── function setup() { }
                ├── function draw() { }
                └── // Event handlers

    Connections:
    - Tree structure showing parent-child relationships
    - Annotations showing purpose of each section

    Labels:
    - "Document structure" at top
    - "External resources" near head
    - "Layout and styling" near style
    - "Visual display" near canvas-container
    - "User interaction" near controls
    - "Simulation logic" near script

    Annotations:
    - Note: "p5.js automatically creates canvas in this div"
    - Note: "All interactivity defined in event handlers"
    - Note: "CSS flexbox for responsive layout"

    Color coding:
    - Gray: Document root
    - Yellow: Metadata and resources
    - Light green: Body structure
    - Light blue: Interactive elements
    - Orange: JavaScript code

    Implementation: Tree diagram or hierarchical block diagram
</details>

## Writing the index.md Documentation

The `index.md` file serves as the pedagogical wrapper around the MicroSim, providing context, instructions, learning objectives, and reflective prompts that transform a standalone simulation into an integrated learning experience. This Markdown document becomes a page in the MkDocs navigation hierarchy, appearing alongside other chapter content while offering a dedicated space for interactive exploration. The quality of the `index.md` documentation directly impacts how effectively students engage with and learn from the MicroSim.

A comprehensive `index.md` file follows a structured format that guides students through increasingly sophisticated engagement with the simulation. The document opens with a clear statement of what concept the MicroSim demonstrates and why this concept matters in the broader context of the course. This framing activates prior knowledge and establishes relevance. The introduction should connect to previously covered material, referencing specific chapters or concepts that provide necessary background understanding.

Following the introduction, the documentation provides explicit instructions for using the simulation. This section describes each interactive control (sliders, buttons, dropdowns), explains what parameters they adjust, and suggests specific experiments students should try. Effective instructions follow a progressive disclosure pattern: basic interactions first, followed by more sophisticated explorations. For example, instructions might guide students to first observe default behavior, then adjust one parameter at a time, and finally explore interactions between multiple parameters.

The core of the `index.md` file is the iframe embedding of the `main.html` simulation. The iframe should be sized appropriately for the content, typically matching the canvas dimensions plus control panel width. The Markdown syntax for embedding uses raw HTML, as MkDocs passes HTML through unchanged. After the embedded simulation, the documentation includes guided exploration questions, connections to theory, and suggestions for further investigation.

The structure of an effective `index.md` file:

1. **Concept Overview** — What the MicroSim demonstrates and why it matters
2. **Prerequisites** — Links to chapters or concepts students should understand first
3. **Learning Objectives** — Specific outcomes students should achieve through exploration
4. **Instructions** — How to use the controls and what to try
5. **Embedded Simulation** — The iframe containing main.html
6. **Guided Exploration** — Specific experiments with questions to answer
7. **Conceptual Connections** — How the simulation relates to theory
8. **Extensions** — Advanced topics or related concepts to explore next
9. **References** — Links to related chapters, external resources, or research

When embedding the simulation, use the following iframe template:

```html
<iframe src="./main.html" width="1000" height="600" frameborder="0"></iframe>
```

The `src` attribute uses a relative path (`./main.html`) since both files are in the same directory. The width and height should accommodate the canvas plus controls comfortably. Setting `frameborder="0"` removes the default border for cleaner integration. For responsive designs, consider wrapping the iframe in a container div with appropriate CSS classes from the MkDocs Material theme.

## Iframe Embedding Techniques

Embedding MicroSims into MkDocs pages via iframes provides several technical and pedagogical advantages that align with best practices for web-based learning environments. The iframe (inline frame) element creates a nested browsing context, effectively sandboxing the p5.js simulation within its own document space. This isolation prevents CSS conflicts, namespace collisions in JavaScript, and ensures that errors or performance issues within the simulation don't affect the parent page's functionality or the broader MkDocs site.

From a security perspective, iframes provide a natural boundary between trusted navigation content and potentially untrusted interactive code. While MicroSims you create are trusted, the iframe sandbox serves as a defense-in-depth layer that limits what the embedded content can access. Modern browsers enforce same-origin policies that prevent iframes from accessing parent page content unless explicitly permitted, protecting student navigation state and preventing unintended interactions between multiple embedded simulations on the same page.

The technical implementation of iframe embedding in MkDocs Material is straightforward because Markdown processors pass raw HTML through unchanged. This means you can insert iframe elements directly into your `index.md` files without special plugins or extensions. However, several attributes and best practices enhance the user experience and accessibility of embedded MicroSims.

Essential iframe attributes for MicroSim embedding:

- `src` — Relative path to main.html (use `./main.html` for same directory)
- `width` — Total width in pixels (canvas + controls + margins)
- `height` — Total height in pixels (canvas + controls + margins)
- `frameborder` — Set to "0" for clean integration
- `title` — Descriptive title for screen readers (accessibility requirement)
- `loading` — Set to "lazy" for performance optimization on long pages
- `allow` — Permissions policy (typically not needed for p5.js simulations)

For responsive designs that adapt to different screen sizes, consider using CSS wrapper techniques instead of fixed iframe dimensions. The MkDocs Material theme provides responsive utilities, or you can define custom CSS that makes iframes scale proportionally. The following example shows a responsive iframe wrapper:

```html
<div style="position: relative; padding-bottom: 60%; height: 0; overflow: hidden;">
    <iframe src="./main.html"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            title="Graph Traversal Visualization"
            loading="lazy">
    </iframe>
</div>
```

This wrapper uses the "padding-bottom percentage trick" where the percentage is calculated as (height/width) × 100%. For a 1000×600 simulation, that's (600/1000) × 100% = 60%. The absolutely positioned iframe then fills this responsive container.

<details markdown="1">
    <summary>Responsive Iframe Embedding MicroSim</summary>
    Type: microsim

    Learning objective: Demonstrate how iframe embedding works and how responsive wrappers adapt to different viewport sizes

    Canvas layout (1000x600px):
    - Left side (700x600): Visual demonstration area
    - Right side (300x600): Control panel

    Visual elements in demonstration area:
    - Nested rectangle structure showing iframe within page
    - Outer rectangle (light gray): "MkDocs Page Content"
    - Middle rectangle (white): "Iframe Boundary"
    - Inner rectangle (light blue): "MicroSim Canvas"
    - Labels and borders clearly showing each level
    - Resize handles on outer rectangle to show responsive behavior

    Interactive controls (right panel):
    - Slider: "Viewport Width" (300px - 1200px, default 1000px)
    - Slider: "Viewport Height" (200px - 800px, default 600px)
    - Checkbox: "Show Frame Border" (toggle iframe border visibility)
    - Checkbox: "Responsive Wrapper" (toggle between fixed and responsive sizing)
    - Button: "Reset to Defaults"
    - Display: Current dimensions (viewport and iframe)

    Default parameters:
    - Viewport width: 1000px
    - Viewport height: 600px
    - Frame border: visible
    - Responsive wrapper: off

    Behavior:
    - When viewport sliders move, outer rectangle resizes
    - If responsive wrapper enabled, inner rectangles scale proportionally
    - If responsive wrapper disabled, inner rectangles may clip or overflow
    - Frame border checkbox toggles visibility of iframe boundary
    - Labels update to show current pixel dimensions
    - Color coding: gray (page), white (iframe), blue (canvas), red (clipping/overflow)

    Annotations:
    - Text showing "Parent Page Context" outside iframe
    - Text showing "Sandboxed Simulation Context" inside iframe
    - Arrow labels showing CSS properties used for responsive behavior

    Implementation notes:
    - Use p5.js for rendering
    - Demonstrate actual scaling calculations
    - Show overflow scenarios when responsive wrapper disabled
    - Include visual indicators for aspect ratio preservation
</details>

## Interactive Controls: Sliders

Sliders represent one of the most effective interaction paradigms for educational simulations, providing continuous parameter adjustment with immediate visual feedback. In p5.js MicroSims, sliders allow students to explore parameter spaces intuitively, developing understanding of how quantitative changes affect system behavior. Unlike discrete controls such as buttons or dropdowns, sliders make the relationship between input and output visible through analog manipulation, supporting the development of quantitative intuition.

The HTML5 range input (`<input type="range">`) provides native slider functionality that works across all modern browsers without requiring custom JavaScript widgets. These native controls are accessible by default, support keyboard navigation, and provide consistent behavior across platforms. In p5.js simulations, sliders typically reside in the control panel region and connect to global variables that the `draw()` function reads on each frame, creating a reactive relationship between user input and visual output.

Creating an effective slider control requires several components working together. The HTML defines the input element with minimum, maximum, step, and default values. A corresponding label provides textual description and displays the current numeric value. JavaScript event listeners capture changes to the slider and update global simulation variables. Finally, the p5.js `draw()` function uses these variables to modify visual elements, closing the feedback loop from user action to displayed result.

Here's a complete example of slider implementation in a MicroSim:

```html
<!-- HTML Control Panel -->
<div id="controls">
    <label>
        Gravity: <span id="gravityValue">9.8</span> m/s²
        <input type="range" id="gravitySlider"
               min="0" max="20" step="0.1" value="9.8">
    </label>
</div>

<script>
// Global variable (p5.js sketch)
let gravity = 9.8;

// Event listener
document.getElementById('gravitySlider').addEventListener('input', function(e) {
    gravity = parseFloat(e.target.value);
    document.getElementById('gravityValue').textContent = gravity.toFixed(1);
});

function draw() {
    // Use gravity variable in physics calculations
    velocity += gravity * deltaTime;
    // ... rest of simulation
}
</script>
```

Best practices for slider design in educational MicroSims:

- **Clear labels** — Include both the parameter name and units of measurement
- **Visible current value** — Display the numeric value that updates as slider moves
- **Appropriate ranges** — Set min/max to show interesting behavior without extremes that break the simulation
- **Meaningful step values** — Match step size to the precision that matters for the concept
- **Sensible defaults** — Initialize to a value that demonstrates the core concept clearly
- **Immediate feedback** — Update the visualization every frame, not just on mouseRelease
- **Multiple slider interactions** — Design simulations where adjusting combinations reveals patterns

Sliders excel when exploring continuous phenomena such as physical constants, probability distributions, growth rates, or timing parameters. They make abstract numerical values concrete by tying them to visual consequences, helping students build mental models that connect quantitative inputs to qualitative system behaviors.

## Interactive Controls: Buttons

Buttons provide discrete, action-oriented controls that complement the continuous adjustment offered by sliders. In educational MicroSims, buttons serve multiple pedagogical functions: triggering state transitions, resetting simulations to initial conditions, stepping through algorithms incrementally, toggling between visualization modes, and randomizing parameters for exploratory learning. The discrete nature of button interactions makes them ideal for actions with clear before-and-after states, where the moment of transition itself carries pedagogical significance.

The HTML5 button element (`<button>`) provides semantic, accessible interaction that clearly communicates affordance—students immediately recognize buttons as clickable elements that perform actions. Unlike sliders which encourage gradual exploration, buttons encourage hypothesis testing: students predict what will happen, click the button, and observe the outcome. This prediction-action-observation cycle aligns with constructivist learning theories and supports active engagement with conceptual material.

Common button patterns in educational MicroSims include:

- **Start/Stop buttons** — Control animation playback, allowing students to pause and examine states
- **Reset buttons** — Return simulation to initial conditions for repeated experimentation
- **Step buttons** — Advance algorithms one iteration at a time for detailed examination
- **Randomize buttons** — Generate new scenarios, supporting exploration of edge cases
- **Mode toggles** — Switch between different visualization approaches for the same data
- **Example selection** — Load predefined scenarios that illustrate specific concepts
- **Challenge buttons** — Present problems or questions for students to solve using the simulation

Implementing buttons in p5.js MicroSims follows a straightforward pattern. HTML defines the button element with descriptive text and semantic meaning. JavaScript event listeners capture click events and call functions that modify simulation state. The p5.js sketch responds to these state changes in the `draw()` function, updating the visualization accordingly. Unlike sliders which read input values continuously, buttons typically set flags or invoke functions that have immediate effects.

Example button implementation for algorithm stepping:

```html
<!-- HTML Control Panel -->
<div id="controls">
    <button id="stepButton">Step Forward</button>
    <button id="resetButton">Reset</button>
    <button id="autoButton">Auto Run</button>
</div>

<script>
// Global state variables
let currentStep = 0;
let isAutoRunning = false;
let algorithm = [];  // Array of algorithm states

// Step button
document.getElementById('stepButton').addEventListener('click', function() {
    if (currentStep < algorithm.length - 1) {
        currentStep++;
    }
});

// Reset button
document.getElementById('resetButton').addEventListener('click', function() {
    currentStep = 0;
    isAutoRunning = false;
});

// Auto run toggle
document.getElementById('autoButton').addEventListener('click', function() {
    isAutoRunning = !isAutoRunning;
    this.textContent = isAutoRunning ? 'Pause' : 'Auto Run';
});

function draw() {
    // Render algorithm state at currentStep
    displayAlgorithmState(algorithm[currentStep]);

    // Auto-advance if enabled
    if (isAutoRunning && frameCount % 60 === 0) {  // Every second
        if (currentStep < algorithm.length - 1) {
            currentStep++;
        } else {
            isAutoRunning = false;
        }
    }
}
</script>
```

Effective button design for educational purposes requires attention to labeling, feedback, and state management. Button labels should use action verbs that clearly communicate what will happen ("Start Traversal" rather than "Go"). Visual feedback such as color changes, disabled states, or confirmation messages helps students understand the effects of their actions. For toggleable buttons, the label or appearance should reflect the current state, making it clear whether clicking will enable or disable a feature.

<details markdown="1">
    <summary>Algorithm Visualization with Step Controls MicroSim</summary>
    Type: microsim

    Learning objective: Demonstrate how button controls enable step-by-step exploration of algorithms, using bubble sort as an example

    Canvas layout (900x600px):
    - Left side (600x600): Visualization area showing array bars
    - Right side (300x600): Control panel

    Visual elements:
    - Array of 12 vertical bars with varying heights (representing values)
    - Two bars highlighted when being compared (yellow outline)
    - Sorted portion of array shown in green
    - Unsorted portion shown in blue
    - Current pass number and comparisons count displayed

    Interactive controls (right panel):
    - Button: "Step Forward" (advance one comparison)
    - Button: "Step to End of Pass" (complete current pass)
    - Button: "Reset" (generate new random array)
    - Button: "Auto Run" (toggle automatic stepping)
    - Slider: "Animation Speed" (100-2000ms per step, default 500ms)
    - Dropdown: "Array Size" (5, 8, 12, 16 elements)
    - Checkbox: "Show Comparisons" (display comparison count)
    - Display: Current state ("Comparing elements 3 and 4")

    Default parameters:
    - Array size: 12 elements
    - Animation speed: 500ms
    - Show comparisons: enabled
    - Initial state: random unsorted array

    Behavior:
    - "Step Forward" highlights two elements, compares, swaps if needed
    - "Step to End of Pass" completes the current bubble sort pass
    - "Reset" generates new random array and resets algorithm state
    - "Auto Run" toggles automatic stepping at specified speed
    - Animation speed slider only affects auto run timing
    - Array size dropdown generates new array when changed
    - Visual feedback shows algorithm progress with color coding
    - Status text explains what comparison is happening

    Algorithm visualization:
    - Use bubble sort for clarity and simplicity
    - Highlight elements being compared in yellow
    - Mark sorted elements in green
    - Mark unsorted elements in blue
    - Show swap animation when elements exchange positions
    - Display pass number and total comparisons

    Implementation notes:
    - Use p5.js for rendering bars as rectangles
    - Store array and algorithm state in global variables
    - Implement bubble sort with step-by-step state capture
    - Use seeded randomness for reproducible arrays
    - Include visual transitions for swaps (smooth animation)
</details>

## Ensuring Reproducibility with Seeded Randomness

Randomness plays a crucial role in educational simulations, introducing variability that helps students see patterns across different scenarios rather than memorizing a single example. However, pure randomness creates a pedagogical challenge: when every student sees different behavior, instruction becomes difficult, debugging is nearly impossible, and students cannot easily share or compare their explorations. Seeded randomness resolves this tension by making randomness reproducible—simulations generate different scenarios, but the same seed always produces the same sequence of random values.

In computational terms, seeded randomness uses deterministic pseudorandom number generators (PRNGs) that produce sequences of numbers that appear random but are entirely determined by an initial seed value. The p5.js library includes a `randomSeed()` function that sets the seed for its internal PRNG. Once seeded, subsequent calls to `random()`, `noise()`, and related functions produce the same sequence every time the program runs. This determinism enables several important capabilities for educational MicroSims.

The pedagogical benefits of seeded randomness in MicroSims include:

- **Debugging** — Developers can reproduce issues exactly by using the same seed
- **Instruction** — Instructors can reference specific scenarios by seed value
- **Comparison** — Students can share seeds to explore the same scenario and compare approaches
- **Assessment** — Quiz questions can reference specific seeds for consistent grading
- **Documentation** — Screenshots and examples in documentation remain accurate
- **Progressive disclosure** — Carefully chosen seeds can demonstrate concepts in increasing complexity

Implementing seeded randomness in a p5.js MicroSim requires only a few lines of code. The simplest approach uses a fixed seed value that remains constant across all page loads. This creates a consistent default experience where every student sees the same initial state. A more sophisticated approach provides a text input or dropdown where students can enter different seed values, enabling exploration of alternative scenarios while maintaining reproducibility.

Basic seeded randomness implementation:

```javascript
function setup() {
    createCanvas(800, 600);

    // Set random seed for reproducibility
    randomSeed(42);  // The answer to everything

    // Generate random elements
    // These will be the same every time the simulation runs
    for (let i = 0; i < 20; i++) {
        let x = random(width);
        let y = random(height);
        let diameter = random(20, 80);
        circles.push({x: x, y: y, d: diameter});
    }
}
```

Advanced implementation with user-controllable seed:

```html
<!-- HTML Control Panel -->
<div id="controls">
    <label>
        Random Seed:
        <input type="number" id="seedInput" value="42" min="1" max="9999">
    </label>
    <button id="regenerateButton">Regenerate</button>
</div>

<script>
let seed = 42;

document.getElementById('regenerateButton').addEventListener('click', function() {
    seed = parseInt(document.getElementById('seedInput').value);
    regenerateSimulation();
});

function regenerateSimulation() {
    randomSeed(seed);
    // Clear and regenerate all random elements
    circles = [];
    for (let i = 0; i < 20; i++) {
        circles.push({
            x: random(width),
            y: random(height),
            d: random(20, 80)
        });
    }
}
</script>
```

When documenting MicroSims that use seeded randomness, include notes about interesting seed values in the `index.md` file. For example: "Try seed 1234 to see a highly connected graph" or "Seed 5678 demonstrates an edge case with isolated nodes." This guided exploration helps students discover important scenarios without exhaustive random searching.

The choice of default seed value can itself be pedagogically meaningful. Seed 42 (a reference to *The Hitchhiker's Guide to the Galaxy*) is a common choice in computer science education. Alternatively, choose seeds that produce clear demonstrations of the concept being taught. Test multiple seeds during development and select ones that show typical behavior, interesting edge cases, or progressive levels of complexity.

## MicroSim Metadata Standards

Metadata provides structured information about MicroSims that supports discovery, cataloging, assessment alignment, and potential integration with learning management systems. Following Dublin Core metadata standards ensures consistency across MicroSims and compatibility with educational technology ecosystems that consume standardized metadata formats. The `metadata.json` file in each MicroSim directory stores this information in a machine-readable JSON format that can be parsed by build tools, indexed by search systems, or exported to LMS platforms.

Dublin Core is an internationally recognized metadata standard (ISO 15836) originally developed for describing web resources, now widely adopted in educational contexts. The standard defines 15 core elements that capture essential information about any resource: title, creator, subject, description, publisher, contributor, date, type, format, identifier, source, language, relation, coverage, and rights. For MicroSims in intelligent textbooks, a subset of these elements provides sufficient metadata while avoiding documentation overhead.

The essential Dublin Core elements for MicroSim metadata:

| Element | Description | Example |
|---------|-------------|---------|
| title | Name of the MicroSim | "Graph Traversal Visualization" |
| creator | Author or development team | "Claude Skills Framework" |
| subject | Concept or topic demonstrated | "Graph Algorithms, BFS, DFS" |
| description | Brief explanation of learning value | "Interactive visualization comparing breadth-first and depth-first graph traversal strategies" |
| date | Creation or last modified date | "2025-01-15" |
| type | Resource type | "InteractiveSim" or "Simulation" |
| format | Technical format | "text/html, application/javascript, p5.js" |
| identifier | Unique ID within textbook | "microsim-graph-traversal-viz" |
| language | Natural language used | "en" (English) |
| rights | License or usage terms | "CC BY-SA 4.0" |

Additional educational metadata fields extend Dublin Core for learning-specific purposes:

| Field | Description | Example |
|-------|-------------|---------|
| learningObjectives | Specific outcomes students should achieve | ["Understand difference between BFS and DFS", "Identify traversal order patterns"] |
| bloomsLevel | Taxonomy level(s) addressed | ["Understand", "Apply", "Analyze"] |
| prerequisites | Required prior knowledge | ["Basic graph concepts", "Tree data structures"] |
| estimatedTime | Expected interaction duration | "10-15 minutes" |
| difficulty | Complexity level | "Intermediate" |
| keywords | Searchable tags | ["graph", "traversal", "algorithm", "visualization"] |

A complete `metadata.json` file structure:

```json
{
    "dublin_core": {
        "title": "Graph Traversal Visualization",
        "creator": "Claude Skills Framework",
        "subject": "Graph Algorithms, Breadth-First Search, Depth-First Search",
        "description": "Interactive p5.js simulation comparing breadth-first search (BFS) and depth-first search (DFS) traversal strategies on graph data structures, demonstrating visit order and algorithmic differences",
        "date": "2025-01-15",
        "type": "InteractiveSim",
        "format": "text/html, application/javascript, p5.js",
        "identifier": "microsim-graph-traversal-viz",
        "language": "en",
        "rights": "CC BY-SA 4.0"
    },
    "educational": {
        "learningObjectives": [
            "Explain the difference between breadth-first and depth-first traversal strategies",
            "Predict the visit order for a given graph and algorithm",
            "Analyze the stack/queue data structures underlying each algorithm"
        ],
        "bloomsLevels": ["Understand", "Apply", "Analyze"],
        "prerequisites": [
            "Understanding of graph terminology (nodes, edges, adjacency)",
            "Familiarity with tree data structures",
            "Basic knowledge of stack and queue abstract data types"
        ],
        "estimatedTime": "10-15 minutes",
        "difficulty": "Intermediate",
        "keywords": ["graph", "traversal", "BFS", "DFS", "algorithm", "visualization", "data structures"]
    },
    "technical": {
        "version": "1.0",
        "p5jsVersion": "1.7.0",
        "canvasSize": "700x600",
        "controlPanelSize": "300x600",
        "parameters": [
            {"name": "algorithm", "type": "dropdown", "options": ["BFS", "DFS"]},
            {"name": "animationSpeed", "type": "slider", "min": 50, "max": 1000, "default": 500}
        ]
    }
}
```

This metadata serves multiple purposes throughout the MicroSim lifecycle. During development, it provides a specification checklist ensuring all educational requirements are met. During deployment, build scripts can extract metadata to generate navigation, search indexes, or course catalogs. During instruction, learning management systems can import metadata to align simulations with course objectives, track student interactions, and assess learning outcomes. Well-maintained metadata transforms a collection of individual simulations into a structured, discoverable learning resource library.

## Principles of Educational Simulation Design

Designing effective educational simulations requires balancing technical capabilities, pedagogical goals, and cognitive load management. While the technical implementation of MicroSims using p5.js is relatively straightforward, creating simulations that genuinely enhance learning requires attention to educational design principles drawn from research in instructional technology, cognitive science, and visualization theory. The following principles provide a framework for evaluating and improving MicroSim designs.

**Focus on a single concept.** The "Micro" in MicroSim is deliberate—these simulations work best when they demonstrate one concept clearly rather than attempting to model complex systems comprehensively. A focused simulation allows students to develop deep intuition about a specific phenomenon without cognitive overload from extraneous details. If you find yourself adding many controls or visualization modes, consider whether the simulation should be split into multiple MicroSims, each addressing a different facet of the broader topic.

**Provide immediate visual feedback.** The power of interactive simulations comes from the tight coupling between user action and visual response. Every slider movement, button click, or parameter change should produce immediate, visible consequences in the visualization. This immediacy helps students build causal mental models connecting inputs to outputs. Avoid designs where students must click "Apply" or "Calculate" buttons to see results—continuous reactivity is preferable in most educational contexts.

**Enable hypothesis testing.** Effective simulations encourage students to form predictions, test them, observe outcomes, and refine their understanding. Design controls and scenarios that invite questions: "What happens if I increase this parameter?" "How does this algorithm behave with different data?" "What's the relationship between these two variables?" Include suggested experiments in the `index.md` documentation that guide students through increasingly sophisticated explorations.

**Support multiple levels of engagement.** Students approach simulations with varying prior knowledge and learning goals. Design MicroSims that support both surface-level observation (watching animations with default settings) and deep exploration (manipulating multiple parameters, testing edge cases, connecting to theory). Provide suggested starting points for different learning objectives, and include both guided explorations and open-ended challenges.

**Make abstract concepts tangible.** Use simulations to transform abstract ideas into concrete, manipulable objects. Algorithm performance becomes visible through animation timing. Mathematical relationships become adjustable through sliders. Probability distributions become observable through repeated random sampling. The visual representation should leverage spatial reasoning, color coding, animation, and interactive manipulation to make invisible concepts perceivable.

**Include realistic constraints and edge cases.** While simulations simplify reality, they should respect important constraints and reveal edge cases that deepen understanding. If simulating physical systems, respect conservation laws. If demonstrating algorithms, include scenarios where performance degrades or special cases arise. These realistic touches prevent students from forming oversimplified mental models that fail in practical applications.

**Maintain performance and responsiveness.** Educational simulations must run smoothly across a range of devices, from high-end desktops to budget laptops and tablets. Aim for consistent 60 frames per second (FPS) performance even with maximum complexity settings. Use efficient algorithms, limit particle counts, and optimize drawing operations. If performance becomes problematic, simplify the visualization or reduce default complexity rather than accepting laggy, unresponsive behavior that frustrates learners.

**Design for accessibility.** Not all students interact with simulations in the same ways. Ensure keyboard navigation works for all controls. Provide text alternatives for color coding (using both color and shape/pattern). Include descriptions of what's happening for screen reader users. Test with different input methods and assistive technologies. Accessibility is not just ethical—it often improves usability for all students.

**Encourage exploration through seeded randomness.** As discussed earlier, use seeded randomness to create variety while maintaining reproducibility. Provide a "Randomize" button that generates new scenarios with different seeds. Document interesting seed values that demonstrate specific concepts. This approach balances the engagement value of novelty with the pedagogical value of shared reference points.

**Align with learning objectives.** Every MicroSim should map clearly to specific learning objectives from your course or chapter. The simulation should help students achieve outcomes like "explain the difference between X and Y," "predict the behavior of system Z under different conditions," or "analyze the trade-offs between approaches A and B." If you cannot articulate what learning objective a simulation addresses, reconsider whether it belongs in your textbook.

<details markdown="1">
    <summary>MicroSim Design Quality Checklist</summary>
    Type: infographic

    Purpose: Provide a visual, interactive checklist for evaluating educational simulation design quality

    Layout: Tabbed interface with five categories, each expandable to show detailed criteria

    Categories and criteria:

    **1. Pedagogical Alignment**
    - [ ] Focuses on a single concept or closely related concept cluster
    - [ ] Maps to specific learning objectives from course/chapter
    - [ ] Addresses appropriate Bloom's taxonomy level(s)
    - [ ] Includes guided exploration questions in documentation
    - [ ] Supports hypothesis testing and experimentation
    - [ ] Provides scaffolding for different knowledge levels

    **2. Interaction Design**
    - [ ] Provides immediate visual feedback to all interactions
    - [ ] Controls are clearly labeled with units where applicable
    - [ ] Default parameter values demonstrate core concept clearly
    - [ ] Multiple sliders/controls enable exploration of relationships
    - [ ] Reset button returns to meaningful initial state
    - [ ] Randomize button (if applicable) generates new scenarios

    **3. Visual Design**
    - [ ] Visual elements are clear and uncluttered
    - [ ] Color coding is consistent and meaningful
    - [ ] Important features are visually prominent
    - [ ] Animation speed supports observation and analysis
    - [ ] Canvas size is appropriate for content complexity
    - [ ] Layout separates visualization from controls clearly

    **4. Technical Quality**
    - [ ] Maintains 60 FPS performance on target devices
    - [ ] Uses seeded randomness for reproducibility
    - [ ] main.html is self-contained (only p5.js external dependency)
    - [ ] Code is well-commented for future modification
    - [ ] No console errors or warnings
    - [ ] Works across modern browsers (Chrome, Firefox, Safari, Edge)

    **5. Accessibility & Documentation**
    - [ ] Keyboard navigation works for all controls
    - [ ] Color coding supplemented by shape/pattern/text
    - [ ] iframe has descriptive title attribute
    - [ ] index.md provides clear usage instructions
    - [ ] metadata.json is complete and accurate
    - [ ] Interesting seed values documented
    - [ ] Prerequisites clearly stated

    Interactive features:
    - Click each category to expand/collapse detailed criteria
    - Checkbox items can be checked off during review
    - Progress bar shows percentage of criteria met in each category
    - Overall quality score displayed (percentage of all boxes checked)
    - Color coding: Red (<60%), Yellow (60-80%), Green (>80%)
    - "Export Report" button generates markdown checklist with current state

    Visual style: Modern checklist interface with expandable sections
    Color scheme: Blue headers, green checkmarks, amber warnings
    Implementation: HTML/CSS/JavaScript with localStorage for persistence
</details>

## Summary and Key Takeaways

Interactive MicroSims transform intelligent textbooks from static information repositories into dynamic learning environments where students actively construct understanding through experimentation and exploration. Built with the p5.js JavaScript library, these focused simulations demonstrate single concepts through immediate visual feedback, adjustable parameters, and reproducible scenarios. The standardized MicroSim architecture—comprising `main.html` for the simulation, `index.md` for pedagogical context, and `metadata.json` for discovery and cataloging—ensures consistency while supporting integration with the broader MkDocs Material textbook framework.

Effective MicroSim design balances technical implementation with pedagogical intention. Sliders and buttons provide intuitive interaction patterns that encourage hypothesis testing and parameter space exploration. Seeded randomness generates variability while maintaining reproducibility, enabling shared reference points between students and instructors. Iframe embedding provides security boundaries and prevents namespace conflicts while maintaining seamless visual integration with surrounding content.

The principles of educational simulation design emphasize focus, feedback, and alignment with learning objectives. By concentrating on single concepts, providing immediate visual responses to interactions, and connecting simulations to specific course outcomes, MicroSims become powerful tools for making abstract ideas tangible and testable. As you create MicroSims for your own intelligent textbooks, use these principles and patterns to craft experiences that genuinely enhance student understanding rather than merely adding interactivity for its own sake.

Key concepts covered in this chapter:

- **MicroSims** are focused, interactive simulations demonstrating single educational concepts
- **p5.js** provides an accessible yet powerful framework for creative coding and visualization
- **Interactive simulations** engage students in active learning through manipulation and observation
- **MicroSim directory structure** standardizes organization with main.html, index.md, and metadata.json
- **main.html** contains self-contained p5.js simulations with canvas and control panel regions
- **index.md** provides pedagogical context, instructions, and iframe embedding
- **Iframe embedding** sandboxes simulations while integrating them seamlessly into MkDocs pages
- **Seeded randomness** balances variability with reproducibility for educational purposes
- **Interactive controls (sliders)** enable continuous parameter exploration with immediate feedback
- **Interactive controls (buttons)** trigger discrete actions and state transitions
- **MicroSim metadata** follows Dublin Core standards for discovery, cataloging, and LMS integration
- **Educational simulation design principles** guide creation of pedagogically effective interactive elements
