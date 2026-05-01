---
name: init-textbook
description: Scaffolds a new intelligent textbook project from scratch — creates mkdocs.yml, the docs/ directory tree, contact.md, license.md (CC BY-NC-SA 4.0), license.png badge, and starter index/about/course-description pages. Use this skill at the very start of a new textbook project, before any chapters, learning graph, or MicroSims exist. Trigger on phrases like "init textbook", "initialize textbook", "new textbook project", "scaffold a textbook", "set up a new book", or when the user is in an empty directory and asks to start building an intelligent textbook. After scaffolding, route the user to the book-installer skill to layer on optional features (math, mascot, slide viewer, learning graph viewer, etc.).
---

# init-textbook

## Purpose

This skill drops a complete, sensible default scaffold into an empty (or
nearly empty) project directory so the user can run `mkdocs serve` and see a
working intelligent textbook within minutes. The scaffold matches the
consensus pattern across our recent textbooks (cybersecurity, networking,
information-systems, ancient-history, statistics-course, token-efficiency,
quantum-computing, world-history, intelligent-textbooks, book-mascots) so the
project starts from the same baseline as everything else in the workspace.

The scaffold is intentionally **minimal-but-complete**: it ships only the
features that every recent textbook ends up using anyway (search, code copy,
admonitions, math via arithmatex, side navigation, CC BY-NC-SA license, the
intelligent-textbook URI scheme). Everything else — mascots, slide viewer,
learning graph viewer, custom 404, social cards, glightbox image zoom, Google
Analytics, comments, kanban, etc. — is left commented out or absent so the
user can layer it on incrementally via the **book-installer** skill once they
actually need it.

This separation of concerns matters: `init-textbook` is run **once** at
project birth; `book-installer` is run **many times** thereafter to add
features. Trying to ship every feature in the initial scaffold turned out to
make new books slow to start and littered with config the user didn't
understand. The 38-feature list under book-installer is the menu, not the
default order.

## When to Use

Trigger this skill when the user says any of:

- "init textbook" / "initialize textbook" / "init-textbook"
- "create a new textbook"
- "scaffold a new book"
- "start a new intelligent textbook"
- "set up a new mkdocs textbook project"
- "I'm in an empty directory and want to start a book about X"

Do **not** trigger when:

- The directory already has a `mkdocs.yml` and `docs/` — that's a job for
  `book-installer` (to add features) or for individual generator skills.
- The user is asking how to *use* an existing textbook — that's a docs
  question, not a scaffolding job.

## What This Skill Creates

Relative to the project root the user is in:

```
<project-root>/
├── mkdocs.yml                     # rendered from assets/templates/mkdocs.yml
└── docs/
    ├── index.md                   # home page
    ├── about.md                   # audience + how to read
    ├── course-description.md      # seed for learning-graph-generator
    ├── contact.md                 # LinkedIn contact info
    ├── license.md                 # CC BY-NC-SA 4.0 deed
    ├── chapters/
    │   └── index.md               # "list of chapters" landing page
    ├── learning-graph/
    │   └── index.md               # learning-graph section landing page
    ├── sims/
    │   └── index.md               # MicroSim catalog landing page
    ├── css/
    │   └── extra.css              # cover-image + iframe styles
    ├── js/                        # empty — populated by book-installer features
    └── img/
        └── license.png            # CC BY-NC-SA 4.0 badge image
```

All template files use `{{PLACEHOLDER}}` markers that the skill substitutes
with values gathered from the user.

## Inputs the Skill Must Gather

Before writing any files, ask the user for the following. Provide sensible
defaults where possible and let the user accept them with a single yes.

