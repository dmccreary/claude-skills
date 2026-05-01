---
name: stochastic-image-qa-gate
description: Adds a post-generation visual quality-assurance gate to image-generation pipelines (Mastra workflows, NB2/Gemini Nano Banana 2, DALL-E, etc). Use this skill whenever the user asks to add a visual QA gate, validate image output before publish, do post-generation QA for an image agent, build a QA gate for a sticker or branded image agent, set up stochastic image quality checks, create a vision-LLM image validator, catch image generation misses or duplicates or misspellings, prevent broken images from reaching production, or add rubric-based image QA. Also triggers when discussing how to defend against false positives in image-quality checks, soft-kill / inactive flags for QA-failed outputs, or Levenshtein softening for cursive-script OCR. The pattern: after image gen, send the rendered image back to a vision LLM with a structured rubric, compute severity deterministically from the rubric JSON in code (never let the model decide severity), soft-kill via isActive=false instead of throwing — preserving evidence for human review. Originally extracted from the Lorignite sticker agent in shilpiworks.
---

# Stochastic Image QA Gate

A post-generation quality-assurance gate for image-generation agents. Catches the failure modes that prompt tweaking can't fix because they're stochastic in the underlying image model: misspellings (especially in cursive script), palette violations, duplicated words, missing brand elements.

## When this applies

The pipeline must:
- Generate images via a stochastic model (NB2, DALL-E, Imagen, etc.)
- Have a clear "expected output" spec for each generation (a quote that must render letter-perfect, a brand palette, required elements like a wordmark)
- Persist outputs to a database (or another store with an "active/inactive" flag)

If the pipeline writes images directly to disk with no DB record, soft-kill via `isActive=false` won't work. Fall back to writing a sidecar `<image>.qa.json` file and skipping flagged images in downstream processing.

## Why a gate at all

Three classes of failure that prompt tweaking won't fix because they're stochastic in the underlying image model:

1. **Text hallucinations in cursive script.** Pointed cursive with thin upstrokes and ligatures is hard for image models to letter-form correctly. "learned" can render as "leariyned". No prompt rewording fully eliminates this.
2. **Palette spec misses.** When a prompt says "the focal word must be lime green #D0E156", the model honors it ~85–95% of the time. The miss rate stays nonzero.
3. **Element duplication.** When a prompt asks for a focal-word treatment + a brand mark, the model occasionally renders the focal word twice — once styled, once stripped.

A QA gate catches all three by re-reading the rendered image with a vision LLM and a structured rubric.

## The four pieces

A complete gate has four parts. Build all four — without all of them, the soft-kill semantics break.

### 1. Rubric design

Choose 3–6 rubric items. Each must be:
- **Independently checkable from the image alone** — the model needs only the PNG and the spec to score it
- **Severity-tagged** — KILL-class (unshippable miss) or SOFT-class (degraded but readable)

Typical KILL items: `letterPerfect`, `noDuplicates`, `paletteCore` (e.g. brand-focal color is correct).

Typical SOFT items: `brandmarkPresent`, `paletteClean` (no off-brand colors leaked in), `compositionBalanced`.

See [references/rubric-design.md](references/rubric-design.md) for the full design framework + item catalog + false-positive defenses.

### 2. Vision-LLM call

Send the generated PNG to Gemini Flash (or another vision-capable model) with the rubric as the system prompt and a JSON response schema. Get back per-item `{ passes: bool, issue?: string }`.

**Severity is computed in code from the JSON.** Never ask the model "is this a kill?" — that's where false positives concentrate. The model judges per-item booleans; your function buckets the booleans into pass / soft / kill.

For text-rendering checks, soften with Levenshtein distance: if the model claims the rendered text mismatches the expected text, but the OCR'd output is within 2 edits (lowercased, punct-stripped), downgrade to SOFT instead of KILL. Cursive OCR misreads its own rendering ~5–10% of the time; this guard recovers those false positives without losing real misses (3+ edits).

See [references/canonical-implementation.md](references/canonical-implementation.md) for the full Lorignite source distilled into the four critical functions.

### 3. Mastra workflow step

