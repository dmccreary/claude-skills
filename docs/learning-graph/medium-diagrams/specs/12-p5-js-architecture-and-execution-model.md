# p5.js Architecture and Execution Model

**Chapter:** 12 - Interactive Elements Microsims
**Generator:** mermaid-generator
**Match Score:** 94/100
**Difficulty:** Medium

## Specification

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