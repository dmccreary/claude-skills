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
      "tip": "Optional tip or advanced detail"
    }
  ]
}
```

## Field Definitions

### Top-Level Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `title` | string | Yes | — | Display title; `diagram.js` renders it as an `<h1>` above the diagram and uses it as the image `alt` text. Do **not** also bake it into the image or add it as an `index.md` body `# Title` H1 (see SKILL.md → Title Rendering) |
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
| `panel` | string | Layout-dependent | Which label strip holds this callout. `top-bottom`: `"top"` or `"bottom"`. `dual-panel`: `"left"` or `"right"`. Omit for `side-panel`. Assign by proximity — see [Panel Assignment](#panel-assignment-top-bottom--dual-panel) |
| `hint` | string | Yes | Visual description for quiz mode — describes what the structure looks like without naming it |
| `description` | string | Yes | Full educational description shown in explore mode |
| `tip` | string | No | Tip or advanced detail (omit field entirely if not needed) |

## Position Guidelines

- `x` = 0 is the left edge, `x` = 100 is the right edge
- `y` = 0 is the top edge, `y` = 100 is the bottom edge
- Place markers at the visual center of each structure
- Space markers at least 5-8 percentage points apart to avoid overlap
- Initial positions are estimates — use `?edit=true` to calibrate after image generation

## Panel Assignment (top-bottom / dual-panel)

The `panel` field is required for the `top-bottom` and `dual-panel` layouts and
omitted for `side-panel`. It decides which label strip a callout sits in.

**Assign `panel` by proximity — put each label in the strip nearest its marker.
Never assign by an alternating / odd-even (parity) pattern.** In `top-bottom` the
leader line's length is dominated by the vertical gap between the marker and its
strip (the top strip sits above the image, the bottom strip below), so a parity
pattern drags labels far from their structures and crosses the lines.

Rule for `top-bottom`:

1. Sort callouts by `y` (0 = top of image).
2. Upper half (smallest `y`) → `"panel": "top"`; lower half → `"panel": "bottom"`.
   For an odd count the extra label goes on `top`. Splitting at the median keeps
   the strips balanced while every label lands on its closer edge.
3. Within each strip, order callouts left-to-right by ascending `x` so leaders
   don't cross.

Rule for `dual-panel` (same idea, rotated): sort by `x`; left half → `"left"`,
right half → `"right"`; order each side top-to-bottom by ascending `y`.

```json
{ "id": 1, "label": "…", "x": 12, "y": 18, "panel": "top",    "…": "…" }
{ "id": 7, "label": "…", "x": 61, "y": 82, "panel": "bottom", "…": "…" }
```

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
      "tip": "Do not confuse the nucleus with the nucleolus — the nucleolus is a dense region inside the nucleus."
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
      "tip": "The cell membrane is selectively permeable — small nonpolar molecules cross freely."
    }
  ]
}
```
