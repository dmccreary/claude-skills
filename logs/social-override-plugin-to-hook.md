# Social Override: Migrate from Python Plugin to MkDocs Hook

**Date:** 2026-04-16
**Author:** Dan McCreary (with Claude)
**Status:** `digital-citizenship` migrated and verified. Install script rewritten. 21 other projects still on the broken pattern — migration plan below.

## TL;DR

The `social_override` plugin was installed as a Python **entry-point package**
across many MkDocs textbook projects. Because every project used the same
distribution name (`social_override`) and the same top-level module name
(`plugins`), installing the plugin editable (`pip install -e .`) in multiple
projects caused them to silently steal each other's plugin code at import time.
Whichever project's editable finder landed first in `sys.meta_path` "won" the
`plugins.social_override` import for every build — regardless of which project
was actually running `mkdocs build`.

Symptom: social media previews (LinkedIn / Twitter / Slack / iMessage) did not
show the intended `cover.png` image; instead they showed the auto-generated
Material social card or nothing at all.

Fix: drop the entry-point-plugin mechanism, use MkDocs `hooks:` instead. Hooks
are loaded by **file path**, so there is no namespace collision across
projects. Each project owns its own copy of the hook file, independently.

## Root-cause diagnosis (done in `digital-citizenship`)

1. `mkdocs build --verbose` showed only `Running 'page_context' event from
   plugin 'social_override'` — never `post_page`. But the local file defined
   both hooks. That meant the **local file wasn't the file being loaded**.
2. `print()` and module-level `open('/tmp/debug.log', 'w')` statements added
   to the local plugin file never executed during a build. Hard proof the
   file wasn't imported.
3. `importlib.metadata.entry_points(group='mkdocs.plugins')` returned **two**
   entries named `social_override`, from two different distributions:
   - `social_override` v0.1 → editable install pointing at
     `/Users/dan/Documents/ws/fluid-power-systems/plugins`
   - `mkdocs-social-override` v1.0.0 → editable install pointing at
     `/Users/dan/Documents/ws/economics-course/plugins`
4. `economics-course`'s `plugins/social_override.py` is a completely different
   implementation — it only has `on_page_context` (no `on_post_page`) and it
   mutates `page.meta['image']` instead of rewriting the emitted `og:image`
   HTML tag. That's the code that was actually running during every
   `mkdocs build` in `digital-citizenship`.
5. `mkdocs` is a console-script entry point, so its Python process does **not**
   have CWD on `sys.path`. The local `plugins/` directory therefore loses to
   the editable-install meta-path finders in `site-packages`.

The old plugin file in `digital-citizenship` also had a second, latent bug:
the Twitter regex looked for `name="twitter:image"` but Material 9.x emits
`property="twitter:image"`, so even if the correct plugin code had been
running, the Twitter tag would never have been rewritten.

## Changes made to `digital-citizenship`

**`mkdocs.yml`** — removed the old plugin entry and added a top-level hooks
block:

```diff
 plugins:
   - search
   - glightbox
   - social
-  - social_override
+
+hooks:
+  - plugins/social_override.py
```

**`plugins/social_override.py`** — rewritten as a hook module (top-level
functions, no `BasePlugin` subclass, no `get_plugin()` factory). Also fixed
the Twitter regex to match `property="twitter:image"` (and still accept
`name="twitter:image"` for forward-compatibility). Final contents:

```python
"""MkDocs hook that replaces the social plugin's auto-generated og:image
and twitter:image meta tags with a custom image URL from a page's
`image:` frontmatter field.

Loaded via the `hooks:` entry in mkdocs.yml, not as a plugin — this
avoids collisions with other projects that also install a package
called `social_override` or a top-level module called `plugins`.
"""

import re


def on_page_context(context, page, config, **kwargs):
    """Stash the custom image path on the page for the post_page hook."""
    if page.meta and 'image' in page.meta:
        page.custom_image = page.meta['image']
    return context


def on_post_page(html, page, config, **kwargs):
    """Replace the social plugin's generated og:image / twitter:image
    tags with the page's custom cover image URL."""
    if not hasattr(page, 'custom_image'):
        return html

    site_url = config['site_url'].rstrip('/')
    image_path = '/' + page.custom_image.lstrip('/')
    full_image_url = site_url + image_path

    og_pattern = re.compile(r'<meta\s+property="og:image"[^>]*?>')
    for tag in og_pattern.findall(html):
        if '/assets/images/social/' in tag:
            new_tag = f'<meta property="og:image" content="{full_image_url}">'
            html = html.replace(tag, new_tag)

    twitter_pattern = re.compile(
        r'<meta\s+(?:property|name)="twitter:image"[^>]*?>'
    )
    for tag in twitter_pattern.findall(html):
        if '/assets/images/social/' in tag:
            attr = 'property' if 'property=' in tag else 'name'
            new_tag = f'<meta {attr}="twitter:image" content="{full_image_url}">'
            html = html.replace(tag, new_tag)

    return html
```

