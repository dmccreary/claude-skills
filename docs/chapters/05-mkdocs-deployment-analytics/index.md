---
title: MkDocs Site Features, Deployment, and Analytics
description: Expands the MkDocs Material feature set, walks through commit-push-branch and GitHub Pages deployment, and covers Google Analytics and Claude's layered project memory.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 13:05:00
version: 0.09
---

# MkDocs Site Features, Deployment, and Analytics

## Summary

This chapter expands the MkDocs Material feature set -- search, syntax highlighting, image zoom, comments, and page feedback -- and walks through the Git commit, push, and branch workflow. It finishes with deploying a site to GitHub Pages and registering it with Google Analytics 4. Students will be able to configure a MkDocs site and publish it live after completing this chapter.

## Concepts Covered

This chapter covers the following 16 concepts from the learning graph:

1. Code Syntax Highlighting
2. Image Zoom Lightbox
3. Comment System
4. Page Feedback Widget
5. About Page
6. Local Development Server
7. Git Commit
8. Git Branching
9. GitHub Pages Deployment
10. Git Push
11. Never Use Master Branch
12. gh-deploy Command
13. Google Analytics GA4
14. IDE Agent Integration
15. Measurement ID
16. CLAUDE.md Project Memory

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)

---

!!! mascot-welcome "Let's put the site live."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 4 got your files tracked and your site building locally. This chapter finishes the job: richer site features, the rest of the Git workflow, and getting your book onto the open web where readers can actually find it. Right tool, right task!

## More MkDocs Material Features

Beyond navigation and search, the MkDocs Material theme offers several reader-facing features worth turning on deliberately. **Code syntax highlighting** colors code samples by language structure so they're easier to read, usually with a copy control attached. An **image zoom lightbox** enlarges a picture in an overlay when a reader selects it, useful for detailed diagrams that are hard to read at thumbnail size. A **comment system** is an embedded discussion feature letting readers leave remarks directly on a page, while a **page feedback widget** is a simpler control asking whether a page was helpful, collecting signal about which material needs revision without requiring a full comment thread. Every book also needs an **about page**: a page describing the book's purpose, its author, and how to cite it.

Before you enable any of these, you'll want to see your changes without waiting for a full deployment. A **local development server** is a process that serves your site on the authoring machine and refreshes it as files change, letting you preview instantly.

| Feature | Concept | Reader Benefit |
|---------|---------|-----------------|
| Copy-button code blocks | Code Syntax Highlighting | Easier to read and reuse commands |
| Click-to-enlarge images | Image Zoom Lightbox | Detailed diagrams stay legible |
| Discussion threads | Comment System | Readers can ask questions in place |
| "Was this helpful?" | Page Feedback Widget | Signals which pages need revision |
| Purpose and citation info | About Page | Establishes what the book is and who made it |
| Instant local preview | Local Development Server | See changes before publishing |

## Committing, Pushing, and Branching

Chapter 4 covered staging a change with `git add` and checking it with `git status`. Recording that staged change permanently is a **Git commit**: the instruction that records marked changes as a permanent snapshot with an explanatory message. A commit only exists on your machine until you run **Git push**: the instruction that sends locally recorded snapshots to the shared hosted copy on GitHub.

```bash
git commit -m "Add Chapter 5: deployment and analytics"
git push
```

Notice the message after `-m` in that first command — it's not optional decoration, it's the explanation a future reader (often you, months later) will rely on to understand why the change happened. **Git branching** is maintaining parallel lines of development so work in progress doesn't disturb the published state — you can experiment on a branch, and the site your readers see stays untouched until you merge that work back in.

## Deploying to GitHub Pages

**GitHub Pages deployment** is publishing a built site through a hosting service attached to its repository — GitHub builds your `docs/` folder into a live website at a public URL. Doing that by hand would mean running the site build command, then manually pushing the built output to a special hosting branch. The **gh-deploy command** collapses that into one step: the instruction that builds a site and publishes it to its hosting branch in one step.

