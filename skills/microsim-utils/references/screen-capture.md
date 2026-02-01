---
name: microsim-screen-capture
description: This skill automates the capture of high-quality screenshots for MicroSim visualizations using Chrome headless mode. Use this skill when working with MicroSims that need preview images for social media sharing, documentation, or quality assessment. The skill handles JavaScript-heavy visualizations that require proper rendering time and external CDN resources.
---

# MicroSim Screen Capture

## Overview

This skill automates the process of capturing high-quality screenshots of MicroSim visualizations using Chrome headless mode. It properly handles dynamic JavaScript content, external CDN libraries (like vis-network.js, p5.js, Chart.js), and ensures the visualization has time to fully render before capturing.

## When to Use This Skill

Use this skill when:

- Creating preview images for MicroSims that need social media metadata (`og:image`)
- Generating screenshots for MicroSim documentation
- Capturing visualizations for quality assessment or archival purposes
- Working with the microsim-standardization skill to achieve a perfect 100/100 quality score

**Typical user requests:**
- "Create a screenshot of this MicroSim"
- "I need a preview image for the org-chart MicroSim"
- "Generate a social media preview for this visualization"
- "Capture a screenshot of the main.html file"

## Workflow

### Step 1: Validate the MicroSim Directory

Before capturing a screenshot, verify:

1. The MicroSim directory exists at the provided path (typically `docs/sims/{microsim-name}/`)
2. The directory contains a `main.html` file
3. The MicroSim name follows kebab-case convention (lowercase letters and dashes only)

### Step 2: Run the Screenshot Capture Script

Execute the `bk-capture-screenshot` script with the MicroSim directory path:

```bash
~/.local/bin/bk-capture-screenshot <microsim-directory-path>
```

**Example:**
```bash
~/.local/bin/bk-capture-screenshot /Users/dan/Documents/ws/intro-to-graph/docs/sims/org-chart
```

The script will:

1. Extract the MicroSim name from the directory path (e.g., `org-chart` from `.../sims/org-chart/`)
2. Locate the `main.html` file in the directory
3. Use Chrome headless mode with optimal flags for JavaScript visualization rendering
4. Save the screenshot as `{microsim-name}.png` in the MicroSim directory (e.g., `org-chart.png`)
5. Display the output file path and size upon success

**Important Chrome flags used:**
- `--headless=new`: Uses the modern headless mode
- `--disable-web-security` + `--allow-file-access-from-files`: Allows loading external CDN resources (critical for vis-network, p5.js, etc.)
- `--timeout=5000`: Gives JavaScript 5 seconds to load and render the visualization
- `--window-size=1200,800`: Sets a standard viewport size suitable for social media previews
- `--hide-scrollbars`: Ensures clean screenshots without scrollbar artifacts

### Step 3: Verify the Screenshot

After the script completes:

1. Check that the image file was created: `{microsim-name}.png`
2. Verify the file size is reasonable (typically 20-100KB for rendered visualizations)
3. Use the Read tool to view the screenshot and confirm the visualization rendered properly
4. If the visualization area appears blank/white, the JavaScript may need more time to render - try increasing the `--timeout` value in the script

### Step 4: Update MicroSim Metadata (Optional)

If capturing the screenshot as part of MicroSim standardization, update the `index.md` YAML frontmatter:

```yaml
---
title: MicroSim Title
description: Brief description
image: microsim-name.png
og:image: microsim-name.png
quality_score: 100
---
```

This adds the social media preview metadata and contributes 10 points toward the quality score (5 points for metadata fields + 5 points for the image file existing).

## Troubleshooting

### Screenshot captures but visualization is blank

**Problem:** The screenshot shows the page header/controls but the main visualization area is white/empty.

**Solutions:**
1. The `bk-capture-screenshot` script waits 3 seconds by default; for complex visualizations, you may need to edit the script to increase the delay
2. Check browser console for JavaScript errors (the script filters them out but they may indicate issues)
3. Verify the visualization works when opening `main.html` directly in a browser
4. Ensure the local HTTP server started correctly (the script handles this automatically)

### Chrome not found error

**Problem:** Script reports "Chrome/Chromium not found"

**Solutions:**
1. Install Google Chrome if not present
2. Update the `CHROME_PATHS` array in the script to include your Chrome installation path
3. On macOS, Chrome is typically at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

### External resources not loading

**Problem:** Visualizations that use CDN libraries (vis-network, p5.js, Chart.js) don't render

**Solution:** The `bk-capture-screenshot` script uses a localhost server which properly handles CDN resources. If still not working:
1. Verify internet connectivity (CDNs need to be accessible)
2. Check if the library CDN URL is valid in `main.html`
3. Ensure the HTTP server started successfully (check script output for errors)

### Advanced Usage: localhost Server

The `bk-capture-screenshot` script automatically starts a local HTTP server to serve the MicroSim content. This ensures proper loading of CDN resources (vis-network, p5.js, Chart.js, etc.) which can fail with `file://` URLs.

The script:
1. Starts a Python HTTP server on an available port
2. Navigates Chrome to the localhost URL
3. Waits for JavaScript to render
4. Captures the screenshot
5. Automatically cleans up the server process

## Technical Details

### Why Chrome Headless?

Chrome headless mode is used because:
1. **JavaScript Support:** Full Chrome rendering engine handles complex JavaScript visualizations
2. **CDN Loading:** Can fetch external resources from CDNs (with proper flags)
3. **Timing Control:** Can wait for async content to load before capturing
4. **Cross-platform:** Works on macOS, Linux, and Windows
5. **No GUI Required:** Can run in CI/CD environments

### Screenshot Naming Convention

The script names screenshots using the MicroSim directory name to maintain consistency:
- MicroSim: `docs/sims/org-chart/` → Screenshot: `org-chart.png`
- MicroSim: `docs/sims/learning-graph-viewer/` → Screenshot: `learning-graph-viewer.png`

This differs from using a generic name like `preview.png` because:
1. Makes the file purpose immediately clear when viewing the directory
2. Easier to identify which screenshot belongs to which MicroSim in bulk operations
3. Follows naming conventions used elsewhere in the project

### Default Screenshot Dimensions

The default viewport size is 1200x800 pixels because:
- **Width (1200px):** Standard desktop viewport, suitable for most visualizations
- **Height (800px):** Captures header + controls + visualization without excessive whitespace
- **Aspect Ratio (3:2):** Works well for social media og:image tags
- **File Size:** Produces reasonably sized PNG files (typically 20-100KB)

To customize dimensions, modify the `--window-size` flag in the script.

## Resources

### ~/.local/bin/bk-capture-screenshot

User-installed Bash script that automates the entire screenshot capture process. The script:
- Validates input and checks for required files
- Locates Chrome/Chromium across different platforms
- Starts a local HTTP server to properly load CDN resources
- Waits 3 seconds for JavaScript to fully render
- Runs Chrome headless with optimized flags for JavaScript visualizations
- Saves screenshot as `{microsim-name}.png` in the MicroSim directory
- Reports success/failure with file size information

The script is designed to be:
- **Self-contained:** No external dependencies beyond Chrome and Python
- **Reliable:** Uses localhost server instead of file:// URLs for better CDN support
- **Error-tolerant:** Filters out common Chrome headless warnings that don't affect functionality
- **User-friendly:** Clear colored output with success indicators
