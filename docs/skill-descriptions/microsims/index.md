# Educational MicroSim Skills

Educational MicroSims are lightweight, interactive educational simulations designed for browser-based learning. 
MicroSims are designed to run in a rectangular `iframe` placed within the a page of a textbook.
The default height of a MicroSim is 500px and they are designed to be width-responsive so they
will adapt to various screen sizes and window resize events.

## MicroSim Generator List

This list is ordered based on the most general purpose tools to the most case specific tool.

1. **General MicroSim with p5:** - use for most general MicroSim used for interactive animations and simulations
2. **General Chart Generation with ChartJS** - used for generating charts
3. **Mermaid Generator**  - used for static workflow and flow chart diagrams
4. **Vis Network Graph Generator** - used to generate interactive network graph diagrams
5. **Math Function Plot Generator** - uses the powerful Plotly.js library for plotting math functions
6. **Timeline Generator** - used to generate timelines from a list of events
7. **Map Generator** - generates maps using the Leaflet library
8. **Venn Diagram Generator** - generates Venn Diagrams
9. **Bubble Chart Generator** - specialize to only generate bubble charts

## Common Elements to All MicroSims

All MicroSims are designed to run in a non-scrolling iframe that contains width-responsive drawing elements.

Sample `iframe` 

```html
<iframe src="http://example.com/microsims/my-microsim/main.html" height="500px" width="100%" scrolling="no">
```

MicroSims are packaged in a directory with the following files:

1. main.html - holds the main HTML code with possible inline CSS, JavaScript and data
2. index.md - documentation and `iframe` reference to a local `main.html`
3. style.css - optional CSS file
4. script.js - optional JavaScript file
5. data.json - optional JSON data file

Each of the skills below contains an assets directory that has these files with the string `template-` before the file names above.

All MicroSims should be designed to be width-responsive meaning that the components recenter and stretch if the containing window is resized.

## MicroSim P5 Generator

**Name:** microsim-pg<br/>
**Width Responsive:** Yes
This is a general skill that generates any p5.js application that can be tested in the p5.js editor.
It is ideal for simulations and animations where the user control the behavior through a set of
controls at the bottom of the drawing area.

See the [Microsim-p5 Description](./microsim-p5.md)

## Chart Generator

**Name:** chartjs-generator<br/>
This generator creates general charts such as:

1. bar charts
2. bubble charts
3. doughnut charts
4. line charts
5. pie charts
6. polar plot charts
7. radar charts
8. scatter charts

The default is 500px high and a width that fills 100% of the enclosing container.
If the user does not provide the title, chart type and data, the skill will prompt
them for the appropriate information.

See the [ChartJS Generator](./chartjs-generator.md) skill description.

## Mermaid
**Name:** timeline-generator<br/>
**Width Responsive:** Yes (with limitations in that the size of the shapes may not change, but they are re-centered)

The Mermaid.js library is ideal for allowing the user to specify the content of a drawing and a layout st

## 1. Process & Flow Diagrams
These diagrams illustrate workflows, processes, and sequential operations.

1. Flowchart/Graph - General-purpose flowcharts showing decision points, processes, and flow direction
1. State Diagram - Models state transitions and lifecycle of systems or objects
1. Sequence Diagram - Shows interactions between entities over time in a sequential order
1. User Journey - Maps user experiences and touchpoints across different stages

## 2. Structural & Relationship Diagrams
These diagrams model the structure and relationships between components or entities.

1. Class Diagram - Object-oriented design showing classes, attributes, methods, and relationships
1. Entity Relationship (ER) Diagram - Database schemas showing entities, attributes, and relationships
1. C4 Diagram - Software architecture context, containers, components, and code views
1. Block Diagram - High-level system component diagrams showing functional blocks

See the [Mermaid Generator](./mermaid-generator.md)

## Vis-Network MicroSim

**Name:** vis-network
This skill will create a graph network diagram using the vis-network JavaScript library.
The user should provide a list of nodes and edges as well as an optional list of groups.

See the [Vis Network](./vis-network.md) skill description.

## Math Function Plotter

See the [Math Function Plotter Plotly](./math-function-plotter-plotly.md) skill description.


## Timeline Generator

**Name:** timeline-generator<br/>
**Width Responsive:** Yes
This skill will take an input of events and generate a timeline using the vis-timeline JavaScript library.
The user must specify the following information and JSON is a good format:

```json
{
  "title": "Sample Timeline",
  "events": [
    {
        "start_date": {
        "year": "2025",
        "month": "11",
        "day": "16"
        },
        "text": {
        "headline": "Project Initiated",
        "text": "The project was formally initiated with stakeholder approval and budget allocation."
        },
        "group": "Planning",
        "notes": "This milestone marked the official start of the project after months of preparation and proposal development."
    }
  ]
}
```

See the [Timeline Generator](./timeline-generator.md) skill description.

## Venn Diagram

This uses the Venn.js library which has not been maintained for several years.  Use with caution.

See the [Venn Diagram Generator ](./venn-diagram-generator.md) skill description.

## Bubble Chart

This is a specialization of the ChartJS skill.  

See the [Bubble Chart](./bubble-chart-generator.md) skill description.
