---
name: html-table-generator
description: This skill generates interactive HTML table MicroSims with clickable cells that reveal detailed information in a sliding panel. Use this skill for matrix comparisons, framework analyses, or any tabular data where cells contain summary values but need expandable explanations. Creates a complete MicroSim package with separated HTML, CSS, JavaScript, and JSON data files.
---

# Interactive HTML Table with Detail Panel

## Overview

This skill generates interactive HTML tables where each cell is clickable, revealing detailed information in a sliding side panel. The pattern is ideal for educational comparisons where:
- Rows represent categories/items (e.g., cultural traditions, theories, technologies)
- Columns represent dimensions/criteria (e.g., aspects, features, metrics)
- Cells contain short summary values but need expandable context

## When to Use This Skill

Use this skill when:
- Creating framework comparison matrices (e.g., ethical frameworks, cultural perspectives)
- Building feature comparison tables with detailed explanations
- Presenting multi-dimensional analyses where each intersection needs context
- Need clickable cells with sliding detail panels

**Do NOT use this skill for:**
- Simple star-rating comparisons → use comparison-table-generator
- Timeline data → use timeline-guide
- Network relationships → use vis-network-guide

## Example Use Cases

1. **Cultural Fairness Frameworks** - 6 traditions × 5 dimensions matrix
2. **Learning Theory Comparison** - Multiple theories × various aspects
3. **Technology Stack Comparison** - Platforms × evaluation criteria
4. **Ethical Framework Analysis** - Philosophies × ethical dimensions

## File Structure

```
docs/sims/[microsim-name]/
├── index.md          # Documentation page with iframe
├── main.html         # Minimal HTML structure
├── style.css         # Light theme styling
├── script.js         # Matrix generation and interactions
├── data.json         # All row/column data
└── [name].png        # Screenshot for index page
```

## Architecture: Separation of Concerns

### 1. data.json - All Content Data

Structure your data with rows and columns:

```json
{
  "rows": [
    {
      "name": "Row Name",
      "subtitle": "Optional subtitle",
      "metadata": ["Tag 1", "Tag 2"],
      "cells": {
        "column1Key": {
          "value": "Short Display Value",
          "emphasis": "high|medium|low|balanced|unique",
          "description": "Detailed explanation...",
          "example": "Concrete example..."
        }
      }
    }
  ],
  "columns": [
    { "key": "column1Key", "name": "Column Display Name" }
  ]
}
```

### 2. style.css - Light Theme Styling

Use aliceblue background with dark text for MkDocs consistency:

```css
body {
    font-family: 'Inter', sans-serif;
    background: aliceblue;
    padding: 10px;
    color: #333;
}

.matrix-wrapper {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

th {
    background: #e8f4f8;
    font-weight: 600;
    color: #1a1a2e;
}

td.cell {
    cursor: pointer;
    transition: all 0.2s ease;
    background: #f8fafc;
}

td.cell:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
```

### 3. Emphasis Color System (Light Theme)

Use semantic colors with reduced opacity for light backgrounds:

| Emphasis | Color | Use Case |
|----------|-------|----------|
| high | `rgba(20,184,166,0.2)` | Primary/strong values |
| medium | `rgba(139,92,246,0.15)` | Secondary values |
| low | `rgba(239,68,68,0.12)` | Minimal/weak values |
| balanced | `rgba(245,158,11,0.18)` | Neutral/mixed values |
| unique | `rgba(6,182,212,0.18)` | Distinctive/special values |

### 4. script.js - Dynamic Matrix Generation

```javascript
let data = null;

async function init() {
    const response = await fetch('./data.json');
    data = await response.json();
    generateMatrix();
    setupEventListeners();
}

function generateMatrix() {
    const tbody = document.getElementById('matrix-body');
    tbody.innerHTML = '';

    data.rows.forEach(row => {
        const tr = document.createElement('tr');

        // Row header cell
        const nameCell = document.createElement('td');
        nameCell.className = 'row-name';
        nameCell.innerHTML = `${row.name}<span class="sub">${row.subtitle}</span>`;
        tr.appendChild(nameCell);

        // Data cells
        data.columns.forEach(col => {
            const cell = document.createElement('td');
            const cellData = row.cells[col.key];
            cell.className = `cell emphasis-${cellData.emphasis}`;
            cell.textContent = cellData.value;
            cell.addEventListener('click', () => showDetail(row, col.key, col.name));
            tr.appendChild(cell);
        });

        tbody.appendChild(tr);
    });
}

function showDetail(row, colKey, colName) {
    const cellData = row.cells[colKey];
    document.getElementById('detail-row').textContent = row.name;
    document.getElementById('detail-column').textContent = colName;
    document.getElementById('detail-description').textContent = cellData.description;
    document.getElementById('detail-example').textContent = cellData.example;

    document.getElementById('detail-panel').classList.add('open');
    document.getElementById('overlay').classList.add('open');
}

function closeDetail() {
    document.getElementById('detail-panel').classList.remove('open');
    document.getElementById('overlay').classList.remove('open');
}

document.addEventListener('DOMContentLoaded', init);
```

