---
title: "Development Tools: Editor, Terminal, and Git Basics"
description: Sets up Visual Studio Code, the integrated terminal, Git version control fundamentals, and the first MkDocs site configuration.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 12:55:00
version: 0.09
---

# Development Tools: Editor, Terminal, and Git Basics

## Summary

This chapter sets up the core development environment: Visual Studio Code and its integrated terminal, Git repository structure, and the first commands (add, status) used to track changes. It also introduces MkDocs and the initial `mkdocs.yml` configuration that will host the book's content. Students will be able to navigate a project in VS Code and check the status of a Git repository after this chapter.

## Concepts Covered

This chapter covers the following 16 concepts from the learning graph:

1. Git
2. Visual Studio Code
3. VS Code Terminal
4. MkDocs
5. Git Add Command
6. Git Status
7. Git Repository Structure
8. MkDocs Material Theme
9. mkdocs.yml Configuration
10. Blank Line Before Lists
11. MkDocs Plugins
12. Site Build Command
13. Version Control Basics
14. GitHub Integration
15. Navigation Structure
16. Search Configuration

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)

---

!!! mascot-welcome "Let's set up the workshop."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every builder needs a workbench. This chapter sets up yours: the editor, the terminal inside it, and the two systems — Git and MkDocs — that turn your files into a tracked history and a published website. Right tool, right task!

## Your Editor: Visual Studio Code

**Visual Studio Code** is a source code editor with an integrated terminal, extension support, and file navigation, commonly used for authoring textbook content. Everything in this book — chapters, skills, scripts — lives as plain text files, and VS Code is where you'll read, edit, and organize them. Its **VS Code terminal** is a command-line shell embedded directly in the editor window, letting you run commands without leaving the authoring environment or switching to a separate application.

#### Diagram: VS Code Interface Layout for Textbook Development

<iframe src="../../sims/vs-code-interface-layout-for-textbook-development/main.html" width="100%" height="500px" scrolling="no"></iframe>

<details markdown="1">
<summary>VS Code Interface Layout for Textbook Development (reused MicroSim)</summary>
Type: infographic
**sim-id:** vs-code-interface-layout-for-textbook-development<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/vs-code-interface-layout-for-textbook-development

Reused from this book's own MicroSim catalog. Learning objective: Identify the Explorer, Editor, Terminal, Outline, and Preview panes in a typical VS Code layout for textbook authoring.
</details>

Once you know where the terminal pane lives, a small set of commands covers most of what you'll type into it while building this book:

#### Diagram: Command-Line Interface Basics

<iframe src="../../sims/command-line-interface-basics-interactive-infographic/main.html" width="100%" height="780px" scrolling="no"></iframe>

<details markdown="1">
<summary>Command-Line Interface Basics (reused MicroSim)</summary>
Type: infographic
**sim-id:** command-line-interface-basics-interactive-infographic<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/command-line-interface-basics-interactive-infographic

Reused from this book's own MicroSim catalog. Learning objective: Recognize the six terminal commands (`ls`, `cd`, `pwd`, `mkdir`, `cat`, `python`) used most often while developing this book.
</details>

## Version Control with Git

**Git** is a distributed version control system that records snapshots of a project over time and allows changes to be reviewed, reverted, and merged. That capability — reviewing and reverting — is what **version control basics** actually means as a practice: recording successive states of a project so any prior state can be recovered and any change can be attributed to whoever made it.

!!! mascot-thinking "A repository is a time machine, not just a backup."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A backup keeps one extra copy. Git keeps *every* recorded snapshot, with a full history of who changed what and when. Once you internalize that, "I'll just experiment and see what happens" stops being scary — you can always step back to any earlier snapshot.

A project tracked by Git has a specific **Git repository structure**: the layout of a project including the working files you edit, the history database that records every snapshot, and the ignore rules that exclude generated artifacts (like a `site/` build folder) from ever being tracked. Recording a snapshot is a two-step process. The **Git add command** marks changed files for inclusion in the next recorded snapshot — it doesn't record anything yet, it just says "include this." **Git status** reports which files have changed and which are already marked for the next snapshot, so you can check your work before committing to it.

```bash
git status                    # see what changed
git add docs/chapters/index.md   # mark one file for the next snapshot
git status                    # confirm it's now staged
```

Before typing that last command in the example, notice what it's for: running `git status` a second time isn't redundant — it's how you confirm the `add` actually staged the file you meant to stage, before you commit anything.

#### Diagram: Git Branching and Merging

<iframe src="../../sims/git-branching-and-merging-visualization-microsim/main.html" width="100%" height="620px" scrolling="no"></iframe>

