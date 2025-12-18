---
name: install-learning-graph-viewer
description: This skill installs an interactive learning graph viewer application into an intelligent textbook project. Use this skill when working with a textbook that has a learning-graph.json file and needs a visual, interactive graph exploration tool with search, filtering, and statistics capabilities.
---

# Install Learning Graph Viewer

## Overview

This skill installs a complete interactive graph visualization application into the `/docs/sims/graph-viewer/` directory of an intelligent textbook project. The viewer provides an interactive way to explore learning graphs with features like node search, category filtering, and real-time statistics.

## When to Use This Skill

Use this skill when:

- A learning graph has been generated (learning-graph.json exists in /docs/learning-graph/)
- The textbook needs an interactive visualization tool for exploring concept dependencies
- Students or instructors need to filter, search, and analyze the learning graph structure

**Prerequisites:**

- `/docs/learning-graph/learning-graph.json` must exist
- The JSON file must have metadata with a `title` field
- The JSON file must have proper `classifierName` values in groups (see Step 3.5)
- MkDocs project structure must be in place

## Installation Workflow

### Step 1: Verify Prerequisites

Before installation, verify that the learning graph JSON file exists:

```bash
ls docs/learning-graph/learning-graph.json
```

If the file doesn't exist, use the `learning-graph-generator` skill first to create the learning graph.

### Step 2: Create Directory Structure

Create the graph-viewer directory:

```bash
mkdir -p docs/sims/graph-viewer
```

### Step 3: Install Viewer Files

Copy the four essential files from the skill's assets directory to the target location:

```bash
cp assets/main.html docs/sims/graph-viewer/main.html
cp assets/script.js docs/sims/graph-viewer/script.js
cp assets/local.css docs/sims/graph-viewer/local.css
cp assets/index.md docs/sims/graph-viewer/index.md
```

### Step 3.5: Verify classifierName Values in JSON (IMPORTANT)

The learning-graph.json file must have human-readable `classifierName` values in the groups section. **This is critical for the legend to display correctly.**

Check the groups section of learning-graph.json:

```json
"groups": {
  "FOUND": {
    "classifierName": "Foundation Concepts",  // CORRECT - human readable
    "color": "LightCoral"
  },
  "BLOOM": {
    "classifierName": "BLOOM",  // WRONG - just the ID, not human readable
    "color": "PeachPuff"
  }
}
```

If any `classifierName` values are just the group ID (like "BLOOM", "VISUA"), update them to be human-readable (like "Bloom's Taxonomy", "Visualization Types").

Common taxonomy mappings:

| Group ID | classifierName |
|----------|----------------|
| FOUND | Foundation Concepts |
| BLOOM | Bloom's Taxonomy |
| VISUA | Visualization Types |
| LIBRA | Libraries & Tools |
| SPECI | Specification |
| COGNI | Cognitive Science |
| AUDIE | Audience Adaptation |
| EVALU | Evaluation & Testing |
| ITERA | Iteration & Workflow |
| ACCES | Accessibility |
| DEPLO | Deployment |
| CAPST | Capstone |

### Step 4: Extract Title from Learning Graph JSON

Read the title from the learning graph metadata:

```bash
# Use Python or jq to extract the title
python3 -c "import json; data = json.load(open('docs/learning-graph/learning-graph.json')); print(data.get('metadata', {}).get('title', 'Learning Graph'))"
```

If the metadata or title field doesn't exist, use a default title like "Learning Graph" or the course name.

### Step 5: Update Title in main.html

Replace the "TITLE" placeholder in main.html with the extracted title:

1. Read the extracted title from Step 4
2. In `docs/sims/graph-viewer/main.html`, replace all instances of "TITLE" with the actual course title
3. This appears in two locations:
   - The `<title>` tag: `<title>Learning Graph Viewer for TITLE</title>`
   - The page heading: `<h4>Learning Graph for TITLE</h4>`

### Step 6: Update MkDocs Navigation (Optional)

If the user wants the graph viewer in the site navigation, add it to `mkdocs.yml`:

```yaml
nav:
  - MicroSims:
    - Graph Viewer: sims/graph-viewer/index.md
```

