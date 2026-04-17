---
name: book-installer
description: Installs and configures project infrastructure including MkDocs Material intelligent textbook templates, learning graph viewers, and skill tracking systems. Routes to the appropriate installation guide based on what the user needs to set up.
---

# Book Installer

## Overview

This meta-skill handles installation and setup tasks for intelligent textbook projects. It consolidates three installation skills into a single entry point with on-demand loading of specific installation guides.

## When to Use This Skill

Use this skill when users request:

- Setting up a new MkDocs Material project
- Creating a new intelligent textbook from scratch
- Installing a learning graph viewer
- Setting up skill usage tracking with hooks
- Bootstrapping project infrastructure

## Step 1: Handle Help Requests

If the user asks for "help", "what can you do", or "list features", display this numbered list directly (do not load a reference file):

```
Book Installer Features (most → least common):

 1. Simple mkdocs.yml template - Minimal starter config for new projects
 2. Site logo - Add custom logo to header
 3. Favicon - Browser tab/bookmark icon
 4. Cover image & social preview - Home page image + og:image metadata
 4b. Generate cover image - Auto-generate cover using AI (API or ChatGPT)
 5. Math equations - KaTeX (recommended) or MathJax
 6. Code syntax highlighting - Language-aware code blocks
 7. Code copy button - One-click copy for code blocks
 8. Mermaid diagrams - Flowcharts, sequence diagrams from text
 9. Content tabs - Tabbed sections for alternatives
10. Image zoom (GLightbox) - Click to enlarge images
11. Custom admonitions - Prompt boxes with copy button
12. Interactive quizzes - Self-assessment questions
13. Abbreviations & tooltips - Glossary hover definitions
14. Task lists - Checkbox lists
15. Simple feedback - Thumbs up/down per page
16. Detailed comments (Giscus) - GitHub Discussions integration
17. Tags & categorization - Page tagging system
18. Search enhancements - Suggestions and highlighting
19. Table of contents config - TOC sidebar options
20. Blog support - Add blog section
21. Announcement bar - Dismissible top banner
22. Privacy & cookie consent - GDPR compliance
23. Learning graph viewer - Interactive concept visualization
24. Skill usage tracker - Claude Code analytics hooks
25. Google Analytics - requires a Google Analytics property ID G-*
26. .gitignore installer - make sure that `site` and `.cache` are not in the main branch
27. extra CSS installer for iframe and customer prompt admonition
28. extra JavaScript installer - for prompt admonition copy button
29. Feature checklist - auto-detect and document which features are implemented
30. Learning mascot - add a pedagogical agent character to guide students
31. Instructor's guide - comprehensive teacher's guide with classroom tips
32. Custom 404 page - friendly error page with mascot image
33. Document status indicators - colored dots in nav showing page lifecycle state
34. Kanban board - GitHub Projects board for tracking textbook development
35. Mascot chapter updater - retrofit existing chapters with mascot admonitions

Type a number or feature name to install.

Note: If you see `navigation.tabs` in mkdocs.yml, remove it. These books
use side navigation optimized for wide landscape screens.
```

After displaying the list, wait for user to specify which feature they want.

---

## Step 1b: Check for Navigation Tabs (Existing Projects)

When working with an existing mkdocs.yml, always check for and remove navigation tabs:

```yaml
# REMOVE these lines if present in mkdocs.yml:
theme:
  features:
    - navigation.tabs        # DELETE
    - navigation.tabs.sticky # DELETE
```

These books use side navigation optimized for wide landscape screens. Top navigation tabs waste vertical space and are not appropriate for this format.

---

## Step 2: Identify Installation Type

Match the user's request to the appropriate installation guide:

### Routing Table

