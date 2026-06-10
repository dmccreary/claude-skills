---
name: register-book-analytics
description: >-
  Register an intelligent textbook / MkDocs site with Google Analytics and wire the
  Measurement ID into mkdocs.yml, then build, verify, commit and deploy. Use this skill
  whenever the user wants to "register a book/site with Google Analytics", "add GA to
  mkdocs", "set up analytics for a new book", "get a G- tracking ID into mkdocs.yml", or
  asks to onboard a new MkDocs Material documentation site to Google Analytics 4. Trigger
  even if the user only mentions adding a tracking ID, GA4, a measurement ID, or analytics
  for a docs site built with MkDocs Material.
---

# Register a Book with Google Analytics (MkDocs Material)

This skill registers a new MkDocs Material site as a Google Analytics 4 (GA4) property,
captures the Measurement ID, writes it into `mkdocs.yml`, verifies the tag is injected,
and commits/deploys.

## Inputs to gather first

Read these from the repo and/or confirm with the user:

- **Repo path** – local folder containing `mkdocs.yml` (e.g. `~/Documents/ws/<book>`).
- **Site URL** – usually `site_url:` in `mkdocs.yml` (e.g. `https://dmccreary.github.io/<book>/`).
- **GA settings** (defaults below, override if the user says otherwise):
  - Reporting time zone: **US / Chicago** (GMT-05:00 Chicago Time)
  - Business size: **Small – 1 to 10 employees**
  - Industry category: **Jobs & Education** (GA4 has no literal "Education and Training"
    option; "Jobs & Education" is the correct closest match — use it unless told otherwise)
  - Business objective: **Understand web and/or app traffic** (best fit for a docs site)

Open `mkdocs.yml` and confirm there is no existing `extra.analytics` block before starting.

## Step 1 — Create the GA4 property (Claude in Chrome)

Requires the Claude in Chrome extension connected and the user logged into Google Analytics.

1. Navigate to `https://analytics.google.com/analytics/web/` and wait for it to load.
2. Open **Admin → Create property** (or the "Create property" card on Home). This launches a
   4-step wizard: Property creation → Business details → Business objectives → Data collection.
3. **Property creation:** enter the property **name** (match the book's `site_name`). Change
   the **Reporting time zone** — click the time-zone dropdown, type `Chicago`, select
   "(GMT-05:00) Chicago Time". Leave currency as USD. Click **Next**.
4. **Business details:** open the **Industry category** dropdown, type `Education`, select
   **Jobs & Education**. Select **Small - 1 to 10 employees**. Click **Next**.
5. **Business objectives:** check **Understand web and/or app traffic**. The action button on
   this step is labeled **Create** (not "Next") — click it to create the property.

## Step 2 — Create the Web data stream and capture the Measurement ID

The number shown in the stream list (e.g. `15014865793`) is the **Stream ID, NOT** the
Measurement ID. The Measurement ID (format `G-XXXXXXXXXX`) only appears in the Google tag.

1. On the **Data collection** step choose **Web** as the platform.
2. In "Set up your web stream": set **Website URL** (protocol `https://` + host/path, e.g.
   `dmccreary.github.io/<book>/`) and a **Stream name** (the book name). Leave Enhanced
   measurement on. Click **Create & continue**.
3. The "Set up a Google tag" panel appears. Read the **Measurement ID** from the snippet —
   it appears as `gtag/js?id=G-XXXXXXXXXX` and `gtag('config', 'G-XXXXXXXXXX')`.
4. **Verify the exact characters** by zooming into the code block (don't trust a quick glance;
   `0/O`, `1/I`, `Q/O` are easy to misread). Record the `G-...` value.

## Step 3 — Add the ID to mkdocs.yml

MkDocs Material reads analytics from `extra.analytics`. If an `extra:` block already exists,
**merge** into it rather than adding a second `extra:` key (duplicate top-level keys break YAML).

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
  # ...keep any existing schema/social/etc. keys here...
```

## Step 4 — Build and verify the tag (do this before deploying)

Build to a temporary directory and confirm the ID is injected into the HTML:

```bash
cd <repo>
mkdocs build -q -d /tmp/site_verify        # mkdocs-material must be installed
grep -c "G-XXXXXXXXXX" /tmp/site_verify/index.html   # expect >= 1
grep -o "googletagmanager.com/gtag/js?id=G-XXXXXXXXXX" /tmp/site_verify/index.html
```

A non-zero count confirms Material picked up the analytics config.

## Step 5 — Commit, push, deploy

```bash
cd <repo>
git add mkdocs.yml
git commit -m "Add Google Analytics property G-XXXXXXXXXX to mkdocs.yml"
git push origin main
mkdocs gh-deploy      # builds and pushes the site to the gh-pages branch
```

After deploy, optionally confirm the live tag:
`curl -s https://dmccreary.github.io/<book>/ | grep -o "G-XXXXXXXXXX"`.

## Environment notes / known limitations

These matter when running inside the Cowork sandbox (vs. the user's own terminal):

- **GitHub credentials:** the Cowork Linux sandbox has **no push credentials**. `git push`
  and `mkdocs gh-deploy` (which pushes to `gh-pages`) will fail with
  "could not read Username for https://github.com". When this happens, do the GA registration,
  the `mkdocs.yml` edit, the build-verify, and the local `git commit`, then hand the user the
  exact `git push` / `mkdocs gh-deploy` commands to run in their own terminal.
- **Mount delete restrictions:** the sandbox mount may forbid deleting files. This can (a) break
  `mkdocs build` into the existing `site/` dir (build to a temp dir instead, as in Step 4), and
  (b) leave stale `.git/*.lock` files after a commit. If you see
  `unable to unlink .git/HEAD.lock` / `index.lock`, tell the user to run
  `rm -f .git/HEAD.lock .git/index.lock .git/objects/maintenance.lock` before their next git command.
- **Theme:** verification requires `pip install mkdocs-material` if the sandbox only has base mkdocs.
