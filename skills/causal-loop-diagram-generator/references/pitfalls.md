# Pitfalls & Hard-Won Lessons

These are bugs that ate a multi-hour debugging session in the original Winner-Takes-All build. Each one looks obvious in hindsight; none of them are obvious going in. Read this file before changing the renderer or the page integration.

## Footgun #1 — One iframe per diagram on a multi-CLD page

**Symptom:** First 4–5 iframes render, the 6th comes up blank, later ones intermittent. Refresh while scrolled mid-page and the previously-working ones go blank instead.

**Cause:** Both Chrome and Firefox have a per-document rendering ceiling for nested browsing contexts. Around the 5th–6th vis-network instance running in its own iframe, later instances silently fail to paint. No console error, no warning, just blank canvas. Reproducible after fresh browser restart on both engines.

**No amount of patching fixes it.** The original build went through three rounds of attempted fixes — IntersectionObserver lazy loading, a serial load queue, postMessage signaling between iframe and parent, RAF-based dimension polling, ResizeObserver retry loops. *None of them worked.* The limit is in the browser's iframe rendering pipeline, not in the JavaScript timing.

**Solution:** Don't use iframes for inline diagrams. Use `cld-inline.js` to render multiple vis-network instances directly on the article page in a shared JS context. One library load, one document, no per-iframe ceiling. Iframes are still fine for the *fullscreen* viewer (one open at a time, user-initiated).

Three properties make this a textbook footgun:

1. **Silent.** No error in the console; the diagram simply isn't there.
2. **Easy to trigger.** "One iframe per diagram" is the path of least resistance for embedding interactive content in markdown.
3. **Delayed/invisible damage.** It looks fine in development with 3 diagrams. The failure mode appears only when you scale to 6+ on the same page, by which time you've committed to the architecture.

## Footgun #2 — vis-network wipes its container on init

**Symptom:** A title overlay placed inside `#network` in the HTML disappears when the diagram loads.

**Cause:** `new vis.Network(container, data, options)` clears `container.innerHTML` before adding its own canvas. Anything you put inside the container in HTML is gone after init.

**Solution:** Create the overlay div in JavaScript *after* `new vis.Network(...)` returns:

```js
network = new vis.Network(container, {}, options);

const overlay = document.createElement('div');
overlay.id = 'diagram-title-overlay';
overlay.className = 'diagram-title-overlay';
container.appendChild(overlay);
```

The container must be `position: relative` so the absolutely-positioned overlay anchors correctly. See `cld-viewer.js` for the working pattern.

## Footgun #3 — `loading="lazy"` is a hint, not a guarantee

`loading="lazy"` on iframes tells the browser "you may delay this." Browsers vary in how aggressively they pre-fetch — Chrome and Firefox often eagerly load iframes that are within ~1500px of the viewport, regardless of the attribute. When ten iframes all start loading because the browser decided they were "near enough," the connection limit and rendering ceiling both bite.

If you're using iframes anyway (e.g. for the fullscreen viewer), don't rely on `loading="lazy"` to control concurrency. It won't.

## Footgun #4 — `<iframe>.load` event fires too early

The iframe's `load` event fires when its document has finished loading (HTML, linked CSS, linked JS). It does *not* wait for `window.onload` handlers inside the iframe to run, and certainly not for vis-network to finish rendering. So if you build a serial load queue that advances on `iframe.load`, the next iframe starts initializing while the previous one's vis-network is still painting — exactly the race you wanted to avoid.

