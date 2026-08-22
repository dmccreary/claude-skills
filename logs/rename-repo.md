# Repository Rename Session Log

**Date:** August 22, 2026
**Project:** Agent Skills for Intelligent Textbooks (formerly Claude Skills for Intelligent Textbooks)
**Goal:** Rename the GitHub repo `dmccreary/claude-skills` to `dmccreary/ibook-skills` and update every dependent reference

---

## Session Summary

Renamed the repository and swept every reference that derived from the old
name — inside this repo, across ~100 sibling repos under `~/Documents/ws`,
and throughout the machine-level wiring (symlinks, shell profile, hooks).
The work then expanded into three follow-on tasks: renaming the *project*
title to "Agent Skills for Intelligent Textbooks", fixing a stale
`edit_uri` that was silently 404-ing every "Edit this page" link across 61
repos, and renaming three repos' default branch from `master` to `main`.

**Totals:** 6 commits in this repo, 103 sibling repos updated for the name
change (258 files), 56 sibling repos updated for `edit_uri`, 89 symlinks
repointed, 3 default branches renamed.

---

## Phase 0: Scoping

Three ambiguities were resolved with the user before any file was touched,
because each led to materially different work.

| Question | Decision |
|---|---|
| Rename chapter/slide dirs that named the *subject* "Claude Skills"? | **Yes** — full string sweep |
| Rewrite the 22 session transcripts in `logs/`? | **No** — they are a historical record of commands actually run |
| Sweep the ~95 other repos under `ws/`? | **Yes** |

The first decision has a lasting side-effect worth remembering: chapter 9's
directory is now `09-ibook-skills-architecture-development` while its H1 is
still "Claude Skills Architecture and Development", because the prose
teaches Claude Skills as an Anthropic feature. Same for chapter 2 and the
overview deck.

---

## Phase 1: Survey

Initial scope: **231 files, 684 occurrences** in this repo. Categorising the
surrounding context separated genuine repo references (GitHub URLs,
`ws/claude-skills` paths, `BK_HOME` examples) from subject-matter mentions
(chapter directory names, the prose phrase "Claude Skills").

Outside the repo, these would break the moment the directory was renamed:

- 89 symlinks across `~/.claude/skills`, `~/.claude/commands`,
  `~/.local/bin`, `~/.agents/skills`, `~/.codex/skills`,
  `~/.gemini/config/skills`
- `BK_HOME` in `~/.zshrc`
- `~/.claude/CLAUDE.md`, `~/.claude/settings.json`, `.claude/mcp.json`
- Both auto-commit hooks (`auto-commit-claude-skills-stop.sh`,
  `track-claude-skills-edits.sh`)

Two stale git worktrees under `.claude/worktrees/` were pruned first — they
were detached-HEAD copies that would have broken on the parent rename.

---

## Phase 2: GitHub rename

```bash
gh repo rename ibook-skills --repo dmccreary/claude-skills --yes
git remote set-url origin https://github.com/dmccreary/ibook-skills
```

Confirmed `dmccreary/ibook-skills` was unclaimed beforehand. `gh repo rename`
does **not** update the local remote when invoked with `--repo`, so that was
set manually.

---

## Phase 3: In-repo sweep

Renamed via `git mv` (preserving history):

- `docs/chapters/02-getting-started-claude-skills/` → `02-getting-started-ibook-skills/`
- `docs/chapters/09-claude-skills-architecture-development/` → `09-ibook-skills-architecture-development/`
- `docs/slides/claude-skills-overview/` → `ibook-skills-overview/`
- `claude-skills.code-workspace` → `ibook-skills.code-workspace`

Then a string sweep over 209 text files (excluding `.git`, `site/`,
`node_modules`, `logs/`), also renaming the env var `CLAUDE_SKILLS_REPO` →
`IBOOK_SKILLS_REPO`.

Commit `226f8216` — 212 files, 614 insertions, 614 deletions.
`mkdocs build --strict` passed.

---

## Phase 4: Cross-repo sweep

104 repos surveyed. **63 had pre-existing uncommitted work**, several with
100+ dirty files, so the sweep was designed around that constraint:

1. Snapshot each repo's dirty files *before* touching anything
2. Rewrite every hit on disk
3. Stage and commit **only** files that were clean beforehand
4. Leave already-dirty files rewritten but uncommitted

Result: **103 repos committed, 258 files.** 6 files were deliberately left
uncommitted because they already held the user's in-progress work.
`book-dashboard` was the only repo where *every* hit was already dirty, so it
received no commit at all.

Commits were made locally but **not pushed** — pushing ~100 repos is an
outward-facing action left for explicit approval.

---

## Phase 5: Machine wiring and directory rename

Order mattered: the local directory rename had to come **last**, because the
session's working directory lived inside it.

1. `~/.zshrc` — `BK_HOME`
2. `~/.claude/CLAUDE.md`
3. Both hooks — contents *and* filenames
   (`auto-commit-ibook-skills-stop.sh`, `track-ibook-skills-edits.sh`)
4. `~/.claude/settings.json` — hook paths, JSON re-validated
5. `mv claude-skills ibook-skills`
6. Repoint all 89 symlinks

Verified afterwards: `BK_HOME` resolves, `bk-list-skills` runs, all 14 skills
reload.