| Trigger Keywords | Action | Purpose |
|------------------|--------|---------|
| help, what can you do, features, capabilities, list features | Display numbered list (Step 1) | Show quick feature overview |
| 1, simple mkdocs, minimal template, starter config | `references/mkdocs-template.md` (minimal section) | Create simple mkdocs.yml starter |
| enrich, add feature, number 2-24, specific feature name | `references/mkdocs-features.md` | Install specific feature |
| new project, mkdocs, textbook, bootstrap, setup, template, new book | `references/mkdocs-template.md` | Create new MkDocs Material project |
| graph viewer, learning graph, visualization, interactive graph, concept viewer | `references/learning-graph-viewer.md` | Add learning graph viewer to existing project |
| track skills, skill usage, activity tracking, hooks, usage analytics | `references/skill-tracker.md` | Set up skill tracking with hooks |
| generate cover, generate cover image, auto cover, create cover image, run cover script | `references/cover-image-generator.md` | Auto-generate cover image using AI (guides through API/ChatGPT options) |
| cover image, home page, social media, og:image, montage, book cover, index page | `references/home-page-template.md` | Create home page with cover image and social metadata |
| logo, site logo, branding, upper left, header icon | `references/mkdocs-features.md` | Add custom logo with AI prompt examples |
| favicon, browser tab, bookmark icon, .ico | `references/mkdocs-features.md` | Add favicon with AI prompt examples |
| math, equations, latex, mathjax, katex | `references/mkdocs-features.md` | Add math equation support |
| feature checklist, generate feature checklist, feature status, what features | `references/feature-checklist-generator.md` | Auto-detect and document implemented features |
| quiz, quizzes, assessment, multiple choice | `references/mkdocs-features.md` | Add interactive quizzes |
| feedback, thumbs up, thumbs down, was this helpful | `references/mkdocs-features.md` | Add page feedback widget |
| comments, giscus, discussions | `references/mkdocs-features.md` | Add comment system |
| image zoom, lightbox, glightbox, click to enlarge | `references/mkdocs-features.md` | Add image zoom on click |
| code highlighting, syntax, copy button | `references/mkdocs-features.md` | Add code syntax highlighting |
| mermaid, diagrams, flowchart | `references/mkdocs-features.md` | Add Mermaid diagram support |
| admonition, callout, prompt box, copy prompt | `references/mkdocs-features.md` | Add custom admonitions with copy |
| mascot, learning mascot, pedagogical agent, character, guide character, persona | `references/learning-mascot.md` | Add a learning mascot to guide students |
| instructor guide, teacher guide, teachers guide, instructor's guide, classroom guide | `references/instructors-guide.md` | Generate comprehensive instructor's guide |
| 404, error page, not found, custom 404, page not found | `references/custom-404-page.md` | Add custom 404 page with mascot |
| document status, page status, status indicators, status dots, nav status, page lifecycle, review workflow | `references/document-status.md` | Add colored status dots to nav sidebar |
| kanban, project board, kanban board, project management, github project, task board, milestones, 34 | `references/kanban-board.md` | Create GitHub Projects Kanban board for textbook development |
| mascot chapter, update chapter, retrofit mascot, place mascot, add mascot to chapter, mascot placement, 35 | `references/mascot-chapter-updater.md` | Retrofit an existing chapter with mascot admonitions using placement rules |

### Decision Tree

```
Asking for help or what book-installer can do?
  → YES: Display numbered list directly (Step 1)

Creating a new project/textbook from scratch?
  → YES: mkdocs-template.md

Adding a learning graph viewer to existing project?
  → YES: learning-graph-viewer.md

Setting up skill usage tracking?
  → YES: skill-tracker.md

Want to GENERATE a cover image automatically using AI?
  → YES: cover-image-generator.md (guides through API vs ChatGPT options)

Creating a cover image MANUALLY or setting up home page with social metadata?
  → YES: home-page-template.md

Want to generate a feature checklist showing what's implemented?
  → YES: feature-checklist-generator.md

Want to add branding (logo, favicon, cover image)?
  → YES: mkdocs-features.md (Branding Features section)

Want to add a learning mascot (pedagogical agent) to guide students?
  → YES: learning-mascot.md

Want to generate an instructor's/teacher's guide?
  → YES: instructors-guide.md

Want a custom 404 error page with the mascot?
  → YES: custom-404-page.md

Want to add colored status dots to the nav sidebar for page lifecycle tracking?
  → YES: document-status.md

Want a GitHub Projects Kanban board to track textbook development?
  → YES: kanban-board.md

Want to retrofit an existing chapter with mascot admonitions?
  → YES: mascot-chapter-updater.md

Want to add a specific feature (equations, quizzes, feedback, etc.)?
  → YES: mkdocs-features.md (then follow specific feature instructions)
```

## Step 2: Load the Matched Guide

Read the corresponding guide file from `references/` and follow its installation workflow.

## Step 3: Execute Installation