| Variable | Default | Notes |
|----------|---------|-------|
| `SITE_NAME` | (none — must ask) | The book's title in title case (e.g. "Quantum Computing") |
| `SITE_DESCRIPTION` | (none — must ask) | One-sentence description for SEO + social sharing |
| `SITE_AUTHOR` | "Dan McCreary" | Inferred from the `git config user.name` if available |
| `GITHUB_USERNAME` | "dmccreary" | Inferred from `git remote get-url origin` if available |
| `REPO_NAME` | basename of current directory | Inferred from `pwd` |
| `LINKEDIN_URL` | "https://www.linkedin.com/in/danmccreary/" | Author's LinkedIn — optional override |
| `PRIMARY_COLOR` | "indigo" | Material palette primary — common picks: indigo, blue, green, brown, deep orange |
| `ACCENT_COLOR` | "orange" | Material palette accent |
| `YEAR` | current year (2026) | For the copyright line |

If the user is in a hurry and says "use defaults", accept the inferred values
and proceed. Always confirm the substituted values back to the user in a
single block before writing files, so they can spot a wrong repo name or a
typo'd title.

## Workflow

### Step 1 — Verify the directory is fit for scaffolding

Run `ls -la` in the project root. The skill should refuse to overwrite when
any of these already exist:

- `mkdocs.yml`
- `docs/index.md`
- `docs/license.md`

If any are present, stop and tell the user — they likely want
`book-installer` instead. Do not silently merge or overwrite; the user's
existing content is the authoritative source.

### Step 2 — Gather inputs

Infer what you can:

```bash
git config user.name                 # → SITE_AUTHOR fallback
git remote get-url origin 2>/dev/null # → parse for GITHUB_USERNAME and REPO_NAME
basename "$(pwd)"                    # → REPO_NAME fallback
date +%Y                             # → YEAR
```

Then ask the user once, in a single grouped prompt, for the remaining values
(`SITE_NAME`, `SITE_DESCRIPTION`, palette preferences) and to confirm the
inferred values. Do not pepper them with one-question-at-a-time prompts.

### Step 3 — Confirm the substitution table

Before writing anything, echo the resolved values back so the user can
correct them in one shot. Example:

```
About to scaffold:
  SITE_NAME         = Quantum Computing for Skeptics
  SITE_DESCRIPTION  = An interactive intelligent textbook examining...
  SITE_AUTHOR       = Dan McCreary
  GITHUB_USERNAME   = dmccreary
  REPO_NAME         = quantum-computing
  PRIMARY_COLOR     = indigo
  ACCENT_COLOR      = orange
  YEAR              = 2026

Site URL will be: https://dmccreary.github.io/quantum-computing/
Proceed? (yes/no)
```

### Step 4 — Create directories and copy templates

Create the directory tree shown above with `mkdir -p`. Then copy each file
from `assets/templates/` into the project, performing placeholder
substitution on the text files.

For text files, do a simple in-place substitution of every `{{VAR}}` token
(e.g. `{{SITE_NAME}}`, `{{SITE_DESCRIPTION}}`, etc.) with the value gathered
in Step 2. Use a small inline `sed` or Python step — do not require any
external dependencies.

For `docs/img/license.png`, copy the binary as-is (no substitution).

### Step 5 — Verify the result builds

After scaffolding, suggest the user run:

```bash
pip install mkdocs mkdocs-material
mkdocs build --strict
```

`--strict` will catch broken nav links right away. The scaffold is designed
to pass `--strict` with no chapter content yet, because every nav entry that
points at a not-yet-generated file is left commented out.

Do **not** run `mkdocs serve` yourself — per project CLAUDE.md, the user runs
their own `mkdocs serve` in their terminal and watches it for rebuilds.

### Step 6 — Print the next-steps menu

End by pointing the user at `book-installer` for everything else. Show this
exact list (it mirrors the book-installer feature checklist) so the user
knows what is **not** in the scaffold and how to add each thing later:

