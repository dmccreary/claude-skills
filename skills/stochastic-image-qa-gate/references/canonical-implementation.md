# Canonical Implementation: Lorignite QA Gate

The pattern this skill captures was built for the Lorignite sticker agent in the shilpiworks codebase. This file distills the implementation into the four critical functions and where each one lives.

Read this when implementing a new gate from scratch and you want a working reference. The scaffold script (`scripts/scaffold-qa-gate.mjs`) generates equivalent boilerplate, but reading the canonical version first makes the scaffolded output understandable.

## File map (in source codebase)

| File | What it owns |
|---|---|
| `lib/mastra/<agent>-steps.js` | `qaCheckSticker_<agent>()` function + `<agent>VisualQAStep` Mastra step + Levenshtein helpers |
| `lib/mastra/<agent>-workflow.js` | Splices the QA step into the workflow chain via a `.map` step that pulls expectedQuote via getStepResult |
| `lib/mastra/agent-runner.js` | Factory threads `imageResult.qaResult` into `publishProduct` |
| `lib/mastra/publish.js` | Accepts `qaResult` opt, sets `isActive: false` on kill, persists to `features.qa_verdict` |

## 1. The QA call function

```js
export async function qaCheckSticker(base64, expectedQuote) {
  const apiKey = process.env.GOOGLE_API_KEY;
  if (!apiKey) throw new Error('GOOGLE_API_KEY not set');

  const systemPrompt = `You are reviewing a [BRAND] sticker before it ships to customers...
[Describe brand spec — fill, type colors, brandmark location, palette]

