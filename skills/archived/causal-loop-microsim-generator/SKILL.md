---
name: causal-loop-microsim-generator
description: This skill generates interactive Causal Loop Diagram (CLD) MicroSims using the vis-network JavaScript library. Use this skill when users need to create causal loop diagrams for systems thinking education, showing feedback loops, reinforcing and balancing dynamics. The skill creates a complete MicroSim package with index.md, main.html, JavaScript, JSON data, and CSS files in the /docs/sims/ directory. This skill should be used when users request creating CLDs, causal diagrams, feedback loop visualizations, or systems thinking diagrams.
---

# Causal Loop MicroSim Generator

## Overview

This skill generates interactive Causal Loop Diagram (CLD) MicroSims for educational purposes in systems thinking. CLDs visualize cause-and-effect relationships, feedback loops, and system dynamics using nodes (variables) and edges (causal relationships with positive or negative polarity).

## When to Use This Skill

Use this skill when users request:
- Creating a causal loop diagram
- Visualizing feedback loops
- Building systems thinking diagrams
- Generating CLD visualizations
- Creating reinforcing or balancing loop diagrams
- Building system dynamics visualizations

## Workflow

### Step 1: Gather Requirements

Collect the following information from the user:
1. **MicroSim name** (kebab-case, e.g., `ai-flywheel`, `climate-feedback`)
2. **Title** for the diagram
3. **Description** of the system being modeled
4. **Nodes** (variables in the system) with their labels and descriptions
5. **Edges** (causal relationships) with polarity (positive/negative)
6. **Loops** (reinforcing R or balancing B) with descriptions

If the user provides a text description, parse it to identify:
- Key variables (become nodes)
- Causal relationships (become edges with polarity)
- Feedback loops (reinforcing or balancing)

### Step 2: Generate the MicroSim Files

Create the following directory structure in `/docs/sims/{{MICROSIM_NAME}}/`:

```
{{MICROSIM_NAME}}/
├── index.md           # Documentation page
├── main.html          # HTML container
├── {{MICROSIM_NAME}}.js   # JavaScript code using vis-network
├── data.json          # Node and edge data
└── style.css          # Custom CSS styles
```

### Step 3: File Generation Details

#### 3.1 data.json

Generate the JSON data file following the CLD schema. Refer to `assets/rules.md` for the complete JSON schema and best practices.

Key structure:
```json
{
  "metadata": {
    "id": "{{MICROSIM_NAME}}-cld",
    "title": "Title",
    "archetype": "archetype-name",
    "description": "Description",
    "version": "1.0.0"
  },
  "nodes": [...],
  "edges": [...],
  "loops": [...]
}
```

**Node positioning guidelines:**
- Canvas center is approximately (300, 300)
- Space nodes 150-200 pixels apart
- Arrange nodes in a logical flow (clockwise for reinforcing, counter-clockwise for balancing)
- For 4-node loops: use positions like (300,150), (450,300), (300,450), (150,300)

#### 3.2 main.html

Create the HTML file using the template in `assets/templates/main.html`. The HTML should:
- Load vis-network from CDN
- Include the CSS file
- Reference the JavaScript file
- Have a container div for the network

#### 3.3 {{MICROSIM_NAME}}.js

Generate JavaScript using vis-network library. Refer to `assets/templates/microsim.js` for the template.

Key features to implement:
- Load data from data.json
- Configure node appearance (box shape, colors, fonts)
- Configure edge appearance (arrows, polarity colors: green for +, red for -)
- Disable physics for manual positioning
- Add click handlers for showing details
- Support URL parameters for iframe embedding

#### 3.4 style.css

Create CSS for the MicroSim layout. Use the template in `assets/templates/style.css`.

#### 3.5 index.md

Create the documentation page with:
- Title and description
- Learning objectives
- Iframe embed of the MicroSim
- Link to full-screen version
- Explanation of the system dynamics

### Step 4: Update mkdocs.yml

Add the new MicroSim to the navigation in `mkdocs.yml`:

1. Find the `MicroSims:` section in the nav
2. Add a new entry in **alphabetical order**: `- {{Title}}: sims/{{MICROSIM_NAME}}/index.md`

**Important:** Maintain alphabetical ordering of all MicroSim entries.

### Step 5: Remind User About Screenshot

After generating all files, remind the user:

> **Screenshot Required:** Please take a screenshot of the MicroSim and save it as `{{MICROSIM_NAME}}.png` in the `/docs/sims/{{MICROSIM_NAME}}/` directory. This image will be used for social sharing and documentation.

## CLD Design Best Practices

Refer to `assets/rules.md` for detailed rules on:
- JSON schema specification
- Node positioning algorithms
- Edge polarity and curve directions
- Loop labeling conventions
- vis-network configuration options

## Resources

### assets/

- `rules.md` - Comprehensive CLD generation rules and JSON schema
- `templates/main.html` - HTML template
- `templates/microsim.js` - JavaScript template
- `templates/style.css` - CSS template
- `templates/index.md` - Documentation template
- `templates/data.json` - Example JSON data structure

## Example Usage

**User request:** "Create a CLD showing how increased AI usage leads to more training data, which improves model accuracy, which increases AI usage."

**Generated MicroSim:**
- Name: `ai-usage-loop`
- Nodes: AI Usage, Training Data, Model Accuracy
- Edges: All positive polarity forming a reinforcing loop
- Loop: R - AI Improvement Cycle
