# Skill Repository Refactor — Session Report

**Date:** 2026-07-10
**Model:** Claude Fable 5 (Claude Code)
**Scope:** Full review and reorganization of the `skills/` directory — 29 loaded skills consolidated to 14, description token footprint cut by 52%, plus hygiene fixes, shared-reference dedup, and a documentation sweep.

---

## 1. Executive Summary

| Metric | Before | After |
|--------|--------|-------|
| Repo skills | 29 (+2 stray dirs) | **14** |
| Loaded in `~/.claude/skills` | 30/30 — at the hard limit; 2 repo skills silently never loaded | **16** (14 repo + 2 external), 14 free slots |
| Name+description footprint | 8,215 chars ≈ **2,053 tokens** (over the 1%-of-200K budget) | 3,913 chars ≈ **978 tokens (49% of budget)** |
| Meta-skills | 3 (book-installer, microsim-generator, microsim-utils) | **5** (+ book-media-generator, book-publisher) |
| Unversioned or divergent skill copies | 2 real dirs in `~/.claude/skills` (pronounce-button unversioned; interactive-infographic-overlay stale since April) | 0 — all symlinks; pronounce-button adopted into git |
| `skills/archived/` | Referenced 3× by CLAUDE.md but did not exist | Exists, holds 18 verbatim originals + alias-map README |

The work ran as **9 single-commit phases** (one per turn, honoring the repo's auto-commit Stop hook), each independently revertible, with verification after every phase and a full path-integrity sweep at the end.

---

## 2. Initial Review Findings

### 2.1 Token budget measurement

Frontmatter `name:` + `description:` of every SKILL.md is injected into every session's context. Measured at session start: **8,215 chars ≈ 2,053 tokens across 29 skills** — already over the 2,000-token target (1% of a 200K context) before counting externally loaded skills (pi-keys-generator, skill-creator, pronounce-button).

Worst offenders (name+desc): marp-generator ~190 tok, docker-python-lab ~150, linkedin-carousel-generator ~96, causal-loop-diagram-generator ~94, microsim-generator ~92.

### 2.2 The 30-skill limit

`~/.claude/skills` held exactly 30 entries. `docker-python-lab` and `linkedin-carousel-generator` existed in the repo but were **never symlinked** (no free slots) — they silently never loaded.

### 2.3 Anomalies

1. `skills/docker-python-lab-workspace/` — 29 git-tracked files of eval-run output with no SKILL.md; not a skill.
2. `~/.claude/skills/pronounce-button` — a real directory existing **nowhere in any repo** (unversioned skill).
3. `~/.claude/skills/interactive-infographic-overlay` — a stale real directory (April 11) diverged from the repo version; its `references/iframe-height-pinning.md` existed **only** there.
4. `skills/archived/` — documented in CLAUDE.md, did not exist.
5. CLAUDE.md referenced phantom skills (`moving-rainbow`, `vis-network`) and a nonexistent installer name (`install-claude-skills.sh`; the real script is `scripts/bk-install-skills`).
6. `concept-classifier` used lowercase `skill.md` (breaks on case-sensitive filesystems).
7. `microsim-generator/references/causal-loop-guide.md` was a stale copy of a former standalone skill (frontmatter still read `name: causal-loop-microsim-generator`), duplicated and superseded by the standalone `causal-loop-diagram-generator`.

### 2.4 Duplication themes (from three parallel exploration agents)

1. mkdocs.yml nav-editing boilerplate duplicated across 5 content skills; quiz-generator itself warned about concurrent-edit collisions.
2. Bloom's Taxonomy material triplicated (chapter-content verbs file, faq's 466-line guide, quiz logic) — and notably, **no SKILL.md actually loaded either file by name**.
3. Site-metrics collection nominally reimplemented ~5× (in practice, most skills had already converged on the `docs/learning-graph/book-metrics.json` hub — see Phase 4).
4. book-installer features #1/#2 duplicated init-textbook's scaffold (two drifting template copies); feature #25 (Google Analytics) was **listed but had no guide and no routing row at all**; feature #39 overlapped six standalone skills' deliverables (though its guide already delegated properly).
5. marp-generator and textbook-to-presentation-generator contended for the same "make slides from this chapter" triggers.
6. faq-generator and quiz-generator are structural twins (kept separate by user decision).

