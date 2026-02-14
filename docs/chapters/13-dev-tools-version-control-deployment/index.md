# Development Tools, Version Control, and Deployment

## Summary

This final chapter brings together all the tools and techniques needed to complete and deploy your intelligent textbook project. You'll learn to use Visual Studio Code effectively for content development, including working with the integrated terminal. The chapter covers Bash shell scripting, script execution permissions, and essential command-line operations including directory navigation, file creation and editing, and symlink creation for skill installation.

The chapter synthesizes all the skills, tools, and knowledge from previous chapters as you work through the capstone project: creating a complete intelligent textbook from start to finish. This culminating experience demonstrates your ability to apply course description development, learning graph generation, content creation, interactive element integration, and deployment workflows to produce a professional, AI-enhanced educational resource.

## Concepts Covered

This chapter covers the following 10 concepts from the learning graph:

1. Visual Studio Code
2. VS Code for Content Development
3. Terminal in VS Code
4. Bash
5. Shell Scripts
6. Script Execution Permissions
7. Directory Navigation
8. File Creation and Editing
9. Symlink Creation
10. Capstone: Complete Textbook Project

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction to AI and Intelligent Textbooks](../01-intro-ai-intelligent-textbooks/index.md)
- [Chapter 2: Getting Started with Claude and Skills](../02-getting-started-claude-skills/index.md)
- [Chapter 4: Introduction to Learning Graphs](../04-intro-learning-graphs/index.md)
- [Chapter 10: Content Creation Workflows](../10-content-creation-workflows/index.md)
- [Chapter 11: Educational Resources and Assessment](../11-educational-resources-assessment/index.md)
- [Chapter 12: Interactive Elements and MicroSims](../12-interactive-elements-microsims/index.md)

---

## Introduction

Creating intelligent textbooks requires mastery of professional development tools and workflows that streamline content creation, version control, and deployment. This chapter introduces the essential development environment used throughout the intelligent textbook creation process, focusing on Visual Studio Code as the primary content authoring platform and Bash shell scripting for automation.

Unlike traditional textbook authoring tools like Microsoft Word or Google Docs, intelligent textbook development leverages software engineering practices including version control with Git, command-line workflows, and automated deployment pipelines. These practices enable collaborative content development, reproducible builds, and seamless publication to web platforms like GitHub Pages.

By the end of this chapter, you'll work through a comprehensive capstone project that integrates all the skills, tools, and workflows from previous chapters to create a complete intelligent textbook from concept to deployment.

## Visual Studio Code

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft that has become the de facto standard for modern software development and technical content creation. While it was initially designed for programming, its extensibility, integrated terminal, and markdown preview capabilities make it ideal for intelligent textbook authoring.

### Why VS Code for Textbook Development?

Traditional word processors are optimized for print documents with fixed page layouts, while intelligent textbooks are dynamic, web-based resources built from markdown source files. VS Code provides several advantages for this workflow:

- **Markdown editing with live preview:** Real-time rendering of formatted content
- **Integrated Git support:** Version control operations without leaving the editor
- **Built-in terminal:** Execute MkDocs commands, Python scripts, and shell utilities
- **Extension ecosystem:** Plugins for spell-checking, markdown linting, and diagram generation
- **Multi-file management:** Navigate complex textbook structures with hundreds of files
- **Search and replace across files:** Consistent terminology and formatting at scale

### Key Features for Content Creators

The following features are particularly valuable for intelligent textbook development:

- **Explorer panel:** Navigate chapter directories, MicroSim folders, and asset files
- **Search panel:** Find all references to specific concepts across the entire textbook
- **Source control panel:** Track changes, create commits, and push updates to GitHub
- **Extensions marketplace:** Install tools like Markdown All in One, Code Spell Checker, and MkDocs plugins
- **Integrated terminal:** Run `mkdocs serve`, execute Python scripts, and manage dependencies
- **Command palette (Cmd/Ctrl+Shift+P):** Quick access to all VS Code functionality

#### Diagram: VS Code Interface Layout for Textbook Development

<iframe src="../../sims/vs-code-interface-layout-for-textbook-development/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>VS Code Interface Layout for Textbook Development</summary>
    Type: diagram

    Purpose: Show the VS Code interface configured for intelligent textbook authoring

    Components to show:
    - Activity Bar (far left): Explorer, Search, Source Control, Extensions icons highlighted
    - Side Bar (left): Explorer panel showing typical textbook directory structure:
      /docs
        /chapters
          /01-intro-ai-intelligent-textbooks
          /02-getting-started-claude-skills
          (etc.)
        /sims
        /learning-graph
        mkdocs.yml
    - Editor Group (center): Split view showing:
      - Left pane: index.md file in edit mode with markdown content
      - Right pane: Markdown preview pane showing rendered content
    - Panel (bottom): Integrated terminal showing "mkdocs serve" command running
    - Status Bar (bottom): Git branch indicator, file type, cursor position

    Annotations:
    - Arrow pointing to Explorer: "Navigate textbook structure"
    - Arrow pointing to Split editor: "Edit and preview simultaneously"
    - Arrow pointing to Terminal: "Run MkDocs and Python scripts"
    - Arrow pointing to Source Control icon: "Track changes with Git"

    Visual style: Modern interface mockup with realistic VS Code color scheme (dark theme)
    Color scheme: VS Code Dark+ theme colors (dark gray background, syntax highlighting)

    Implementation: SVG diagram or annotated screenshot

---
**MicroSim Generator Recommendations:**

1. markdown/screenshot (best) - VS Code interface doesn't benefit from interactivity, annotated image clearest
2. microsim-p5 (80/100) - If interactive tour/highlighting needed, p5.js with hover zones works
3. mermaid-generator (50/100) - Not designed for UI interface mockups or screenshots

</details>

### Installation and Setup