### 5. main.html - Minimal Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrix Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Matrix Title</h1>
        <p class="subtitle">Subtitle description</p>

        <div class="matrix-wrapper">
            <table>
                <thead>
                    <tr>
                        <th class="row-header">Row Label</th>
                        <th>Column 1</th>
                        <th>Column 2</th>
                        <!-- Add column headers -->
                    </tr>
                </thead>
                <tbody id="matrix-body">
                    <!-- Generated by JavaScript -->
                </tbody>
            </table>
        </div>

        <div class="legend">
            <!-- Legend items -->
        </div>

        <p class="instructions">Click any cell to see details</p>
    </div>

    <div class="overlay" id="overlay"></div>

    <div class="detail-panel" id="detail-panel">
        <button class="close-btn" id="close-btn">&times;</button>
        <h2 id="detail-row"></h2>
        <h3 id="detail-column"></h3>
        <div class="description" id="detail-description"></div>
        <div class="example">
            <div class="example-label">Example</div>
            <div class="example-text" id="detail-example"></div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

## Compact Layout for MkDocs Iframe

MkDocs content area is typically 750-800px wide. Use these compact settings:

```css
body { padding: 10px; }
.matrix-wrapper { padding: 10px; }
th, td { padding: 8px 6px; }
th.row-header { min-width: 120px; }
th.column-header { min-width: 80px; }
h1 { font-size: 1.4rem; }
td.cell { font-size: 0.7rem; }
.legend { font-size: 0.7rem; gap: 12px; padding: 8px; }
```

## Detail Panel Styling

```css
.detail-panel {
    position: fixed;
    top: 0;
    right: -450px;
    width: 420px;
    height: 100vh;
    background: #fff;
    border-left: 1px solid #e0e0e0;
    padding: 30px;
    transition: right 0.3s ease;
    z-index: 100;
    overflow-y: auto;
    box-shadow: -4px 0 30px rgba(0, 0, 0, 0.1);
}

.detail-panel.open { right: 0; }

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.3);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
    z-index: 50;
}

.overlay.open {
    opacity: 1;
    pointer-events: auto;
}

/* Mobile: full-width panel */
@media (max-width: 768px) {
    .detail-panel {
        width: 100%;
        right: -100%;
    }
}
```

## Event Handling

Include keyboard navigation for accessibility:

```javascript
function setupEventListeners() {
    document.getElementById('close-btn').addEventListener('click', closeDetail);
    document.getElementById('overlay').addEventListener('click', closeDetail);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeDetail();
    });
}
```

## Workflow Summary

1. **Gather requirements**: Number of rows/columns, cell values, descriptions, examples
2. **Create data.json**: Structure all content data
3. **Create style.css**: Light theme with emphasis colors
4. **Create script.js**: Matrix generation and panel interactions
5. **Create main.html**: Minimal HTML linking to external files
6. **Create index.md**: Documentation with iframe embed
7. **Capture screenshot**: For index page thumbnail
8. **Update mkdocs.yml**: Add to navigation

## Lessons Learned

1. **Separation of concerns** - Keep data in JSON for easy updates without touching code
2. **Light theme colors** - Use lower opacity values than dark themes (0.15-0.2 vs 0.3-0.5)
3. **Compact layouts** - Systematically reduce all padding/margins/font-sizes for iframe fit
4. **Async data loading** - Use fetch() with proper error handling
5. **Mobile responsiveness** - Full-width detail panel on small screens
6. **Keyboard accessibility** - Always support ESC to close panels

## Reference Implementation

See `ethics-course/docs/sims/fairness-frameworks/` for a complete working example:
- 6 rows (cultural traditions) × 5 columns (dimensions)
- Emphasis-coded cells
- Sliding detail panel with descriptions and examples
- Light theme matching MkDocs styling
