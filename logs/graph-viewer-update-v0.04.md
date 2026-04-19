# Graph Viewer Template Update — v0.03 → v0.04

**Date:** 2026-04-19
**Skill:** `book-installer` (install guide: `references/learning-graph-viewer.md`)
**Templates touched:** `references/assets/{script.js,main.html,local.css}`
**Triggered by:** user report that check-all / uncheck-all buttons were "VERY slow" and the "Loading concepts…" progress text was missing from a freshly installed viewer in the `learning-sciences` textbook.

## Context

The user's working project was `/Users/dan/Documents/ws/learning-sciences`. The learning graph had just been generated (221 nodes, 340 edges) and the `book-installer` skill had been used with the "install learning graph viewer" guide to drop a viewer into `docs/sims/graph-viewer/`.

On test, two bugs appeared that the user said had been fixed in a previous iteration but did not make it into the current templates:

1. **Check-all / uncheck-all checkboxes were very slow.**
2. **The "Loading concepts…" progress indicator never appeared** (blank aliceblue square during initial physics layout).

## Investigation

- Diffed the installed files in `learning-sciences/docs/sims/graph-viewer/` against the skill source at `~/.claude/skills/book-installer/references/assets/`. They matched exactly — confirming the skill source itself still carried the bugs.
- Compared `script.js` MD5 hashes across six downstream projects:

  | Project | Lines | md5 |
  |---|---|---|
  | `calculus` | 363 | `d5fec8…` |
  | `graph-data-modeling-course` | 303 | `c984e7…` |
  | `moss` | 378 | `48470c…` |
  | `learning-graphs` | 284 | `42b44d…` |
  | `learning-linux` | 337 | `181685…` |
  | **skill source** | 381 | `0ce5d4…` |

  Only `moss` had both fixes. Every other downstream project had independently diverged. The skill source had neither fix.

- Located the smoking-gun code in the skill's `script.js`:

  ```js
  // updateVisibility — ran 220 times per click
  allNodes.forEach(node => {
      nodes.update({ id: node.id, hidden: !isVisible });  // per-item call
  });
  allEdges.forEach(edge => {
      edges.update({ id: edge.id, hidden: !isVisible });  // per-item call
  });
  ```

  ~560 round-trips through vis-network per check-all on a 220-node graph. The skill's own `references/learning-graph-viewer.md` troubleshooting table already documented this pattern as a footgun ("Checkbox toggling slow | Per-item DataSet.update() calls | Use batched array update (built-in)"), but the code itself was never updated to match. Textbook case of "fix documented, not implemented."

- The "Loading…" indicator existed in the MOSS version as a `<div id="loading-message">` inside `.graph-container`, styled to center-absolute, and removed by a `network.once('stabilizationIterationsDone', …)` handler. None of this existed in the skill templates.

## Fixes Applied

### script.js (replaced in full with MOSS version)

- **Batched `nodes.update(array)` / `edges.update(array)`** in `updateVisibility()` and `highlightNode()`. Single round-trip per event.
- **Precomputed `nodesWithDeps` (set of edge.from) and `groupCounts`** at load time — avoids recomputing on every stats refresh.
- **Explicit integer edge IDs** assigned at load: `allEdges = (data.edges || []).map((edge, i) => ({ ...edge, id: edge.id ?? i }))`. Batched updates need deterministic IDs to target.
- **`network.once('stabilizationIterationsDone', …)`** removes the loading message.
- **Better error text** — names the expected JSON path (`../../learning-graph/learning-graph.json`).

### main.html

- Added `<div id="loading-message">Loading concepts and edges...</div>` inside `.graph-container`.
- Added `<div id="viewer-version">v0.04</div>` in the same container (top-right badge).

### local.css

```css
#loading-message {
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.3rem; color: #555;
    pointer-events: none; z-index: 20;
}

#viewer-version {
    position: absolute; top: 8px; right: 12px;
    font-size: 0.75rem; color: #999;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    pointer-events: none; z-index: 20; user-select: none;
}
```

### references/learning-graph-viewer.md (skill install guide)

Added a **Viewer Version** section stating the current version (v0.04) and listing the three places future contributors must bump when they change template behavior:

1. The `Viewer Version` section of the install guide.
2. `references/assets/main.html` → the `<div id="viewer-version">…</div>` line.
3. A new entry in the Changelog block.

Added a **Changelog** block with v0.03 (template split from inline code, commit `89275ae6`) and v0.04 (this update).

## Scope Discipline

MOSS's version also narrows the sidebar from 300px → 200px and reorganizes CSS comments into section banners. **Neither was ported.** This update is scoped strictly to:

1. The two user-reported bugs.
2. The version-badge mechanism that prevents a recurrence of the "downstream drift, no one backports" pattern.

## Commits

Committed via the auto-commit hook on turn end. Commit message captured in `.claude-pending-commit.txt` before Stop. Two commits landed in `claude-skills` during the session:

1. `b7519dd9` — Fix wrong template path (`learning-graph-viewer-templates/` → `assets/`) in the install guide. Unrelated to the viewer bugs, but surfaced during the earlier `book-installer` run in the same session.
2. **v0.04 commit** — this session's actual fix.

## Lessons / Footgun Taxonomy

Two named footguns ship with v0.04 closed:

- **Per-item DataSet updates in vis-network / vis-data.** Silent (no error), easy to trigger (the naive `forEach(update)` pattern), damage scales with graph size (so small test graphs feel fine and the bug escapes review). Fix: always pass an array to `update()`.
- **"Fix documented, not implemented" skill templates.** The skill's own troubleshooting table correctly described the perf bug and the fix, but the code shipped with the bug. Structural remedy: the Changelog block in the install guide and the on-canvas `v0.04` badge. A future user can now look at a deployed viewer and know immediately which template version they have.

## Verification

User confirmed on test: "I verified it works. Nice job."

## Follow-ups Worth Considering (not done this turn)

- None of the six other downstream graph-viewer copies (`calculus`, `graph-data-modeling-course`, `learning-graphs`, `learning-linux`, `conversational-ai`) have been re-synced to v0.04. Each will show an older version badge (or none at all) until re-installed. A future task could batch-update them, or the user may choose to let natural reinstalls pick it up.
- MOSS's narrower sidebar (200px) is arguably a UX improvement on wide-screen displays but is a separate decision from these bug fixes.