#### Diagram: MkDocs GitHub Pages Deployment Workflow

<iframe src="../../sims/mkdocs-github-pages-deployment/main.html" width="100%" height="460px" scrolling="no"></iframe>

<details markdown="1">
<summary>MkDocs GitHub Pages Deployment Workflow (reused MicroSim)</summary>
Type: workflow
**sim-id:** mkdocs-github-pages-deployment<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/mkdocs-github-pages-deployment

Reused from this book's own MicroSim catalog. Learning objective: Summarize the steps the `gh-deploy` command runs through, from a local build to a live GitHub Pages URL.
</details>

!!! mascot-tip "One command, one deployment."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    `mkdocs gh-deploy` is genuinely just one command — but it publishes immediately, with no draft or review step of its own. Run `mkdocs build --strict` first and read its warnings; that's your last checkpoint before the site goes live.

Deployment only works cleanly when your default branch follows this project's **Never Use Master Branch** convention: the principal line of development is always named `main`, including in the `edit_uri` configuration that generates each page's "edit this page" link. A repository still named `master` will generate broken edit links even after a successful deploy.

## Measuring Readers with Google Analytics

Once a book is live, **Google Analytics GA4** is a measurement service that records how readers reach and move through a published site — which chapters get read, which links get clicked, where readers drop off. Connecting your site to that service is just one value: the **Measurement ID**, the identifier connecting a site to its analytics property, placed once in the site configuration.

!!! mascot-warning "Aggregate traffic, not individual readers."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Remember the "2.99" design target from Chapter 2? GA4's page-view and click data is exactly the aggregate, non-identifying signal that fits it — you can see that Chapter 14 gets read three times as often as Chapter 28, without ever knowing which specific reader did the reading. Keep it that way; don't wire analytics into anything that ties events to a named individual.

## AI Agents Inside Your Editor: IDE Integration and Project Memory

**IDE agent integration** is running an AI coding agent inside an editor so file context, terminal, and generated changes all share one workspace — instead of copying code back and forth between a chat window and your editor. That agent reads standing instructions from **CLAUDE.md project memory**: a project file holding standing instructions an agent reads at the start of every session, encoding conventions specific to that repository, like this project's `main`-not-`master` rule you just met above.

!!! mascot-thinking "Memory has layers, and layers have priority."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A project's `CLAUDE.md` isn't the only memory an agent reads — there's also a global, user-level file that applies across every project on your machine. When the two disagree, the more specific one — the project's own `CLAUDE.md` — wins. Once you see memory as layered rather than singular, "why did the agent do that" gets a lot easier to answer.

#### Diagram: Claude Code Memory Layers

<iframe src="../../sims/claude-code-memory-layers/main.html" width="100%" height="500px" scrolling="no"></iframe>

<details markdown="1">
<summary>Claude Code Memory Layers (reused MicroSim)</summary>
Type: infographic
**sim-id:** claude-code-memory-layers<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/claude-code-memory-layers

Reused from this book's own MicroSim catalog. Learning objective: Analyze how Claude Code's memory layers load and how a higher-priority layer, such as a project's `CLAUDE.md`, overrides a lower-priority one.
</details>

## Key Takeaways

- Material theme features like **syntax highlighting**, **image zoom**, a **comment system**, and a **page feedback widget** make a published book easier to read and easier to improve; preview all of them locally with the **local development server**.
- **Git commit** records a snapshot with a message; **Git push** sends it to GitHub; **Git branching** keeps in-progress work from disturbing the published site.
- **GitHub Pages deployment** via the one-step **gh-deploy command** publishes your site — but only cleanly if you followed the **Never Use Master Branch** convention.
- **Google Analytics GA4**, connected through a **Measurement ID**, measures aggregate reader traffic without identifying individuals.
- **IDE agent integration** lets an agent act directly in your editor, guided by layered **CLAUDE.md project memory**.

!!! mascot-celebration "Your book is live on the open web."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Commit, push, deploy, measure — that's the full publishing loop, and you now own every step of it. Right tool, right task!
