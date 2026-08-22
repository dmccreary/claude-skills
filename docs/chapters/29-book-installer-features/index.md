---
title: Book Installer Features
description: Covers the book-installer meta-skill's scaffolding and feature-installation routing, auto-detection, installable extras, strict build mode, and the auto-commit hook.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 19:05:00
version: 0.09
---

# Book Installer Features

## Summary

This chapter covers the book-installer meta-skill's feature system: scaffolding a new textbook, routing a feature-installation request, and auto-detecting which features are already installed against a checklist. It includes several installable extras -- the home page template, GitHub Projects Kanban board, strict build mode, auto-commit hook, and custom 404 page. Students will be able to install a new feature into an existing textbook project after this chapter.

## Concepts Covered

This chapter covers the following 13 concepts from the learning graph:

1. Home Page Template
2. GitHub Projects Kanban
3. Strict Build Mode
4. Auto-Commit Hook
5. Deployment Verification
6. Project Instruction Files
7. Custom 404 Page
8. Book Installer Skill
9. Textbook Scaffold
10. Feature Installation Routing
11. Feature Auto-Detection
12. Feature Checklist
13. detect_features.py Script

## Prerequisites

This chapter builds on concepts from:

- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)
- [5. MkDocs Site Features, Deployment, and Analytics](../05-mkdocs-deployment-analytics/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [9. Measuring and Optimizing Token Usage](../09-measuring-optimizing-tokens/index.md)
- [10. Building and Testing Portable Skills](../10-building-testing-portable-skills/index.md)
- [12. Writing a Course Description](../12-writing-course-description/index.md)
- [25. Text-to-Image Models and the Verified Infographic Pipeline](../25-verified-infographic-pipeline/index.md)

---

!!! mascot-welcome "The skill that built the ground you're standing on."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    This entire book started as an empty folder. This chapter is the meta-skill that turned it into a working project, and everything you can bolt onto it afterward. Right tool, right task!

## The Book Installer Meta-Skill

The **Book Installer Skill** is the meta-skill that scaffolds a new book and installs individual site features on request — a meta-skill in exactly Chapter 7's sense, routing between many possible jobs instead of doing one fixed task. Its very first job on any new project is producing a **textbook scaffold**: the initial project structure created for a new book, including configuration, directory layout, and starter pages — the `mkdocs.yml`, `docs/` folder, and starter `index.md` that every other skill in this library then builds on top of.

## Routing a Feature Request

Once a book exists, adding a capability to it is **feature installation routing**: matching a request for a site capability to the specific guide describing how to install it — "add a Kanban board" or "add Google Analytics" each route to a different installation guide inside the same meta-skill, the same routing-table pattern from Chapter 7 applied to site features instead of MicroSim libraries.

#### Diagram: Install Book Environment Dependencies

<iframe src="../../sims/install-book-env/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>Install Book Environment Dependencies (reused MicroSim)</summary>
Type: graph-model
**sim-id:** install-book-env<br/>
**Library:** vis-network<br/>
**Status:** Reused<br/>
**Source:** docs/sims/install-book-env

Reused from this book's own MicroSim catalog. Learning objective: Analyze the dependency graph of software components a textbook scaffold requires, from MkDocs to the skill library itself.
</details>

## Knowing What's Already There

Before installing anything, it helps to know what's already present. **Feature auto-detection** examines a project to determine which capabilities are already installed, so a report reflects reality rather than assumption, performed by **detect_features.py**: the program that inspects a project and reports which site capabilities are installed. The result is a **feature checklist**: a generated document listing available site capabilities and marking which are present in a given book.

!!! mascot-thinking "Detecting reality beats trusting memory."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    It would be easy to just remember which features you've already installed — until a project has been worked on across a dozen sessions and that memory gets unreliable. Auto-detection reads the actual files on disk every time, so the checklist is never wrong about what's really there.

## A Few Installable Features

Among the roughly 40 features this skill can install, a few show up in nearly every book. The **home page template** is the starting page presenting a book's cover, summary, and entry points into its material — the first thing a reader sees. **GitHub Projects Kanban** is a board tracking outstanding work in columns representing stages of progress, useful for coordinating a book's remaining chapters or open issues. A **custom 404 page** replaces the default missing-page message with one offering navigation back into the book, rather than a dead end.

## Keeping a Site Honest: Strict Build Mode and Deployment Verification

Two features protect a book from silently shipping a broken site. **Strict build mode** is a build setting that treats warnings such as broken links as failures, preventing a defective site from being published — this book's own `mkdocs build --strict` runs exactly this check before any chapter regeneration gets treated as finished. **Deployment verification** confirms that a published site renders correctly and that its links and assets resolve after release, catching anything strict mode's local check couldn't see until the site was actually live.

!!! mascot-warning "A clean local build doesn't guarantee a clean deployment."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    `mkdocs build --strict` catches broken internal links, but it can't catch everything that might go wrong once a site is actually hosted — a missing environment variable, a misconfigured base path. Always follow a deployment with a quick manual check of the live site, not just a clean local build.

## Automating the Commit: Auto-Commit Hook and Project Instruction Files

The last feature closes a loop you've been watching all book long. An **auto-commit hook** is a configured callback that records a turn's file changes automatically using a message left for it, so work is never left uncommitted — exactly the mechanism that has been quietly committing every chapter in this book as it was generated, using a marker message written for it each time. That hook, and every other standing convention in this project, lives in **project instruction files**: documents carrying persistent guidance for agents working in a repository, sometimes duplicated under a second filename for platform compatibility — the same `CLAUDE.md` from Chapter 5, and its `AGENTS.md` counterpart from Chapter 10, working together.

!!! mascot-tip "The marker file is the whole trick."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    An auto-commit hook only works if there's a message ready for it when the turn ends. Writing that marker message is a small, deliberate habit — skip it, and the hook has nothing to commit with, no matter how much work actually happened.

## Key Takeaways

- The **Book Installer Skill** produces a **textbook scaffold** for a new book and performs **feature installation routing** for everything added afterward.
- **Feature auto-detection**, via **detect_features.py**, produces an accurate **feature checklist** instead of relying on memory.
- A **home page template**, a **GitHub Projects Kanban** board, and a **custom 404 page** are common installable extras.
- **Strict build mode** catches broken links locally; **deployment verification** checks the site after it's actually live.
- An **auto-commit hook**, configured through **project instruction files**, keeps work from ever being left uncommitted.

!!! mascot-celebration "You now understand the skill that scaffolded this very book."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Scaffold, features, detection, strict builds, auto-commit — that's the entire infrastructure layer underneath every chapter you've read. Right tool, right task!
