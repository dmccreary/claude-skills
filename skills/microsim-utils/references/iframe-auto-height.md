# Iframe Auto-Height Guide

**Purpose:** Make embedded MicroSim iframes resize themselves to fit their
content at runtime, eliminating the need to hand-tune `height="..."`
attributes on every chapter page that embeds a sim.

This is a **runtime postMessage protocol**, complementary to the static
build-time `sync-iframe-heights.py` script. The two can coexist — the
static height in markdown becomes the loading-state default, and the
runtime listener overrides it the moment the sim reports its measured
height.

## When to Use This Guide

Use this when:

- A chapter embeds a MicroSim whose final rendered height is hard to
  predict (responsive layouts, dual-panel diagrams, content that depends
  on the longest callout text, etc.).
- You want to add or update the parent-side listener in a project's
  sitewide `docs/js/extra.js`.
- You want to add the child-side reporter to a new MicroSim type
  (p5.js, Mermaid, vis-network, etc.) so it participates in auto-resize.

## How It Works

A two-part protocol:

1. **Child (inside the iframe)** — after the sim has measured its true
   content height, it calls:
   ```js
   window.parent.postMessage(
     { type: 'microsim-resize', height: <pixels> },
     '*'
   );
   ```
2. **Parent (the chapter page)** — a listener in the sitewide
   `docs/js/extra.js` matches the message's `event.source` against each
   `<iframe>` element's `contentWindow` and updates that iframe's
   `style.height` and `height` attribute.

The message type is the literal string `'microsim-resize'`. Both sides
must agree on this string. Do not change it without updating every
participating MicroSim.

## Part 1 — Parent-Side Listener (`docs/js/extra.js`)

Add this block at the **top** of `docs/js/extra.js`, before any
`DOMContentLoaded` handlers. It runs immediately so it doesn't miss any
early `message` events from fast-loading sims.

```js
// ── MicroSim auto-resize ────────────────────────────────────────────────
// Listens for `{ type: 'microsim-resize', height: <px> }` messages posted
// by embedded MicroSim iframes. When a message arrives, find the iframe
// whose contentWindow sent it and resize its height attribute to fit.
// This eliminates the need to hand-tune per-page iframe heights.
window.addEventListener("message", function (event) {
    const data = event.data;
    if (!data || data.type !== "microsim-resize") return;
    if (typeof data.height !== "number" || data.height <= 0) return;

    const iframes = document.querySelectorAll("iframe");
    for (const iframe of iframes) {
        if (iframe.contentWindow === event.source) {
            iframe.style.height = data.height + "px";
            iframe.setAttribute("height", data.height);
            break;
        }
    }
});
```

**Why match on `event.source`?** A page may embed multiple MicroSim
iframes. Comparing `iframe.contentWindow === event.source` is the only
reliable way to identify which iframe sent the message — `src` strings
and `name` attributes are too easy to spoof or duplicate.

**Why both `style.height` and `setAttribute("height", ...)`?** Some
MkDocs themes and plugins read the HTML attribute, others read the
inline style. Setting both keeps the layout stable across reflows.

## Part 2 — Child-Side Reporter

Each MicroSim that wants to opt in needs to call `postMessage` once it
knows its real content height. The exact recipe depends on the library.

### For diagram-overlay MicroSims (already done)

The shared library at `docs/sims/shared-libs/diagram.js` already
implements `reportHeight()` and calls it from `init()`. Any MicroSim
that uses `diagram.js` participates automatically — no per-sim work
required.

The reporter measures the worst-case height by temporarily filling the
infobox with the longest callout's text, reading
`document.body.scrollHeight + 30`, and restoring the infobox before
posting. The `+ 30` is breathing room for the iframe border and a
tiny scroll buffer.

### For p5.js MicroSims

Add this snippet to your sketch, typically at the end of `setup()` or
inside a `draw()`-once-and-flag pattern:

```js
function reportHeightToParent() {
  if (window.self === window.top) return;          // not embedded
  const height = document.body.scrollHeight + 10;  // small breathing room
  window.parent.postMessage(
    { type: 'microsim-resize', height: height },
    '*'
  );
}

// Call once after the canvas and any controls have laid out
function setup() {
  updateCanvasSize();
  // ... createCanvas, createButton, createSlider, etc. ...
  setTimeout(reportHeightToParent, 50);  // wait one frame for layout to settle
}
```

