# Book Utilities (bk) - Shell Scripts for Claude Skills

This directory contains the **bk*** (Book utilities) collection of shell scripts for managing Claude skills and intelligent textbook projects. All scripts use the `$BK_HOME` environment variable for consistent operation.

## Prerequisites

### Required: BK_HOME Environment Variable

All `bk*` scripts require the `$BK_HOME` environment variable to be set. This variable should point to the root directory of your claude-skills repository.

**Setup:**

Add this line to your shell startup file (`~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):

```bash
export BK_HOME=/path/to/your/claude-skills
```

**Example:**
```bash
export BK_HOME=$HOME/Documents/ws/claude-skills
```

After adding the line, reload your shell configuration:
```bash
source ~/.bashrc  # or ~/.zshrc, etc.
```

**Verify it's set:**
```bash
echo $BK_HOME
```

### Recommended: Personal Binary Location

For easy command-line access from anywhere, install scripts to your personal binary directory:

`$HOME/.local/bin` (or `~/.local/bin`)

Add this to your shell startup file:

**For Bash/Zsh:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**For Fish:**
```fish
set -gx PATH $HOME/.local/bin $PATH
```

## Installation

### Quick Start

1. **Set BK_HOME** (required):
   ```bash
   export BK_HOME=/path/to/claude-skills
   ```

2. **Install bk* scripts**:
   ```bash
   $BK_HOME/scripts/bk-install-scripts
   ```

3. **Install skills** to `~/.claude/skills`:
   ```bash
   bk-install-skills
   ```

4. **Verify with the main menu**:
   ```bash
   bk
   ```

## Available Scripts

All `bk*` scripts require `$BK_HOME` to be set and provide consistent colored output with comprehensive error checking.

**Skill Management:**
- `bk-list-skills` - List available Claude skills
- `bk-analyze-skill-usage` - Generate skill usage analysis report
- `bk-install-skills` - Install skills to ~/.claude/skills

**Script Management:**
- `bk-install-scripts` - Install bk* scripts to ~/.local/bin
- `bk` - Main menu for all utilities

**Textbook Building:**
- `bk-book-status` - Display textbook workflow status
- `bk-generate-book-metrics` - Generate book metrics report

**Image Processing:**
- `bk-resize-images` - Compress images for web
- `bk-capture-screenshot` - Capture MicroSim screenshots

**Plugin Installation:**
- `bk-install-social-override-plugin` - Install MkDocs social override plugin

### bk

Main menu script that lists all available `bk*` utilities with descriptions and allows running them by number.

**Usage:**
```bash
bk           # Show menu
bk 1         # Run the first utility
```

**Example output:**
```
════════════════════════════════════════════════════════════════
Build/Book Utilities
════════════════════════════════════════════════════════════════
BK_HOME: $HOME/Documents/ws/claude-skills

  1. bk-resize-images              Compress large images to ~300KB PNG format
  2. bk-book-status                Display intelligent textbook building workflow status
```

### bk-install-scripts

Installs symbolic links for all `bk*` scripts to `$HOME/.local/bin`.

**Requirements:** `$BK_HOME` must be set

**Usage:**
```bash
bk-install-scripts
```

**Features:**
- Validates `$BK_HOME` exists
- Creates `$HOME/.local/bin` if needed
- Links all executable `bk*` scripts
- Reports total count and lists all installed links
- Checks if `$HOME/.local/bin` is in PATH

### bk-install-skills

Creates symbolic links in `~/.claude/skills/` for all skills in `$BK_HOME/skills/`.

**Requirements:** `$BK_HOME` must be set

**Usage:**
```bash
bk-install-skills
```

**Features:**
- Validates `$BK_HOME/skills` exists
- Creates `~/.claude/skills` if needed
- Links all skill directories
- Reports installed skills with count
- Checks for broken symlinks and suggests fixes

### bk-list-skills

Lists all available Claude skills from three locations: source (BK_HOME/skills), user (~/.claude/skills), and project (.claude/skills).

**Requirements:** `$BK_HOME` must be set

**Usage:**
```bash
bk-list-skills                    # Default: names with locations
bk-list-skills --full             # Detailed descriptions
bk-list-skills --names-only       # Just skill names
bk-list-skills --json             # JSON format
```

**Features:**
- Shows skills from source repository, global install, and project
- Color-coded output by location
- Counts skills from all three locations
- JSON output includes all metadata

**Example output:**
```
faq-generator (source, global)
glossary-generator (source, global)
learning-graph-generator (source, global)

Skill locations:
  source  - Skills from $HOME/Documents/ws/claude-skills/skills
  global  - Installed skills in ~/.claude/skills
  project - Project-specific skills in .claude/skills
```

### bk-analyze-skill-usage

Generates a comprehensive skill usage analysis report from activity logs. Analyzes skill invocations, performance metrics, and usage patterns to help understand which skills are most used and how they perform.

**Requirements:** `$BK_HOME` must be set, Python 3 installed, activity logging enabled

**Usage:**
```bash
bk-analyze-skill-usage                    # Use default log directory
bk-analyze-skill-usage /path/to/logs      # Use custom log directory
```

**Features:**
- Analyzes skill usage frequency and patterns
- Calculates average and total duration for each skill
- Correlates prompts with skill invocations
- Shows recent skill usage history
- Provides insights and optimization suggestions
- Reports total time automated by skills

**Output includes:**
- Most used skills ranking
- Performance metrics (average/total duration)
- Common prompts that trigger skills
- Recent skill usage table (last 20 invocations)
- Insights about frequently used and slowest skills

### bk-book-status

Displays the status of intelligent textbook building workflow by running a Python analysis script.

**Requirements:** `$BK_HOME` must be set, Python 3 installed

**Usage:**
```bash
bk-book-status
```

**Features:**
- Validates `$BK_HOME/src/site-metrics/book-status.py` exists
- Checks for Python 3 availability
- Runs workflow status analysis

### bk-resize-images

Compresses large images to approximately 300KB PNG format for web optimization.

**Requirements:** `$BK_HOME` must be set, Python 3 and Pillow installed

**Usage:**
```bash
bk-resize-images [args]
```

**Features:**
- Validates `$BK_HOME/src/resize-images/compress-images.py` exists
- Checks for Python 3 and Pillow/PIL
- Passes all arguments to Python script
- Changes to `$BK_HOME` before running

### bk-capture-screenshot

Captures high-quality screenshots of MicroSims using Chrome headless mode. Can be run from within a MicroSim directory or by providing a path.

**Requirements:** Google Chrome or Chromium installed

**Usage:**
```bash
cd /path/to/microsim && bk-capture-screenshot   # Use current directory
bk-capture-screenshot /path/to/microsim         # Specify directory path
```

**Features:**
- Automatically detects MicroSim name from directory
- Validates main.html exists
- Uses Chrome headless mode for rendering
- Handles JavaScript-heavy visualizations with proper timeout
- Allows loading external CDN resources
- Generates PNG file named after the MicroSim
- Provides clear success/failure feedback with file size

**Output:**
- Creates `{microsim-name}.png` in the MicroSim directory
- Screenshot size: 1200x800 pixels
- Includes all rendered content after JavaScript execution

**Technical details:**
- Uses `--headless=new` for latest Chrome headless mode
- 5-second timeout for JavaScript rendering
- Disables web security to allow CDN resources
- Hides scrollbars for clean captures

### bk-install-social-override-plugin

Installs the social_override plugin for mkdocs-material into the current directory for custom social media card images.

**Requirements:** `$BK_HOME` must be set, pip installed

**Usage:**
```bash
cd /path/to/mkdocs-project
bk-install-social-override-plugin
```

**Features:**
- Validates `$BK_HOME` is set
- Warns if mkdocs.yml not found in current directory
- Creates plugin files in current directory
- Installs plugin with pip
- Provides clear next steps for configuration

## Architecture

### Consistent Design Pattern

All `bk*` scripts follow a consistent pattern:

1. **Validation**: Check `$BK_HOME` is set and exists
2. **Directory checks**: Validate required subdirectories exist
3. **Colored output**: Use consistent color scheme (green=success, yellow=warning, blue=info, red=error)
4. **Error handling**: Provide helpful error messages with suggestions
5. **Visual formatting**: Use consistent separators and formatting

### Color Scheme

- **Green**: Success messages, checkmarks
- **Yellow**: Warnings, important paths
- **Blue**: Section headers, informational text
- **Red**: Errors, failures

### Error Messages

All scripts provide actionable error messages:
- What went wrong
- What was expected
- How to fix it (with examples)

## Requirements

- **Bash** shell (version 4.0 or later)
- **$BK_HOME** environment variable set
- Standard Unix tools: `find`, `grep`, `sed`
- Python 3 (for scripts that call Python programs)
- Specific Python packages as needed (Pillow for image scripts)

## Benefits of BK_HOME Design

1. **Consistency**: All scripts use the same base directory
2. **Portability**: Works from any directory after installation
3. **Validation**: Scripts check environment before running
4. **Flexibility**: Easy to switch between different claude-skills installations
5. **Error Prevention**: Clear error messages guide users to fix configuration

## Notes

- All `bk*` scripts validate `$BK_HOME` before running
- Scripts use `$BK_HOME` to locate resources (skills, Python programs, etc.)
- Symbolic linking strategy keeps scripts current with repository
- Consistent error messages help troubleshooting
- Scripts can be run from any directory (once installed)
- The `bk` menu automatically discovers and lists all `bk*` scripts