**15 symlinks remained broken** — verified against commit `fa205dc5` to be
*pre-existing* breakage pointing at skills consolidated into meta-skills long
ago (`concept-classifier`, `story-generator`, `readme-generator`, …), not
caused by the rename.

---

## Phase 6: Follow-on work

### Project title

Renamed to **"Agent Skills for Intelligent Textbooks"**. Chosen because
"Agent Skills" matches the cross-platform `AGENTS.md` convention and the
`~/.agents/skills/` layout the repo already installs into — it carries the
portability point rather than implying Claude exclusivity.

Commits `6748b946` (mkdocs.yml, README.md, docs/index.md) and `f3cd8594`
(about page, slides gallery, overview deck, `book-status.json`, MARP guide).
Genuine attribution to Claude Code and Claude AI was left intact.

### edit_uri: master → main

`edit_uri: 'blob/master/docs'` was pointing at a branch that does not exist,
so every "Edit this page" link 404'd. Found the same bug in **61 other
repos**, of which **58 actually default to `main`**.

Fixed 58 (54 + 2 committed, 5 left uncommitted due to pre-existing changes).

### Default branch renames

Three repos genuinely used `master`: `ai-racing-league`, `dmccreary`,
`robot-faces`. Before renaming, confirmed all three deploy Pages from
`gh-pages`, have zero open PRs, and no workflows referencing `master`.

```bash
gh api -X POST repos/dmccreary/$r/branches/master/rename -f new_name=main
git -C $r fetch origin --prune
git -C $r branch -m master main
git -C $r branch -u origin/main main
git -C $r remote set-head origin -a
```

Ran `dmccreary` as a canary first. All dirty files and unpushed commits
survived (18→18, 56→56).

---

## Gotchas worth remembering

**`rg` is a shell function, not a binary.** The first cross-repo sweep
silently did nothing. `rg` is defined as a zsh wrapper function in `.zshrc`,
so a `bash script.sh` cannot see it — `rg -l` produced no output, every repo
hit the empty-list guard, and the run reported success having changed
nothing. Use `grep -rIl` in scripts, or verify with `command -v`.

**zsh does not word-split unquoted parameters.** `for f in $files` passed the
entire newline-separated list to perl as one filename. Bash would have split
it; zsh does not. Pipe into `while IFS= read -r` instead.

**Bash replacement strings take backslashes literally.** Repointing symlinks
with `${target//ws\/claude-skills/ws\/ibook-skills}` produced
`ws\/ibook-skills` — a literal backslash — breaking all 89 links at once. The
escape is needed in the *pattern*, not the *replacement*. Used `sed` instead.

**shields.io escapes hyphens as `--`.** Badge URLs contained
`dmccreary%2Fclaude--skills`, which never matched a `claude-skills` search.
Two badges rendered the old name while linking to the new repo, surviving the
sweep and its verification. Search for `claude--skills` separately.

**MkDocs composes the homepage `<title>` from front matter *plus*
`site_name`.** Changing only `site_name` produced "Claude Skills for
Intelligent Textbooks - Agent Skills for Intelligent Textbooks".
`docs/index.md` front matter must change too.

**`timeout` is not available on macOS** by default, and the Bash tool caps
foreground commands at 2 minutes. Long sweeps across ~100 repos must run in
the background with progress logging.

---

## GitHub rename redirect: what actually carries over

Verified empirically rather than assumed:

| Old URL | Result |
|---|---|
| `github.com/dmccreary/claude-skills` | **301** → `ibook-skills` |
| `git ls-remote https://github.com/dmccreary/claude-skills` | **works** — returns current refs |
| `dmccreary.github.io/claude-skills/` | **404 — no redirect** |

**GitHub Pages does not inherit the rename redirect.** This matters: the
deployed site still carries six absolute `github.io/claude-skills/…` URLs in
its `canonical`, `og:url`, `og:image` and `twitter:image` tags, all of which
now 404 — so the social preview card is broken until the site is redeployed.
`site_url` is already correct in source; one `mkdocs gh-deploy` fixes it.

**The repo redirect is not permanent.** It survives only until someone
creates a new repo named `dmccreary/claude-skills`. Do not recreate that name
as a stub — it would silently break every old link.

---

## Commits in this repo

```
f3cd8594  Rename remaining title references to Agent Skills for Intelligent Textbooks
73992059  Update TODO.md for the edit_uri sweep and branch renames
6748b946  Rename project to "Agent Skills for Intelligent Textbooks"
5ed06d51  Add TODO.md tracking rename follow-up work
143c29ed  Update project title in README.md          (authored by Dan)
226f8216  Rename repo from claude-skills to ibook-skills
```

---

## Outstanding work

Tracked in detail in [TODO.md](../TODO.md):

1. **`mkdocs gh-deploy`** — the live site predates the rename; six Pages URLs 404
2. **Push ~112 repos** — name-change and `edit_uri` commits, all local
3. **11 files left uncommitted** across 6 repos — they already held in-progress work
4. **15 stale symlinks** — pre-existing, pointing at consolidated-away skills
5. **Two naming side-effects** — `install-ibook-skills.sh` in teaching content,
   and chapter directories disagreeing with their titles
6. The project title still appears in 3 sibling repos (`tracking-ai-course`,
   `raspberry-pi-stem`, `intelligent-textbooks`)

A LinkedIn announcement was published during the session covering the rename
and the portability rationale.