RUBRIC — evaluate each item independently:
  letterPerfect: Does the rendered text match EXPECTED PHRASE letter-for-letter?
    [Critical: cursive ligatures can hide hallucinated extra letters.]
    Set renderedText to what you actually see on the sticker.

  noDuplicates: Does any word from the phrase appear more than once?

  scriptColorIsLime: Is the cursive/script focal word in lime green (close to #D0E156)?

  brandmarkPresent: Is "[BRAND_NAME]" visible on the sticker?

  paletteClean: Is the palette restricted to [BRAND_PALETTE]? Any blue/teal/gold/neon is a fail.

For any failed item, set "issue" to a one-line description.`;

  const userPrompt = `EXPECTED PHRASE on the sticker (must appear letter-perfect): "${expectedQuote}"
Evaluate the attached sticker image against the rubric and return JSON.`;

  // Retry loop on 429/503 with exponential backoff
  const MAX_ATTEMPTS = 5;
  let res;
  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    res = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          systemInstruction: { parts: [{ text: systemPrompt }] },
          contents: [{ parts: [
            { inlineData: { mimeType: 'image/png', data: base64 } },
            { text: userPrompt },
          ]}],
          generationConfig: {
            responseMimeType: 'application/json',
            responseSchema: QA_RUBRIC_SCHEMA,  // see scripts/scaffold for schema shape
            temperature: 0.1,  // low for consistency
          },
        }),
      },
    );
    if (res.ok) break;
    const retriable = res.status === 429 || res.status === 503;
    if (!retriable || attempt === MAX_ATTEMPTS) {
      throw new Error(`qaCheckSticker: Gemini error ${res.status}`);
    }
    await new Promise(r => setTimeout(r, Math.min(1000 * 2 ** (attempt - 1), 16000)));
  }
  const data = await res.json();
  const rubric = JSON.parse(data.candidates?.[0]?.content?.parts?.[0]?.text);

  return computeSeverity(rubric, expectedQuote);
}
```

## 2. Severity computation (the part that matters)

```js
function computeSeverity(rubric, expectedQuote) {
  const failures = [];
  let severity = 'pass';

  // letterPerfect with Levenshtein softening — defends against cursive OCR false positives
  if (!rubric.letterPerfect?.passes) {
    const rendered = rubric.letterPerfect?.renderedText || '';
    const dist = levenshtein(normalizeForCompare(rendered), normalizeForCompare(expectedQuote));
    if (dist <= 2 && rendered.length > 0) {
      // Likely OCR misread, not a real text-rendering miss. Mark soft.
      failures.push(`text-soft: model OCR'd "${rendered}" vs expected "${expectedQuote}" (Levenshtein ${dist}, likely OCR confusion)`);
      if (severity === 'pass') severity = 'soft';
    } else {
      failures.push(`text spelling: rendered "${rendered}" vs expected "${expectedQuote}" (Levenshtein ${dist})`);
      severity = 'kill';
    }
  }

  if (!rubric.noDuplicates?.passes) {
    failures.push(`duplicate words: ${rubric.noDuplicates.issue}`);
    severity = 'kill';
  }

  if (!rubric.scriptColorIsLime?.passes) {
    failures.push(`script color: ${rubric.scriptColorIsLime.issue}`);
    severity = 'kill';
  }

  if (!rubric.brandmarkPresent?.passes) {
    failures.push(`brandmark missing: ${rubric.brandmarkPresent.issue}`);
    if (severity === 'pass') severity = 'soft';
  }

  if (!rubric.paletteClean?.passes) {
    failures.push(`palette: ${rubric.paletteClean.issue}`);
    if (severity === 'pass') severity = 'soft';
  }

  return { passes: severity === 'pass', severity, failures, raw: rubric };
}
```

## 3. Levenshtein helpers

```js
function normalizeForCompare(s) {
  return (s || '')
    .toLowerCase()
    .replace(/[''""]/g, "'")
    .replace(/[^\w\s']/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function levenshtein(a, b) {
  if (a === b) return 0;
  if (!a) return b.length;
  if (!b) return a.length;
  const prev = new Array(b.length + 1);
  const curr = new Array(b.length + 1);
  for (let j = 0; j <= b.length; j++) prev[j] = j;
  for (let i = 1; i <= a.length; i++) {
    curr[0] = i;
    for (let j = 1; j <= b.length; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      curr[j] = Math.min(curr[j - 1] + 1, prev[j] + 1, prev[j - 1] + cost);
    }
    for (let j = 0; j <= b.length; j++) prev[j] = curr[j];
  }
  return prev[b.length];
}
```

## 4. The Mastra step (does NOT throw on kill)

```js
export const lorigniteVisualQAStep = createStep({
  id: 'lorignite-visual-qa',
  inputSchema: z.object({
    base64: z.string(),
    responseId: z.string(),
    analysis: z.any(),
    textError: z.string().nullable(),
    attempt: z.number(),
    retryFeedbacks: z.array(z.object({ attempt: z.number(), content: z.string() })),
    openaiImageRequests: z.array(z.any()),
    openaiCorrectionRequests: z.array(z.any()),
    expectedQuote: z.string(),
  }),
  outputSchema: z.object({
    base64: z.string(),
    responseId: z.string(),
    analysis: z.any(),
    textError: z.string().nullable(),
    attempt: z.number(),
    retryFeedbacks: z.array(z.object({ attempt: z.number(), content: z.string() })),
    openaiImageRequests: z.array(z.any()),
    openaiCorrectionRequests: z.array(z.any()),
    qaResult: z.any(),
  }),
  execute: async ({ inputData }) => {
    const qa = await qaCheckSticker(inputData.base64, inputData.expectedQuote);

    if (qa.severity === 'kill') {
      // Never throw — soft-kill via isActive=false instead. publishProduct
      // sees qaResult.severity==='kill' and lands the Product inactive,
      // preserving the image + verdict for admin review. False positives
      // are reversible (flip isActive=true).
      console.warn(`Agent QA: KILL → publishing as inactive — ${qa.failures.join('; ')}`);
    } else if (qa.severity === 'soft') {
      console.warn(`Agent QA: SOFT — passing through with flag — ${qa.failures.join('; ')}`);
    } else {
      console.log(`Agent QA: PASS`);
    }

    return {
      base64: inputData.base64,
      responseId: inputData.responseId,
      analysis: inputData.analysis,
      textError: inputData.textError,
      attempt: inputData.attempt,
      retryFeedbacks: inputData.retryFeedbacks,
      openaiImageRequests: inputData.openaiImageRequests,
      openaiCorrectionRequests: inputData.openaiCorrectionRequests,
      qaResult: qa,
    };
  },
});
```

## 5. Workflow splice (.map injects expectedQuote)

```js
export const lorigniteWorkflow = createWorkflow({...})
  .then(lorigniteQuoteStep)
  .then(buildLorigniteImagePromptStep)
  .map(...)
  .then(generateImageStepGemini)
  // Splice in the QA gate. The .map below pulls expectedQuote from the
  // upstream lorignite-quote step (generate-image-gemini doesn't carry
  // it forward) and passes through every field the publish step expects.
  .map(async ({ inputData, getStepResult }) => {
    const quoteOut = getStepResult('lorignite-quote');
    return {
      base64: inputData.base64,
      responseId: inputData.responseId,
      analysis: inputData.analysis,
      textError: inputData.textError,
      attempt: inputData.attempt,
      retryFeedbacks: inputData.retryFeedbacks,
      openaiImageRequests: inputData.openaiImageRequests,
      openaiCorrectionRequests: inputData.openaiCorrectionRequests,
      expectedQuote: quoteOut?.quote || '',
    };
  })
  .then(lorigniteVisualQAStep)
  .commit();
```

## 6. Publish-layer changes

In `agent-runner.js` (the factory):
```js
const published = await publishProduct({
  base64: imageResult.base64,
  analysis,
  type, theme, style, designPrompt, author, contextHint, brand, watermarkText,
  qaResult: imageResult.qaResult,  // ← thread this through
});
```

In `publish.js`:
```js
export async function publishProduct({ base64, analysis, ..., qaResult }) {
  // ...

  if (qaResult) features.qa_verdict = qaResult;

  // QA gate: kill-class verdicts land the product as inactive (soft-kill).
  const initialIsActive = qaResult?.severity === 'kill' ? false : true;

  // ...
  product = await db.product.create({
    data: {
      // ...
      isActive: initialIsActive,
    },
  });
}
```