### 2.5 User decisions (via AskUserQuestion)

- **Scope: Moderate (~14 skills)** — keep the content pipeline (course-description-analyzer, learning-graph, book-chapter, chapter-content, glossary, faq, quiz, reference) as separate skills, honoring the round-1 decision that complex workflows deserve dedicated skills; create 2 new meta-skills; absorb the MicroSim and infrastructure strays.
- **Non-book skills: keep loaded** — docx-to-web-publisher stays standalone; text-to-speech folds into book-media-generator's audio route.
- **Docs site: rewrite around the new roster**, keeping old per-skill pages as a Legacy section with banners so inbound links keep working.

---

## 3. The Approved Plan (verbatim)

> The following is the plan document as approved before implementation began.

# Claude Skills Repo Reorganization — Moderate Consolidation (29 → 14 skills)

## Context

Nine months of experimentation left `skills/` with 29 loadable skills (plus stray dirs). Two problems:

1. **Token budget**: every skill's name+description loads into every session. Measured today: **8,215 chars ≈ 2,053 tokens — already over the 1%-of-200K (≈2,000 token) budget** before counting externally-loaded skills (pi-keys-generator, skill-creator, pronounce-button).
2. **30-skill limit**: `~/.claude/skills` holds exactly 30 entries; `docker-python-lab` and `linkedin-carousel-generator` exist in the repo but were **never symlinked** (no free slots) — they silently never load.

A prior consolidation round (36→19, documented in `docs/consolidation-plan/index.md`) established the meta-skill router pattern (SKILL.md keyword Routing Table → on-demand `references/<x>.md` guides), proven in book-installer, microsim-generator, microsim-utils. This is round 2, per user decisions:

- **Moderate scope**: keep the content pipeline (course-description-analyzer, learning-graph, book-chapter, chapter-content, glossary, faq, quiz, reference) as separate skills; create 2 new meta-skills (book-media-generator, book-publisher); absorb MicroSim strays; absorb the two infrastructure strays (init-textbook, register-book-analytics) into book-installer since they duplicate its features #1/#2/#25.
- **Keep non-book skills loaded**: docx-to-web-publisher stays standalone; text-to-speech folds into book-media-generator's audio route.
- **Docs site**: rewrite `docs/skill-descriptions/` around the new roster; keep old per-skill pages under a "Legacy" nav section with a banner.

Projected result: **14 loaded repo skills, ~3,700 chars ≈ ~930 tokens (~0.47%)**, 16 free slots.

## Final roster (14)