**Deleted from the project root** (no longer used by the hooks mechanism):

- `setup.py`
- `social_override.egg-info/`
- `plugins/__init__.py`
- `plugins/__pycache__/`

**Uninstalled** the editable package:

```bash
pip uninstall -y social_override
```

**Story index frontmatter cleanup** (related, fixed in the same session): all
15 story `index.md` files under `docs/stories/` had three bad frontmatter
lines each: two malformed YAML keys (`og:image:` and `twitter:image:` — dead
weight, no plugin reads them) and a `social:\n  cards: false` block that
disabled card generation for those pages. The `social:` block was the actual
reason stories had no previews even when the plugin *was* working. Removed
all three lines from every story; kept the `image:` field, which is what
the hook reads.

### Verification

Rebuilt with `mkdocs build`. Verified in `site/`:

| Page type | URL in `<meta property="og:image">` | Expected? |
|---|---|---|
| `site/index.html` (cover) | `…/digital-citizenship/img/cover.png` | ✅ custom |
| `site/stories/avas-quiet-courage/index.html` | `…/stories/avas-quiet-courage/cover.png` | ✅ custom |
| `site/chapters/01-…/index.html` (no `image:` field) | `…/assets/images/social/chapters/01-…/index.png` | ✅ fallback to auto-generated card |

All 15 stories and the cover page now emit both `og:image` and `twitter:image`
tags pointing to real cover images. Pages without an `image:` frontmatter
field fall through to Material's auto-generated social card as expected.

## Changes made to the install script

**`~/Documents/ws/claude-skills/scripts/bk-install-social-override-plugin`**

The old script created `plugins/__init__.py`, `plugins/social_override.py`
(class-based, with the broken twitter regex), and `setup.py`, then ran
`pip install -e .`. That's exactly how the cross-project collision got seeded
in the first place.

The rewritten script:

1. **Writes only `plugins/social_override.py`** with the corrected,
   module-level hook code (no `BasePlugin` class, no `get_plugin()` factory,
   no `__init__.py`).
2. **Ships the Twitter regex fix** so previews actually work on Twitter/X.
3. **Detects and removes legacy artifacts** before writing the hook file —
   if it finds an old `setup.py` mentioning `social_override`,
   `social_override.egg-info/`, a `plugins/__init__.py` with
   `SocialOverridePlugin`, or a pip-installed `social_override` package, it
   removes them. This way running the new script over an old install cleans
   up the mess automatically.
4. **Does NOT run `pip install -e .`** anymore. There is no package to
   install.
5. **Prints corrected next-steps**: add a **top-level** `hooks:` block in
   `mkdocs.yml` (not under `plugins:`), with a big warning about that exact
   confusion, and a `grep` command to verify the output. Also explicitly
   notes that pages without an `image:` frontmatter field fall through to
   the default Material card — so the change is backwards-compatible with
   pages that never set a custom image.

Executable bit preserved (`chmod +x`).

## Migration plan for other textbooks under `~/Documents/ws/`

A scan on 2026-04-16 found three categories of projects still on the old
pattern:

### Category A — old plugin entry + local plugin file (18 projects)

These have `- social_override` in `mkdocs.yml` AND a local
`plugins/social_override.py`. Most also have `setup.py` and
`social_override.egg-info/`.

| Project | Twitter regex bug present? | Plugin variant |
|---|---|---|
| `biology` | Yes | original |
| `calculus` | Yes | original |
| `chemistry` | Yes | original |
| `claude-skills` | Yes | original |
| `ecology` | Yes | original |
| `economics-course` | N/A | alternate (meta-only, no tag replace) |
| `fluid-power-systems` | Yes | original |
| `functions` | Yes | original |
| `intelligent-textbooks` | Yes | original |
| `intro-to-graph` | Yes | original |
| `intro-to-physics-course` | Yes | original |
| `microsims` | Yes | original |
| `moving-rainbow` | Yes | original |
| `personal-finance` | Yes | original |
| `signal-processing` | Yes | original |
| `systems-thinking` | Yes | original |
| `tracking-ai-course` | Yes | original |
| `us-geography` | N/A | alternate (meta-only, no tag replace) |