VS Code can be downloaded from [code.visualstudio.com](https://code.visualstudio.com) for macOS, Windows, and Linux. For intelligent textbook development, install these recommended extensions:

| Extension | Purpose | Installation Command |
|-----------|---------|---------------------|
| Markdown All in One | Keyboard shortcuts, auto-preview, TOC generation | `code --install-extension yzhang.markdown-all-in-one` |
| Code Spell Checker | Catch typos in markdown content | `code --install-extension streetsidesoftware.code-spell-checker` |
| Markdown Preview Enhanced | Advanced preview with diagrams and export | `code --install-extension shd101wyy.markdown-preview-enhanced` |
| Python | Syntax highlighting for Python scripts | `code --install-extension ms-python.python` |

After installation, configure VS Code for optimal markdown editing by adding these settings to your user settings (Cmd/Ctrl+,):

```json
{
  "editor.wordWrap": "on",
  "editor.formatOnSave": true,
  "markdown.preview.breaks": true,
  "files.trimTrailingWhitespace": true
}
```

## VS Code for Content Development

While VS Code is a powerful general-purpose editor, intelligent textbook content development requires specific workflows and practices that differ from traditional software development. This section covers techniques for efficiently authoring markdown content, managing chapter files, and integrating with the MkDocs build system.

### Content Authoring Workflow

A typical content development session follows this pattern:

1. **Open the project folder:** Use File → Open Folder to load the entire textbook repository
2. **Start the development server:** Open integrated terminal and run `mkdocs serve`
3. **Navigate to target chapter:** Use Explorer panel to locate the chapter's index.md file
4. **Edit in split view:** Open markdown preview (Cmd/Ctrl+K V) to see rendered output
5. **Save frequently:** VS Code auto-saves, but Cmd/Ctrl+S forces immediate update
6. **Preview in browser:** Navigate to `http://localhost:8000` to see the full site

This workflow enables rapid iteration, where changes to markdown files are immediately reflected in the browser preview within 1-2 seconds of saving.

### Multi-File Editing Techniques

Intelligent textbooks often require editing multiple files simultaneously—for example, updating a concept definition in the glossary while editing chapter content. VS Code provides several techniques for efficient multi-file editing:

- **Split editor groups:** Drag tabs to create side-by-side or stacked editor layouts
- **Quick Open (Cmd/Ctrl+P):** Type partial filename to instantly open any file
- **Go to Symbol (Cmd/Ctrl+Shift+O):** Navigate to specific headers within long markdown files
- **Breadcrumbs:** Show file path and document structure at top of editor
- **Tab groups:** Organize related files (e.g., all Chapter 3 materials) in separate tab groups

For complex editing tasks like renaming a concept across all chapters, use VS Code's search and replace across files feature:

- Open Search panel (Cmd/Ctrl+Shift+F)
- Enter search term: "Configuration Item (CI)"
- Enter replacement: "Configuration Item"
- Review matches in context
- Replace All to update all instances

### Markdown Productivity Tips

The following keyboard shortcuts and features accelerate markdown authoring:

- **Cmd/Ctrl+B:** Toggle bold formatting on selected text
- **Cmd/Ctrl+I:** Toggle italic formatting
- **Cmd/Ctrl+Shift+V:** Open markdown preview in new tab
- **Cmd/Ctrl+K V:** Open preview to the side
- **Alt+Shift+F:** Auto-format current markdown file
- **Cmd/Ctrl+/:** Toggle comment on selected lines (useful for temporary removal)

The Markdown All in One extension adds additional shortcuts:

- **Cmd/Ctrl+Shift+]:** Insert/update table of contents
- **Alt+C:** Check/uncheck task list items
- **Ctrl+Shift+[:** Decrease heading level
- **Ctrl+Shift+]:** Increase heading level

## Terminal in VS Code

The integrated terminal in VS Code eliminates context switching between the editor and a separate terminal application, enabling seamless execution of build commands, Python scripts, and Git operations. This integration is particularly valuable for intelligent textbook workflows where content editing and script execution are tightly coupled.

### Accessing the Integrated Terminal

The terminal can be opened in several ways:

- **Keyboard shortcut:** Ctrl+` (backtick) toggles terminal visibility
- **Menu:** View → Terminal
- **Command Palette:** Cmd/Ctrl+Shift+P, then type "Terminal: Create New Integrated Terminal"

By default, the terminal appears in the Panel area at the bottom of the VS Code window, but it can be moved to the side or floated as a separate panel.

### Terminal Features for Textbook Development

The integrated terminal provides several advantages over standalone terminal applications:

- **Automatic working directory:** Terminal opens in the project root directory
- **Output linking:** Click file paths in error messages to jump to that file
- **Split terminals:** Run multiple commands simultaneously (e.g., `mkdocs serve` in one, Python scripts in another)
- **Command history:** Use up/down arrows to recall previous commands
- **Copy/paste integration:** Cmd/Ctrl+C/V work as expected (no special terminal shortcuts needed)

### Common Terminal Commands for Textbook Projects

The following commands are executed frequently during intelligent textbook development:

| Command | Purpose | Typical Output |
|---------|---------|----------------|
| `mkdocs serve` | Start local development server | `Serving on http://127.0.0.1:8000` |
| `mkdocs build --strict` | Build site and fail on warnings | `INFO - Building documentation...` |
| `python docs/learning-graph/analyze-graph.py` | Validate learning graph structure | `Quality score: 87/100` |
| `./scripts/list-skills.sh` | List available Claude skills | `Available skills: glossary-generator, quiz-generator...` |
| `git status` | Check current repository state | `On branch main, nothing to commit` |
| `git add . && git commit -m "message"` | Stage and commit changes | `[main abc1234] message` |

### Managing Multiple Terminal Sessions

Complex workflows often require multiple simultaneous terminal sessions. VS Code supports this through terminal splitting and tabs:

- **Create new terminal:** Click + icon in terminal toolbar
- **Split terminal:** Click split icon to create side-by-side terminals
- **Rename terminal:** Right-click terminal tab, select "Rename"
- **Kill terminal:** Click trash icon or exit the shell process

A typical intelligent textbook development session might maintain three terminal sessions:

1. **Development server terminal:** Running `mkdocs serve` continuously
2. **Script execution terminal:** For running Python analysis scripts and skill invocations
3. **Git operations terminal:** For staging commits and pushing changes
#### Diagram: Terminal Workflow for Textbook Development

<iframe src="../../sims/terminal-workflow-textbook/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Terminal Workflow for Textbook Development</summary>
    Type: workflow

    Purpose: Illustrate the typical terminal command sequence for developing and deploying textbook content

    Visual style: Flowchart with terminal command boxes and decision points

    Steps:
    1. Start: "Open project in VS Code"
       Hover text: "File → Open Folder, select textbook repository"

    2. Process: "Open integrated terminal (Ctrl+`)"
       Hover text: "Terminal opens in project root directory"

    3. Process: "mkdocs serve"
       Hover text: "Starts development server on localhost:8000"

    4. Decision: "Need to run Python scripts?"
       Hover text: "Learning graph analysis, content generation, etc."

    5a. Process: "Create new terminal (+)"
        Hover text: "Keep mkdocs serve running in first terminal"

    5b. Continue to step 6

    6. Process: "Edit markdown files"
       Hover text: "Changes auto-reload in browser within 1-2 seconds"

    7. Process: "python docs/learning-graph/analyze-graph.py"
       Hover text: "Validate learning graph quality and structure"

    8. Decision: "Quality check passed?"
       Hover text: "Review quality-metrics.md for issues"

    9a. Process: "Fix identified issues"
        Hover text: "Edit learning-graph.csv, re-run analysis"
        Returns to step 6

    9b. Continue to step 10

    10. Process: "git add . && git commit -m 'message'"
        Hover text: "Stage all changes and create commit"

    11. Process: "git push origin main"
        Hover text: "Push commits to GitHub repository"

    12. Process: "mkdocs gh-deploy"
        Hover text: "Build site and deploy to GitHub Pages"

    13. End: "Textbook published"
        Hover text: "Changes live at https://username.github.io/textbook-name"

    Color coding:
    - Blue: Terminal commands
    - Yellow: Decision points
    - Green: Git operations
    - Orange: Deployment steps

    Swimlanes:
    - Terminal 1 (Development Server)
    - Terminal 2 (Script Execution)
    - Terminal 3 (Git Operations)

    Implementation: SVG flowchart with interactive hover states (HTML/CSS/JavaScript)

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (95/100) - Terminal command workflow with sequential steps is ideal flowchart
2. microsim-p5 (73/100) - Custom workflow with interactive command highlighting possible
3. vis-network (55/100) - Can model workflow as graph but less intuitive than flowchart