```
Scaffold complete. Next steps via the book-installer skill:

  Branding & content polish
    2.  Site logo                       (book-installer 2)
    3.  Favicon                         (book-installer 3)
    4.  Cover image & social preview    (book-installer 4)
    5.  Math equations (KaTeX/MathJax)  (book-installer 5)
    8.  Mermaid diagrams                (book-installer 8)
   10.  Image zoom (GLightbox)          (book-installer 10)
   11.  Custom prompt admonitions       (book-installer 11)

  Educational features
   12.  Interactive quizzes             (book-installer 12)
   23.  Learning graph viewer           (book-installer 23)
   30.  Learning mascot                 (book-installer 30)
   31.  Instructor's guide              (book-installer 31)
   33.  Document status indicators      (book-installer 33)
   37.  Slide generator                 (book-installer 37)

  Engagement & analytics
   15.  Simple feedback (thumbs)        (book-installer 15)
   16.  Detailed comments (Giscus)      (book-installer 16)
   25.  Google Analytics                (book-installer 25)

  Project hygiene
   24.  Skill usage tracker             (book-installer 24)
   26.  .gitignore installer            (book-installer 26)
   29.  Feature checklist (auto-detect) (book-installer 29)
   34.  Kanban project board            (book-installer 34)
   36.  About page (richer)             (book-installer 36)
   38.  Reading level analysis          (book-installer 38)

Then, when the course-description.md is filled in:
   - course-description-analyzer  (validate completeness)
   - learning-graph-generator     (build 200-concept DAG)
   - book-chapter-generator       (design chapter structure)
   - chapter-content-generator    (fill chapters)
   - microsim-generator           (interactive sims)
   - glossary-generator, faq-generator, quiz-generator
```

The numbers match the book-installer feature checklist (see
`skills/book-installer/SKILL.md` Step 1) so the user can paste the number
straight into book-installer.

## Why these defaults and not others

Every choice here is the consensus across the 10 most recent textbooks in the
workspace. The reasoning is worth understanding so the skill can be extended
sensibly:

- **No `navigation.tabs`.** The project CLAUDE.md is explicit: these books
  use side navigation optimized for wide landscape screens. Top tabs waste
  vertical space.
- **`pymdownx.arithmatex` is enabled but no MathJax/KaTeX JS yet.** Every
  recent book ends up needing equations. The extension itself is cheap to
  enable; the renderer is a one-line book-installer add. Generating math
  output without a renderer simply renders LaTeX as code, which is harmless.
- **`exclude_docs:` is populated up front.** Without it, every book ends up
  with `image-prompt*.md` and `TODO.md` files leaking into the search index
  and sitemap. The exclude block is small and cheap.
- **`extra.schema:` URI is always present.** This is how books are
  discovered as intelligent textbooks across GitHub; cost is one line, value
  is real.
- **`generator: false` is on by default.** Every recent book sets this;
  no point omitting it from the scaffold.
- **`watch:` lists `docs` and `mkdocs.yml`.** This makes `mkdocs serve`
  reload on config edits, which is what the user expects.
- **No `social` plugin in the default.** It needs `pip install
  "mkdocs-material[imaging]"` plus a system-level Cairo install on macOS.
  Failing on first build is a worse experience than a comment that says how
  to enable it.
- **No mascot logo path baked in.** Several recent books point `theme.logo`
  at `img/mascot/neutral.png` — but only after the mascot exists. Pointing
  at a missing file breaks the build. The scaffold leaves `theme.logo`
  commented out and the `learning-mascot` book-installer feature wires it
  up later.
- **Light palette only at first.** Auto light/dark with custom colors (as
  in cybersecurity, networking, information-systems) requires a non-trivial
  CSS file. The scaffold uses a single Material palette pair (indigo/orange
  by default, easily swapped) and lets the user opt into dark mode later
  via book-installer if they want it.

## MicroSim Status Indicators

Every scaffolded book ships with a colored status indicator wired into the
left nav for `docs/sims/<sim>/index.md` pages. The vocabulary is fixed at
three values and the indicator is glanceable at a distance:

| Status     | Color  | Meaning                                            |
|------------|--------|----------------------------------------------------|
| `scaffold` | red    | Spec exists; no implementation yet.                |
| `built`    | orange | Implementation exists; not yet reviewed by author. |
| `approved` | green  | Author tested it and approved it for learners.     |

How to use the vocabulary:

- **`scaffold`** — every MicroSim `index.md` should be born with
  `status: scaffold` in its frontmatter. The `microsim-generator` skill (and
  any sim-scaffolding skill that follows this convention) sets this when
  it first writes the file.