Wrap the QA call in a `createStep` named `<agent>-visual-qa`. Insert it AFTER the image-gen step in the workflow. It needs:
- Expected spec as input (typically pull via `getStepResult('<quote-step-id>')` since the upstream image-gen step doesn't carry it forward)
- Every field the downstream publish step expects, passed through unchanged (base64, analysis, attempt, retry feedbacks, etc.)
- An additional `qaResult` field carrying the verdict

**The step must NEVER throw on KILL.** Throwing aborts the workflow → no DB row → image bytes lost → no false-positive recovery. Always return successfully with `qaResult` attached. The publish layer reads severity downstream.

### 4. Publish-layer threading

Three small changes to the publish path:
- The agent-runner factory (or whatever invokes `publishProduct`) extracts `imageResult.qaResult` and threads it through
- `publishProduct`'s signature accepts a new `qaResult` option
- DB write: when `qaResult?.severity === 'kill'`, set `isActive: false`. Always persist `qaResult` to a `features.qa_verdict` JSON field for review.

The product/sticker row lands in the DB either way. Storefront filters on `isActive=true` and the gate's verdict is preserved for admin review. False-positive recovery = flipping `isActive=true` on a single row.

See [references/threading.md](references/threading.md) for the exact source patches for the shilpiworks-style codebase pattern.

## Implementation

The scaffold script generates the boilerplate Mastra step + QA function for a new agent:

```bash
node ~/.claude/skills/stochastic-image-qa-gate/scripts/scaffold-qa-gate.mjs \
  --agent <agent-name> \
  --quote-step <upstream-quote-step-id> \
  --output <path/to/output-file.js>
```

It writes a single JavaScript file with:
- `qaCheckSticker_<agent>` function — the vision-LLM call with placeholder rubric items
- `<agent>VisualQAStep` Mastra step (id: `<agent>-visual-qa`) — passes through to publish, never throws
- `levenshtein` + `normalizeForCompare` helpers
- A header comment listing the workflow + publish wiring needed

After running the scaffold, customize the rubric items in the generated function for the agent's brand spec, then wire into the workflow per [references/threading.md](references/threading.md).

## Common mistakes

- **Throwing on KILL.** Loses the image, the verdict, and any recovery path. Always soft-kill via `isActive=false`.
- **Letting the model decide severity.** Models are inconsistent at "is this a kill or soft?". Compute in code from per-item booleans.
- **No Levenshtein guard on letter-perfect.** Cursive script will produce a steady stream of false-positive kills. Add the guard.
- **Forgetting to thread `qaResult` through the factory.** The QA step's output reaches `result.result` in Mastra, but the factory must explicitly pull `imageResult.qaResult` and pass it to `publishProduct` — it isn't automatic.
- **Putting agent-specific rubrics in the skill.** Per-agent rubrics live in the agent's QA function, not in the skill. The skill provides the structure; rubrics are content.
- **Stringified vs JSON Prisma column.** If `features` is `String` (JSON-stringified), the publish step must `JSON.stringify` the qaResult before write. If it's `Json`, pass through directly.

## Verifying the gate after wiring

Fire one agent run via the trigger script. Verify:
1. The agent run completes with `status='success'` even if QA killed (the run succeeds; the product is just inactive)
2. The Product row exists with `isActive: false` and `features.qa_verdict` populated
3. The storefront page (filtered by isActive) does NOT show the killed product
4. The Vercel/agent logs show `Agent (<agent> QA): KILL → publishing as inactive` with the rubric reasons

Pass: the gate is wired correctly. Fail: trace which of the four pieces is missing.

## False-positive monitoring (after first 10–20 runs)

Once the gate has fired some KILLs in production, look at the inactive products in admin:
- For each, judge: was the verdict correct (real miss, kill confirmed)? Or false positive (sticker is actually fine, override to active)?
- Track the false-positive rate. If > 30%, revisit rubric thresholds — the gate is too strict.
- If 0%, it's possibly too lenient — check that real misses are being caught.

A healthy gate kills ~10–25% of runs with a ~5–15% false-positive rate. The trade is preserving evidence for cheap human override vs. shipping bad output to the brand.
