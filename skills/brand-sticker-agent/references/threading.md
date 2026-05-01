# Threading: Shared Infrastructure for Multi-Brand

This file documents what gets touched in shared code (vs. forked per brand) when adding a brand sticker agent. Read this once before adding the FIRST brand to a codebase that doesn't yet have brand isolation. Skip if the shared infra is already in place.

## What's shared across all brands

Five shared files take additive changes to support brand isolation. After the first brand is added, every subsequent brand uses these unchanged.

### `frontend/lib/mastra/agent-runner.js` (factory)

Adds two optional config options + threads `qaResult` through:

```js
export function createAgentRunner(config) {
  const {
    type, theme, defaultStyle, workflowName, workflow, quoteStepId,
    brand,           // NEW: persisted to features.brand
    watermarkText,   // NEW: edge watermark text override
    requiredTags,
    // ...
  } = config;

  return async function runAgent({ ... }) {
    // ...
    const published = await publishProduct({
      base64: imageResult.base64,
      analysis,
      type, theme: resolvedTheme, style, designPrompt, author, contextHint,
      brand,                              // NEW: thread through
      watermarkText,                      // NEW
      qaResult: imageResult.qaResult,     // NEW (if QA gate is wired)
    });
    // ...
  };
}
```

### `frontend/lib/mastra/publish.js`

Accepts new options and routes them:

```js
export async function publishProduct({
  base64, analysis, type, theme, style, designPrompt, author, contextHint,
  brand, watermarkText, qaResult,   // NEW
}) {
  // ...
  const buffer = await applyWatermark(rawBuffer, watermarkText);  // NEW: pass watermarkText

  // ...
  if (brand) features.brand = brand;             // NEW
  if (qaResult) features.qa_verdict = qaResult;  // NEW

  // QA-killed products land inactive (preserves evidence)
  const initialIsActive = qaResult?.severity === 'kill' ? false : true;

  // ... db.product.create({ data: { ..., isActive: initialIsActive } });
}
```

### `frontend/lib/mastra/watermark.js`

Accepts the watermark text as a parameter, defaults to the original constant:

```js
const DEFAULT_WATERMARK_TEXT = '© shilpiworks.com';

export async function applyWatermark(pngBuffer, watermarkText = DEFAULT_WATERMARK_TEXT) {
  // ... renders watermarkText along the bottom contour
}
```

### `frontend/lib/mastra/constants.js`

`FORBIDDEN_TAGS` set: add `<brand>` and `<brand> sticker` so the catalog metadata generator doesn't auto-tag products with the brand name (already redundant via `features.brand`).

### `frontend/app/api/telegram/run-agent/agents.js`

One line per brand in the lazy-import map:

```js
'<brand>': () => import('@/lib/mastra/<brand>.js').then(m => m.run<Brand>Agent),
```

## What's forked per brand

These files are brand-specific. Each new brand gets its own copy:

| Path | What |
|---|---|
| `frontend/lib/mastra/data/<brand>-quotes.js` | Categorized seed pool |
| `frontend/lib/mastra/anchors/<brand>/*.png` | Reference images for NB2 |
| `frontend/lib/mastra/<brand>-steps.js` | Mastra steps + helpers |
| `frontend/lib/mastra/<brand>-workflow.js` | Workflow chain |
| `frontend/lib/mastra/<brand>.js` | `createAgentRunner` config |
| `frontend/app/api/agent/<brand>/route.js` | HTTP endpoint |
| `frontend/scripts/trigger-<brand>.js` | Manual trigger |
| `frontend/scripts/batch-<brand>.mjs` | Batch runner |
| `frontend/app/<brand>/page.js` | Brand-themed storefront |
| `brands/<brand>/` (optional) | Brand-kit archival |

## Storefront filtering

The brand's collection page filters by `features.brand`:

```js
async function getBrandProducts() {
  const products = await prisma.product.findMany({
    where: { isActive: true },          // respects QA-kill soft-kill
    orderBy: { createdAt: 'desc' },
  });
  return products
    .map(p => ({ ...p, features: p.features ? JSON.parse(p.features) : null }))
    .filter(p => p.features?.brand === '<brand>');
}
```

Note `isActive: true` — QA-killed products land inactive and don't show on `/<brand>`. The verdict still persists in `features.qa_verdict` for admin review.

If the codebase's `Product.features` Prisma column is stringified JSON (most shilpiworks-style codebases), you can't use Prisma path queries — filter in JS as above. If it's native `Json`, you can use:

```js
where: {
  isActive: true,
  features: { path: ['brand'], equals: '<brand>' },
}
```

## Cron registration (optional, after brand is validated)

Once the brand owner approves the sticker output, add a cron entry to `vercel.json`:

```json
{
  "crons": [
    {
      "path": "/api/agent/<brand>",
      "schedule": "0 14 * * *"
    }
  ]
}
```

Don't add the cron in the same PR that introduces the agent. Ship the agent → manually trigger a starter batch → review with the brand owner → THEN add cron. This prevents bad output from auto-shipping while the brand is still tuning.

## Don't fork what's shared

Tempting to fork the agent-runner factory or publishProduct per brand "for safety". Don't. The shared infra is the multiplier — the more brands share it, the more each fix benefits everyone.

If a brand legitimately needs different infra (e.g. different image model, different DB schema), that's a sign the brand belongs in a different codebase entirely, not a fork inside this one.

## Verifying after wiring

After scaffolding a new brand and customizing the per-brand files:

1. `node frontend/scripts/trigger-<brand>.js` — produces one sticker
2. Check the response JSON for `productId` and `imageUrl`
3. Visit the Blob URL — verify the sticker looks brand-correct
4. Open `/<brand>` in the dev server — verify the sticker shows up
5. Check Prisma: the row exists with `features.brand === '<brand>'` and `isActive === true` (assuming QA passed)

If any step fails, trace through which of the 9 forked files is wrong. The shared infra rarely needs touching after the first brand.