A `postMessage` from inside the iframe (sent after `network.fit()` completes) is a more reliable signal. But this is a workaround for the underlying iframe ceiling problem (footgun #1) — better to skip iframes entirely.

## Footgun #5 — vis-network's default `zoomView` is unusable on Mac trackpads

The default `interaction.zoomView: true` zooms by ~20% per wheel event. On a Mac trackpad, a single two-finger flick fires 50+ wheel events. The diagram zooms from 1× to 100× before the user can let go.

**Solution:** Disable it (`zoomView: false`) and write a custom wheel handler:
- ~4% scale step per event (`ZOOM_PER_TICK = 0.04`)
- cap per-event delta at ~60 units so a fast flick doesn't compound
- **vertical scroll passes through to the page** — only horizontal scroll (`deltaX`) and pinch (`event.ctrlKey`) trigger zoom
- anchor the zoom on the cursor: the world point under the mouse stays under the mouse

`cld-viewer.js` and `cld-inline.js` both implement this pattern; reuse them rather than reimplementing.

## Footgun #6 — `flex: 1; height: auto` collapses children with `height: 100%`

A child element with `height: 100%` needs an *explicit* height somewhere up the chain. `flex: 1; height: auto` on the parent doesn't establish a percentage reference, so the child computes to 0px and vis-network silently initializes against a 0×0 container. The diagram never renders.

**Solution:** Either use `flex: 1; min-height: 0` on the child (so it fills via flex sizing instead of percentage) or give the container an explicit pixel height. The reference `cld-viewer/main.html` uses the explicit-height approach.

## Footgun #7 — "Save Positions" must use `network.getPositions()`, not the original data

After the user drags nodes, the in-memory `cldData.nodes[i].position` is *not* updated — vis-network tracks position changes internally. Calling `JSON.stringify(cldData)` produces the *original* positions, not the dragged ones.

**Solution:** Call `network.getPositions()` to get the live positions:

```js
const livePositions = network.getPositions(); // { nodeId: {x, y}, ... }

const updated = JSON.parse(JSON.stringify(cldData));
updated.nodes.forEach(n => {
    const p = livePositions[n.id];
    if (p) n.position = { x: Math.round(p.x), y: Math.round(p.y) };
});
updated.loops?.forEach(loop => {
    const p = livePositions['loop_' + loop.id];  // synthetic key prefix
    if (p) loop.position = { x: Math.round(p.x), y: Math.round(p.y) };
});
```

Note the `loop_<id>` key prefix — loop annotation circles are added as synthetic nodes with that namespacing, and you have to remap them back when serializing.

## Footgun #8 — MicroSim iframe border standard is `border: 2px solid blue`

The site-wide CSS rule for `iframe` is:

```css
iframe {
    width: 100%;
    overflow: hidden;
    border: 2px solid blue;
}
```

That harsh blue 2px border is **deliberate** — it's an unmissable visual signal that the framed content is **interactive** (a MicroSim, CLD viewer, or other live element), as opposed to a static image, screenshot, or block quote. Aesthetics are explicitly secondary to the affordance.

**Do not soften this border** in `extra.css` or in inline styles. The same standard applies to the `.cld-inline` div: it also gets `border: 2px solid blue` so users can see at a glance that they can interact with it.

## Footgun #9 — Path math after MkDocs `use_directory_urls`

MkDocs Material defaults to `use_directory_urls: true`, which turns `docs/articles/foo.md` into the URL `/articles/foo/` (a directory, not a file). Relative paths in HTML inside the article need to account for the extra path segment:

- From `/articles/foo/`, `..` is `/articles/`, NOT the site root.
- To reference `/sims/...` from the article, use `../../sims/...`.
- To reference `/articles/cld-inline.js` from the article, use `../cld-inline.js`.

Get this wrong and the diagrams 404. Verify by browsing to the article and watching the network tab.

## Quick mental checklist when adding a CLD page

- [ ] Inline rendering, not iframes (footgun #1)
- [ ] Title overlay created in JS after vis-network init (footgun #2)
- [ ] Custom zoom handler with vertical-scroll-passthrough (footgun #5)
- [ ] Containers have explicit heights or `flex: 1; min-height: 0` (footgun #6)
- [ ] Save Positions uses `network.getPositions()` (footgun #7)
- [ ] `border: 2px solid blue` on `.cld-inline` and iframes (footgun #8)
- [ ] Relative paths account for directory URLs (footgun #9)
