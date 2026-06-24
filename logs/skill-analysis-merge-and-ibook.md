# Skill Analysis: Merges, Duplication, Orchestration & /ibook

**Date:** 2026-06-23
**Scope:** All 28 skills in `skills/` (now 26 after this turn's merge)
**Trigger:** Request to analyze the intelligent-textbook / MicroSim / infographic
skills for merge opportunities, duplication, better orchestration, and whether
to create an `/ibook` command.

---

## 1. Executive Summary

- **Executed:** Merged `microsim-iframe-tester` + `microsim-layout-reviewer`
  into the `microsim-utils` meta-skill (28 → 26 skills, freeing 2 slots under
  the 30-skill cap).
- **Created:** `/ibook` command (`commands/ibook.md`) — a passive runbook that
  lists every textbook skill in dependency order with prerequisites, inputs/
  outputs, and quality gates, and detects "you are here" without auto-running
  anything.
- **Recommended (not executed):** Two further merges and several documentation
  clarifications — see §5.

---

## 2. The Three Skill Families

### A. Foundation / infrastructure (2)
`init-textbook`, `book-installer`

Two-layer architecture, intentionally:
- **`init-textbook`** = bootstrap once. Creates the minimal working scaffold
  (`mkdocs.yml`, `docs/` tree, license, social hook, starter pages). Refuses if
  `mkdocs.yml` exists.
- **`book-installer`** = layer features many times. A dispatcher to **23**
  reference guides (mkdocs-features, learning-graph-viewer, mascot, book-metrics,
  slides, about-page, etc.). Modifies `mkdocs.yml` in place; never recreates it.

**Fuzzy boundary (by design):** both can write `docs/index.md`, `docs/about.md`,
`docs/css/extra.css`, `docs/img/cover.png`. `init-textbook` writes minimal
scaffolding versions; `book-installer`'s `home-page-template` / `about-page` /
`cover-image-generator` guides replace them with publication-quality versions
(asking before overwrite). This is acceptable — not duplication to remove.

**Recommendation:** Keep separate. The split is sound. The only risk is users
not knowing `init-textbook` must run first and `book-installer` second — which
the new `/ibook` runbook now makes explicit (Phase 0).

### B. Content pipeline (13)
`course-description-analyzer`, `learning-graph-generator`, `book-chapter-generator`,
`chapter-content-generator`, `glossary-generator`, `faq-generator`,
`quiz-generator`, `reference-generator`, `readme-generator`,
`linkedin-announcement-generator`, `press-release-generator`,
`textbook-to-presentation-generator`, `register-book-analytics`

Clean linear data-flow, no duplicate outputs. Hand-off artifacts:

```
course-description.md
  → learning-graph.json   (single source of truth for structure)
    → chapters/*/index.md (outlines → content)
      → glossary.md, faq.md, quiz.md, references.md
        → book-metrics.json   (single source of truth for COUNTS)
          → README, LinkedIn post, press release  (all read the same hub)
```

**Key finding — the `book-metrics.json` hub:** three skills (`readme-generator`,
`linkedin-announcement-generator`, `press-release-generator`) all read
`docs/learning-graph/book-metrics.json` so every artifact reports identical
numbers. This is correct design; the risk is the file being stale/missing. The
`/ibook` runbook makes generating it an explicit gate (Phase 6.1) before any
Phase 7 announce skill.

**Hard quality gates discovered (now encoded in `/ibook`):**
1. course-description quality score **≥ 85** before learning graph
2. learning graph must be a **valid DAG** (no cycles)
3. **edge-direction validation** in both `book-chapter-generator` and
   `chapter-content-generator`
4. **≥ 30% of chapters** written before `faq-generator`

### C. Visualization / MicroSim / infographic (11 → 9 after merge)
`microsim-generator` (meta), `microsim-utils` (meta), `concept-classifier`,
`interactive-infographic-overlay`, `causal-loop-diagram-generator`,
`verified-infographic-generator`, `diagram-reports-generator`,
`chapter-image-enhancer`, `story-generator`, and (retired) `microsim-iframe-tester`
+ `microsim-layout-reviewer`.

See duplication analysis below.

---

## 3. Duplication Findings

| Pair | Verdict | Action |
|------|---------|--------|
| `microsim-iframe-tester` + `microsim-layout-reviewer` vs `microsim-utils` | **Same family — three MicroSim QA tools that should live together.** iframe-tester (geometric/Playwright), layout-reviewer (visual/Claude Vision), and utils' existing `sync-iframe-heights.py` (build-time) are complementary. | **MERGED into microsim-utils** (this turn) |
| `causal-loop-diagram-generator` vs `microsim-generator`'s `causal-loop-guide` | **Overlapping but distinct.** The guide makes a *single* embedded diagram; the standalone skill makes a multi-diagram *article* with progressive build-up + shared `cld-viewer`. | Keep both; document the distinction (recommended) |
| `interactive-infographic-overlay` vs `verified-infographic-generator` | **Not duplicates.** One overlays interactive labels on an existing illustration (explore/quiz/edit modes); the other fact-checks statistics and renders a static poster. | Keep both |
| `concept-classifier` vs `microsim-generator` p5 guide | Both produce p5.js sims, but concept-classifier is a specialized data-driven quiz pattern. | Keep standalone for now; candidate for a p5 sub-guide later |

---

## 4. What Was Executed This Turn — the QA-skill merge

**Goal:** consolidate the two MicroSim QA skills into `microsim-utils`, since all
three QA concerns (height sync, control-visibility, visual review) belong to the
same maintenance family.

**Moved (git mv, history preserved):**
- `microsim-iframe-tester/scripts/test-iframe-heights.py` →
  `microsim-utils/scripts/test-iframe-heights.py`
- `microsim-layout-reviewer/references/visual-checklist.md` →
  `microsim-utils/references/visual-checklist.md`
- `microsim-layout-reviewer/references/common-fixes.md` →
  `microsim-utils/references/common-fixes.md`

**Created (new sub-guides):**
- `microsim-utils/references/iframe-tester.md`
- `microsim-utils/references/layout-reviewer.md`

**Retired (deleted):**
- `skills/microsim-iframe-tester/` (incl. the deprecated Node.js
  `test-iframe-heights.js`, `package.json`, `package-lock.json`, and bundled
  `node_modules/` — the skill's own SKILL.md already declared the JS path
  "should not be used"; only the Python script was kept)
- `skills/microsim-layout-reviewer/`
- The two now-dangling symlinks in `~/.claude/skills/`

**Updated cross-references:**
- `microsim-utils/SKILL.md` — description, when-to-use, routing table (2 new
  rows), decision tree, an "iframe-height utilities at a glance" comparison
  table, two new "Available Utilities" sections, two new examples, and the
  "After Creating New MicroSim" workflow
- `microsim-generator/SKILL.md` — Step 6C script path now points to
  `microsim-utils/scripts`; Step 9 now invokes the `microsim-utils`
  layout-reviewer guide instead of the standalone skill (5 references updated)
- `CLAUDE.md` — both meta-skill tables list the new sub-guides
- `visual-checklist.md` — internal reference re-pointed to the `iframe-tester`
  utility

**Net:** 28 → **26 skills**. No functionality lost except the explicitly-
deprecated Node.js tester.

---

## 5. Recommended (Deferred) — needs separate approval

1. **Document the causal-loop distinction.** Add a one-line note to
   `microsim-generator`'s `causal-loop-guide.md`: "single diagram only — for a
   multi-CLD systems-thinking article, use the standalone
   `causal-loop-diagram-generator` skill." Prevents confusion between the two.

2. **Consider `concept-classifier` → a `microsim-generator` p5 sub-guide.** Would
   free one more slot. Deferred because it's a distinct, reusable pedagogical
   pattern and the slot pressure is now relieved (26/30).

3. **No other content-pipeline merges.** Each of the 13 content skills has a
   distinct output and a distinct place in the data flow; merging any would hurt
   discoverability without reducing real surface area.

---

## 6. Orchestration Improvement — `/ibook`

The 12-step workflow already lived in `CLAUDE.md` prose but was not actionable.
`commands/ibook.md` turns it into an **8-phase runbook** that:
- detects which artifacts exist (read-only) and shows "you are here";
- recommends the single next skill + its gate;
- lists the full ordered path with inputs/outputs/gates;
- never auto-runs a skill (the user invokes each manually).

Phase 0 explicitly orders `init-textbook` (once) before `book-installer`
(repeatable) — the foundation the request asked to highlight — because every
later skill reads/writes into the structure those two create.

A slash command (not a skill) was the right home: it costs **nothing** against
the 30-skill cap and matches the existing `commands/skills.md` pattern.
