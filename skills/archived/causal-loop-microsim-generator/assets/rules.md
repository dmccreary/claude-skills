# Causal Loop Diagram Generation Rules

This document provides comprehensive rules for generating Causal Loop Diagram (CLD) MicroSims using the vis-network library.

## 1. JSON Data Schema

### 1.1 Complete Schema Structure

```json
{
  "metadata": {
    "id": "string (kebab-case-cld)",
    "title": "string",
    "archetype": "string (optional - systems archetype name)",
    "description": "string",
    "learning_objectives": ["array of strings"],
    "version": "string (semver)",
    "created_date": "ISO 8601 date string",
    "updated_date": "ISO 8601 date string",
    "author": "string",
    "tags": ["array of strings"],
    "notes": "string (optional)"
  },
  "nodes": [
    {
      "id": "string (snake_case)",
      "label": "string (display name)",
      "position": {"x": number, "y": number},
      "type": "string (stock|variable|parameter)",
      "description": "string",
      "examples": ["array of strings (optional)"],
      "measurement": "string (optional)"
    }
  ],
  "edges": [
    {
      "id": "string (source_to_target)",
      "source": "string (node id)",
      "target": "string (node id)",
      "polarity": "string (positive|negative)",
      "description": "string",
      "strength": "string (weak|moderate|strong) (optional)",
      "delay": {
        "present": boolean,
        "duration": "string (optional)",
        "description": "string (optional)"
      },
      "curve": {
        "type": "string (curvedCW|curvedCCW|horizontal|vertical)",
        "roundness": number (0.1-0.5)
      }
    }
  ],
  "loops": [
    {
      "id": "string (unique loop id)",
      "type": "string (reinforcing|balancing)",
      "path": ["array of node ids in order"],
      "label": "string (display name)",
      "description": "string",
      "behavior_pattern": "string (optional)",
      "position": {"x": number, "y": number},
      "is_primary": boolean (optional)
    }
  ],
  "leverage_points": [
    {
      "id": "string",
      "target_type": "string (node|edge)",
      "target_id": "string",
      "leverage_level": number (1-12),
      "title": "string",
      "description": "string",
      "intervention_strategies": ["array of strings"],
      "expected_impact": "string",
      "difficulty": "string (low|moderate|high)"
    }
  ],
  "scenarios": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "changes": [
        {
          "target_type": "string (node|edge)",
          "target_id": "string",
          "change_description": "string"
        }
      ],
      "predicted_outcomes": "string"
    }
  ],
  "educational_content": {
    "discussion_questions": ["array of strings"],
    "key_insights": ["array of strings"],
    "common_misconceptions": [
      {
        "misconception": "string",
        "correction": "string"
      }
    ],
    "extension_activities": ["array of strings"],
    "related_concepts": ["array of strings"]
  }
}
```

### 1.2 Required Fields

- `metadata.id` - Unique identifier in kebab-case ending with `-cld`
- `metadata.title` - Human-readable title
- `metadata.description` - Brief description of the system
- `nodes` - At least 2 nodes required
- `edges` - At least 1 edge required
- For each node: `id`, `label`, `position`
- For each edge: `id`, `source`, `target`, `polarity`

### 1.3 Optional but Recommended

- `loops` - Identifies feedback loops for educational purposes
- `leverage_points` - For intervention analysis
- `educational_content` - For learning applications

## 2. Node Positioning Rules

### 2.1 Canvas Dimensions

- Standard canvas size: 600x600 pixels
- Center point: (300, 300)
- Recommended working area: 100-500 on both axes
- Leave 100px margin from edges for labels

### 2.2 Positioning Strategies

#### Simple 2-Node Loop
```
Node 1: (300, 150)
Node 2: (300, 450)
```

#### 3-Node Loop (Triangle)
```
Node 1: (300, 100)  - Top
Node 2: (450, 400)  - Bottom Right
Node 3: (150, 400)  - Bottom Left
```

#### 4-Node Loop (Diamond/Square)
```
Node 1: (300, 150)  - Top
Node 2: (450, 300)  - Right
Node 3: (300, 450)  - Bottom
Node 4: (150, 300)  - Left
```

#### 5-Node Loop (Pentagon)
```
Node 1: (300, 100)  - Top
Node 2: (470, 220)  - Top Right
Node 3: (410, 420)  - Bottom Right
Node 4: (190, 420)  - Bottom Left
Node 5: (130, 220)  - Top Left
```

### 2.3 Multi-Loop Diagrams

For diagrams with multiple loops:
- Identify shared nodes between loops
- Position shared nodes at intersection points
- Maintain minimum 150px spacing between non-connected nodes
- Use asymmetric layouts when loops share edges

### 2.4 Loop Center Calculation

The loop indicator (R or B symbol) should be placed at the centroid of the loop:

```
center_x = average of all node x positions in the loop
center_y = average of all node y positions in the loop
```

## 3. Edge Configuration Rules

### 3.1 Polarity Colors

- **Positive (+)**: Green `#28a745` - "More of A leads to more of B"
- **Negative (-)**: Red `#dc3545` - "More of A leads to less of B"

### 3.2 Edge Labels

- Positive edges: Display `+`
- Negative edges: Display `-`
- Font size: 48px for visibility
- White stroke (2-3px) for readability

### 3.3 Curve Directions

Use curve settings to prevent edge overlap:

```javascript
// Clockwise curve
{
  type: 'curvedCW',
  roundness: 0.4
}

// Counter-clockwise curve
{
  type: 'curvedCCW',
  roundness: 0.4
}
```

**Guidelines:**
- Use `curvedCW` for edges going clockwise around a loop
- Use `curvedCCW` for edges going counter-clockwise
- Increase `roundness` (up to 0.5) for parallel edges between same nodes
- For bidirectional relationships, use opposite curve directions

