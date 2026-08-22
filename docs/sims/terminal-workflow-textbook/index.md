---
title: Terminal Workflow for Textbook Development
description: Interactive Mermaid visualization showing terminal workflow for textbook development
image: /sims/terminal-workflow-textbook/terminal-workflow-textbook.png
og:image: /sims/terminal-workflow-textbook/terminal-workflow-textbook.png
quality_score: 80
---
# Terminal Workflow for Textbook Development

<iframe src="main.html" width="100%" height="1750px" scrolling="no"></iframe>
[Run Terminal Workflow for Textbook Development in Fullscreen](main.html){ .md-button .md-button--primary }

**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/ibook-skills/sims/terminal-workflow-textbook/main.html" width="100%" height="1750px"></iframe>
```




This workflow demonstrates the complete terminal command sequence for developing, validating, and deploying intelligent textbook content using MkDocs and Git.

## Interactive Diagram

## Development Workflow

This workflow demonstrates the complete terminal command sequence for developing, validating, and deploying intelligent textbook content using MkDocs and Git.

### Terminal Setup

**Terminal 1 (Development Server):** Runs `mkdocs serve` continuously on localhost:8000

**Terminal 2 (Scripts):** Execute Python scripts for analysis and validation

**Terminal 3 (Git):** Version control operations and deployment

### Key Commands

1. **Start Development Server** - `mkdocs serve` - Auto-reload on file changes
2. **Validate Learning Graph** - `python docs/learning-graph/analyze-graph.py`
3. **Stage and Commit** - `git add . && git commit -m "Update chapter content"`
4. **Push Changes** - `git push origin main`
5. **Deploy to GitHub Pages** - `mkdocs gh-deploy`

### Quality Checks

Always run validation scripts before committing to ensure:

- Learning graph is a valid DAG (no circular dependencies)
- All concept references are valid
- Taxonomy distribution is balanced
- Markdown syntax is correct