### Step 7: Inform the User

Provide the user with instructions to test the installation:

1. Run `mkdocs serve` to start the local development server
2. Navigate to the appropriate URL based on their repository name:
   - Format: `http://localhost:8000/REPO_NAME/sims/graph-viewer/main.html`
   - The REPO_NAME can be extracted from the git repository or inferred from the project structure
3. Alternatively, if added to navigation, they can access it through the MkDocs site menu

## Viewer Features

The installed graph viewer provides:

**Search Functionality:**

- Type-ahead search with dropdown results
- Shows category information for each node
- Focuses and selects matching nodes in the visualization

**Category Filtering:**

- Sidebar legend with color-coded categories
- Checkboxes to show/hide specific taxonomy groups
- "Check All" and "Uncheck All" bulk operations
- Collapsible sidebar for expanded viewing

**Real-time Statistics:**

- Visible node count
- Visible edge count
- Foundational node count (concepts with no dependencies)

**Interactive Visualization:**

- vis.js network graph with physics simulation
- Color-coded nodes by taxonomy category
- Directed edges showing concept dependencies
- Zoomable and draggable interface

## Technical Details

**File Structure:**

```
docs/sims/graph-viewer/
├── main.html      # Main application HTML
├── script.js      # JavaScript logic for visualization
├── local.css      # Styling for the viewer
└── index.md       # Documentation page with iframe embed
```

**Dependencies:**

- vis-network.js (loaded from CDN in main.html)
- learning-graph.json (loaded from ../../learning-graph/learning-graph.json)

**Data Path:**
The script.js file loads the learning graph from a relative path: `../../learning-graph/learning-graph.json`. This assumes the standard intelligent textbook structure where `/docs/sims/` and `/docs/learning-graph/` are siblings.

## Common Issues and Fixes

### Issue 1: Legend colors don't match node colors

**Symptom:** When filtering by category, the visible nodes are a different color than the legend swatch.

**Cause:** The script must pass the groups configuration to vis-network's `groups` option. Without this, vis-network uses its own default color scheme.

**Fix:** The script.js builds a `visGroups` object from the JSON groups and passes it to vis-network:

```javascript
const visGroups = {};
Object.entries(groups).forEach(([groupId, groupInfo]) => {
    visGroups[groupId] = {
        color: {
            background: groupInfo.color,
            border: groupInfo.color
        }
    };
});

const options = {
    groups: visGroups,  // This is required!
    // ... other options
};
```

### Issue 2: Legend shows group IDs instead of readable names

**Symptom:** The legend shows "FOUND", "BLOOM" instead of "Foundation Concepts", "Bloom's Taxonomy".

**Cause:** The `classifierName` values in learning-graph.json are set to the group IDs instead of human-readable names.

**Fix:** Update the groups section in learning-graph.json to have proper classifierName values (see Step 3.5).

### Issue 3: Hierarchical layout doesn't work well

**Symptom:** The graph layout is messy or nodes overlap badly when using hierarchical layout.

**Cause:** Hierarchical layout doesn't work well with DAGs that have complex dependency structures.

**Fix:** Use physics-based layout with forceAtlas2Based solver instead:

```javascript
layout: {
    randomSeed: 42,
    improvedLayout: true
},
physics: {
    enabled: true,
    solver: 'forceAtlas2Based',
    forceAtlas2Based: {
        gravitationalConstant: -50,
        centralGravity: 0.01,
        springLength: 100,
        springConstant: 0.08
    }
}
```

**Do NOT use:**

```javascript
layout: {
    hierarchical: {
        enabled: true,
        // This doesn't work well with learning graphs
    }
}
```

## Resources

### assets/

This skill includes four asset files that get copied to the target directory:

- **main.html** - The main viewer application HTML file with vis-network integration
- **script.js** - Interactive JavaScript for search, filtering, and visualization (uses physics-based layout and proper groups configuration)
- **local.css** - Stylesheet for the viewer interface
- **index.md** - Documentation page explaining the viewer features

These files are ready to use without modification (except for the TITLE placeholder in main.html).
