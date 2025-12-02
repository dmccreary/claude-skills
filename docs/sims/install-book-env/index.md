---
title: Install Book Environment Dependencies
description: An interactive dependency graph visualization showing all software components required to set up an intelligent textbook development environment using MkDocs Material and Claude Skills.
quality_score: 90
---

# Install Book Environment Dependencies

This MicroSim visualizes the dependency graph for setting up an intelligent textbook development environment. It shows all the software components required to build a book using MkDocs Material and Claude Skills.

<iframe src="main.html" width="100%" height="400px"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

Copy this iframe to embed in your website:

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/install-book-env/main.html" width="100%" height="400px"></iframe>
```

## Reading the Graph

- **Arrows point in the direction of dependency** - if A has an arrow to B labeled "DEPENDS_ON", then A depends on B
- **Navigate from right to left** to see what needs to be installed first
- **Hover over nodes** to see descriptions of each component

## Dependency Layers

The graph is organized into layers from left (foundational) to right (goal):

| Layer | Components | Description |
|-------|-----------|-------------|
| **Foundation** | Permissions | User permissions to install software |
| **System** | Unix Shell, File System | Basic OS capabilities |
| **Runtime** | Python 3.10+, Node.js, Git | Language runtimes and tools |
| **Package Manager** | pip, npm | Package installation tools |
| **Python Packages** | MkDocs, Material, PyMdown | Documentation framework |
| **Claude Tools** | Claude Code, GitHub Repo, Claude Skills | AI-assisted development |
| **Goal** | Build Book | The final output |

## Installation Order

To set up the environment, install components in this order:

1. Ensure you have proper **permissions** on your system
2. Open a **Unix shell** (Terminal on macOS/Linux, WSL on Windows)
3. Install **Python 3.10+**, **Node.js**, and **Git**
4. Use **pip** to install MkDocs packages:
   ```bash
   pip install mkdocs mkdocs-material pymdown-extensions
   ```
5. Use **npm** to install Claude Code:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
6. Clone the **GitHub repository** with Claude Skills
7. Configure **Claude Skills** in your project
8. **Build the book** using `mkdocs build` or `mkdocs serve`

## Lesson Plan

**Target Audience:** Developers, technical writers, and educators new to intelligent textbook development

**Learning Objectives:**

- Understand the software dependencies required for building intelligent textbooks
- Recognize the layered architecture of development environments
- Identify the installation order for setting up the environment

**Prerequisites:**

- Basic familiarity with command-line interfaces
- Understanding of package managers (pip, npm)

**Activities:**

1. **Exploration (5 min):** Interact with the dependency graph, hovering over nodes to understand each component's role
2. **Trace Dependencies (5 min):** Starting from "Build Book," trace backwards to identify all required components
3. **Hands-On Setup (20 min):** Follow the installation order to set up the environment on your machine
4. **Discussion (5 min):** Why do certain components depend on others? What happens if a dependency is missing?

**Assessment:**

- Can the student explain why Python must be installed before pip?
- Can the student successfully run `mkdocs serve` after completing the installation?

## References

1. [MkDocs Documentation](https://www.mkdocs.org/) - Official documentation for the MkDocs static site generator
2. [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Documentation for the Material theme with advanced features
3. [Claude Code Documentation](https://docs.anthropic.com/claude-code) - Official guide for Claude Code CLI tool

## Developer Notes

**Operating system dependencies not shown:** This diagram does not include all dependencies for every operating system. For example, on macOS, Claude Code is typically installed via Homebrew, which requires Xcode Command Line Tools to be installed first. This additional installation step can take approximately 15 minutes.

**vis-network edge label bug:** vis-network has a rendering bug with edge labels on perfectly horizontal edges (where both nodes share the same y-coordinate). The label may not appear on initial load but becomes visible after any node interaction. The workaround is to apply a slight y-offset between connected nodes to give the edge enough angle for the label to render correctly on initial load.
