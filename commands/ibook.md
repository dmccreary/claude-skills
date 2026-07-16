---
description: Show the ordered runbook of skills for building a complete intelligent textbook from a course description
---

# /ibook — Intelligent Textbook Build Runbook

Present the ordered sequence of skills required to build a complete intelligent
textbook from a course description. This is a **passive runbook**: it tells the
user which skill to run next and why, but it does **not** auto-run any skill.
The user invokes each skill manually so they stay in control of every quality
gate.

## What this command does

1. **Detect current state** — check which pipeline artifacts already exist in
   the project (read-only) to determine how far along the book is.
2. **Show "you are here"** — mark completed phases, the current phase, and the
   remaining phases.
3. **Recommend the next skill** — name the single next skill to invoke, its
   prerequisites, and the quality gate that must pass before moving on.
4. **List the full ordered runbook** so the user can see the whole path.

## Step 1: Detect current state (read-only)

Run these checks from the project root (the directory containing `mkdocs.yml`).
Do **not** modify anything.

```bash
# Foundation
test -f mkdocs.yml                                   && echo "✓ scaffold (mkdocs.yml)"
test -f docs/course-description.md                   && echo "✓ course description"
# Knowledge model
test -f docs/learning-graph/learning-graph.json      && echo "✓ learning graph"
# Structure + content
ls docs/chapters/*/index.md 2>/dev/null | head -1    && echo "✓ chapters exist"
# Supporting content
test -f docs/glossary.md                             && echo "✓ glossary"
test -f docs/faq.md                                  && echo "✓ faq"
ls docs/chapters/*/quiz.md 2>/dev/null | head -1     && echo "✓ quizzes exist"
# Visualizations
ls docs/sims/*/main.html 2>/dev/null | head -1       && echo "✓ microsims exist"
# Metrics hub + publish
test -f docs/learning-graph/book-metrics.json        && echo "✓ book-metrics.json (hub)"
test -f README.md                                    && echo "✓ README"
```

Use the results to locate the user in the pipeline and recommend the next
uncompleted step.

## Step 2: Present the ordered runbook

The pipeline has **8 phases**. Foundation (Phase 0) runs once; later phases
respect the data-flow hand-offs. Each skill is invoked by the user with the
Skill tool. **Bold gates** must pass before continuing.

### Phase 0 — Project foundation (run once, in an empty repo)

| Order | Skill | Produces | Notes |
|-------|-------|----------|-------|
| 0.1 | `book-installer` → init-textbook (feature 0) | `mkdocs.yml`, `docs/` tree, license, starter `index.md`/`about.md`/`course-description.md`, social hook | Run **first**, in a near-empty directory. Refuses if `mkdocs.yml` already exists. |
| 0.2 | `book-installer` (other features) | Optional features layered onto the scaffold (math, mascot, learning-graph-viewer, document-status, etc.) | Run **many times**, as needed. Install **learning-graph-viewer** before Phase 1 visualizations and **book-metrics** before Phase 7. |

> **Why Phase 0 is special:** the feature-0 scaffold creates the core files
> every later skill assumes exist (`mkdocs.yml`, `docs/course-description.md`,
> `docs/learning-graph/`, `docs/chapters/`, `docs/sims/`). The rest of
> `book-installer` is a dispatcher that layers optional features on top.
> Skipping Phase 0 breaks every downstream skill, because they read and write
> into this structure.

### Phase 1 — Knowledge model

| Order | Skill | Reads | Writes | **Gate** |
|-------|-------|-------|--------|----------|
| 1.1 | `course-description-analyzer` | user input / draft | `docs/course-description.md` + assessment | **Quality score ≥ 85** before continuing |
| 1.2 | `learning-graph-generator` | `docs/course-description.md` | `docs/learning-graph/learning-graph.json` (+ CSV, taxonomy, quality metrics) | **DAG valid — zero circular dependencies** |

### Phase 2 — Chapter structure

| Order | Skill | Reads | Writes | **Gate** |
|-------|-------|-------|--------|----------|
| 2.1 | `book-chapter-generator` | `learning-graph.json`, `course-description.md` | `docs/chapters/*/index.md` (outlines only) | **Edge-direction validation** — prerequisites must point the right way |

### Phase 3 — Chapter content

| Order | Skill | Reads | Writes | **Gate** |
|-------|-------|-------|--------|----------|
| 3.1 | `chapter-content-generator` | chapter outlines, `learning-graph.json`, glossary (optional) | populated `docs/chapters/*/index.md` | **Edge-direction validation** (again) before writing |
| 3.2 | `book-media-generator` → chapter-images *(optional)* | chapter markdown | freely-licensed images + attribution | Enrich text-heavy chapters |

