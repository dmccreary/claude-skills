---
name: microsim-add-icons
description: Add clickable Creative Commons license and fullscreen icons to an existing MicroSim's control region. Use this skill when enhancing a MicroSim with navigation icons in the lower right corner. Adds approximately 40 lines of code for icon functionality.
---

# MicroSim Add Icons

## Overview

Add clickable Creative Commons license and fullscreen navigation icons to the control region of an existing p5.js MicroSim. The icons appear in the lower right corner and use distance-based click detection. This adds approximately 40 lines of code to the simulation.

## When to Use This Skill

Use this skill when:
- Adding license information access to a MicroSim
- Enabling fullscreen mode via an icon
- Enhancing a MicroSim with clickable UI elements
- Following the icons demo pattern from the MicroSims repository

## Workflow

### Step 1: Identify the Target MicroSim

Ask the user which MicroSim JavaScript file to modify, or identify it from context. The file should be a p5.js MicroSim following the standard pattern with:
- Global variables section
- `setup()` function
- `draw()` function
- `windowResized()` function

### Step 2: Read the Existing File

Read the entire JavaScript file to understand its structure and identify where to add the icon code.

### Step 3: Add Icon Variables

Add the following variables to the global variables section, after the existing slider variables:

```javascript
// Icon variables
let iconSize = 24;
let iconMargin = 5;
let ccIconX, ccIconY;  // Creative Commons icon position
let fsIconX, fsIconY;  // Fullscreen icon position
```

Also add or update the `sliderRightMargin` variable:

```javascript
let sliderRightMargin = 70;
```

This reserves space on the right side of sliders for the icons.

### Step 4: Add drawIcons() Function

Add the complete `drawIcons()` function after the `draw()` function:

```javascript
function drawIcons() {
  // Calculate icon positions (right to left)
  fsIconX = canvasWidth - iconMargin - iconSize/2;
  fsIconY = drawHeight + controlHeight/2;

  ccIconX = fsIconX - iconSize - iconMargin;
  ccIconY = fsIconY;

  // Draw Creative Commons icon
  fill('black');
  noStroke();
  textAlign(CENTER, CENTER);
  textSize(20);
  text('ⓒ', ccIconX, ccIconY);
  // Draw Fullscreen icon
  text('⛶', fsIconX, fsIconY);
}
```

### Step 5: Call drawIcons() in draw()

Add the following code at the end of the `draw()` function, just before the closing brace:

```javascript
  // Draw icons in lower right corner of control region
  drawIcons();
}
```

### Step 6: Add mousePressed() Function

Add the complete `mousePressed()` function after the `drawIcons()` function:

```javascript
function mousePressed() {
  // Check if Creative Commons icon was clicked
  let distCC = dist(mouseX, mouseY, ccIconX, ccIconY);
  if (distCC < iconSize/2) {
    // Get the base URL (remove '/sims/icons/main.html' from current URL)
    let baseUrl = window.location.href.split('/sims/')[0];
    window.open(baseUrl + '/license/', '_blank');
    return;
  }

  // Check if Fullscreen icon was clicked
  let distFS = dist(mouseX, mouseY, fsIconX, fsIconY);
  if (distFS < iconSize/2) {
    // Open main.html in a new window/tab (same behavior as the fullscreen button)
    window.open('main.html', '_blank');
    return;
  }
}
```

### Step 7: Update windowResized() Function

Update the `windowResized()` function to use `sliderRightMargin` when resizing sliders:

```javascript
function windowResized() {
  // Update canvas size when the container resizes
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  // resize the speed slider and any other sliders here
  speedSlider.size(canvasWidth - sliderLeftMargin - sliderRightMargin);
  redraw();
}
```

If there are multiple sliders, update all slider size calculations to use `sliderRightMargin`.

### Step 8: Update setup() Function

If the slider size is set in `setup()`, update it to use `sliderRightMargin`:

```javascript
speedSlider.size(canvasWidth - sliderLeftMargin - sliderRightMargin);
```

### Step 9: Verify and Test

After making all changes:
1. Verify that all edits were successful
2. Inform the user that the icons have been added
3. Note that approximately 40 lines of code were added
4. Suggest testing the icons by opening the MicroSim

## Code Size Impact

Adding icons increases the JavaScript file size by approximately 40 lines:
- 6 lines for icon variables
- 1 line to call `drawIcons()`
- 18 lines for the `drawIcons()` function
- 19 lines for the `mousePressed()` function
- Additional spacing and comments

The icons can be omitted from minimal MicroSims to reduce file size.

## Icon Functionality

**Creative Commons Icon (ⓒ):**
- Positioned second from the right in the control region
- Clicking opens `/license/` page in a new tab
- Uses relative URL calculation to work in any deployment

**Fullscreen Icon (⛶):**
- Positioned at the far right of the control region
- Clicking opens `main.html` in a new window/tab
- Provides full-page viewing experience

Both icons use distance-based click detection with `dist()` function, creating circular clickable regions with a radius of `iconSize/2` (12 pixels).

## Common Variations

**Different Icon Symbols:**
Replace the Unicode characters `ⓒ` and `⛶` with other symbols as needed:
- License: ⓒ, ©, 🅭
- Fullscreen: ⛶, ⤢, ⛶
- Help: ?, ⓘ, ❓
- Settings: ⚙, ⚙️

**Additional Icons:**
To add more icons, follow the same pattern:
1. Add position variables (e.g., `helpIconX`, `helpIconY`)
2. Calculate position in `drawIcons()` (move left by `iconSize + iconMargin`)
3. Draw the icon in `drawIcons()`
4. Add click detection in `mousePressed()`
5. Increase `sliderRightMargin` by 30 pixels per additional icon

**Custom Actions:**
Modify the `mousePressed()` function to perform different actions:
- Open different URLs
- Toggle simulation features
- Display help overlays
- Share via social media