### 3.4 Two-Node Loops

When two nodes have edges in both directions:
```json
{
  "id": "a_to_b",
  "curve": {"type": "curvedCW", "roundness": 0.4}
},
{
  "id": "b_to_a",
  "curve": {"type": "curvedCCW", "roundness": 0.4}
}
```

## 4. Loop Identification Rules

### 4.1 Reinforcing Loops (R)

- All edges have the same polarity OR
- Even number of negative edges
- Behavior: Exponential growth or collapse
- Label: "R" or "R1", "R2" for multiple

### 4.2 Balancing Loops (B)

- Odd number of negative edges
- Behavior: Goal-seeking, oscillation, stability
- Label: "B" or "B1", "B2" for multiple

### 4.3 Loop Notation

```json
{
  "id": "main_loop",
  "type": "reinforcing",
  "path": ["node1", "node2", "node3", "node1"],
  "label": "Growth Cycle",
  "position": {"x": 300, "y": 300}
}
```

**Path convention:** Start with any node, list all nodes in order, end with the starting node.

## 5. vis-network Configuration

### 5.1 Recommended Options

```javascript
const options = {
  layout: {
    improvedLayout: false  // Use manual positioning
  },
  physics: {
    enabled: false  // Disable physics for fixed positions
  },
  interaction: {
    selectConnectedEdges: false
  },
  nodes: {
    shape: 'box',
    margin: 10,
    font: {
      size: 20,
      face: 'Arial'
    },
    borderWidth: 2,
    shadow: true,
    color: {
      background: 'white',
      border: 'dodgerblue',
      highlight: {
        background: 'lightskyblue',
        border: 'darkblue'
      }
    }
  },
  edges: {
    arrows: {
      to: { enabled: true, scaleFactor: 1.2 }
    },
    width: 2,
    smooth: {
      type: 'curvedCW',
      roundness: 0.4
    },
    font: {
      size: 48,
      strokeWidth: 3,
      strokeColor: 'white'
    }
  }
};
```

### 5.2 Node Types

| Type | Description | Typical Use |
|------|-------------|-------------|
| `stock` | Accumulation variable | Resources, inventory, population |
| `variable` | Flow or rate variable | Rates, decisions, activities |
| `parameter` | External constant | Policies, fixed factors |

### 5.3 Loop Indicators as Nodes

Add loop indicators as special ellipse nodes:

```javascript
{
  id: 'loop_R1',
  label: 'R',
  shape: 'ellipse',
  size: 30,
  color: {
    background: '#dc3545',  // Red for reinforcing
    border: 'black'
  },
  font: {
    color: 'white',
    size: 16
  }
}
```

- Reinforcing: Red background (#dc3545)
- Balancing: Green background (#28a745)

## 6. Systems Thinking Archetypes

### 6.1 Common Archetypes

| Archetype | Loops | Key Pattern |
|-----------|-------|-------------|
| `limits-to-growth` | R + B | Growth limited by constraint |
| `fixes-that-fail` | B + R | Quick fix creates side effects |
| `shifting-the-burden` | 2B + R | Symptomatic vs fundamental solution |
| `success-to-the-successful` | 2R | Winner-take-all dynamics |
| `tragedy-of-the-commons` | Multiple R + B | Shared resource depletion |
| `escalation` | 2R | Arms race pattern |
| `drifting-goals` | B + R | Standards erosion |
| `accidental-adversaries` | Complex | Partnership breakdown |

### 6.2 Archetype Detection

When generating a CLD, identify the archetype by:
1. Count reinforcing and balancing loops
2. Identify shared variables between loops
3. Look for characteristic patterns (delays, constraints)

## 7. Educational Content Guidelines

### 7.1 Learning Objectives (Bloom's Taxonomy)

Include objectives at multiple levels:
- **Remember**: Identify loop types
- **Understand**: Explain relationships
- **Apply**: Predict system behavior
- **Analyze**: Identify leverage points
- **Evaluate**: Assess interventions
- **Create**: Design modifications

### 7.2 Discussion Questions

Create questions that:
- Explore "what if" scenarios
- Challenge assumptions
- Connect to real-world examples
- Encourage systems perspective

### 7.3 Key Insights

Highlight:
- Non-obvious relationships
- Counterintuitive behaviors
- Delay effects
- Unintended consequences

## 8. File Naming Conventions

| File | Naming Pattern | Example |
|------|----------------|---------|
| Directory | `kebab-case` | `ai-flywheel/` |
| JSON data | `data.json` | `data.json` |
| JavaScript | `{name}.js` | `ai-flywheel.js` |
| HTML | `main.html` | `main.html` |
| CSS | `style.css` | `style.css` |
| Documentation | `index.md` | `index.md` |
| Screenshot | `{name}.png` | `ai-flywheel.png` |

## 9. mkdocs.yml Navigation Update

When adding to `mkdocs.yml`, maintain alphabetical ordering:

```yaml
- MicroSims:
    - Introduction: sims/index.md
    - Agent CLD: sims/agent-cld/index.md
    - AI Flywheel: sims/ai-flywheel/index.md  # New entry
    - CLD Editor: sims/cld-editor/index.md
    - CLD Viewer: sims/cld-viewer/index.md
```

## 10. Quality Checklist

Before completing a CLD MicroSim, verify:

- [ ] All nodes have unique IDs
- [ ] All edges reference valid node IDs
- [ ] Polarity is specified for all edges
- [ ] Loop paths form complete cycles
- [ ] Loop types match polarity analysis
- [ ] Positions prevent node overlap
- [ ] Edge curves prevent overlap
- [ ] metadata.id matches directory name
- [ ] index.md contains working iframe
- [ ] mkdocs.yml updated with alphabetical entry