</details>

## Bash

Bash (Bourne Again Shell) is the default command-line shell on macOS and most Linux distributions, providing a text-based interface for executing commands, running scripts, and automating workflows. While Windows uses PowerShell by default, Windows Subsystem for Linux (WSL) provides access to Bash on Windows systems.

Understanding Bash is essential for intelligent textbook development because the MkDocs build system, Python script execution, Git version control, and deployment automation all rely on command-line operations.

### Shell vs. Terminal vs. Bash

These terms are often used interchangeably but have distinct meanings:

- **Terminal:** The application that provides a text interface (e.g., Terminal.app on macOS, Windows Terminal)
- **Shell:** The program that interprets commands (e.g., Bash, Zsh, Fish, PowerShell)
- **Bash:** A specific shell implementation, currently the most widely used on Unix-like systems

When you open the integrated terminal in VS Code, you're opening a terminal application that runs a shell (typically Bash or Zsh on macOS/Linux, PowerShell on Windows).

### Bash Command Structure

Bash commands follow a consistent structure:

```bash
command [options] [arguments]
```

For example, the command `ls -la /docs/chapters` breaks down as:

- **Command:** `ls` (list directory contents)
- **Options:** `-la` (long format, show hidden files)
- **Arguments:** `/docs/chapters` (directory to list)

Options typically start with `-` (single dash) for short options or `--` (double dash) for long options. Multiple short options can be combined: `-l -a` is equivalent to `-la`.

### Essential Bash Commands for Textbook Development

The following commands are used frequently in intelligent textbook workflows:

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Print working directory | `pwd` → `/Users/username/textbook-project` |
| `ls` | List directory contents | `ls -la docs/chapters` |
| `cd` | Change directory | `cd docs/chapters/01-intro` |
| `mkdir` | Create directory | `mkdir docs/sims/new-microsim` |
| `touch` | Create empty file | `touch docs/chapters/05-graphs/index.md` |
| `cp` | Copy files | `cp template.md chapter-03.md` |
| `mv` | Move/rename files | `mv old-name.md new-name.md` |
| `rm` | Remove files | `rm docs/chapters/draft.md` |
| `cat` | Display file contents | `cat mkdocs.yml` |
| `grep` | Search text | `grep "learning graph" docs/**/*.md` |
| `chmod` | Change file permissions | `chmod +x scripts/install-skills.sh` |
| `ln` | Create symbolic link | `ln -s ~/.claude/skills/glossary-generator ./` |

### Bash Environment and Variables

Bash maintains environment variables that configure shell behavior and store system information. Common variables include:

- `$HOME`: User's home directory (e.g., `/Users/username`)
- `$PATH`: Directories searched for executable commands
- `$PWD`: Current working directory
- `$USER`: Current username

You can display variable values using `echo`:

```bash
echo $HOME      # /Users/username
echo $PATH      # /usr/local/bin:/usr/bin:/bin
echo $PWD       # /Users/username/textbook-project
```

### Command Chaining and Redirection

Bash allows combining multiple commands using operators:

- **Sequential execution (`;`):** Run commands one after another regardless of success
  ```bash
  cd docs/learning-graph; python analyze-graph.py learning-graph.csv quality-metrics.md
  ```

- **Conditional execution (`&&`):** Run second command only if first succeeds
  ```bash
  mkdocs build --strict && mkdocs gh-deploy
  ```

- **Output redirection (`>`):** Save command output to file
  ```bash
  python analyze-graph.py learning-graph.csv > quality-report.txt
  ```

- **Append to file (`>>`):** Add command output to end of existing file
  ```bash
  echo "Quality check completed" >> build-log.txt
  ```

- **Pipe (`|`):** Send output of one command as input to another
  ```bash
  ls -la | grep ".md"     # List only markdown files
  ```

## Directory Navigation

Efficient directory navigation is fundamental to command-line workflows, enabling quick access to chapter files, MicroSim directories, Python scripts, and configuration files. While graphical file browsers are intuitive, command-line navigation is often faster for developers who have memorized their project structure.

### Understanding File Paths

File paths specify the location of files and directories in the filesystem hierarchy. There are two types of paths:

