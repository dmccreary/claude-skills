# data.json Schema Reference

## Complete Schema

```json
{
  "title": "Diagram Title",
  "orientation": "landscape",
  "image": "filename.png",
  "layout": "side-panel",
  "showNumbers": true,
  "callouts": [
    {
      "id": 1,
      "label": "Structure Name",
      "x": 40.2,
      "y": 16.1,
      "radius": 5,
      "color": "#8E44AD",
      "hint": "Visual hint describing what the structure looks like",
      "description": "Educational description of the structure and its function.",
      "ap_tip": "Optional exam tip or advanced detail"
    }
  ]
}
```

## Field Definitions

### Top-Level Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `title` | string | Yes | — | Display title shown above the diagram |
| `orientation` | string | Yes | — | `"landscape"` or `"portrait"` |
| `image` | string | Yes | — | Filename of the diagram image (must be in same directory) |
| `layout` | string | No | `"side-panel"` | `"side-panel"`, `"top-bottom"`, or `"dual-panel"` |
| `showNumbers` | boolean | No | `true` | Whether to show numbered markers on the image |

### Callout Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | Yes | Unique sequential ID starting at 1 |
| `label` | string | Yes | Structure name displayed in label panel |
| `x` | number | Yes | Horizontal position as percentage (0-100) of image width |
| `y` | number | Yes | Vertical position as percentage (0-100) of image height |
| `radius` | number | Yes | Marker circle radius in relative units (typically 3-6) |
| `color` | string | Yes | Hex color for the marker (e.g., `"#8E44AD"`) |
| `hint` | string | Yes | Visual description for quiz mode — describes what the structure looks like without naming it |
| `description` | string | Yes | Full educational description shown in explore mode |
| `ap_tip` | string | No | Exam tip or advanced detail (omit field entirely if not needed) |

## Position Guidelines

- `x` = 0 is the left edge, `x` = 100 is the right edge
- `y` = 0 is the top edge, `y` = 100 is the bottom edge
- Place markers at the visual center of each structure
- Space markers at least 5-8 percentage points apart to avoid overlap
- Initial positions are estimates — use `?edit=true` to calibrate after image generation

## Recommended Color Palette

Use distinct colors to make markers easily identifiable:

| Hex | Color | Suggested Use |
|-----|-------|---------------|
| `#8E44AD` | Purple | Nucleus, central structures |
| `#E74C3C` | Red | Energy-related structures |
| `#3498DB` | Blue | Membrane structures |
| `#2ECC71` | Green | Photosynthetic structures |
| `#E67E22` | Orange | Transport structures |
| `#1ABC9C` | Teal | Storage structures |
| `#F39C12` | Gold | Signaling structures |
| `#9B59B6` | Violet | Genetic structures |
| `#34495E` | Dark Gray | Structural elements |
| `#16A085` | Sea Green | Fluid/matrix regions |

## Example: Animal Cell

```json
{
  "title": "Animal Cell",
  "orientation": "landscape",
  "image": "animal-cell.png",
  "callouts": [
    {
      "id": 1,
      "label": "Nucleus",
      "x": 40.2,
      "y": 16.1,
      "radius": 5,
      "color": "#8E44AD",
      "hint": "Large round purple structure near the center of the cell.",
      "description": "The control center of the cell, enclosed by a double-membrane nuclear envelope with pores. Contains DNA organized into chromosomes.",
      "ap_tip": "Do not confuse the nucleus with the nucleolus — the nucleolus is a dense region inside the nucleus."
    },
    {
      "id": 2,
      "label": "Cell membrane",
      "x": 89.3,
      "y": 21.1,
      "radius": 3.5,
      "color": "#E67E22",
      "hint": "Thin outer boundary line enclosing the entire cell.",
      "description": "The flexible outer boundary made of a phospholipid bilayer with embedded proteins. Controls what enters and exits the cell.",
      "ap_tip": "The cell membrane is selectively permeable — small nonpolar molecules cross freely."
    }
  ]
}
```