**Important:** projects with the **alternate** variant (`economics-course`,
`us-geography`) probably never had working previews at all — that variant
only rewrites `page.meta['image']`; it does not replace the emitted meta
tag the Material social plugin generates. Migration still fixes these, but
the "before" behavior is different.

### Category B — plugin entry but NO local plugin file (3 projects)

These are already silently broken — they reference `- social_override` in
`mkdocs.yml` but have no local plugin file, so at build time they depend on
whichever sibling project's editable install happens to own the
`plugins.social_override` name. Since `economics-course` currently holds
that name (the only remaining editable install of this family after the
`digital-citizenship` cleanup), they get the alternate variant — which
doesn't work.

- `geometry-course`
- `it-management-graph`
- `quantum-computing`

### Category C — commented out (safe to ignore)

- `circuits` has `# - social_override` in `mkdocs.yml`. No action needed.

### Migration recipe (per project)

For each Category A and Category B project, run the following:

```bash
cd ~/Documents/ws/<project>
bk-install-social-override-plugin
```

The rewritten installer handles removal of legacy artifacts automatically.
It will:

1. `pip uninstall -y social_override` if still installed in this venv
2. Remove `setup.py` if it mentions `social_override`
3. Remove `social_override.egg-info/`
4. Remove `plugins/__init__.py` if it references `SocialOverridePlugin`
5. Write the new hook file at `plugins/social_override.py`

After the installer runs, edit the project's `mkdocs.yml` manually (the
script does not edit it) to swap the plugin entry for a hook entry:

```diff
 plugins:
   - search
   - social
-  - social_override

+hooks:
+  - plugins/social_override.py
```

Then verify:

```bash
mkdocs build
grep 'og:image" content' site/index.html
```

The output should point to your custom cover image (if the page has an
`image:` frontmatter field) or to `/assets/images/social/...` (Material's
generated card) for pages that don't.

### Also clean up the stray editable install

After all projects are migrated, uninstall the last cross-project editable
package:

```bash
pip uninstall -y mkdocs-social-override
```

This is the `economics-course` editable install still hooked into site-packages
(`/Users/dan/miniconda3/envs/mkdocs/lib/python3.11/site-packages/__editable___mkdocs_social_override_1_0_0_finder.py`).
Once removed, nothing outside each project's own repo can interfere with
its hook code.

### Suggested migration order

Start with projects where social previews are most visible (published
sites, actively shared):

1. **Highest-value publishable books** — any with active social sharing
2. **The "alternate variant" projects** (`economics-course`, `us-geography`)
   which likely never had working previews
3. **Category B silent-breakage projects** (`geometry-course`,
   `it-management-graph`, `quantum-computing`)
4. **Remaining Category A projects** in whatever order

All 21 projects can be migrated safely in any order — the hook is
per-project, and the legacy-artifact cleanup in the installer is
idempotent.

### Per-project verification checklist

For each migrated project:

- [ ] `plugins/social_override.py` exists and contains module-level
      `on_page_context` / `on_post_page` functions (no class)
- [ ] `setup.py`, `social_override.egg-info/`, `plugins/__init__.py` all gone
- [ ] `pip show social_override` returns nothing
- [ ] `mkdocs.yml` has a top-level `hooks:` block listing
      `plugins/social_override.py`
- [ ] `mkdocs.yml` no longer has `- social_override` under `plugins:`
- [ ] `mkdocs build` succeeds
- [ ] `grep 'og:image" content' site/index.html` shows the cover image URL
      (if the cover page has an `image:` frontmatter field)
