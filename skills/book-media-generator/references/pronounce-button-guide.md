# Glossary Pronunciation Guide (ElevenLabs)

Add a verifiable pronunciation recording and accessible audio controls to a
glossary term or term heading. The active route publishes an MP3 and a JSON
provenance sidecar; it does not trust a successful HTTP status by itself.

## When to Use

Use this guide for requests such as:

- "Create a pronunciation for Bryophytes."
- "Add pronunciation audio to the Sphagnum Moss glossary entry."
- "Add pronunciation controls for evapotranspiration in chapter 3."

## Prerequisites

- Set `ELEVENLABS_API_KEY` in the environment. Never hard-code or commit it.
- Use the active generator at
  `scripts/audio/generate-pronunciation.py` inside this skill.
- Work from the textbook repository root so `--output-root` can identify the
  exact tree in which publication is allowed.

## 1. Discover Current Capabilities

Do not treat a remembered model name, voice name, or voice ID as current
inventory. Before the first generation in a project, inspect the primary API:

- `GET /v1/models` for available models and their capabilities.
- `GET /v2/voices` for voices available to the authenticated account.
- [Create speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)
  for the current request body and `output_format` options.
- [Models](https://elevenlabs.io/docs/overview/models) for model-specific
  latency, language, and text normalization behavior.

Confirm that the selected voice ID is present and that the selected model is
available for text-to-speech. The generator defaults to
`eleven_multilingual_v2`, output format `mp3_44100_128`, and the historical
Sarah voice ID `EXAVITQu4vr4xnSDxMaL`; discovery, not the label in this guide,
is the authority.

For a reusable project-specific correction, prefer a versioned pronunciation
dictionary and pass its `pronunciation_dictionary_locators` in an extended
workflow. ElevenLabs documents dictionary versions and model support in its
[pronunciation dictionary guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries).

## 2. Generate and Verify the Artifact

Try the actual term first. Escalate only after listening:

1. Plain term.
2. A readable phonetic rendering if the plain term is wrong.
3. CMU Arpabet through `--ssml` when an exact phoneme correction is needed.

Plain term:

```bash
python3 SCRIPT "Biogeography" \
  --output-root . \
  --output docs/audio/biogeography.mp3
```

Explicit phonetic rendering:

```bash
python3 SCRIPT "Gah-mee-toh-fyte" \
  --output-root . \
  --output docs/audio/gametophyte.mp3
```

CMU Arpabet:

```bash
python3 SCRIPT "evapotranspiration" \
  --ssml "IH0 V AE2 P OW0 T R AE2 N S P ER0 EY1 SH AH0 N" \
  --output-root . \
  --output docs/audio/evapotranspiration.mp3
```

`SCRIPT` is the path to this skill's
`scripts/audio/generate-pronunciation.py`. The generator:

- confines output to `--output-root` and requires an `.mp3` destination;
- converts the term to a single safe filename component when no output is
  supplied;
- requests an explicit `output_format`;
- rejects a non-audio content type and a body without an MP3 signature;
- stages both files beside the destination and uses `os.replace` only after
  validation and durable writes;
- records the request fingerprint, audio SHA-256, model, voice, format,
  byte count, `request-id`, and `x-trace-id` in `FILE.mp3.json`;
- reuses an existing byte-matching artifact without another API call; and
- refuses to replace a non-matching artifact unless `--force` is explicit.

If a run fails, do not rename an error body to `.mp3` or delete the previous
artifact. Diagnose the response and retain the last verified pair.

After generation, inspect the sidecar and listen to the entire clip. A file
existing on disk is not sufficient verification.

## 3. Add Native, CSP-Compatible Controls

Use the browser's native controls. They provide familiar play, pause, seek,
volume, and download behavior without an inline event handler:

```html
<div class="pronunciation" data-pronunciation>
  <audio
    id="audio-bryophytes"
    controls
    preload="metadata"
    aria-label="Pronunciation of Bryophytes"
    src="../audio/bryophytes.mp3">
    <a href="../audio/bryophytes.mp3">Download the Bryophytes pronunciation</a>
  </audio>
  <span class="pronunciation__phonetic">BRY-oh-fytes</span>
  <span
    class="pronunciation__status"
    role="status"
    aria-live="polite">Ready</span>
</div>
```

Copy `assets/pronunciation/pronunciation-controls.js` from this skill to
`docs/javascripts/pronunciation-controls.js`, then load it as an external
script in `mkdocs.yml`:

```yaml
extra_javascript:
  - javascripts/pronunciation-controls.js
```

The controller uses `addEventListener`; it contains no inline click attribute
or other inline script. It reports loading, playback, completion, and media errors in
the live status region. This keeps the markup compatible with a Content
Security Policy that disallows inline script.

Adjust the MP3 URL for the rendered page location. With MkDocs directory
URLs, common mappings are:

| Source file | Rendered page | Audio URL |
|---|---|---|
| `docs/glossary.md` | `/glossary/` | `../audio/TERM.mp3` |
| `docs/appendices/terms.md` | `/appendices/terms/` | `../../audio/TERM.mp3` |
| `docs/chapters/03/index.md` | `/chapters/03/` | `../../audio/TERM.mp3` |

The phonetic text is useful visual confirmation, but it does not replace an
accessible label or an audio fallback link.

## 4. Preview and Verify

Serve the site over HTTP and verify the actual route, not a `file://` copy:

1. The control is visible at desktop and mobile widths.
2. Keyboard focus reaches the native audio element.
3. Play and pause work and the status text changes.
4. Muting and volume changes work.
5. A broken source produces a visible error state.
6. The browser console has no CSP, media, or JavaScript errors.
7. The full clip audibly matches the requested term.

Record the preview URL, MP3 path, sidecar path, and verification result in the
work report.

## Batch Generation

Batch generation is one API request per term unless an artifact and sidecar
already match. Before a batch, report the number of unmatched terms and the
expected request count. Generate into one approved root, then inspect the
failed and changed set before modifying glossary markup.
