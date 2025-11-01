# vis.js Network Format Reference for Learning Graph Generator

## Overview

This document defines the **standard JSON format** for learning graphs compatible with the **vis.js Network library**. Use this format when generating learning graphs to ensure proper visualization.

## Purpose

When using the **Learning Graph Generator skill**, the final JSON output must conform to this specification to work with vis.js network visualizations commonly used in educational web applications.

## JSON Structure

### Top-Level Schema

```json
{
  "nodes": [...],
  "edges": [...],
  "metadata": {...}
}
```

### Complete Example

```json
{
  "nodes": [
    {
      "id": 1,
      "label": "Complex Numbers",
      "group": "MATH"
    },
    {
      "id": 2,
      "label": "Euler's Formula",
      "group": "MATH"
    }
  ],
  "edges": [
    {
      "from": 1,
      "to": 2
    }
  ],
  "metadata": {
    "title": "Course Learning Graph",
    "description": "200 interconnected concepts",
    "nodeCount": 200,
    "edgeCount": 229,
    "taxonomies": {
      "MATH": "Mathematical Foundations",
      "FFT": "FFT Algorithm & Implementation"
    }
  }
}
```

## Node Format

### Required Properties

| Property | Type   | Description                          | Example               |
|----------|--------|--------------------------------------|-----------------------|
| `id`     | number | Unique identifier (1-based index)    | `1`, `2`, `3`        |
| `label`  | string | Display text (max 32 chars)          | `"Complex Numbers"`  |

### Optional Properties

| Property | Type   | Description                          | Example               |
|----------|--------|--------------------------------------|-----------------------|
| `group`  | string | Taxonomy/category for styling        | `"MATH"`, `"FFT"`    |
| `title`  | string | Tooltip text on hover                | `"Foundational concept"` |
| `shape`  | string | Node shape                           | `"dot"`, `"box"`, `"star"` |
| `color`  | string | Override group color                 | `"red"`, `"#FF0000"` |
| `x`      | number | Fixed horizontal position            | `-900`, `900`        |
| `y`      | number | Fixed vertical position              | `0`, `100`           |
| `fixed`  | object | Lock position                        | `{"x": true, "y": false}` |

### Node Example with All Properties

```json
{
  "id": 1,
  "label": "Complex Numbers",
  "group": "MATH",
  "title": "Foundational mathematical concept",
  "shape": "box",
  "color": "red",
  "x": -900,
  "fixed": {"x": true, "y": false}
}
```

## Edge Format

### Required Properties

| Property | Type   | Description                          | Example               |
|----------|--------|--------------------------------------|-----------------------|
| `from`   | number | Source node ID (prerequisite)        | `1`                  |
| `to`     | number | Target node ID (dependent)           | `2`                  |

### Optional Properties

| Property | Type   | Description                          | Example               |
|----------|--------|--------------------------------------|-----------------------|
| `arrows` | string/object | Arrow direction                | `"to"`, `{"to": true}` |
| `color`  | string | Edge color                           | `"gray"`, `"#888888"` |
| `width`  | number | Edge thickness                       | `1`, `2`, `3`        |
| `label`  | string | Text on edge                         | `"prerequisite"`     |
| `dashes` | boolean/array | Dashed line style               | `true`, `[5, 5]`     |

### Edge Example

```json
{
  "from": 1,
  "to": 2,
  "arrows": "to",
  "color": "gray",
  "width": 1
}
```

## Metadata Format

Optional but recommended for documentation and analytics.

### Standard Metadata Properties

```json
{
  "metadata": {
    "title": "FFT Benchmarking Course Learning Graph",
    "description": "200 interconnected concepts for a 10-week course",
    "nodeCount": 200,
    "edgeCount": 229,
    "version": "1.0",
    "generated": "2025-10-30",
    "taxonomies": {
      "MATH": "Mathematical Foundations",
      "FFT": "FFT Algorithm & Implementation",
      "SIG": "Signal Processing",
      "ARM": "ARM Architecture & DSP Hardware",
      "MEM": "Memory Management & Optimization",
      "FXP": "Fixed-Point Arithmetic",
      "BENCH": "Benchmarking & Testing",
      "LIB": "FFT Libraries & Integration",
      "OPT": "Optimization Techniques"
    }
  }
}
```

## Important Distinctions

### ❌ WRONG: D3.js Format

```json
{
  "nodes": [
    {
      "id": 1,
      "label": "Complex Numbers",
      "taxonomy": "MATH"          // ❌ Wrong property name
    }
  ],
  "links": [                      // ❌ Wrong array name
    {
      "source": 1,                // ❌ Wrong property name
      "target": 2                 // ❌ Wrong property name
    }
  ]
}
```

### ✅ CORRECT: vis.js Format

```json
{
  "nodes": [
    {
      "id": 1,
      "label": "Complex Numbers",
      "group": "MATH"             // ✅ Correct for vis.js
    }
  ],
  "edges": [                      // ✅ Correct array name
    {
      "from": 1,                  // ✅ Correct property name
      "to": 2                     // ✅ Correct property name
    }
  ]
}
```

## Python Conversion Template

### Standard CSV to vis.js JSON Converter

```python
#!/usr/bin/env python3
"""
Convert concept dependencies CSV to vis.js network JSON format.
"""

import csv
import json

def convert_csv_to_json(csv_file, json_file):
    """Convert CSV to vis.js network format."""
    nodes = []
    edges = []

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            concept_id = int(row['ConceptID'])
            label = row['ConceptLabel']
            taxonomy = row['TaxonomyID']
            deps = row['Dependencies'].strip()

            # Create node (vis.js format)
            node = {
                "id": concept_id,
                "label": label,
                "group": taxonomy
            }
            nodes.append(node)

            # Create edges (vis.js format: from/to)
            if deps:
                dependencies = [int(d) for d in deps.split('|')]
                for dep in dependencies:
                    edge = {
                        "from": dep,
                        "to": concept_id
                    }
                    edges.append(edge)

    # Create graph structure
    graph = {
        "nodes": nodes,
        "edges": edges,
        "metadata": {
            "title": "Learning Graph",
            "nodeCount": len(nodes),
            "edgeCount": len(edges)
        }
    }

    # Write to JSON file
    with open(json_file, 'w') as f:
        json.dump(graph, f, indent=2)

    return graph
```