<details markdown="1">
<summary>Git Branching and Merging (reused MicroSim)</summary>
Type: microsim
**sim-id:** git-branching-and-merging-visualization-microsim<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/git-branching-and-merging-visualization-microsim

Reused from this book's own MicroSim catalog. Learning objective: Apply branch creation and merge operations to see how a Git repository's history diverges and reconverges.
</details>

## Connecting to GitHub

**GitHub integration** is connecting a local repository to a hosted service that stores the shared copy and provides issues, reviews, and site hosting. Your local Git history and GitHub's copy stay in sync only when you explicitly push and pull — nothing syncs automatically in the background.

!!! mascot-warning "Never rename your default branch to 'master.'"
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    This project's convention — and a growing industry standard — is `main`, not `master`, for the default branch, including inside `mkdocs.yml`'s `edit_uri`. It's a small detail, but consistency here avoids broken edit links and confused collaborators later.

## Building Your Site with MkDocs

**MkDocs** is a static site generator that builds a navigable website from a directory of markdown files and a configuration file. This book's own site — the one you're reading right now — is exactly that: markdown files in `docs/`, rendered by MkDocs into the pages you see. Most MkDocs sites, including this one, use the **MkDocs Material theme**: a widely used presentation layer for MkDocs providing search, navigation, admonitions, code highlighting, and responsive layout — everything from the mascot admonitions in this chapter to the search box at the top of the page comes from this theme.

Everything about how a site looks and behaves is declared once, in the **mkdocs.yml configuration**: the file that declares a site's title, theme, plugins, extensions, and navigation tree. You can extend what the theme can do with **MkDocs plugins**: optional packages that add capabilities to a site generator, such as search enhancements or image handling. Once your markdown and configuration are ready, the **site build command** renders markdown sources into a complete static website you can preview locally or deploy.

#### Diagram: MkDocs Build Process Workflow

<iframe src="../../sims/mkdocs-build-process/main.html" width="100%" height="460px" scrolling="no"></iframe>

<details markdown="1">
<summary>MkDocs Build Process Workflow (reused MicroSim)</summary>
Type: workflow
**sim-id:** mkdocs-build-process<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/mkdocs-build-process

Reused from this book's own MicroSim catalog. Learning objective: Summarize the stages MkDocs runs through to turn markdown source files into a static website.
</details>

## Navigation and Search

Two more `mkdocs.yml` settings shape how a reader actually finds content. **Navigation structure** is the ordered hierarchy of pages presented to readers as a site's menu, declared explicitly in `mkdocs.yml` rather than inferred automatically from the filesystem — that's why adding a new chapter file isn't enough by itself; it also has to be added to the `nav:` list before it appears in the sidebar. **Search configuration** controls how a site indexes its content and presents matches to a reader, powering the search box every Material-theme site includes by default.

| Setting | Concept | What It Controls |
|---------|---------|-------------------|
| `theme.name` | MkDocs Material Theme | Overall look, admonitions, code highlighting |
| `nav:` | Navigation Structure | The sidebar menu, in the order you declare it |
| `plugins:` | MkDocs Plugins | Added capabilities like search or image handling |
| `plugins: - search` | Search Configuration | How content is indexed and matched |

## One More Formatting Rule: Blank Lines Before Lists

One markdown detail catches nearly every new contributor at least once. The **blank line before lists** rule requires an empty line between a paragraph and a following list so the list renders correctly — skip it, and MkDocs may render the list items as part of the preceding paragraph instead of as a list at all.

!!! mascot-tip "When in doubt, add the blank line."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    This paragraph you're reading has a blank line before it and one before the list two lines down — that's not an accident, it's the rule in action. If a list ever renders as squished-together text instead of bullets, check for a missing blank line first.

## Key Takeaways

- **Visual Studio Code** and its embedded **VS Code terminal** are where you'll read, edit, and run commands for this entire book.
- **Git** tracks every snapshot of your project; **Git add** stages a change, **Git status** confirms what's staged, and the whole practice is **version control basics** in action.
- **GitHub integration** connects your local history to a shared, hosted copy — always on the `main` branch, never `master`.
- **MkDocs** with the **Material theme**, configured through **mkdocs.yml**, **plugins**, **navigation structure**, and **search configuration**, turns your markdown into the site a reader browses.
- Always leave a **blank line before a list** — it's a small rule that prevents a surprisingly common rendering bug.

!!! mascot-celebration "Your workshop is fully set up."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Editor, terminal, version control, and a site generator — that's the full toolchain every later chapter assumes you have running. Right tool, right task!
