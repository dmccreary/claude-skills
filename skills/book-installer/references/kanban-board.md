---
name: install-kanban-board
description: Creates a GitHub Projects Kanban board for an intelligent textbook project and adds project management documentation to the book.
---

# Install Kanban Board

## Overview

Sets up a GitHub Projects (v2) Kanban board for tracking textbook development progress, links it to the repository, populates it with standard textbook milestones, and adds a project management guide to the book's documentation.

- **Time:** ~5 minutes
- **Creates:** GitHub Project board + `docs/project-management.md`
- **Requires:** `gh` CLI authenticated with `project` scope

## Step 1: Verify Prerequisites

### 1a. Check gh authentication and project scope

```bash
gh auth status
```

If the output does **not** include `project` in the scopes list, refresh the token:

```bash
gh auth refresh -s project
```

### 1b. Identify the repository

```bash
REPO_OWNER="dmccreary"
REPO_NAME=$(basename "$(git rev-parse --show-toplevel)")
echo "Repository: $REPO_OWNER/$REPO_NAME"
```

### 1c. Gather the book title

Extract the site name from mkdocs.yml for the project title:

```bash
BOOK_TITLE=$(grep '^site_name:' mkdocs.yml | sed 's/site_name: *//')
echo "Book title: $BOOK_TITLE"
```

## Step 2: Create the GitHub Project

```bash
PROJECT_URL=$(gh project create \
  --owner "$REPO_OWNER" \
  --title "$BOOK_TITLE" \
  --format json | jq -r '.url')
echo "Project URL: $PROJECT_URL"
```

Extract the project number from the URL (needed for subsequent commands):

```bash
PROJECT_NUMBER=$(echo "$PROJECT_URL" | grep -o '[0-9]*$')
echo "Project number: $PROJECT_NUMBER"
```

## Step 3: Add a Priority Field

Add a priority field so items can be triaged:

```bash
gh project field-create "$PROJECT_NUMBER" \
  --owner "$REPO_OWNER" \
  --name "Priority" \
  --data-type "SINGLE_SELECT" \
  --single-select-options "High,Medium,Low"
```

## Step 4: Link the Project to the Repository

```bash
gh project link "$PROJECT_NUMBER" \
  --owner "$REPO_OWNER" \
  --repo "$REPO_OWNER/$REPO_NAME"
```

## Step 5: Populate with Standard Textbook Milestones

Create draft issues for the standard intelligent textbook development workflow:

```bash
# Foundation
gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Write course description" \
  --body "Create docs/course-description.md covering audience, prerequisites, learning objectives (Bloom's Taxonomy), and 10-15 topic areas."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Generate learning graph" \
  --body "Enumerate ~200 concepts, map dependencies as a DAG, assign taxonomy categories, and validate with analyze-graph.py."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Design chapter structure" \
  --body "Use book-chapter-generator to create chapter outlines from the learning graph. Ensure concept prerequisites are respected."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Generate glossary" \
  --body "Create ISO 11179-compliant glossary from learning graph concepts. Definitions must be precise, concise, distinct, and non-circular."

# Content creation
gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Write chapter content" \
  --body "Generate detailed chapter content with worked examples, practice exercises, and admonitions using chapter-content-generator."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Create MicroSims" \
  --body "Build interactive p5.js simulations for key concepts. Each MicroSim gets its own directory under docs/sims/ with main.html, style.css, script.js, and index.md."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Generate quizzes" \
  --body "Create multiple-choice quizzes for each chapter aligned to Bloom's Taxonomy levels using quiz-generator."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Generate FAQs" \
  --body "Create frequently asked questions from course content using faq-generator."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Generate references" \
  --body "Create curated reference lists (10 per chapter) prioritizing Wikipedia for reliability using reference-generator."

# Polish and deploy
gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Create cover image and home page" \
  --body "Generate cover image using AI and configure home page with social media metadata (og:image, Twitter Cards)."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Add learning graph viewer" \
  --body "Install interactive vis-network graph viewer for concept exploration."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Run book metrics" \
  --body "Generate metrics report: chapter count, concept coverage, glossary completeness, quiz distribution, MicroSim count, word counts."

gh project item-create "$PROJECT_NUMBER" --owner "$REPO_OWNER" \
  --title "Deploy to GitHub Pages" \
  --body "Run mkdocs gh-deploy. Verify site renders correctly, all links work, and MicroSims load properly."
```

## Step 6: Inform the User

Display the project board URL:

