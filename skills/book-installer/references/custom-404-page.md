---
name: custom-404-page
description: Adds a custom 404 error page with the project's learning mascot to an MkDocs Material intelligent textbook. Uses the theme override system with a static HTML template.
---

# Custom 404 Page with Mascot

This guide adds a friendly, branded 404 error page that displays the project's learning mascot when visitors land on a missing page. Instead of the default "404 - Not found" text, students see the mascot's warning pose with an encouraging message.

## What This Guide Creates

1. **`overrides/404.html`** — A Jinja2 template that extends the Material theme's base layout
2. **mkdocs.yml updates** — `custom_dir` and `static_templates` configuration

## Prerequisites

- Existing MkDocs Material project
- A learning mascot configured with images in `docs/img/mascot/` (use `learning-mascot.md` first if needed)
- The mascot must have a `warning.png` pose (or another appropriate pose image)

## Important: Why Not 404.md?

MkDocs does **not** support `.md` files as 404 pages. The 404 page is a static fallback served by the web server, not part of the content build pipeline. You **must** use a `.html` file in the theme overrides directory.

## Workflow

### Step 1: Gather Project Information

Read the project's `mkdocs.yml` and `CLAUDE.md` to determine:

1. **Repository name** — from `site_url` or `repo_url` in mkdocs.yml (needed for absolute image paths)
2. **Mascot name** — from CLAUDE.md mascot section
3. **Mascot warning image** — typically `docs/img/mascot/warning.png`
4. **Custom message** — default: "Sorry — that page is under construction. Please check back later!"

Extract the repo name (the path segment after the domain):

```python
# From site_url: https://dmccreary.github.io/my-book/
# repo_name = "my-book"
```

### Step 2: Check for Existing Overrides Directory

```bash
ls overrides/ 2>/dev/null || echo "MISSING"
```

If the `overrides/` directory already exists, check whether a `404.html` already exists there. If so, confirm with the user before overwriting.

### Step 3: Create the Overrides Directory

```bash
mkdir -p overrides
```

### Step 4: Create 404.html

Create `overrides/404.html` using this template. Replace the variables:

- `{REPO_NAME}` — the repository/project name from the site URL path
- `{MASCOT_NAME}` — the mascot character's name
- `{MASCOT_IMAGE}` — the mascot pose to use (typically `warning.png`)
- `{MESSAGE}` — the friendly message to display

```html
{% extends "base.html" %}

{% block content %}
<div style="text-align: center; padding: 3rem 1rem;">
  <img src="/{REPO_NAME}/img/mascot/{MASCOT_IMAGE}" alt="{MASCOT_NAME} warning" style="width: 150px; margin-bottom: 1rem;">
  <h1>404 — Page Not Found</h1>
  <p style="font-size: 1.2rem;">{MESSAGE}</p>
  <p style="margin-top: 1.5rem;"><a href="/{REPO_NAME}/" style="font-size: 1.1rem;">&larr; Return to Home</a></p>
</div>
{% endblock %}
```

**Example** for a bioinformatics book with Olli the Octopus:

```html
{% extends "base.html" %}

{% block content %}
<div style="text-align: center; padding: 3rem 1rem;">
  <img src="/bioinformatics/img/mascot/warning.png" alt="Olli warning" style="width: 150px; margin-bottom: 1rem;">
  <h1>404 — Page Not Found</h1>
  <p style="font-size: 1.2rem;">Sorry — that page is under construction. Please check back later!</p>
  <p style="margin-top: 1.5rem;"><a href="/bioinformatics/" style="font-size: 1.1rem;">&larr; Return to Home</a></p>
</div>
{% endblock %}
```

**Example** for a biology book with Gregor the Tree Frog:

```html
{% extends "base.html" %}

{% block content %}
<div style="text-align: center; padding: 3rem 1rem;">
  <img src="/biology/img/mascot/warning.png" alt="Gregor warning" style="width: 150px; margin-bottom: 1rem;">
  <h1>404 — Page Not Found</h1>
  <p style="font-size: 1.2rem;">Ribbit! This page seems to have hopped away. Please check back later!</p>
  <p style="margin-top: 1.5rem;"><a href="/biology/" style="font-size: 1.1rem;">&larr; Return to Home</a></p>
</div>
{% endblock %}
```

### Step 5: Update mkdocs.yml

Add `custom_dir` and `static_templates` to the `theme:` section. If `custom_dir` already exists, just add `404.html` to the `static_templates` list.

**If no custom_dir exists yet:**

```yaml
theme:
  name: material
  custom_dir: overrides
  static_templates:
    - 404.html
  # ... rest of theme config
```

**If custom_dir already exists:**

Just add `static_templates` if missing:

```yaml
theme:
  name: material
  custom_dir: overrides
  static_templates:
    - 404.html
  # ... rest of existing config
```

**Important:** `custom_dir` must appear before other theme settings like `logo`, `favicon`, `palette`, etc. Place it immediately after `name: material`.

### Step 6: Verify

1. Rebuild or let mkdocs serve pick up the changes
2. Navigate to a nonexistent URL, e.g., `http://127.0.0.1:8000/{REPO_NAME}/this-page-does-not-exist/`
3. Verify:
   - [ ] Mascot image appears centered on the page
   - [ ] "404 — Page Not Found" heading is visible
   - [ ] Custom message is displayed
   - [ ] "Return to Home" link works
   - [ ] Site header, sidebar, and footer are intact (inherited from base.html)

### Step 7: Report to User

```
Custom 404 page installed!

Files created:
  - overrides/404.html (mascot: {MASCOT_NAME}, pose: {MASCOT_IMAGE})

Updated:
  - mkdocs.yml (added custom_dir and static_templates)

Test by visiting any nonexistent URL on your dev server.
```

## Customization Options

### Different Mascot Poses

The `warning.png` pose is recommended for 404 pages, but other poses work too:

| Pose | When to Use |
|------|-------------|
| `warning.png` | Default — signals something is wrong (recommended) |
| `encouraging.png` | Softer tone — "We're still building this!" |
| `thinking.png` | Playful — "Hmm, I can't find that page..." |
| `neutral.png` | Professional — no emotional framing |

### Custom Messages by Mascot Personality

Tailor the message to match the mascot's established voice:

- **Olli the Octopus** (bioinformatics): "Sorry — that page is under construction. Please check back later!"
- **Gregor the Tree Frog** (biology): "Ribbit! This page seems to have hopped away. Please check back later!"
- **Generic**: "This page doesn't exist yet. It may be under construction — please check back soon!"

### Adding a Search Suggestion

For a more helpful 404 page, you can add a search link:

```html
<p style="margin-top: 1rem;">
  Try searching for what you need: <a href="/{REPO_NAME}/search/">Search</a>
</p>
```

## Troubleshooting

### Mascot Image Not Showing

The image path must be **absolute** starting from the site root (e.g., `/bioinformatics/img/mascot/warning.png`), not relative. This is because the 404 page can be served from any URL depth.

### 404 Page Shows Default Instead of Custom

- Verify `custom_dir: overrides` is in the `theme:` section of mkdocs.yml
- Verify `static_templates: [404.html]` is listed
- Verify the file is at `overrides/404.html` (not `docs/404.html` or `overrides/404.md`)
- Restart mkdocs serve after changing mkdocs.yml

### Site Navigation Missing on 404 Page

The template must extend `base.html` with `{% extends "base.html" %}`. This inherits the full Material theme layout including header, sidebar, and footer.