- **`built`** — once a generator writes a real implementation (substantive
  HTML/JS in the sim directory, not just a placeholder), it should bump the
  status to `built`. The book author still needs to sign off.
- **`approved`** — the human author flips this manually after they've
  loaded the sim, exercised the controls, and confirmed the learning value.
  Generators should never auto-advance to `approved`.

The plumbing is already in place after `init-textbook` runs:

- `mkdocs.yml` has `extra.status` declaring the three names with tooltip
  text (Material won't render the indicator unless the name is registered
  here).
- `docs/css/extra.css` defines `--md-status--scaffold`, `--md-status--built`,
  and `--md-status--approved` as CSS custom properties holding inline SVG
  data URIs, plus the `:after` rules that paint them red/orange/green.

**Do not add `theme.icon.status` to `mkdocs.yml`.** The Material docs make
this look like the right knob for setting status icons; on the community
edition it is silently ignored and the indicator falls back to a generic
"i in a circle" icon with no build-time warning. The CSS-variable approach
in `extra.css` is what actually works on community Material and is the
load-bearing piece. (This footgun cost an afternoon to track down on the
xapi-course book — see `xapi-course/logs/microsim-status-icons.md` for the
full incident report.)

If a future book wants a fourth status (e.g. `in-review`) or different
colors, the pattern is: add an `extra.status.<name>` entry to `mkdocs.yml`,
and add a matching `--md-status--<name>` CSS variable + `.md-status--<name>:after`
rule + `.md-status--<name>:hover:after` rule to `extra.css`. Keep the two
files in sync — adding only one half is the failure mode.

## Footgun Avoidance

- **Never overwrite an existing `mkdocs.yml`.** The Step 1 check is
  load-bearing: the silent-overwrite footgun (delete user's careful nav
  list, replace with template) is exactly the kind of damage that's hard to
  undo if it makes it into a commit.
- **Confirm substitutions in one block before writing.** A typo in
  `REPO_NAME` ripples into the site URL, edit URI, and copyright link.
  Showing the resolved table and waiting for "yes" makes the error visible
  before files exist.
- **Do not enable plugins that need extra pip installs by default.**
  Default-enabled `social` plugin would fail-on-first-build for any user
  without Cairo installed. Users hate "fresh project doesn't build."

## Files in this skill

```
init-textbook/
├── SKILL.md                                   # this file
└── assets/
    └── templates/
        ├── mkdocs.yml                         # the main config template
        └── docs/
            ├── index.md
            ├── about.md
            ├── course-description.md
            ├── contact.md
            ├── license.md
            ├── chapters/
            │   └── index.md
            ├── learning-graph/
            │   └── index.md
            ├── sims/
            │   └── index.md
            ├── css/
            │   └── extra.css
            └── img/
                └── license.png                # CC BY-NC-SA 4.0 badge
```

## Examples

### Example 1: Fresh start, defaults

**User:** "init textbook"

**Skill response:**
1. `ls -la` shows directory is empty (or just has `.git/`).
2. Read `git config user.name`, `git remote get-url origin`, `basename "$(pwd)"`.
3. Ask the user for `SITE_NAME` and `SITE_DESCRIPTION`; offer to default the rest.
4. Echo the resolved table; wait for confirmation.
5. Create directories, copy + substitute templates, copy `license.png`.
6. Suggest `mkdocs build --strict`.
7. Print the next-steps menu pointing at `book-installer`.

### Example 2: Directory already has content

**User:** "scaffold a new textbook"

**Skill response:** notices `mkdocs.yml` is present, refuses to overwrite,
suggests the user either invoke `book-installer` to add features to the
existing project, or run `init-textbook` from a fresh directory.

### Example 3: User wants a specific palette

**User:** "init-textbook for a biology book, primary=green accent=amber"

**Skill response:** uses `green` / `amber` for the palette in mkdocs.yml,
proceeds with the rest of the defaults inferred from git, asks only for
`SITE_NAME` and `SITE_DESCRIPTION`.