## JavaScript Loading Template

### Standard vis.js Network Initialization

```javascript
function drawGraph() {
  // Fetch the graph data from JSON file
  fetch('learning-graph.json')
    .then(response => response.json())
    .then(data => {
      // Create DataSets for vis.js
      const nodes = new vis.DataSet(data.nodes);
      const edges = new vis.DataSet(data.edges);

      // Optional: Customize nodes after loading
      nodes.forEach(function (node) {
        if (node.group === "MATH") {
          node.x = -900;
          node.fixed = { x: true, y: false };
          node.shape = "box";
          node.color = "red";
        } else if (node.group === "OPT") {
          node.x = 900;
          node.fixed = { x: true, y: false };
          node.shape = "star";
          node.color = "gold";
        }
      });

      // Create network
      const container = document.getElementById('mynetwork');
      const graphData = {
        nodes: nodes,
        edges: edges
      };

      // Network options
      const options = {
        physics: {
          enabled: true,
          solver: 'forceAtlas2Based',
          stabilization: {
            iterations: 1000,
            updateInterval: 25
          }
        },
        edges: {
          arrows: {
            to: {
              enabled: true,
              type: 'arrow'
            }
          },
          smooth: {
            type: 'continuous'
          }
        },
        nodes: {
          shape: 'dot',
          size: 20,
          font: {
            size: 14,
            color: 'black'
          },
          borderWidth: 2
        }
      };

      // Initialize network
      const network = new vis.Network(container, graphData, options);
    })
    .catch(error => {
      console.error("Error loading JSON:", error);
    });
}
```

## Group/Taxonomy Colors

Recommended color scheme for educational taxonomy groups:

```javascript
const taxonomyColors = {
  "MATH": "#E74C3C",    // Red - Foundational
  "FFT": "#3498DB",     // Blue - Core algorithms
  "SIG": "#2ECC71",     // Green - Signal processing
  "ARM": "#9B59B6",     // Purple - Hardware
  "MEM": "#F39C12",     // Orange - Memory
  "FXP": "#1ABC9C",     // Teal - Numeric precision
  "BENCH": "#E67E22",   // Dark orange - Testing
  "LIB": "#95A5A6",     // Gray - Libraries
  "OPT": "#F1C40F"      // Yellow/Gold - Optimization
};
```

## Validation Checklist

When generating learning graph JSON for vis.js, verify:

- [ ] Top-level object has `nodes` array (not `vertices`)
- [ ] Top-level object has `edges` array (not `links`)
- [ ] Each node has `id` (number) and `label` (string)
- [ ] Nodes use `group` property (not `taxonomy` or `category`)
- [ ] Each edge has `from` (number) and `to` (number)
- [ ] Edges use `from`/`to` (not `source`/`target`)
- [ ] All `from` and `to` values reference valid node IDs
- [ ] No self-loops (edge where `from === to`)
- [ ] Graph forms valid DAG (no cycles) for learning paths
- [ ] Optional: metadata object included for documentation

## Common Mistakes to Avoid

| Mistake | Issue | Solution |
|---------|-------|----------|
| Using `links` | vis.js won't find edges | Use `edges` |
| Using `source`/`target` | Edges won't connect | Use `from`/`to` |
| Using `taxonomy` | Groups won't work | Use `group` |
| String IDs | Type mismatch errors | Use numeric IDs |
| Missing `label` | Blank nodes | Always include labels |
| Circular edges | Cycles in learning path | Validate DAG structure |

## File Naming Convention

**Recommended:**
- `learning-graph.json` - Main graph file
- `concept-dependencies.csv` - Source CSV file
- `convert-to-json.py` - Conversion script

**Not Recommended:**
- `graph.json` - Too generic
- `network.json` - Ambiguous
- `data.json` - Not descriptive

## vis.js Documentation References

- **Official docs:** https://visjs.github.io/vis-network/docs/network/
- **Node options:** https://visjs.github.io/vis-network/docs/network/nodes.html
- **Edge options:** https://visjs.github.io/vis-network/docs/network/edges.html
- **Physics:** https://visjs.github.io/vis-network/docs/network/physics.html
- **Examples:** https://visjs.github.io/vis-network/examples/

## Summary for SKILL Generation

### Quick Reference Card

**For Learning Graph Generator Skill:**

1. **Array names:** `nodes` and `edges` (not links/vertices)
2. **Node structure:** `{id: number, label: string, group: string}`
3. **Edge structure:** `{from: number, to: number}`
4. **Group property:** Use for taxonomy categories (enables coloring)
5. **Metadata:** Optional but recommended for documentation
6. **Validation:** Ensure DAG structure (no cycles)
7. **Python template:** Use provided converter code
8. **Testing:** Load in vis.js Network to verify rendering

### Integration Workflow

```
CSV (concept-dependencies.csv)
    ↓
Python Script (convert-to-json.py)
    ↓
JSON (learning-graph.json) [vis.js format]
    ↓
HTML + JavaScript (vis.Network)
    ↓
Interactive Graph Visualization
```

---

**Document Version:** 1.0
**Created:** 2025-10-30
**For Use With:** Learning Graph Generator Skill
**Target Library:** vis.js Network v9.x+
**Status:** Production-ready reference