| Skill | Change |
|---|---|
| book-installer | absorbs init-textbook (as feature #0), register-book-analytics (merges into feature #25) |
| course-description-analyzer | unchanged |
| learning-graph-generator | unchanged |
| book-chapter-generator | unchanged (points at canonical nav guide) |
| chapter-content-generator | unchanged + becomes canonical home of Bloom's reference |
| glossary-generator | unchanged (drop legacy INSTALL.md/README.md; canonical nav guide) |
| faq-generator | Bloom's guide replaced by pointer to canonical |
| quiz-generator | same |
| reference-generator | canonical nav guide pointer |
| microsim-generator | absorbs concept-classifier, causal-loop-diagram-generator, interactive-infographic-overlay, docker-python-lab |
| microsim-utils | absorbs diagram-reports-generator |
| **book-media-generator** (NEW) | marp-generator, textbook-to-presentation-generator, story-generator, verified-infographic-generator, chapter-image-enhancer, text-to-speech, pronounce-button (adopted from ~/.claude/skills) |
| **book-publisher** (NEW) | readme-generator, linkedin-announcement-generator, linkedin-carousel-generator, press-release-generator |
| docx-to-web-publisher | unchanged |

## Conversion conventions (all merges)

- Absorbed SKILL.md body → `references/<route>-guide.md` in the meta-skill; frontmatter stripped, replaced with H1 + `> Formerly the standalone skill \`<old-name>\`.`
- Absorbed skill's own references flattened with a route prefix (`cld-`, `overlay-`, `marp-`, `pptx-`, `story-`, `tts-`, `carousel-`, `infographic-`) to avoid collisions; scripts/assets → `scripts/<route>/`, `assets/<route>/`.
- Add a routing-table row `| Trigger Keywords | Guide File | Purpose |` per absorbed skill; keep the old skill's distinctive trigger words **verbatim** in the meta-skill description (glossary, faq, quiz, MARP, causal-loop, classifier, python lab, pronounce…) so muscle-memory invocations still route.
- Cross-meta-skill references use the established `$HOME/.claude/skills/<owner>/...` absolute-path convention (already used by microsim-generator → microsim-utils, `microsim-generator/SKILL.md:569`).
- Legacy INSTALL.md/README.md inside absorbed skills are NOT migrated (they go to the archive with the original dir).
- Originals: `git mv skills/<name> skills/archived/<name>` intact + `skills/archived/README.md` alias table (old name → new meta-skill → keywords). Archived dirs never load: discovery is one level deep, and the installer gets an explicit skip.

## Key merge details

**microsim-generator** (+4):
- causal-loop-diagram-generator **replaces** the stale `references/causal-loop-guide.md` (whose frontmatter still says `name: causal-loop-microsim-generator`); its assets → `assets/causal-loop/`. The standalone version wins wholesale (multi-loop articles, cld-inline.js, cld-viewer).
- concept-classifier → `references/concept-classifier-guide.md` (side effect: retires the lowercase `skill.md` bug); templates → `assets/concept-classifier/`.
- interactive-infographic-overlay → `references/infographic-overlay-guide.md`; shared-libs (diagram.js, grid-diagram.js, CSS) → `assets/infographic-overlay/`; **first salvage `references/iframe-height-pinning.md` from the stale real dir `~/.claude/skills/interactive-infographic-overlay/` (exists ONLY there)** and merge into the overlay guide or microsim-utils' iframe-auto-height.md.
- docker-python-lab → `references/docker-python-lab-guide.md`; assets → `assets/docker-python-lab/`.
- Update the Quick Reference Routing Table (~line 261) and `references/routing-criteria.md` with 4 new rows.

**microsim-utils** (+1): diagram-reports-generator → `references/diagram-reports.md`; `scripts/diagram-report.py` moves in (no name collision with the 6 existing scripts).

**book-installer** (+2, internal dedup):
- init-textbook → `references/init-textbook.md` as feature **#0 "New textbook scaffold"**; its `assets/templates/` → `assets/init-textbook/`; rewrite `references/mkdocs-template.md` (features #1/#2) to source starter files from that single copy (kills the scaffold drift).
- register-book-analytics → merged into `references/google-analytics.md` (feature #25).
- Rewrite feature #39 to **delegate** to the standalone content skills + book-publisher readme route instead of embedding parallel generation logic.

**book-publisher** (NEW router, ~150 lines modeled on microsim-utils):
- Routes: readme (badges, site stats), linkedin-post, linkedin-carousel, press-release.
- Metrics dedup: `readme-generator/scripts/collect-site-metrics.py` (372 lines) moves to `book-installer/scripts/` as the canonical collector; all 4 routes read `docs/learning-graph/book-metrics.json`, falling back to running that script (matches the /ibook Phase 6→7 contract). Delete the 3 inline metric-collection reimplementations in the linkedin/press guides.
- Rename `slide-patterns.md` → `carousel-slide-patterns.md`.

**book-media-generator** (NEW router):
- Routes: marp-deck (HTML decks → docs/slides/), pptx-lecture (.pptx download), story (graphic novels → docs/stories/), verified-infographic (fact-checked posters), chapter-images (Wikimedia/gov sourcing), text-to-speech, pronounce-button.
- **Top of SKILL.md: slides disambiguation rule** — published/embedded on site → marp; downloadable/classroom/"PowerPoint" → pptx; ambiguous → ask. (Fixes today's marp vs textbook-to-presentation trigger contention.)
- `image-prompt-template.md` collision: verified-infographic's copy → `references/poster-image-prompt.md`; overlay's copy lives in microsim-generator as `overlay-image-prompt.md`; diff during move, cross-link shared "annotation-free" rules.
- pronounce-button adopted from `~/.claude/skills/pronounce-button/` (unversioned!) → route guide + `scripts/audio/generate-pronunciation.py`; ElevenLabs API-key setup note shared by both audio routes.

**Shared-reference dedup for the kept-separate content skills** (no merging):
- NEW canonical `book-installer/references/mkdocs-nav-editing.md` (book-installer owns mkdocs.yml domain), carrying quiz-generator's concurrent-edit warning + "serialize nav edits, re-read before write". The 5 content skills (book-chapter Step 4.5, glossary Step 9, faq Step 10, quiz Step 14, reference Step 7) replace inline boilerplate with a pointer.
- NEW canonical `chapter-content-generator/references/blooms-taxonomy.md` = merge of its bloom-taxonomy-verbs.md + faq-generator's 466-line blooms-taxonomy-guide.md; faq/quiz point at it.
- Canonical files get a top comment: `<!-- Canonical copy. Do not fork; reference by path. -->`

## Hygiene fixes

1. `git rm -r skills/docker-python-lab-workspace/` — 29 files of committed eval-run output, not a skill (its `evals/` origin stays with the archived docker-python-lab).
2. Adopt pronounce-button into the repo (see above), then `rm -rf ~/.claude/skills/pronounce-button` (real dir; installer skips real dirs, manual removal needed).
3. Salvage iframe-height-pinning.md, then `rm -rf ~/.claude/skills/interactive-infographic-overlay` (stale Apr-11 real dir).
4. Patch `scripts/bk-install-skills`: skip `archived` in the main loop (`case "$skill_name" in archived) continue ;; esac` after ~line 104). Its existing stale-symlink cleanup (lines 59–81) auto-removes absorbed skills' symlinks on each rerun.
5. CLAUDE.md: fix `install-claude-skills.sh` → `bk-install-skills` (lines 56/283–292); remove phantom `moving-rainbow` and `vis-network` entries; update repo tree, meta-skill table (5 meta-skills), 12-step workflow names; archived/ references become true.
6. `commands/ibook.md`: rewrite phase tables to `meta-skill → route` form for absorbed skills (content-pipeline names unchanged).
7. **Symlink-count constraint**: at 30/30 today, do NOT rerun the installer before Phase 1 — Phase 0 does manual symlink surgery only; full reruns are safe once merges shrink the roster.

## Phasing (one commit per turn — auto-commit Stop hook; write `.claude-pending-commit.txt` each turn)

Within every merge phase, order operations: create new files → `git mv` originals to archived → rerun installer. Any intermediate state keeps every capability reachable.

| Phase | Scope | Repo skills after |
|---|---|---|
| 0 | Hygiene: rm workspace dir; adopt pronounce-button; installer patch; salvage overlay file; minimal CLAUDE.md ref fixes; manual ~/.claude/skills cleanup | 30 → 30 |
| 1 | microsim-generator merge (4 absorbed) + routing table + trimmed description | 26 |
| 2 | microsim-utils merge (diagram-reports) | 25 |
| 3 | book-installer merge (init-textbook #0, register-book-analytics #25) + scaffold dedup + feature #39 delegation | 23 |
| 4 | book-publisher NEW (4 absorbed) + collect-site-metrics.py → book-installer/scripts + metrics-hub rewiring | 20 |
| 5 | book-media-generator NEW (6 absorbed + pronounce-button) + slides disambiguation rule | 14 |
| 6 | Content-skill dedup: canonical mkdocs-nav-editing.md + blooms-taxonomy.md, pointer rewrites, opportunistic description trims for kept skills | 14 |
| 7 | Docs & commands sweep: CLAUDE.md full update; commands/ibook.md; docs/skill-descriptions restructure around 14-skill roster + Legacy section with banner; mkdocs.yml nav; mark docs/consolidation-plan as superseded (link to new plan); grep bk-list-skills / bk-analyze-skill-usage for hardcoded rosters | 14 |
| 8 | Verification & budget tuning (below); lengthen any under-triggering description (headroom exists) | 14 |

## Verification (after each phase; full pass in Phase 8)

1. **Budget recount**: loop `skills/*/SKILL.md`, sum name+description chars ÷ 4 → target ≤ ~1,000 tokens by Phase 5 (from 2,053).
2. **Broken-path grep**: extract every `references/…`, `scripts/…`, `assets/…`, `$HOME/.claude/skills/…` mention from each meta-skill's SKILL.md + guides; `test -e` each. Then `grep -rn '<old-skill-name>' skills/ commands/ CLAUDE.md --exclude-dir=archived` → only alias README + "Formerly" lines may match.
3. **Symlink health**: `find ~/.claude/skills -xtype l` → empty; no real dirs remain; count = 14 repo + externals ≤ 30; `ls ~/.claude/skills | grep archived` → empty.
4. **Fresh-session check**: new claude session → skill list shows the 14 + externals, no archived names.
5. **Trigger smoke tests** (scratch textbook project): "add a quiz to chapter 3", "make a slide deck from chapter 2", "turn this into a PowerPoint for class", "add pronunciation for the term Neuron", "create a causal loop diagram", "add a Python lab", "write a press release" — confirm correct skill/route engages.
6. `mkdocs build --strict` after Phase 7.

## Risks

- **Trigger regression from shortened descriptions** — highest for marp (746-char description full of quoted phrases) and docker-python-lab. Mitigation: per-phase checklist that every distinctive trigger noun survives in the absorbing description; smoke tests; ~1,000 tokens of headroom to re-lengthen.
- **Muscle memory** — alias table in skills/archived/README.md; old names kept as substrings in new descriptions.
- **Cross-skill path coupling** (publisher → book-installer script; content skills → book-installer nav guide; media/microsim cross-refs): each cross-reference carries a one-line fallback; pairings documented in CLAUDE.md.
- **Downstream textbook repos** referencing old skill names: out of scope; learning-graph-generator script paths deliberately untouched.
- **anthropic-skills plugin duplicates** (register-book-analytics, microsim-p5) load regardless of this repo — flag to user for separate cleanup, not part of this refactor.

*(End of approved plan.)*

---

## 4. Phase-by-Phase Results

### Pre-phase: uncommitted work rescued

Before Phase 0, a large uncommitted change to `skills/microsim-utils/scripts/sync-iframe-heights.py` (292+/274−, from a prior session) was committed separately as `cd7476fa` so the auto-commit hook would not sweep unrelated work into the hygiene commit.

### Phase 0 — Hygiene (`68fc791b`)

- Removed `skills/docker-python-lab-workspace/` (29 files of eval output).
- Adopted `pronounce-button` into the repo (previously unversioned).
- Salvaged `iframe-height-pinning.md` from the stale local overlay copy (documents the non-obvious `reportHeight()` design in `diagram.js`).
- Patched `bk-install-skills` to skip `skills/archived/`.
- Replaced the 2 real dirs in `~/.claude/skills` with symlinks (manual surgery only — installer rerun unsafe at 30/30).
- Minimal CLAUDE.md fixes (installer name, phantom skills).
- **State: 30 loaded, budget 2,053 tokens.**

### Phase 1 — microsim-generator merge (`fe08c732`)

- 4 skills became routed guides: `concept-classifier-guide.md`, `causal-loop-guide.md` (**replacing** the stale copy whose frontmatter still carried the old standalone skill name — the richer multi-loop-article version won), `infographic-overlay-guide.md`, `docker-python-lab-guide.md`.
- Assets namespaced (`assets/causal-loop/`, `assets/concept-classifier/`, `assets/infographic-overlay/`, `assets/docker-python-lab/`); references prefixed (`cld-*`, `overlay-*`); salvaged height-pinning doc wired in as `overlay-iframe-height-pinning.md`.
- Routing table +3 rows (causal-loop row enriched), decision tree, 4 new scoring profiles in `routing-criteria.md`, 4 new routing examples.
- Installer rerun freed slots — `linkedin-carousel-generator` got loaded **for the first time ever**.
- **State: 27 loaded, budget 1,776 tokens.** (26 repo + externals; count shown includes external symlinks.)

### Phase 2 — microsim-utils merge (`a6e5377f`)

- `diagram-reports-generator` → `references/diagram-reports.md` + `scripts/diagram-report.py` (no collision with the 6 existing scripts).
- Guide text de-specialized from its geometry-course origins.
- **State: budget 1,729 tokens.**

### Phase 3 — book-installer merge (`f93e0172`)

- init-textbook → **feature #0** with the scaffold templates as the single canonical copy in `assets/init-textbook/`; the drifted duplicate starter templates under `references/assets/templates/` were deleted; `mkdocs-template.md` Option 1 now defers to feature #0.
- register-book-analytics → `references/google-analytics.md`. **Discovery:** feature #25 was listed in the help menu but had *no guide and no routing row at all* — requests would have fallen through. Now it routes.
- **Discovery:** the feature #39 guide (`supplementary-content-generator.md`) already delegated to the standalone skills — the planned "delegation rewrite" was mostly unnecessary; only its README step needed repointing (done in Phase 4).
- **Flagged:** `mkdocs-template.md` Option 2 (Conda + Cairo full setup) references asset files that don't exist in the repo — pre-existing breakage, left for a separate decision.
- **State: 25 loaded, budget 1,629 tokens.**

### Phase 4 — book-publisher NEW (`ac26066d`)

- 4 skills became routed guides: readme, linkedin-post, linkedin-carousel, press-release; support files moved with `carousel-` prefixes.
- **Plan deviation (justified):** the metrics dedup was already half-built — all four skills had converged on reading `docs/learning-graph/book-metrics.json` (produced by `bk-generate-book-metrics`). So `collect-site-metrics.py` was NOT moved to book-installer; it stayed in `book-publisher/scripts/` as the fallback scanner it always was, and the "all routes read the hub, never recount" contract is stated once in the router's Step 2.
- Cross-references inside guides rewritten from old skill names to route names (a rename pass briefly clobbered two "Formerly" attribution lines; caught and restored during verification).
- book-installer feature #39 now delegates its README step to book-publisher.
- **State: 22 loaded, budget 1,433 tokens.**

### Phase 5 — book-media-generator NEW (`d133ef8b`)

- 7 skills became routed guides: marp-deck, pptx-lecture, story, verified-infographic, chapter-images, text-to-speech, pronounce-button. Prefix renames: `marp-*`, `pptx-*`, `tts-*`, `infographic-*`, `scripts/story/`, `scripts/audio/`.
- **Slides disambiguation rule at the top of the router**: web deck on the site → MARP; downloadable/classroom/"PowerPoint" → pptx; ambiguous → ask one question. (Resolves the long-standing marp vs textbook-to-presentation trigger contention.)
- The two image-prompt templates proved to be genuinely different documents (locked poster prompt vs annotation-free overlay illustration) — kept separate as planned, cross-linked on the shared annotation-free rule.
- Shared ElevenLabs API-key note for both audio routes.
- **Milestone: repo hits the 14-skill target. 16 loaded total, budget 978 tokens (~0.49%).**

### Phase 6 — Content-skill dedup (`73fba782`)

- NEW canonical `book-installer/references/mkdocs-nav-editing.md`: read-before-write, **serialize concurrent nav edits** (quiz-generator's collision warning promoted to a shared rule with "batch all nav changes into one edit"), only-touch-your-section, number-only chapter labels, placement table. The 5 content skills replaced their boilerplate with a pointer + their artifact-specific YAML.
- NEW canonical `chapter-content-generator/references/blooms-taxonomy.md` merging the verbs file and faq's 466-line guide. **Discovery:** neither original was loaded by name from any SKILL.md — dangling files. All three consumers now have explicit pointers.
- Dropped glossary-generator's legacy standalone `INSTALL.md`/`README.md`; fixed two stale file references the merge exposed.

### Phase 7 — Docs & commands sweep (`2d94e412`)

- **CLAUDE.md**: repo tree rewritten for the 14-skill layout; meta-skill table expanded to 5 rows; 12-step workflow gained step 13 "Publish & Announce"; archived/ references finally true.
- **commands/ibook.md**: every absorbed-skill reference converted to `meta-skill → route` form (Phase 0 → book-installer feature 0; Phase 4 visualization rows → microsim-generator routes; Phase 7 publish rows → book-publisher routes; minimal-viable-path updated).
- **docs/skill-descriptions/index.md**: rebuilt around the current roster with routing tables and a "Where Did Skill X Go?" alias table; the three per-skill page sections bannered as legacy snapshots with "(Legacy)" nav labels (URLs preserved).
- **docs/consolidation-plan/index.md**: bannered as superseded (36→19→14 history).
- `bk-list-skills` / `bk-analyze-skill-usage`: no hardcoded rosters found.
- **`mkdocs build --strict` passed.**

### Phase 8 — Final verification & repair (this session's last phase)

A repo-wide path-integrity check tested **191 path references** across all five meta-skills (relative `references/`, `assets/`, `scripts/` paths plus `$HOME/.claude/skills/...` cross-skill paths), plus an old-skill-name sweep and a trigger-keyword audit.

**Move-induced breakage found and fixed:**

- Salvaged `overlay-iframe-height-pinning.md` still pointed at pre-move names (`assets/main-template.html`, `data-json-schema.md`) → repointed to `assets/infographic-overlay/…`, `overlay-data-json-schema.md`.
- `cld-json-schema.md` / `cld-layout-templates.md` still referenced `assets/cld-viewer/` → `assets/causal-loop/cld-viewer/`.
- The poster/overlay image-prompt cross-links and the book-metrics pointer rewritten to explicit `$HOME/.claude/skills/<owner>/…` paths (machine-checkable).
- Seven guides still instructed the reader to invoke a retired standalone skill (textbook-to-presentation-generator ×3, interactive-infographic-overlay, readme-generator, linkedin-announcement-generator, `/story-generator` ×3) → all now name the meta-skill route.

**Trigger-keyword audit: 31/31** distinctive keywords from the archived skills verified present in the absorbing meta-skill descriptions.

**Pre-existing debt catalogued** (predates this reorg; spawned as a separate follow-up task rather than expanding scope): broken template paths in venn/plotly/comparison-table/celebration/mermaid guides and microsim-utils' standardization.md; `mkdocs-template.md` Option 2's five missing assets; `cover-image-generator.md`'s missing `src/image-generation/generate-cover.sh`; `linkedin-post-guide.md` documenting a `linkedin-metrics-extractor.py` that was never shipped; `routing-criteria.md` → `scripts/check-version.py`.

---

## 5. Final State

- **14 repo skills** (5 meta-skills, 8 content-pipeline skills, 1 standalone), 16 loaded total, **14 free slots** under the 30-skill limit.
- **978 tokens** of always-loaded description text — **49% of the 2,000-token budget**, down from 103%. Headroom exists to lengthen any description that under-triggers in practice.
- `skills/archived/` holds 18 verbatim originals with an alias-map README (old name → new route → trigger keywords); never loaded (installer skip + one-level discovery), restorable via `git mv` + installer rerun.
- Zero broken symlinks, zero real dirs in `~/.claude/skills`, `mkdocs build --strict` clean.
- Every phase is one commit — `git log` reads as the step-by-step story, and any single merge can be reverted independently.

### Commit map

| Phase | Commit | Subject |
|-------|--------|---------|
| pre | `cd7476fa` | Resolve CANVAS_HEIGHT from metadata.json and main.html, scan all of docs/ (rescued prior-session work) |
| 0 | `68fc791b` | Phase 0 hygiene for skills reorganization (29 → 14 plan) |
| 1 | `fe08c732` | Fold 4 stray MicroSim skills into the microsim-generator meta-skill |
| 2 | `a6e5377f` | Fold diagram-reports-generator into the microsim-utils meta-skill |
| 3 | `f93e0172` | Fold init-textbook and register-book-analytics into book-installer |
| 4 | `ac26066d` | Create book-publisher meta-skill from the four promotion/publishing skills |
| 5 | `d133ef8b` | Create book-media-generator meta-skill from the seven media skills |
| 6 | `73fba782` | Deduplicate nav-editing and Bloom's taxonomy references across content skills |
| 7 | `2d94e412` | Update docs, CLAUDE.md, and /ibook runbook for the 14-skill architecture |
| 8 | `1977c2cd` | Repair move-induced references found by the final verification sweep |

## 6. Outstanding Items

1. **Follow-up task chip spawned**: "Fix stale asset paths in round-1 meta-skill guides" — repoint or remove the ~30 pre-existing broken references listed in §4 Phase 8.
2. **Decision for Dan**: delete `mkdocs-template.md` Option 2 outright? Its Conda/Cairo assets never existed in the repo, and feature 0 is now the canonical scaffold. (Included in the follow-up task's scope.)
3. **anthropic-skills plugin duplicates**: the plugin independently ships `register-book-analytics` and `microsim-p5`, which load regardless of this repo — separate cleanup, user-level plugin configuration.
4. **Trigger smoke tests in real usage**: the keyword audit passed statically; the true test is natural requests in a real textbook project ("add a quiz to chapter 3", "make slides for chapter 2", "add pronunciation for Neuron", "create a causal loop diagram", "add a Python lab"). Budget headroom exists to re-lengthen any description that under-triggers.
5. **Downstream textbook repos** may reference old skill names in their own CLAUDE.md files — the alias map in `skills/archived/README.md` is the lookup table when they do.