- [ ] One random page **with** an `image:` field rewrites to the custom URL
- [ ] One random page **without** an `image:` field falls back to
      `/assets/images/social/...` (Material's default card)

## Why this approach

- **Hooks are per-project by design.** A file path in `mkdocs.yml` cannot
  collide with another project's file path.
- **No pip installs means no site-packages pollution.** Each project is
  self-contained.
- **The hook file is the same across every project**, so it can be updated
  in one place (the installer script) and redistributed by re-running the
  installer.
- **Backwards-compatible behavior.** Pages without `image:` frontmatter
  continue to get Material's auto-generated social card — nothing changes
  for them.

## Related fix — story frontmatter in `digital-citizenship`

Before the plugin-vs-hook issue was diagnosed, a separate bug was fixed in
`digital-citizenship/docs/stories/`: 14 of the 15 story `index.md` files
had a `social:\n  cards: false` block in their YAML frontmatter. That block
disables Material's social plugin from generating cards for those pages
entirely, so there were no `og:image` tags in the rendered HTML at all —
which also meant `social_override` had nothing to rewrite. That issue was
fixed first (removing the block from all 14 stories), but previews still
didn't work afterwards, which is what led to uncovering the deeper
plugin-collision problem described above.

Story-generator skill follow-up: the template used by the story-generator
skill still produces the bad `og:image:` / `twitter:image:` / `social:
cards: false` frontmatter block. Anyone generating new stories with that
skill will re-introduce the issue for those pages. Worth updating the
skill template to emit only the single `image:` field.

## Migration execution results — 2026-04-16

The migration plan was executed across all 21 affected projects in a single
session. Per-project workflow:

1. `cd` into the project, `git status --short` to check working state
2. `git pull` (skipped gracefully when uncommitted work blocked it)
3. `bk-install-social-override-plugin` — auto-cleaned old `setup.py`,
   `social_override.egg-info/`, `plugins/__init__.py`, and
   `pip uninstall social_override` when present, then wrote the new
   hook file
4. Manually edited `mkdocs.yml`: removed `- social_override` from the
   `plugins:` list and added a top-level `hooks:` block with
   `- plugins/social_override.py`
5. `rm -rf plugins/__pycache__`
6. `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/opt/cairo/lib mkdocs build`
7. `grep 'og:image" content' site/index.html` — verified the rewritten tag

### Results

**20 projects verified successfully**: every build emitted an `og:image`
meta tag with the expected image URL.

| Project | `site/index.html` `og:image` value | Notes |
|---|---|---|
| biology | `…/biology/img/cover.png` | ✅ |
| calculus | `…/calculus/img/cover.png` | ✅ |
| chemistry | `…/chemistry/img/cover.png` | ✅ |
| claude-skills | `…/claude-skills/img/cover.png` | ✅ |
| ecology | `…/ecology/img/cover.png` | ✅ |
| economics-course | `…/economics-course/assets/images/social/index.png` | ✅ fallback — no `image:` in index frontmatter, hook correctly leaves the auto-generated card in place |
| fluid-power-systems | `…/fluid-power-systems/img/cover.jpg` | ✅ |
| functions | `…/functions/img/cover.png` | ✅ |
| intelligent-textbooks | `…/intelligent-textbooks/img/cover-social-media-preview.png` | ✅ |
| intro-to-graph | `…/intro-to-graph/img/cover-social-media.png` | ✅ |
| intro-to-physics-course | `…/intro-to-physics-course/img/cover.png` | ✅ |
| microsims | `…/microsims/img/cover.png` | ✅ |
| moving-rainbow | `…/moving-rainbow/img/cover.png` | ✅ |
| personal-finance | `…/personal-finance/img/cover-landscape.png` | ✅ |
| signal-processing | `…/signal-processing/img/cover-social-media.jpg` | ✅ |
| systems-thinking | `…/systems-thinking/img/cover-wide-small.jpg` | ✅ |
| tracking-ai-course | `…/tracking-ai-course/img/cover.png` | ✅ |
| us-geography | `…/us-geography/img/logo.png` | ✅ hook works. Also has a pre-existing `docs/overrides/main.html` template that emits a second, relative-path `og:image` tag — unrelated to this migration, but worth cleaning up separately since social scrapers may pick the first match |
| it-management-graph | `…/it-management-graph/img/cover.png` | ✅ |
| quantum-computing | `…/quantum-computing/img/cover.png` | ✅ |

**1 project blocked (not by the migration itself):**

- **geometry-course** — `mkdocs.yml` has an unresolved git merge conflict
  at lines 22–27 (`<<<<<<< HEAD` … `>>>>>>> 105046b`) that pre-dates this
  session. The migration steps themselves completed:
  hook file written at `plugins/social_override.py`, `- social_override`
  replaced with `hooks:` block, bad frontmatter cleaned from `docs/index.md`.
  The build fails on the merge conflict only. A manual conflict resolution
  is required before `mkdocs build` can run.

### Final state verification

After the run:

```text
=== Still using old '- social_override' plugin entry ===
(empty — zero projects)

=== Now using hooks ===
Count: 22
(21 migrated + digital-citizenship already on hooks)

=== Editable social_override / mkdocs-social-override installs ===
(empty — zero installs)
```

The cross-project entry-point collision is fully dismantled.

### Collateral fixes made during the run

These were not part of the original plan but were discovered and fixed
because they were blocking verification:

1. **Bad homepage frontmatter fixed in 7 projects.** The same
   `social:\n  cards: false` + malformed `og:image:` / `twitter:image:`
   YAML keys that blocked `digital-citizenship`'s story pages were also
   present on homepage `docs/index.md` files. Cleaned up in:
   - `intelligent-textbooks/docs/index.md`
   - `intro-to-physics-course/docs/index.md`
   - `signal-processing/docs/index.md`
   - `systems-thinking/docs/index.md`
   - `tracking-ai-course/docs/index.md`
   - `geometry-course/docs/index.md`

   (The 7th was `digital-citizenship/docs/stories/*` in the original session.)

   **Still carrying the problem but not cleaned up during this run**:
   `circuits/docs/index.md` — wasn't in the migration set because it has
   `# - social_override` commented out in `mkdocs.yml`. Build-breaking
   severity is low there since no hook is expected, but the bad frontmatter
   is still dead weight and should be cleaned when touched.

2. **`mkdocs-exclude` installed** via `pip install mkdocs-exclude` because
   `signal-processing/mkdocs.yml` references the `- exclude:` plugin but
   it wasn't in the environment. Pre-existing issue — the project wasn't
   building cleanly before this session either. Not a migration-caused
   problem.

3. **`mkdocs-social-override` 1.0.0 editable package uninstalled** early
   in the run (during `economics-course` migration). This was the last
   remaining cross-project editable install left over from the old
   pattern and it was still pinned in site-packages pointing at
   `economics-course/plugins/`. Removing it immediately ensured the
   remaining migrations couldn't accidentally re-use it.

4. **`mkdocs_social_override.egg-info/` directory** (underscored variant)
   removed from `economics-course`. The installer script only looks for
   `social_override.egg-info/` (dashed), so it missed the underscored
   variant that `economics-course`'s `setup.py` had generated. Manual
   cleanup. **Installer script improvement candidate**: also match the
   underscored variant.

### Notes on `cairo`

Every `mkdocs build` in this run had to be prefixed with:

```bash
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/opt/cairo/lib
```

Without this, `cairosvg` fails to load `libcairo.2.dylib` from the
Homebrew install location, which makes Material's social plugin silently
skip card generation. The result: no `og:image` tags in the HTML, and the
hook has nothing to rewrite. Worth persisting this in `~/.zshrc`:

```bash
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/opt/cairo/lib
```

Or switching to a conda-forge channel that wires the dylib up natively.

### Per-project follow-ups the user needs to do

1. **Resolve the merge conflict in `geometry-course/mkdocs.yml`**
   (lines 22–27). Once resolved, the migration is already in place — just
   run `mkdocs build` to verify.
2. **Commit each project's changes individually.** Most projects had
   pre-existing uncommitted work mixed with the migration changes. Review
   each `git status` carefully before committing — the migration touched:
   - `mkdocs.yml` (plugin → hook swap)
   - `plugins/social_override.py` (new contents)
   - `docs/index.md` (for the 6 projects with bad homepage frontmatter)
   - Deletions: `setup.py`, `social_override.egg-info/`,
     `plugins/__init__.py`
3. **Persist `DYLD_FALLBACK_LIBRARY_PATH`** in your shell config so the
   `social` plugin works by default.
4. **Update the `story-generator` skill** to stop emitting bad frontmatter
   for new stories.
5. **Test with https://www.opengraph.xyz/** once each project is
   pushed/rebuilt on GitHub Pages.

### Installer script improvement candidate

During the run, two edge cases came up that the installer could handle
automatically:

1. **Match `mkdocs_social_override.egg-info/`** (with underscore) in
   addition to `social_override.egg-info/`. Different `setup.py` name
   conventions across projects generated both variants.
2. **Also uninstall `mkdocs-social-override`** (the alternate
   distribution name) in addition to `social_override`. Some projects
   used that name in their `setup.py`.

Worth adding to `bk-install-social-override-plugin` in a follow-up
edit so future runs don't leave those artifacts behind.