- **Absolute paths:** Start from the root directory (`/` on Unix, `C:\` on Windows)
  ```bash
  /Users/username/Documents/textbook-project/docs/chapters/01-intro/index.md
  ```

- **Relative paths:** Start from the current working directory
  ```bash
  # If current directory is /Users/username/Documents/textbook-project
  docs/chapters/01-intro/index.md
  ```

Special directory references:

- `.` (single dot): Current directory
- `..` (double dot): Parent directory
- `~` (tilde): User's home directory
- `-` (dash): Previous working directory

### Navigating the Filesystem

The `cd` (change directory) command moves between directories:

```bash
# Navigate to home directory
cd ~

# Navigate to specific project directory
cd ~/Documents/textbook-project

# Navigate to subdirectory (relative path)
cd docs/chapters

# Go up one level to parent directory
cd ..

# Go up two levels
cd ../..

# Return to previous directory
cd -

# Navigate to root directory
cd /
```

### Intelligent Textbook Directory Structure

A typical intelligent textbook project has this structure:

```
textbook-project/
├── docs/
│   ├── chapters/
│   │   ├── 01-intro-ai-intelligent-textbooks/
│   │   │   └── index.md
│   │   ├── 02-getting-started-claude-skills/
│   │   │   └── index.md
│   │   └── (more chapters...)
│   ├── sims/
│   │   ├── graph-traversal/
│   │   │   ├── main.html
│   │   │   └── index.md
│   │   └── (more MicroSims...)
│   ├── learning-graph/
│   │   ├── learning-graph.csv
│   │   ├── learning-graph.json
│   │   ├── analyze-graph.py
│   │   └── quality-metrics.md
│   ├── glossary.md
│   ├── faq.md
│   └── index.md
├── scripts/
│   ├── install-claude-skills.sh
│   └── list-skills.sh
├── .claude/
│   ├── skills/
│   └── commands/
├── mkdocs.yml
├── README.md
└── requirements.txt
```

### Navigation Best Practices

Efficient navigation requires understanding project structure and using shortcuts:

- **Use tab completion:** Type first few characters and press Tab to autocomplete
  ```bash
  cd docs/ch<Tab>     # Autocompletes to docs/chapters/
  ```

- **Use wildcards for pattern matching:**
  ```bash
  ls docs/chapters/*/index.md     # List all chapter index files
  ```

- **Create shell aliases for frequent destinations:**
  ```bash
  alias chapters="cd ~/Documents/textbook-project/docs/chapters"
  alias sims="cd ~/Documents/textbook-project/docs/sims"
  ```

- **Use `pushd` and `popd` for temporary directory changes:**
  ```bash
  pushd docs/learning-graph    # Navigate and save previous location
  python analyze-graph.py learning-graph.csv quality-metrics.md
  popd                         # Return to previous location
  ```
#### Diagram: Interactive Directory Navigation Practice MicroSim

<iframe src="../../sims/interactive-directory-navigation-practice-microsim/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Interactive Directory Navigation Practice MicroSim</summary>
    Type: microsim

    Learning objective: Practice Bash directory navigation commands in a simulated filesystem without risk of breaking a real project

    Canvas layout (900x700px):
    - Left side (550x700): Simulated terminal interface showing:
      - Current working directory display at top
      - Command input field
      - Command output area
      - Command history (last 5 commands)
    - Right side (350x700): Visual filesystem tree showing:
      - Root directory
      - Expandable/collapsible directories
      - Current location highlighted in yellow
      - Files shown as leaf nodes

    Visual elements:
    - Terminal with black background, green text (retro style)
    - Filesystem tree with folder icons (📁) and file icons (📄)
    - Current directory highlighted with yellow background
    - Valid commands show success in green, errors in red
    - Breadcrumb trail showing path to current location

    Simulated filesystem structure:
    ```
    /home/student/
    ├── textbook-project/
    │   ├── docs/
    │   │   ├── chapters/
    │   │   │   ├── 01-intro/
    │   │   │   │   └── index.md
    │   │   │   └── 02-graphs/
    │   │   │       └── index.md
    │   │   ├── sims/
    │   │   │   └── graph-viz/
    │   │   │       └── main.html
    │   │   └── learning-graph/
    │   │       ├── learning-graph.csv
    │   │       └── analyze-graph.py
    │   ├── scripts/
    │   │   └── install-skills.sh
    │   └── mkdocs.yml
    └── Downloads/
        └── readme.txt
    ```

    Interactive controls (right panel):
    - Display: Current working directory (e.g., "/home/student")
    - Text input: Command entry field
    - Button: "Execute Command"
    - Button: "Clear Terminal"
    - Button: "Reset to Home"
    - Checkbox: "Show hidden files"
    - Display: Challenge progress (5 challenges)

    Supported commands:
    - `pwd`: Display current directory
    - `ls`: List current directory contents
    - `ls -la`: List with details
    - `cd <directory>`: Change to specified directory
    - `cd ..`: Go to parent directory
    - `cd ~`: Go to home directory
    - `cd -`: Go to previous directory

    Default parameters:
    - Starting directory: /home/student
    - Challenge mode: Enabled
    - Show hints: True

    Challenges (progressively harder):
    1. "Navigate to the textbook-project directory"
       Solution: `cd textbook-project`
    2. "List the contents of the docs directory without changing into it"
       Solution: `ls docs`
    3. "Navigate to the chapters directory using a relative path"
       Solution: `cd docs/chapters`
    4. "Navigate to the scripts directory from chapters"
       Solution: `cd ../../scripts`
    5. "Return to the previous directory using the dash shortcut"
       Solution: `cd -`

    Behavior:
    - When user enters command, parse and validate it
    - If valid, update current directory and filesystem tree highlight
    - Display command output in terminal area
    - Show error message for invalid commands
    - Track challenge completion (green checkmark when solved)
    - Provide hint button that shows first step of current challenge

    Interactive features:
    - Click directories in tree view to highlight them (doesn't navigate)
    - Hover over directories shows full path
    - Right-click file/directory shows properties (size, permissions)
    - Double-click directory in tree auto-fills `cd` command

    Feedback:
    - Success messages: "✓ Navigated to /home/student/textbook-project"
    - Error messages: "✗ Directory not found: 'doc' (did you mean 'docs'?)"
    - Challenge completion: "🎉 Challenge 1 complete! (4 remaining)"
    - Hints: "💡 Hint: Try using 'cd' followed by the directory name"

    Implementation notes:
    - Use p5.js for rendering
    - Store filesystem as nested JavaScript object
    - Track current working directory as array of path segments
    - Parse commands using string splitting and regex
    - Implement basic tab completion (suggest directory names)
    - Save progress to localStorage for session persistence


---
**MicroSim Generator Recommendations:**

1. microsim-p5 (94/100) - Interactive directory navigation simulator with terminal emulation is p5.js strength
2. vis-network (85/100) - Can show filesystem as interactive tree graph with navigation
3. mermaid-generator (78/100) - Tree diagram for filesystem but limited interactivity

</details>

## File Creation and Editing

Command-line file creation and editing are essential skills for automating textbook workflows, especially when generating multiple files from templates or making bulk updates. While VS Code is the primary editor for content development, knowing command-line file operations enables scripting and automation.

### Creating Files

The `touch` command creates empty files or updates the modification timestamp of existing files:

```bash
# Create a new chapter index file
touch docs/chapters/14-future-directions/index.md

# Create multiple files at once
touch docs/chapters/14-future-directions/{index.md,exercises.md,glossary.md}
```

The `echo` command combined with output redirection creates files with initial content:

```bash
# Create file with single line of content
echo "# Chapter 14: Future Directions" > docs/chapters/14-future-directions/index.md

# Append content to existing file
echo "## Summary" >> docs/chapters/14-future-directions/index.md
```

For multi-line content, use a here-document:

```bash
cat << EOF > docs/chapters/14-future-directions/index.md
# Chapter 14: Future Directions

## Summary

This chapter explores emerging trends in AI-assisted education.

## Concepts Covered

1. Large Language Models
2. Adaptive Learning Systems
3. Real-time Content Generation
EOF
```

### Editing Files

While command-line text editors like `vim`, `nano`, and `emacs` are available, most intelligent textbook developers prefer editing in VS Code. However, simple text transformations can be performed using command-line tools:

**`sed` (stream editor):** Perform find-and-replace operations

```bash
# Replace all occurrences of "CMDB" with "Configuration Management Database"
sed -i '' 's/CMDB/Configuration Management Database/g' docs/chapters/*/index.md

# Add a line after a specific pattern
sed -i '' '/## Summary/a\
This chapter covers fundamental concepts.' docs/chapters/14-future-directions/index.md
```

**`awk` (text processing):** Extract and transform structured text

```bash
# Extract all level-2 headers from a file
awk '/^## / {print $0}' docs/chapters/01-intro/index.md

# Print only lines containing "learning graph"
awk '/learning graph/ {print}' docs/chapters/*/index.md
```

**`grep` (pattern matching):** Search for text patterns

```bash
# Find all chapters mentioning "MicroSim"
grep -r "MicroSim" docs/chapters/

# Count occurrences of "learning graph" in all markdown files
grep -r "learning graph" docs/ --include="*.md" | wc -l
```

### File Manipulation Operations

Common file operations for textbook projects:

| Operation | Command | Example |
|-----------|---------|---------|
| Copy file | `cp source destination` | `cp chapter-template.md chapter-05.md` |
| Copy directory | `cp -r source destination` | `cp -r templates/chapter docs/chapters/05-new` |
| Move/rename | `mv source destination` | `mv old-chapter.md new-chapter.md` |
| Delete file | `rm filename` | `rm docs/chapters/draft.md` |
| Delete directory | `rm -r dirname` | `rm -r docs/chapters/deprecated` |
| Create directory | `mkdir dirname` | `mkdir docs/chapters/15-appendix` |
| Create nested directories | `mkdir -p path/to/dir` | `mkdir -p docs/sims/new-sim/assets` |

### Safe File Operations

To prevent accidental data loss, use these practices:

- **Use `-i` flag for interactive confirmation:**
  ```bash
  rm -i docs/chapters/draft.md    # Prompts "remove docs/chapters/draft.md?"
  ```

- **Use `-n` flag for no-clobber (don't overwrite):**
  ```bash
  cp -n source.md destination.md  # Only copies if destination doesn't exist
  ```

- **Preview operations before executing:**
  ```bash
  # Preview files that would be deleted
  find docs/chapters -name "draft*.md"
  # Then delete them
  find docs/chapters -name "draft*.md" -delete
  ```

- **Use version control as a safety net:**
  ```bash
  git status                      # Check for uncommitted changes
  git stash                       # Temporarily save current changes
  # Perform risky operations
  git stash pop                   # Restore changes if needed
  ```

## Shell Scripts

Shell scripts are text files containing sequences of Bash commands that automate repetitive tasks. In intelligent textbook development, shell scripts are used to install Claude skills, generate content, validate quality, and deploy to production.

### Anatomy of a Shell Script

A basic shell script has three components:

1. **Shebang line:** Specifies the interpreter (always first line)
   ```bash
   #!/bin/bash
   ```

2. **Comments:** Explain what the script does (start with `#`)
   ```bash
   # Install Claude skills to global skills directory
   ```

3. **Commands:** The actual operations to perform
   ```bash
   ln -s $(pwd)/skills/* ~/.claude/skills/
   ```

### Example: Installing Claude Skills

The `install-claude-skills.sh` script creates symbolic links from the project's skills directory to the global Claude skills directory:

```bash
#!/bin/bash

# Install Claude skills to global skills directory
# This makes skills available to all Claude projects

SKILLS_DIR="$HOME/.claude/skills"
PROJECT_SKILLS="$(pwd)/skills"

# Create skills directory if it doesn't exist
mkdir -p "$SKILLS_DIR"

# Link each skill to global directory
for skill in "$PROJECT_SKILLS"/*; do
    skill_name=$(basename "$skill")
    echo "Installing skill: $skill_name"
    ln -sf "$skill" "$SKILLS_DIR/$skill_name"
done

echo "Skills installation complete!"
```

### Script Components Explained

**Variables:**
```bash
SKILLS_DIR="$HOME/.claude/skills"      # Directory where skills are installed
PROJECT_SKILLS="$(pwd)/skills"         # Directory containing project skills
```

**Command substitution:**
```bash
skill_name=$(basename "$skill")        # Extracts filename from full path
```

**For loops:**
```bash
for skill in "$PROJECT_SKILLS"/*; do   # Iterate over each skill directory
    # Commands here execute for each skill
done
```

**Conditional creation:**
```bash
mkdir -p "$SKILLS_DIR"                 # Create directory if it doesn't exist
```

**Symbolic links:**
```bash
ln -sf "$skill" "$SKILLS_DIR/$skill_name"    # -s = symbolic, -f = force (replace if exists)
```

### Script Best Practices

Effective shell scripts follow these conventions:

- **Start with shebang:** `#!/bin/bash` on line 1
- **Use meaningful variable names:** `SKILLS_DIR` not `dir1`
- **Quote variables:** `"$variable"` prevents word splitting
- **Check for errors:** Use `set -e` to exit on any command failure
- **Add help text:** Provide usage instructions when run with `-h` or `--help`
- **Use functions:** Break complex scripts into reusable functions
- **Validate inputs:** Check that required files/directories exist

### Example: Advanced Script with Error Handling

```bash
#!/bin/bash
set -e  # Exit on any error

# Validate learning graph quality before deployment

LEARNING_GRAPH_CSV="docs/learning-graph/learning-graph.csv"
QUALITY_THRESHOLD=70

# Check that learning graph file exists
if [ ! -f "$LEARNING_GRAPH_CSV" ]; then
    echo "Error: Learning graph file not found: $LEARNING_GRAPH_CSV"
    exit 1
fi

# Run quality analysis
echo "Analyzing learning graph quality..."
python docs/learning-graph/analyze-graph.py "$LEARNING_GRAPH_CSV" quality-metrics.md

# Extract quality score from quality-metrics.md
quality_score=$(grep "Quality Score:" quality-metrics.md | awk '{print $3}' | cut -d'/' -f1)

echo "Quality score: $quality_score/100"

# Check if quality meets threshold
if [ "$quality_score" -lt "$QUALITY_THRESHOLD" ]; then
    echo "Error: Quality score ($quality_score) is below threshold ($QUALITY_THRESHOLD)"
    echo "Review quality-metrics.md for issues"
    exit 1
fi

echo "✓ Quality check passed! Ready for deployment."
```

This script demonstrates:
- Error handling with `set -e`
- File existence checks
- External command execution (Python script)
- Text parsing with `grep`, `awk`, and `cut`
- Conditional logic with `if` statements
- Meaningful exit codes (0 = success, 1 = failure)

## Script Execution Permissions

Unix-like systems (macOS, Linux) use a permission system to control who can read, write, or execute files. Before a shell script can be run, it must have execute permissions set.

### Understanding File Permissions

File permissions are displayed by `ls -l`:

```bash
$ ls -l scripts/install-claude-skills.sh
-rwxr-xr-x  1 username  staff  512 Jan 15 10:30 install-claude-skills.sh
```

The permission string `-rwxr-xr-x` breaks down as:

- **File type:** `-` (regular file), `d` (directory), `l` (symbolic link)
- **Owner permissions:** `rwx` (read, write, execute)
- **Group permissions:** `r-x` (read, execute, no write)
- **Other permissions:** `r-x` (read, execute, no write)

### Permission Notation

Permissions can be represented in two formats:

**Symbolic notation:**
```
r = read (4)
w = write (2)
x = execute (1)
```

**Numeric notation (octal):**
```
rwx = 4+2+1 = 7
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
```

Common permission combinations:

| Octal | Symbolic | Meaning |
|-------|----------|---------|
| 755 | -rwxr-xr-x | Owner can read/write/execute, others can read/execute |
| 644 | -rw-r--r-- | Owner can read/write, others can read only |
| 700 | -rwx------ | Owner can read/write/execute, others have no access |
| 775 | -rwxrwxr-x | Owner and group can read/write/execute, others can read/execute |

### Making Scripts Executable

To make a script executable, use the `chmod` command:

```bash
# Add execute permission for owner
chmod +x scripts/install-claude-skills.sh

# Add execute permission for everyone
chmod a+x scripts/install-claude-skills.sh

# Set specific permissions using numeric notation
chmod 755 scripts/install-claude-skills.sh
```

After setting execute permissions, the script can be run directly:

```bash
# Run with full path
./scripts/install-claude-skills.sh

# Run with relative path
cd scripts
./install-claude-skills.sh

# Run from anywhere if in PATH
install-claude-skills.sh
```
#### Diagram: Permission Bits Visual Infographic

<iframe src="../../sims/permission-bits-visual-infographic/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Permission Bits Visual Infographic</summary>
    Type: infographic

    Purpose: Explain Unix file permission system with visual representation of permission bits

    Layout: Grid layout with three main sections

    Section 1 - Permission String Breakdown (top):
    - Large text: `-rwxr-xr-x`
    - Each character highlighted separately:
      - `-` → "File type: Regular file"
      - `rwx` → "Owner: Read, Write, Execute"
      - `r-x` → "Group: Read, Execute only"
      - `r-x` → "Others: Read, Execute only"
    - Color coding: Owner (blue), Group (green), Others (orange)

    Section 2 - Octal Representation (middle):
    - Visual breakdown showing how rwx maps to numbers:
      ```
      r w x
      4 2 1
      ```
    - Example calculations:
      - rwx = 4+2+1 = 7
      - r-x = 4+0+1 = 5
      - r-- = 4+0+0 = 4
    - Final octal: **755**

    Section 3 - Common Permissions (bottom):
    - Cards showing common permission sets:

      Card 1: "Executable Script"
      - Octal: 755
      - Symbolic: -rwxr-xr-x
      - Use case: Shell scripts that should run
      - Icon: 📜 with ⚡

      Card 2: "Private Script"
      - Octal: 700
      - Symbolic: -rwx------
      - Use case: Scripts with sensitive data
      - Icon: 🔒

      Card 3: "Markdown File"
      - Octal: 644
      - Symbolic: -rw-r--r--
      - Use case: Documentation files
      - Icon: 📝

      Card 4: "Directory"
      - Octal: 755
      - Symbolic: drwxr-xr-x
      - Use case: Standard project directories
      - Icon: 📁

    Interactive elements:
    - Hover over permission bits to see explanation
    - Click octal number to toggle between symbolic and numeric views
    - Click "Common Permissions" cards to see full explanation and chmod command
    - Slider to build custom permissions: drag to set r/w/x for owner/group/others
      - Displays resulting chmod command in real-time

    Visual style: Modern, clean design with monospace font for permission strings
    Color scheme:
    - File type: Gray
    - Owner permissions: Blue (#3498db)
    - Group permissions: Green (#2ecc71)
    - Other permissions: Orange (#e67e22)
    - Background: White with subtle shadows for cards

    Implementation: HTML/CSS/JavaScript with interactive permission builder

---
**MicroSim Generator Recommendations:**

1. markdown table (best) - Permission notation reference doesn't require interactivity, table clearest
2. microsim-p5 (85/100) - If interactive permission calculator needed, p5.js with inputs works well
3. chartjs-generator (15/100) - Not designed for permission reference or calculators

</details>

### Security Considerations

Execute permissions should be granted carefully:

- **Only make scripts executable if they need to be run:** Don't blindly `chmod +x` all files
- **Review scripts before making them executable:** Malicious scripts can damage systems
- **Be cautious with scripts from untrusted sources:** Always inspect before running
- **Use least privilege:** Grant minimum permissions necessary (e.g., 700 for personal scripts instead of 777)

### Troubleshooting Permission Issues

Common permission-related errors:

**Error: "Permission denied"**
```bash
$ ./scripts/install-claude-skills.sh
-bash: ./scripts/install-claude-skills.sh: Permission denied
```
**Solution:** Add execute permission
```bash
chmod +x scripts/install-claude-skills.sh
```

**Error: "No such file or directory" when script exists**
```bash
$ ./scripts/install-claude-skills.sh
-bash: ./scripts/install-claude-skills.sh: No such file or directory
```
**Cause:** Incorrect shebang line (e.g., Windows line endings)
**Solution:** Convert line endings to Unix format
```bash
dos2unix scripts/install-claude-skills.sh
```

## Symlink Creation

Symbolic links (symlinks) are special files that act as pointers to other files or directories, enabling multiple paths to access the same content. In intelligent textbook development, symlinks are used to install Claude skills globally while maintaining the skills in the project repository.

### Why Use Symlinks for Skills?

Claude Code looks for skills in `~/.claude/skills/` by default. Without symlinks, you would need to:

- Copy skill files to `~/.claude/skills/` every time they're updated
- Maintain duplicate copies in each project
- Manually synchronize changes across projects

Symlinks solve this by creating a reference in `~/.claude/skills/` that points to the original skill files in the project repository. When the original files are updated, the changes are immediately reflected in all projects using that symlink.

### Creating Symlinks

The `ln` command creates symbolic links:

```bash
# Syntax
ln -s /path/to/original /path/to/link

# Example: Link a single skill
ln -s ~/Documents/textbook-project/skills/glossary-generator ~/.claude/skills/glossary-generator

# Example: Link all skills in a directory
ln -s ~/Documents/textbook-project/skills/* ~/.claude/skills/
```

**Flags:**
- `-s`: Create symbolic link (not a hard link)
- `-f`: Force overwrite if link already exists
- `-n`: Don't dereference existing symlink (useful when updating)

### Symlinks vs. Copies

Understanding the difference is crucial:

| Operation | Copy | Symlink |
|-----------|------|---------|
| Storage | Duplicates content | Only stores pointer (~1KB) |
| Updates | Manual re-copy needed | Automatic (follows original) |
| Deletion | Independent files | Deleting symlink doesn't affect original |
| Portability | Works if original is deleted | Breaks if original is moved/deleted |
| Permissions | Uses copy's permissions | Uses original's permissions |

### Verifying Symlinks

Use `ls -l` to see symlink targets:

```bash
$ ls -l ~/.claude/skills/glossary-generator
lrwxr-xr-x  1 username  staff  72 Jan 15 10:30 glossary-generator -> /Users/username/Documents/textbook-project/skills/glossary-generator
```

The `->` arrow indicates this is a symlink pointing to the target path.

### Managing Symlinks

**List all symlinks in a directory:**
```bash
find ~/.claude/skills/ -type l -ls
```

**Check if a symlink target exists:**
```bash
test -e ~/.claude/skills/glossary-generator && echo "Target exists" || echo "Broken symlink"
```

**Remove a symlink:**
```bash
rm ~/.claude/skills/glossary-generator     # Removes link only, original unaffected
```

**Update a symlink to point to a new target:**
```bash
ln -sf /new/path/to/skill ~/.claude/skills/glossary-generator
```

### Project-Local vs. Global Skills

Claude Code supports two skill installation strategies:

**Global skills (`~/.claude/skills/`):**
- Available to all projects
- Ideal for stable, mature skills used across multiple textbooks
- Installed via `scripts/install-claude-skills.sh`

**Project-local skills (`.claude/skills/`):**
- Available only to the current project
- Ideal for experimental or project-specific skills
- Installed by creating `.claude/skills/` directory in project root

The installation script can be modified to install to project-local directory by changing:

```bash
# From:
SKILLS_DIR="$HOME/.claude/skills"

# To:
SKILLS_DIR="$(pwd)/.claude/skills"
```

### Troubleshooting Symlinks

**Problem: "Skill not found" error in Claude Code**

Possible causes:
1. Symlink not created correctly
2. Target path is incorrect
3. Permissions issue on target directory

**Solution:**
```bash
# Verify symlink exists
ls -l ~/.claude/skills/

# Check target is accessible
ls -l ~/Documents/textbook-project/skills/glossary-generator

# Re-create symlink with correct path
ln -sf ~/Documents/textbook-project/skills/glossary-generator ~/.claude/skills/glossary-generator
```

**Problem: "Permission denied" when running skill**

**Solution:**
```bash
# Ensure original skill directory has correct permissions
chmod -R 755 ~/Documents/textbook-project/skills/
```
#### Diagram: Skill Installation Workflow Diagram

<iframe src="../../sims/skill-installation-workflow/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Skill Installation Workflow Diagram</summary>
    Type: diagram

    Purpose: Show the relationship between project skills directory, global skills directory, and Claude Code's skill discovery

    Components to show:
    - Project repository structure (left side):
      ```
      ~/Documents/textbook-project/
      ├── skills/
      │   ├── glossary-generator/
      │   │   ├── SKILL.md
      │   │   └── templates/
      │   ├── quiz-generator/
      │   │   └── SKILL.md
      │   └── learning-graph-generator/
      │       ├── SKILL.md
      │       └── scripts/
      └── scripts/
          └── install-claude-skills.sh
      ```

    - Global skills directory (center):
      ```
      ~/.claude/skills/
      ├── glossary-generator -> ~/Documents/textbook-project/skills/glossary-generator
      ├── quiz-generator -> ~/Documents/textbook-project/skills/quiz-generator
      └── learning-graph-generator -> ~/Documents/textbook-project/skills/learning-graph-generator
      ```

    - Claude Code (right side):
      - Search icon looking in ~/.claude/skills/
      - Successfully finding skills via symlinks
      - Loading SKILL.md files

    Connections:
    - Dashed arrows from global skills to project skills (labeled "symlink")
    - Solid arrow from install-claude-skills.sh to global skills (labeled "creates")
    - Solid arrow from Claude Code to global skills (labeled "reads from")

    Annotations:
    - Label on project skills: "Original files (version controlled)"
    - Label on global skills: "Symlinks (not version controlled)"
    - Label on symlinks: "Points to original, no duplication"
    - Callout: "When original files update, changes immediately available to Claude"

    Visual style: System architecture diagram with clear flow
    Color scheme:
    - Project files: Blue
    - Symlinks: Orange (with dotted line style)
    - Claude Code: Purple

    Implementation: SVG diagram with labeled components and directional arrows

---
**MicroSim Generator Recommendations:**

1. timeline-generator (97/100) - Project timeline showing phase progression is perfect vis-timeline use
2. mermaid-generator (85/100) - Workflow flowchart showing capstone phases with decision points
3. chartjs-generator (75/100) - Gantt-style timeline chart showing project phases and milestones

</details>

## Capstone: Complete Textbook Project

The capstone project synthesizes all skills, tools, and workflows from this course by guiding you through the complete process of creating an intelligent textbook from initial concept to published website. This comprehensive project mirrors real-world educational content development and demonstrates your ability to apply course concepts independently.

### Project Overview

You will create an intelligent textbook on a subject of your choice, following the complete workflow:

1. Develop a comprehensive course description
2. Generate a 200-concept learning graph with dependencies
3. Design chapter structure based on concept dependencies
4. Create chapter content with interactive elements
5. Generate glossary, quiz, and FAQ content
6. Build and deploy the textbook to GitHub Pages

The project typically requires 15-25 hours depending on textbook scope and prior experience. You are encouraged to choose a subject in which you have expertise, as domain knowledge significantly accelerates content creation.

### Project Requirements

Your completed textbook must include:

**Foundation (Required):**
- Course description meeting all quality criteria (score ≥ 85/100)
- Learning graph with 200 concepts, validated dependencies (DAG structure), and taxonomy categorization
- 6-12 chapters with clear concept mapping
- MkDocs configuration with proper navigation

**Content (Required):**
- At least 3 complete chapters with rich content (~3,000 words each)
- Minimum 15 non-text elements across chapters (lists, tables, diagrams, MicroSims, etc.)
- Glossary with 50+ terms following ISO 11179 standards
- One complete chapter quiz (10+ questions, multiple Bloom's levels)

**Interactive Elements (Choose at least 2):**
- At least one MicroSim demonstrating a key concept
- At least one interactive infographic or timeline
- Learning graph visualization using vis-network
- FAQ page with 20+ questions

**Deployment (Required):**
- GitHub repository with complete source files
- Deployed website on GitHub Pages
- README with project overview and build instructions

### Phase 1: Course Design (3-5 hours)

**Step 1: Course Description Development**

Use the `course-description-analyzer` skill to create your course description:

```bash
# In Claude Code, invoke the skill
/skill course-description-analyzer
```

Your course description should specify:
- Course title and target audience (reading level)
- Prerequisites and assumed knowledge
- Main topics covered (15-25 topics)
- Topics explicitly out of scope (5-10 topics)
- Learning outcomes across all six Bloom's Taxonomy levels

**Quality check:**
```bash
# Skill will generate quality score
# Target: ≥ 85/100
```

**Step 2: Learning Graph Generation**

Use the `learning-graph-generator` skill to create your concept map:

```bash
/skill learning-graph-generator
```

The skill will:
- Enumerate 200 concepts from your course description
- Map concept dependencies (directed acyclic graph)
- Categorize concepts by taxonomy
- Validate graph quality

**Quality check:**
```bash
cd docs/learning-graph
python analyze-graph.py learning-graph.csv quality-metrics.md

# Target: Quality score ≥ 70/100
# Ensure zero circular dependencies
```

**Step 3: Chapter Structure Design**

Use the `book-chapter-generator` skill to design chapters:

```bash
/skill book-chapter-generator
```

The skill creates chapter directories with:
- Chapter title and summary
- List of concepts covered in each chapter
- Prerequisites linking to earlier chapters

**Review:**
- Verify concept dependencies are respected (prerequisites taught before dependents)
- Ensure even distribution (no chapter has >40 concepts)
- Check that foundational concepts appear in early chapters

### Phase 2: Content Creation (8-15 hours)

**Step 4: Generate Chapter Content**

For each chapter, use the `chapter-content-generator` skill:

```bash
/skill chapter-content-generator
# Provide chapter name or path when prompted
```

The skill generates:
- Detailed educational content at appropriate reading level
- Diverse non-text elements (lists, tables, diagrams)
- Specifications for complex elements (MicroSims, infographics) in `<details markdown="1">` blocks

**Minimum requirement:** Complete 3 chapters with rich content

**Step 5: Create Interactive Elements**

Implement at least one MicroSim using the `microsim-p5` skill:

```bash
/skill microsim-p5
```

Choose a concept that benefits from interactive visualization, such as:
- Algorithm visualization (sorting, graph traversal)
- System behavior simulation (networking, resource allocation)
- Parameter exploration (statistical distributions, optimization)

**Step 6: Build Supporting Resources**

Generate glossary:
```bash
/skill glossary-generator
```

Generate chapter quizzes:
```bash
/skill quiz-generator
# Generate quiz for at least one chapter
```

Generate FAQ:
```bash
/skill faq-generator
```

### Phase 3: Integration and Quality Assurance (2-4 hours)

**Step 7: Configure MkDocs**

Update `mkdocs.yml` navigation to include all content:

```yaml
nav:
  - Home: index.md
  - Learning Graph:
      - Introduction: learning-graph/index.md
      - Concept List: learning-graph/list-concepts.md
      - Quality Analysis: learning-graph/quality-metrics.md
  - Chapters:
      - Chapter 1: chapters/01-chapter-name/index.md
      - Chapter 2: chapters/02-chapter-name/index.md
      # Add all chapters
  - Resources:
      - Glossary: glossary.md
      - FAQ: faq.md
  - MicroSims:
      - Simulation Name: sims/sim-name/index.md
```

**Step 8: Test Locally**

Build and serve the textbook locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally
mkdocs serve

# Open browser to http://localhost:8000
```

**Quality checks:**
- All navigation links work
- Images and MicroSims load correctly
- No broken internal links
- Consistent formatting across chapters
- Glossary terms properly defined
- Quiz questions display correctly

**Step 9: Build Validation**

Test strict build (fail on warnings):

```bash
mkdocs build --strict
```

Fix any warnings or errors reported by MkDocs.

### Phase 4: Deployment (1-2 hours)

**Step 10: GitHub Repository Setup**

Initialize Git repository (if not already done):

```bash
git init
git add .
git commit -m "Initial commit: Complete intelligent textbook project"
```

Create GitHub repository and push:

```bash
# Create repository on GitHub (github.com/new)
# Then:
git remote add origin https://github.com/username/textbook-name.git
git branch -M main
git push -u origin main
```

**Step 11: Deploy to GitHub Pages**

Configure GitHub Pages in repository settings:
- Settings → Pages → Source: Deploy from branch
- Branch: gh-pages
- Folder: / (root)

Deploy using MkDocs:

```bash
mkdocs gh-deploy
```

This command:
1. Builds the static site
2. Creates/updates `gh-pages` branch
3. Pushes to GitHub
4. Triggers GitHub Pages deployment

**Wait 2-5 minutes** for deployment to complete, then visit:
```
https://username.github.io/textbook-name/
```

**Step 12: Documentation**

Update `README.md` with:

```markdown
# [Textbook Title]

An intelligent textbook on [subject] created using Claude Skills.

## Overview

[Brief description of textbook content and target audience]

## Features

- 200-concept learning graph with dependency mapping
- [X] chapters with interactive elements
- [Y] MicroSims demonstrating key concepts
- Comprehensive glossary with [Z] terms
- Chapter quizzes aligned to Bloom's Taxonomy

## Live Site

View the textbook: https://username.github.io/textbook-name/

## Building Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally
mkdocs serve
```

## Project Structure

```
textbook-name/
├── docs/              # Textbook content
├── skills/            # Claude skills used
├── scripts/           # Utility scripts
└── mkdocs.yml         # Site configuration
```

## License

[Your chosen license]
```

### Project Evaluation Checklist

Use this checklist to verify project completeness:

**Foundation:**
- [ ] Course description with quality score ≥ 85/100
- [ ] Learning graph with 200 concepts
- [ ] Zero circular dependencies in learning graph
- [ ] Learning graph quality score ≥ 70/100
- [ ] 6-12 chapters created with concept mapping
- [ ] MkDocs configuration complete

**Content:**
- [ ] At least 3 complete chapters (~3,000 words each)
- [ ] 15+ non-text elements total across chapters
- [ ] Glossary with 50+ ISO 11179-compliant terms
- [ ] At least one complete chapter quiz (10+ questions)

**Interactive Elements:**
- [ ] At least one MicroSim implemented and functional
- [ ] At least one interactive infographic or timeline
- [ ] Learning graph visualization (optional but recommended)
- [ ] FAQ page with 20+ questions (optional)

**Deployment:**
- [ ] GitHub repository created and pushed
- [ ] Website deployed to GitHub Pages
- [ ] All links functional in deployed site
- [ ] README.md with complete documentation
- [ ] No build warnings or errors

**Quality:**
- [ ] Consistent markdown formatting across chapters
- [ ] All images and MicroSims load correctly
- [ ] No broken internal links
- [ ] Mobile-responsive design (MkDocs Material default)
- [ ] Search functionality works (MkDocs Material default)

### Next Steps and Extensions

After completing the capstone project, consider these extensions:

**Advanced Features:**
- Install learning graph viewer with interactive exploration
- Add custom CSS styling to match your branding
- Implement additional MicroSims for complex concepts
- Create video walkthroughs of key topics
- Add social media preview images

**Collaboration:**
- Invite subject matter experts to review content
- Set up GitHub Issues for feedback collection
- Create contribution guidelines for open-source collaboration
- Establish content review workflows

**Analytics and Improvement:**
- Add Google Analytics to track visitor engagement
- Monitor which pages receive most traffic
- Identify chapters with high bounce rates for improvement
- Survey learners for feedback

**Publication:**
- Share on social media and educational platforms
- Submit to open educational resources (OER) repositories
- Present at conferences or webinars
- Write blog post about development process

## Summary

This chapter equipped you with the essential development tools and workflows for creating intelligent textbooks. You learned to use Visual Studio Code as a comprehensive content authoring platform, leveraging its integrated terminal, markdown preview, and Git integration. You mastered Bash command-line operations including directory navigation, file manipulation, and shell scripting for automation.

The capstone project challenged you to synthesize all course concepts by creating a complete intelligent textbook from concept to deployment. This comprehensive exercise demonstrated the end-to-end workflow: course description development, learning graph generation, chapter structuring, content creation, interactive element integration, quality assurance, and deployment to GitHub Pages.

By completing this chapter and capstone project, you have demonstrated proficiency in:

- Configuring professional development environments for technical content creation
- Executing command-line workflows for build automation and deployment
- Writing shell scripts to automate repetitive tasks
- Managing file permissions and symbolic links for skill installation
- Integrating all course skills into a coherent textbook development workflow
- Publishing educational content to production web platforms

You are now equipped to independently create intelligent, AI-enhanced textbooks that advance educational outcomes through structured knowledge graphs, interactive simulations, and adaptive learning resources.

## References

1. [Bash Scripting Tutorial – Linux Shell Script and Command Line for Beginners](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) - 2024 - freeCodeCamp - Comprehensive tutorial covering Bash scripting fundamentals including variables, command execution, input/output handling, and debugging techniques, essential for automating intelligent textbook build and deployment workflows.

2. [Automating Tasks With Bash Scripts](https://linuxhandbook.com/bash-automation/) - 2024 - Linux Handbook - Practical guide to creating Bash automation scripts with real-world examples including user management, backup automation, and system administration tasks, demonstrating automation principles applicable to textbook development workflows and skill installation.