### Phase 4 — Visualizations (interleave with or follow Phase 3)

| Order | Skill | Use for |
|-------|-------|---------|
| 4.1 | `microsim-generator` | Interactive sims (p5.js, Chart.js, Plotly, vis-network, Mermaid, timeline, map, Venn, …) — routes by type |
| 4.2 | `microsim-generator` → infographic-overlay | Labeled diagrams: callout markers or grid zones over a scientific illustration |
| 4.3 | `microsim-generator` → causal-loop | Full systems-thinking **article** with multiple linked feedback loops |
| 4.4 | `book-media-generator` → verified-infographic | Fact-checked statistics poster (claims verified against sources first) |
| 4.5 | `microsim-generator` → concept-classifier | Scenario-classification quiz MicroSim |
| 4.6 | `microsim-utils` | **QA each new sim**: `layout-reviewer` (Claude Vision) then `iframe-tester` (Playwright); also screenshots + index page |

### Phase 5 — Supporting content

| Order | Skill | Reads | Writes | **Gate / prereq** |
|-------|-------|-------|--------|-------------------|
| 5.1 | `glossary-generator` | concept list | `docs/glossary.md` | After learning-graph concept list is final |
| 5.2 | `faq-generator` | content, learning graph, glossary | `docs/faq.md` | **≥ 30% of chapters written** + glossary exists |
| 5.3 | `quiz-generator` | chapter content, learning graph | `docs/chapters/*/quiz.md` | After chapter content exists (≥ 1000 words/chapter) |
| 5.4 | `reference-generator` | chapter titles/content | `docs/chapters/*/references.md` | After chapters are finalized |

### Phase 6 — Metrics & quality assurance

| Order | Skill | Produces | Notes |
|-------|-------|----------|-------|
| 6.1 | `book-installer` → book-metrics | **`docs/learning-graph/book-metrics.json`** | The **single source of truth** for all counts. Phase 7 skills read this — generate it here so README, LinkedIn, and press release report identical numbers. |
| 6.2 | `microsim-utils` → diagram-reports | legacy diagram-specification planning report | Optional; does not inventory rendered visuals or confirm coverage |
| 6.3 | `microsim-utils` → standardization | quality scores | Bulk audit of all sims |

### Phase 7 — Publish & announce

| Order | Skill | Reads | Produces | Notes |
|-------|-------|-------|----------|-------|
| 7.1 | `book-publisher` → readme | `book-metrics.json` | `README.md` | Reads the metrics hub — never recounts |
| 7.2 | `book-installer` → google-analytics (feature 25) | `mkdocs.yml` | GA4 wired into `mkdocs.yml` | First-time analytics setup |
| 7.3 | **Deploy** | — | live GitHub Pages site | `mkdocs gh-deploy` |
| 7.4 | `book-publisher` → linkedin-post | `book-metrics.json` | LinkedIn post | Reads the same hub |
| 7.5 | `book-publisher` → press-release | `book-metrics.json` | AP-style press release | Reads the same hub |
| 7.6 | `book-media-generator` → pptx-lecture *(optional)* | chapters | `.pptx` lecture deck | For classroom delivery |
| 7.7 | `book-media-generator` → story *(optional)* | topic | graphic-novel narrative + panels | Enrichment for a Stories section |

## Step 3: Recommend the next action

After detecting state, tell the user the **one** next skill to run and the gate
it must clear, e.g.:

> You have a learning graph but no chapters yet. **Next: run
> `book-chapter-generator`** (Phase 2.1). It reads `learning-graph.json` and
> writes chapter outlines. Gate: the edge-direction validation must pass before
> it writes any files.

## The minimal viable path

If the user wants the shortest route to a deployable book, collapse to:

`book-installer` (feature 0 scaffold) → `course-description-analyzer` (≥85) →
`learning-graph-generator` (DAG) → `book-chapter-generator` →
`chapter-content-generator` → `glossary-generator` → `quiz-generator` →
`book-installer` (book-metrics) → `book-publisher` (readme) → **deploy**.

## Rules for this command

- **Never auto-run a skill.** Recommend; the user invokes.
- **Respect the gates.** If a gate artifact is missing or failing (e.g. no
  `book-metrics.json` before Phase 7), say so and point back to the step that
  produces it.
- **Phase 0 is mandatory.** If `mkdocs.yml` is absent, the only valid next step
  is `book-installer` feature 0 (the init-textbook scaffold).
- Keep the "you are here" summary short; link each skill by name so the user can
  invoke it directly.
