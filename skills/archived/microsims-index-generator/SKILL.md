---
name: microsims-index-generator
description: This skill generates a comprehensive index page for MicroSims in an intelligent textbook project. Use this skill when working with an MkDocs-based textbook that has MicroSims in a /docs/sims/ directory and needs an updated index page with screenshots, descriptions, and navigation. The skill captures missing screenshots, generates alphabetically-sorted grid cards using mkdocs-material format, and updates the mkdocs.yml navigation.
---

# MicroSims Index Generator

## Overview

This skill automates the creation and maintenance of a MicroSims index page for intelligent textbooks built with MkDocs Material theme. It scans the `/docs/sims/` directory, captures screenshots for MicroSims missing preview images, and generates a professionally formatted index page using mkdocs-material grid cards.

## When to Use This Skill

Use this skill when:

- A new MicroSim has been added and the index needs updating
- Multiple MicroSims exist but lack preview screenshots
- The MicroSims index page needs to be reformatted to grid cards
- The mkdocs.yml navigation section for MicroSims needs synchronization

## Prerequisites

- MkDocs project with Material theme configured
- `attr_list` and `md_in_html` markdown extensions enabled in mkdocs.yml
- MicroSims located in `/docs/sims/<microsim-name>/` directories
- Each MicroSim directory contains:
  - `main.html` - The interactive simulation
  - `index.md` - Documentation page with title and description
- Screenshot capture tool available at `~/.local/bin/bk-capture-screenshot`

## Workflow

### Step 0: Verify mkdocs.yml Extensions

Before generating the index, verify that `mkdocs.yml` has the required markdown extensions for grid cards to render properly:

```yaml
markdown_extensions:
  - attr_list
  - md_in_html
```

Check the file:
```bash
grep -A 20 "markdown_extensions:" mkdocs.yml
```

If either `attr_list` or `md_in_html` is missing, add them to the `markdown_extensions` section before proceeding. Grid cards will not render without these extensions.

### Step 1: Discover MicroSims

List all MicroSim directories in `/docs/sims/`:

```bash
ls /path/to/project/docs/sims/
```

Exclude the `index.md` file from the list. Each subdirectory represents a MicroSim.

### Step 2: Gather MicroSim Information

For each MicroSim directory, read the `index.md` file to extract:

1. **Title** - From the first H1 heading or YAML frontmatter title
2. **Description** - A short 1-2 sentence summary from the content

Example structure to look for:
```markdown
# MicroSim Title

Description paragraph explaining what the MicroSim does...
```

### Step 3: Check for Missing Screenshots

For each MicroSim, check if a PNG screenshot exists:

```bash
ls /path/to/project/docs/sims/<microsim-name>/*.png
```

The screenshot filename should match the directory name (e.g., `command-syntax/command-syntax.png`).

### Step 4: Capture Missing Screenshots

For each MicroSim missing a screenshot, use the screenshot capture tool:

```bash
~/.local/bin/bk-capture-screenshot /path/to/project/docs/sims/<microsim-name>
```

This tool:
- Captures a 1200x800 screenshot of `main.html` using Chrome headless
- Waits 3 seconds for JavaScript to load
- Saves as `<microsim-name>.png` in the MicroSim directory

For MicroSims with complex animations, increase the delay:
```bash
~/.local/bin/bk-capture-screenshot /path/to/project/docs/sims/<microsim-name> 5
```

### Step 5: Generate Index Page Content

Create the index page at `/docs/sims/index.md` using mkdocs-material grid cards format.

#### Required YAML Frontmatter

```yaml
---
title: List of MicroSims for [Course Name]
description: A list of all the MicroSims used in the [Course Name] course
image: /sims/index-screen-image.png
og:image: /sims/index-screen-image.png
hide:
    toc
---
```

#### Grid Cards Structure

```markdown
# List of MicroSims for [Course Name]

Interactive Micro Simulations to help students learn [subject] fundamentals.

<div class="grid cards" markdown>

-   **[MicroSim Title](./microsim-name/index.md)**

    ---

    ![MicroSim Title](./microsim-name/microsim-name.png)

    Short description of what the MicroSim does and teaches.

</div>
```

#### Card Item Format

Each card follows this exact structure (order matters):

1. **Title with link** - Bold linked title
2. **Horizontal rule** - `---` separator
3. **Image** - Screenshot with alt text matching title
4. **Description** - 1-2 sentence summary

Example card:
```markdown
-   **[Command Syntax Visual Guide](./command-syntax/index.md)**

    ---

    ![Command Syntax Visual Guide](./command-syntax/command-syntax.png)

    Color-coded breakdown of Linux command structure showing commands, options, and arguments with hover explanations.
```

### Step 6: Sort Alphabetically

Sort all MicroSim cards alphabetically by their title. This ensures consistent ordering across the index page and navigation.

### Step 7: Update mkdocs.yml Navigation

Locate the MicroSims section in `mkdocs.yml` and update it with alphabetically sorted entries:

```yaml
  - MicroSims:
    - List of Microsims: sims/index.md
    - Bash vs Zsh: sims/bash-vs-zsh/index.md
    - Command Syntax Guide: sims/command-syntax/index.md
    # ... additional entries alphabetically
```

Keep "List of Microsims" as the first entry, then sort remaining items alphabetically.

## Output Files

This skill creates or updates:

1. `/docs/sims/index.md` - The main MicroSims index page
2. `/docs/sims/<name>/<name>.png` - Screenshot for each MicroSim (if missing)
3. `mkdocs.yml` - Updated navigation section for MicroSims

## Example Output

A complete index page for a Linux course with 12 MicroSims:

```markdown
---
title: List of MicroSims for Learning Linux
description: A list of all the MicroSims used in the Teaching Linux course
image: /sims/index-screen-image.png
og:image: /sims/index-screen-image.png
hide:
    toc
---
# List of MicroSims for Learning Linux

Interactive Micro Simulations to help students learn Linux fundamentals.

<div class="grid cards" markdown>

-   **[Bash vs Zsh Comparison](./bash-vs-zsh/index.md)**

    ---

    ![Bash vs Zsh Comparison](./bash-vs-zsh/bash-vs-zsh.png)

    Side-by-side comparison of `bash` and `zsh` shells with star ratings for compatibility, features, and customization.

-   **[Command Syntax Visual Guide](./command-syntax/index.md)**

    ---

    ![Command Syntax Visual Guide](./command-syntax/command-syntax.png)

    Color-coded breakdown of Linux command structure showing commands, options, and arguments with hover explanations.

</div>
```

## Troubleshooting

### Screenshot Capture Fails

If screenshot capture fails:
1. Verify Chrome/Chromium is installed
2. Check that `main.html` exists in the MicroSim directory
3. Increase delay for JavaScript-heavy simulations
4. Check for CDN loading issues (may need network access)

### Grid Cards Not Rendering

Ensure mkdocs.yml has required extensions:
```yaml
markdown_extensions:
  - attr_list
  - md_in_html
```

### Images Not Displaying

Verify image paths use relative format: `./microsim-name/microsim-name.png`