```
Your Kanban board is ready!

View it at: $PROJECT_URL

Or open it in the browser:
  gh project view $PROJECT_NUMBER --owner $REPO_OWNER --web

The board has been linked to the $REPO_OWNER/$REPO_NAME repository.
13 standard milestones have been added as draft items.

To manage your board:
  - Drag items between columns (Todo → In Progress → Done)
  - Convert draft items to full issues with: gh project item-edit
  - Add new items with: gh project item-create $PROJECT_NUMBER --owner $REPO_OWNER --title "..."
```

## Step 7: Add Project Management Page to the Book

Create `docs/project-management.md` with the following content:

```markdown
# Project Management

## Kanban Board

This project uses a [GitHub Projects Kanban board]($PROJECT_URL)
to track development progress.

### How to Access

1. Visit the [project board]($PROJECT_URL)
2. Or from the repository page, click the **Projects** tab

### Kanban Columns

GitHub Projects uses a board view with three default columns:

| Column | Purpose | When to Move Here |
|--------|---------|-------------------|
| **Todo** | Work that has been identified but not started | New tasks and milestones start here |
| **In Progress** | Work that is actively being developed | Move here when you begin working on a task |
| **Done** | Completed work that has been verified | Move here after the work is committed, reviewed, and deployed |

### Priority Levels

Each item can be assigned a priority:

- **High** - Blocks other work or is needed for the next milestone
- **Medium** - Important but not blocking
- **Low** - Nice to have, can be deferred

### Textbook Development Workflow

The standard intelligent textbook development follows this sequence:

1. **Course description** - Define audience, prerequisites, and learning objectives
2. **Learning graph** - Enumerate concepts and map dependencies
3. **Chapter structure** - Design chapters respecting concept prerequisites
4. **Glossary** - Define all key terms (ISO 11179 standards)
5. **Chapter content** - Write detailed content with examples and exercises
6. **MicroSims** - Build interactive simulations for key concepts
7. **Quizzes** - Create assessments aligned to Bloom's Taxonomy
8. **FAQs** - Anticipate and answer common questions
9. **References** - Curate reliable sources for each chapter
10. **Cover image and home page** - Design visual identity and social metadata
11. **Learning graph viewer** - Add interactive concept explorer
12. **Metrics and QA** - Validate completeness and quality
13. **Deploy** - Publish to GitHub Pages

### Adding New Tasks

From the command line:

```bash
gh project item-create PROJECT_NUMBER --owner dmccreary \
  --title "Task title" \
  --body "Task description"
```

Or use the **+ Add item** button at the bottom of any column in the board view.

### Converting Drafts to Issues

Draft items on the board can be converted to full GitHub issues,
which enables assignment, labels, and cross-referencing in pull requests.
Click the draft item title, then select **Convert to issue** and
choose the repository.
```

**Important:** Replace `$PROJECT_URL` and `PROJECT_NUMBER` with the actual values from Step 2.

## Step 8: Update mkdocs.yml Navigation

Add the project management page to the `nav:` section:

```yaml
nav:
  # ... existing entries ...
  - Project Management: project-management.md
```

Place it near the end of the navigation, before any "About" or "Contact" entries.

## Step 9: Update README.md

Add a Kanban board section to the repository's README.md:

```markdown
## Project Board

Track development progress on the
[Kanban board]($PROJECT_URL).

| Column | Purpose |
|--------|---------|
| **Todo** | Identified work not yet started |
| **In Progress** | Work currently underway |
| **Done** | Completed and verified |
```

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `insufficient scope` error | Token missing `project` scope | Run `gh auth refresh -s project` |
| `Could not resolve to a ProjectV2` | Wrong project number | Run `gh project list --owner dmccreary` to find the correct number |
| Board not visible on repo | Project not linked | Run `gh project link NUMBER --owner dmccreary --repo OWNER/REPO` |
| Items stuck in one column | Board view not configured | Open the board in browser and switch to "Board" layout |

## Fallback: Manual Setup

If `gh project` commands are unavailable or fail, create the board manually:

1. Go to [github.com/dmccreary?tab=projects](https://github.com/dmccreary?tab=projects)
2. Click **New project**
3. Select the **Board** template (Kanban layout)
4. Name it after the book title
5. Click **Create project**
6. In project settings, click **Manage access** → **Link a repository** → select the book repo
7. Add items manually using **+ Add item** at the bottom of the **Todo** column
8. Add a "Priority" single-select field (High / Medium / Low) via the **+** button on the field headers

Then create `docs/project-management.md` manually using the template in Step 7 above.