The `setTimeout(..., 50)` is intentional: p5.js controls (`createButton`,
`createSlider`) are appended to the DOM asynchronously, so reading
`scrollHeight` synchronously inside `setup()` may miss them.

### For Mermaid, vis-network, or other libraries

Use the same pattern: after the diagram has finished rendering (often
inside the library's `onload` or `afterRender` callback), measure
`document.body.scrollHeight` and post the message.

```js
mermaid.run().then(() => {
  if (window.self === window.top) return;
  window.parent.postMessage(
    { type: 'microsim-resize', height: document.body.scrollHeight + 10 },
    '*'
  );
});
```

## Loading-State Default

Even with auto-resize, **always set a sensible `height="..."` attribute
on the iframe in markdown.** It controls the layout during the brief
window between page load and the first `postMessage`. A good default
is "the typical fully-rendered height for this sim." When the message
arrives, the listener overwrites it.

```markdown
<iframe src="../../sims/digital-devices-explorer/main.html"
        height="640px" width="100%"
        frameborder="0" scrolling="no"></iframe>
```

## Coexistence with `sync-iframe-heights.py`

These two systems do not conflict:

| System | When it runs | Source of truth | Best for |
|---|---|---|---|
| `sync-iframe-heights.py` | Build / pre-commit | `// CANVAS_HEIGHT:` comment in `.js` | p5.js sims with fixed canvas heights |
| Runtime postMessage | Page load in browser | `document.body.scrollHeight` at runtime | Sims with responsive or content-dependent heights |

If both are configured, the static height becomes the loading-state
default and the runtime listener overrides it once the sim reports.

## Caveats and Things to Watch

1. **One-shot by default.** `reportHeight()` typically fires once at the
   end of init. If your sim's height can change after load (collapse
   panels, responsive breakpoints, dynamic content), call
   `reportHeight()` again from the relevant event handler, or wire up
   a `ResizeObserver` on `document.body` to post on every change.

2. **`'*'` target origin.** The reporter uses `'*'` because intelligent
   textbook projects are typically deployed under a single GitHub Pages
   origin where the parent and the iframe share an origin anyway. If you
   ever embed a sim cross-origin, tighten this to the actual parent
   origin for security.

3. **Sandboxed iframes.** If the embedding `<iframe>` has a `sandbox`
   attribute, make sure it includes `allow-scripts` or `postMessage`
   from the child will be silently dropped.

4. **Don't trust the height blindly.** Validate that
   `typeof data.height === 'number'` and that the value is positive
   before applying it. The example listener above already does this.

5. **Match by `contentWindow`, never by URL.** Several MicroSims may
   share a base path; matching by `event.source === iframe.contentWindow`
   is the only reliable identification.

6. **Fullscreen mode.** When a sim is opened in its own browser tab
   (not inside an iframe), `window.self === window.top` is true and
   the reporter should no-op. All the snippets above check this.

## Quick Checklist for a New Sim

- [ ] Sim's HTML iframe has a sensible default `height` attribute
- [ ] Sim's JS measures `document.body.scrollHeight` after layout settles
- [ ] Sim's JS guards on `window.self === window.top` and bails if not embedded
- [ ] Sim's JS calls `window.parent.postMessage({ type: 'microsim-resize', height }, '*')`
- [ ] The sitewide `docs/js/extra.js` has the listener block at the top (only need to do this once per project)
- [ ] If the sim's height changes after load, `reportHeight()` is called again on the relevant event

## Reference Implementation

A working end-to-end implementation lives in the `digital-citizenship`
project:

- **Listener:** `docs/js/extra.js` (top of file)
- **Reporter:** `docs/sims/shared-libs/diagram.js`, `reportHeight()`
  method (called from `init()`)
- **Embedding example:** any chapter that embeds an interactive-overlay
  MicroSim, e.g., `docs/chapters/01-welcome-to-digital-world/index.md`
  embedding `digital-devices-explorer`