Each guide contains:
1. Prerequisites and requirements
2. Step-by-step installation commands
3. Configuration options
4. Verification steps
5. Troubleshooting tips

## Available Installation Guides

### mkdocs-features.md

**Purpose:** Detailed configuration for all MkDocs feature enhancements

**Contains:** Full configuration snippets for features 2-24 listed in the help output, including:
- YAML for mkdocs.yml
- JavaScript files to create
- CSS files to create
- Usage examples

**Use when:**
- User selects a feature by number or name
- User wants detailed configuration for a specific feature
- User has a minimal mkdocs.yml and wants to enrich it

### mkdocs-template.md

**Purpose:** Bootstrap a complete MkDocs Material intelligent textbook project

**Creates:**
- Conda virtual environment named 'mkdocs'
- Full MkDocs Material project structure
- Custom CSS for branding
- Social media card plugins
- GitHub Pages deployment configuration
- URI scheme in `extra` section for global discoverability

**URI Scheme:**
New projects automatically include the textbook schema in mkdocs.yml:
```yaml
extra:
  schema: https://dmccreary.github.io/intelligent-textbooks/ns/textbook/v1
```
See the [URI Scheme documentation](https://dmccreary.github.io/intelligent-textbooks/uri-scheme/) for details.

**Prerequisites:**
- Conda installed
- Git installed
- GitHub repository created

### learning-graph-viewer.md

**Purpose:** Add interactive learning graph exploration to existing textbook

**Creates:**
- Interactive vis-network graph viewer
- Search, filtering, and statistics features
- Integration with existing learning-graph.json

**Prerequisites:**
- Existing MkDocs project
- learning-graph.json file present

### skill-tracker.md

**Purpose:** Set up Claude Code skill usage tracking

**Creates:**
- Hook scripts for tracking skill invocations
- Activity log directory structure
- Reporting scripts for usage analysis

**Prerequisites:**
- Claude Code installed
- ~/.claude directory exists

### home-page-template.md

**Purpose:** Create professional home page with cover image and social media optimization

**Creates:**
- docs/index.md with proper frontmatter metadata
- AI image generation prompts for cover with montage background
- Open Graph and Twitter Card configuration

**Features:**
- Cover image design guidance (1.91:1 aspect ratio)
- Montage element suggestions by topic
- Social media preview optimization
- Example prompts for various book themes

**Prerequisites:**
- Existing MkDocs project
- Access to AI image generator (DALL-E, Midjourney, etc.)

### learning-mascot.md

**Purpose:** Design and implement a pedagogical agent (learning mascot) that guides students through the textbook

**Creates:**
- Character design (name, species, appearance, personality, catchphrase)
- AI image generation prompts for consistent mascot poses
- Implementation via inline images, custom CSS admonitions, or JavaScript auto-detection
- CLAUDE.md character guidelines for consistent AI-generated content

**Features:**
- Subject-specific mascot suggestions with reasoning
- Six standard pose variants (welcome, thinking, tip, warning, celebration, encouraging)
- Three implementation methods at different complexity levels
- Restraint guidelines to prevent overuse

**Prerequisites:**
- Existing MkDocs Material project
- Access to AI image generator (DALL-E, Midjourney, etc.)

### instructors-guide.md

**Purpose:** Generate a comprehensive instructor's/teacher's guide for the textbook

**Creates:**
- `docs/teachers-guide/index.md` (or `docs/instructors-guide/index.md` for college-level)
- Navigation entry in mkdocs.yml

**Features:**
- Five levels of intelligent textbooks explained
- Detailed usage instructions for chapters, MicroSims, glossary, FAQ, quizzes, and references
- Classroom tips (before/during/after class suggestions, pacing)
- MicroSim iframe embedding guide for external LMS pages
- Creative Commons license explained in plain English (what you can/cannot do)
- Step-by-step customization guide (fork, clone, change colors/title/logo, deploy)
- Google Analytics setup instructions
- xAPI/LRS overview with FERPA/COPPA/GDPR regulatory warnings
- Learning graph usage tips for teachers
- Pedagogical agent (mascot) documentation (if mascot exists)
- All technical terms defined before use — no assumed prior knowledge

**Prerequisites:**
- Existing MkDocs Material project
- At least some chapter content written

### custom-404-page.md

**Purpose:** Add a custom 404 error page featuring the project's learning mascot

**Creates:**
- `overrides/404.html` — Jinja2 template extending Material base theme with mascot image, friendly message, and home link
- mkdocs.yml updates for `custom_dir` and `static_templates`

**Features:**
- Uses the mascot's warning pose (or other pose) centered on the page
- Inherits full site navigation (header, sidebar, footer) from the Material theme
- Customizable message matched to the mascot's personality and voice
- Absolute image paths so the 404 works from any URL depth

**Prerequisites:**
- Existing MkDocs Material project
- Learning mascot images in `docs/img/mascot/` (use `learning-mascot.md` first if needed)

### document-status.md

**Purpose:** Add per-page colored status dots to the navigation sidebar for tracking page lifecycle state

**Creates:**
- `extra.status` configuration in mkdocs.yml
- CSS rules for colored status dots in extra.css
- `status:` frontmatter on individual pages

**Features:**
- Three-state workflow (spec-complete → prototype → ready-for-testing)
- Colored dots (red, orange, green) visible in the nav sidebar
- Tooltip text on hover
- Customizable status codes for any workflow

**Prerequisites:**
- Existing MkDocs Material project
- Custom CSS file referenced in `extra_css`

### cover-image-generator.md

**Purpose:** Auto-generate cover images using the generate-cover.sh script

**Provides:**
- Interactive questionnaire to determine best workflow
- Commands for API, ChatGPT Pro, or manual generation
- Troubleshooting for common issues

**Workflows:**
- **Full Auto**: OpenAI API with active billing (fastest)
- **Browser Auto**: ChatGPT Pro + macOS (opens browser, pastes prompt)
- **Local Prompt**: ChatGPT Pro, any OS (displays prompt for manual copy)
- **Fallback**: Free tier options with manual generation

**Prerequisites:**
- Existing MkDocs project with mkdocs.yml
- docs/course-description.md with book content description
- One of: OpenAI API billing, ChatGPT Pro subscription, or free AI image generator

### kanban-board.md

**Purpose:** Create a GitHub Projects (v2) Kanban board for tracking textbook development progress

**Creates:**
- GitHub Projects board with Board (Kanban) layout
- Priority field (High / Medium / Low)
- 13 standard textbook milestone draft items
- `docs/project-management.md` with column documentation and workflow guide
- README section about the Kanban board

**Features:**
- Automated setup via `gh project` CLI commands
- Links project to the repository automatically
- Pre-populated milestones matching the 12-step textbook workflow
- Fallback instructions for manual setup if `gh` commands fail

**Prerequisites:**
- `gh` CLI installed and authenticated
- `project` scope on the GitHub token (`gh auth refresh -s project`)
- Existing MkDocs project with mkdocs.yml

### mascot-chapter-updater.md

**Purpose:** Retrofit an existing chapter markdown file with mascot admonitions in the right places, following the placement rules from learning-mascot.md

**Creates:**
- In-place edits to the specified chapter file only (no new files)
- A placement plan shown to the user for confirmation before editing

**Features:**
- LLM-driven workflow for semantic placement (no regex auto-insertion)
- Enforces hard limits: ≤6 admonitions per chapter, one welcome and one celebration maximum, no back-to-back placements
- Image-path guidance for directory-URL rendering (counts `../` from rendered page)
- Voice and body-text rules: 1-3 sentences, in-character, specific to chapter content
- Validation via `scripts/validate-chapter-mascots.py` that flags count limits, back-to-backs, missing `<img>` tags, and body-text length

**Prerequisites:**
- Mascot images present in `docs/img/mascot/` or `docs/img/mascots/`
- `docs/css/mascot.css` loaded and the mascot-test page renders correctly
- Specific chapter file identified by absolute path

## Examples

### Example 1: Ask for Help
**User:** "book-installer help"
**Routing:** Keyword "help" → Display numbered list
**Action:** Show the numbered feature list (Step 1), then wait for user to select a feature

### Example 2: Add a Specific Feature
**User:** "Add math equation support to my book"
**Routing:** Keyword "math" → `references/mkdocs-features.md`
**Action:** Load mkdocs-features.md, find the Math Equations section, and apply the configuration

### Example 2b: Select by Number
**User:** "5"
**Routing:** Number selection after help list → `references/mkdocs-features.md`
**Action:** Load mkdocs-features.md, find Math Equations (item 5), and apply the configuration

### Example 2c: Simple Template
**User:** "1"
**Routing:** Number 1 → `references/mkdocs-template.md` (minimal section)
**Action:** Load mkdocs-template.md and create a simple mkdocs.yml starter config

### Example 3: New Textbook Project
**User:** "I want to create a new intelligent textbook about machine learning"
**Routing:** Keywords "create", "new", "textbook" → `references/mkdocs-template.md`
**Action:** Read mkdocs-template.md and follow its workflow

### Example 4: Add Graph Viewer
**User:** "Add an interactive viewer for the learning graph"
**Routing:** Keywords "viewer", "learning graph", "interactive" → `references/learning-graph-viewer.md`
**Action:** Read learning-graph-viewer.md and follow its workflow

### Example 5: Track Skill Usage
**User:** "I want to track which skills I use most often"
**Routing:** Keywords "track", "skills", "usage" → `references/skill-tracker.md`
**Action:** Read skill-tracker.md and follow its workflow

### Example 6: Create Cover Image
**User:** "Help me create a cover image for my textbook"
**Routing:** Keywords "cover image", "textbook" → `references/home-page-template.md`
**Action:** Read home-page-template.md and follow its workflow

### Example 7: Set Up Home Page with Social Sharing
**User:** "I need to add og:image metadata to my home page"
**Routing:** Keywords "og:image", "home page" → `references/home-page-template.md`
**Action:** Read home-page-template.md and follow its workflow

### Example 8: Generate Cover Image Automatically
**User:** "generate cover image" or "book-installer generate cover image"
**Routing:** Keywords "generate cover image" → `references/cover-image-generator.md`
**Action:** Read cover-image-generator.md, ask user about their resources (API key, ChatGPT Pro, macOS), then run the appropriate generate-cover.sh command

### Example 9: Add a Learning Mascot
**User:** "I want to add a mascot character to my math textbook"
**Routing:** Keywords "mascot", "character" → `references/learning-mascot.md`
**Action:** Read learning-mascot.md, guide user through character design, generate AI image prompts, and implement chosen method (inline, CSS admonitions, or JS detection)

### Example 10: Generate Feature Checklist
**User:** "generate a feature checklist" or "what features do I have"
**Routing:** Keywords "feature checklist" → `references/feature-checklist-generator.md`
**Action:** Read feature-checklist-generator.md, run the detection script, generate docs/feature-checklist.md with detected statuses

### Example 11: Generate Instructor's Guide
**User:** "add a teacher's guide" or "create instructor guide"
**Routing:** Keywords "teacher guide", "instructor guide" → `references/instructors-guide.md`
**Action:** Read instructors-guide.md, gather project variables from mkdocs.yml/course-description.md/CLAUDE.md, generate the guide with all variables substituted, add to navigation

### Example 12: Create Kanban Board
**User:** "set up a kanban board for my textbook" or "create a project board"
**Routing:** Keywords "kanban", "project board" → `references/kanban-board.md`
**Action:** Read kanban-board.md, verify gh auth with project scope, create the GitHub Project, link to repo, populate milestones, create docs/project-management.md, update nav and README

### Example 13: Add Mascots to an Existing Chapter
**User:** "add Sparky admonitions to chapter 2" or "place the mascot in docs/chapters/02-ohms-law/index.md"
**Routing:** Keywords "mascot chapter", "place mascot", "add mascot to chapter" → `references/mascot-chapter-updater.md`
**Action:** Read mascot-chapter-updater.md, survey the chapter, propose a placement plan with line numbers, wait for user confirmation, apply edits, run validate-chapter-mascots.py, and address any flags

## Common Workflows

### Full Project Setup
For a complete new project, users typically run these installations in order:
1. `mkdocs-template.md` - Create the project structure
2. `cover-image-generator.md` - Auto-generate cover image using AI
3. `home-page-template.md` - Configure home page with cover image metadata
4. `learning-graph-viewer.md` - Add graph visualization (after learning graph exists)
5. `skill-tracker.md` - Enable usage analytics (optional)

### Verification Commands

After any installation, verify with:
```bash
# For MkDocs projects
mkdocs serve
# Visit http://127.0.0.1:8000/[project-name]/

# For skill tracker
cat ~/.claude/activity-logs/skill-usage.jsonl | tail -5
```
