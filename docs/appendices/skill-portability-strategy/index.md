# Agent Skill Portability Strategy

## Why This Appendix Exists

The skills in this repository were written for Claude Code. They now also run — with
varying fidelity — in OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot / VS Code, and
a long tail of other agents. That did not happen by accident, and it does not stay
true by accident either.

This appendix is the operating manual for keeping **one skill library** working across
**many agent platforms**. It covers what the standard guarantees, what it does not,
where each platform looks for skills, which frontmatter fields are safe to use, how to
degrade gracefully when a platform lacks a capability, and how to test and validate the
whole library on every commit.

!!! info "The standard this appendix is written against"
    **Agent Skills** — <https://agentskills.io/home>

    Originally developed by Anthropic and released as an open standard, now maintained
    in the open at [github.com/agentskills/agentskills](https://github.com/agentskills/agentskills).
    Everything in this appendix that is labeled "spec" comes from that document. Everything
    else is a vendor extension or an operational recommendation.

---

## 1. The Standard in One Page

A skill is **a folder with a `SKILL.md` file in it**. That is the entire required surface
area.

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + Markdown instructions
├── scripts/          # Optional: executable code the agent can run
├── references/       # Optional: docs loaded on demand
├── assets/           # Optional: templates, schemas, images
└── ...               # Any other files
```

### The Frontmatter Contract

The spec defines exactly **six** fields. This table is the single most important thing in
this appendix — it is the portability contract.

| Field | Required | Constraint | Portability |
|-------|----------|------------|-------------|
| `name` | **Yes** | 1–64 chars, lowercase `a-z0-9-` only, no leading/trailing hyphen, no `--`, **must match the parent directory name** | Universal |
| `description` | **Yes** | 1–1024 chars, non-empty, says *what it does* **and** *when to use it* | Universal |
| `license` | No | Short license name or reference to a bundled license file | Universal (accepted; most clients don't act on it) |
| `compatibility` | No | ≤ 500 chars. Environment requirements — intended product, system packages, network access | Universal (accepted; advisory) |
| `metadata` | No | Map of string keys to string values. Client-specific or org-specific data | Universal (accepted; ignored by the agent) |
| `allowed-tools` | No | Space-separated list of pre-approved tools. **Experimental** — semantics vary by client | Universal syntax, **non-uniform behavior** |

**Any other key is a vendor extension.** Some clients ignore unknown keys; some reject
them with a hard error. See §2.

### Progressive Disclosure — and Its Three Budgets

Every conforming client loads skills in three stages. Each stage has a different cost, and
designing against those costs is what separates a skill that scales to a 14-skill library
from one that doesn't.

| Stage | What loads | When | Budget |
|-------|-----------|------|--------|
| **1. Discovery** | `name` + `description` only | Every session, for *every* installed skill | ~100 tokens per skill; clients cap the aggregate (see §6) |
| **2. Activation** | The full `SKILL.md` body | When the model decides the skill is relevant | Spec recommends **< 5,000 tokens**; keep `SKILL.md` under **500 lines** |
| **3. Execution** | Files in `scripts/`, `references/`, `assets/` | Only when the instructions reach for them | Unbounded, but pay-per-use |

This is why the meta-skill router pattern used in this repository works: `microsim-generator`
pays one description at discovery time, and its sixteen sub-guides in `references/` cost
nothing until a route is chosen.

---

## 2. The Portability Contract: Portable Core vs. Vendor Extension

Every agent that supports Agent Skills reads the six spec fields. Beyond that, each client
has invented its own frontmatter. Understanding which is which is the difference between a
skill that loads everywhere and one that fails to package.

### Claude Code's Extension Fields

Claude Code accepts all six spec fields **plus** a large set of its own. None of these are
portable:

| Extension field | What it does in Claude Code | Elsewhere |
|-----------------|------------------------------|-----------|
| `when_to_use` | Extra trigger phrases, appended to `description` in the listing | Ignored or rejected |
| `model` | Model override for the turn (`sonnet`, `opus`, `inherit`, …) | Ignored or rejected |
| `effort` | Reasoning effort (`low` … `max`) | Ignored or rejected |
| `argument-hint` | Autocomplete hint for `/skill-name` | Cursor/VS Code have their own variants |
| `arguments` | Named positional args for `$name` substitution | Ignored or rejected |
| `disable-model-invocation` | Manual-only skill | **Also supported by Cursor and VS Code** |
| `user-invocable` | Hide from the `/` menu | **Also supported by VS Code** |
| `disallowed-tools` | Remove tools while active | Ignored or rejected |
| `context: fork` / `agent` / `background` | Run the skill in a subagent | VS Code has an experimental `context: fork` |
| `hooks` | Register session hooks | Ignored or rejected |
| `paths` | Glob patterns that gate auto-activation | **Also supported by Cursor** |
| `shell` | `bash` vs `powershell` for inline command injection | Ignored or rejected |

!!! danger "The hard-error rule"
    Claude Code tolerates extension fields. **The distribution paths do not.** Uploading a
    skill to claude.ai, pushing it through the Skills API, or packaging it with
    `package_skill.py` from [anthropics/skills](https://github.com/anthropics/skills)
    validates strictly against the six spec fields and **fails the whole package**:

    ```
    Unexpected key(s) in SKILL.md frontmatter: argument-hint.
    Allowed properties are: allowed-tools, compatibility, description, license, metadata, name
    ```

    This is not a warning you can ignore. One stray `model: sonnet` blocks the upload of an
    otherwise perfect skill. It also blocks the skill from Cowork sessions, cloud sessions,
    and scheduled routines, all of which load skills from your claude.ai account rather than
    from `~/.claude/skills/`.

### The Rule

> **Write the portable core into `SKILL.md`. Push everything vendor-specific either into
> `metadata:` or out of the frontmatter entirely.**

The `metadata:` field exists precisely for this. It is a spec-blessed escape hatch that
every client accepts and no client interprets:

```yaml
---
name: learning-graph-generator
description: Generates a comprehensive learning graph from a course description, including 300-600 concepts with dependencies, taxonomy categorization, and quality validation reports. Use this when the user wants to create a structured knowledge graph for educational content.
license: CC BY-NC 4.0
compatibility: Requires Python 3.10+ with networkx; writes to docs/learning-graph/
metadata:
  ibook.version: "2.1"
  ibook.pipeline-stage: "3"
  ibook.preferred-model: "opus"
---
```

Note `ibook.preferred-model` rather than `model:`. The information survives, the package
validates, and this repository's own tooling can still read it.

!!! tip "Namespace your metadata keys"
    The spec recommends "reasonably unique" key names to avoid collisions. Use a
    reverse-domain or project prefix (`ibook.`, `com.dmccreary.`). Agent Plugins 1.0
    formalizes this same convention for client-specific directories.

---

## 3. Where Skills Live: The Discovery Matrix

A skill that is spec-perfect is still useless if the agent never finds it. Every platform
searches a different set of directories, in a different precedence order.

### Per-Platform Discovery

| Platform | Project scope | User scope | Notes |
|----------|---------------|------------|-------|
| **Claude Code** | `.claude/skills/` (cwd **and every parent up to repo root**); nested `.claude/skills/` load lazily when a file in that subtree is touched | `~/.claude/skills/` | Also plugin skills at `<plugin>/skills/`, namespaced `/plugin:skill`. Precedence: enterprise → personal → project. **Does not read `.agents/skills/`.** |
| **ChatGPT / Codex** | `.agents/skills/` in cwd, parents, and repo root | `$HOME/.agents/skills/` | Plus admin `/etc/codex/skills` and bundled skills. Name conflicts show **both** entries rather than merging |
| **Gemini CLI** | `.gemini/skills/` or `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` | Precedence low→high: built-in → extension → user → workspace. Within a tier, `.agents/skills/` **wins** over `.gemini/skills/` |
| **Cursor** | `.agents/skills/`, `.cursor/skills/`, plus nested project subdirectories (monorepo-friendly) | `~/.agents/skills/`, `~/.cursor/skills/` | Legacy Claude and Codex directories supported for compatibility |
| **VS Code / GitHub Copilot** | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | Extra locations via `chat.agentSkillsLocations`; monorepo parents via `chat.useCustomizationsInParentRepositories` |

### `.agents/skills/` Is the Universal Directory — With One Hole

Four of the five majors read `.agents/skills/` (project) and `~/.agents/skills/` (user)
out of the box. **Claude Code does not.** Its project directory is `.claude/skills/` and
its global directory is `~/.claude/skills/`, and as of this writing there is no setting
that adds the canonical universal path.

That single asymmetry drives the whole installation strategy below.

### Three Single-Source-of-Truth Layouts

#### Layout A — Canonical repo + symlink farm (what this repo does)

Skills live in a git repository. An install script symlinks each skill directory into
every agent's expected location.

```
~/Documents/ws/ibook-skills/skills/     <-- source of truth, version controlled
    ├── book-installer/
    ├── microsim-generator/
    └── ...

~/.claude/skills/microsim-generator  ->  .../ibook-skills/skills/microsim-generator
~/.agents/skills/microsim-generator  ->  .../ibook-skills/skills/microsim-generator
```

**Pros:** one edit updates every agent instantly; git history is authoritative;
`archived/` can be excluded from the loaded set.
**Cons:** symlinks need Developer Mode on Windows; some sandboxed/cloud runners refuse
to traverse symlinks out of the workspace.

#### Layout B — `.agents/skills/` in the repo, one symlink for Claude

Put the skills at the universal path inside the project, then add a *single* symlink
for Claude Code.

```
my-textbook/
├── .agents/skills/          <-- read by Codex, Gemini CLI, Cursor, Copilot
│   └── quiz-generator/
└── .claude/skills  ->  ../.agents/skills
```

**Pros:** one committed directory, four platforms with zero configuration, one
symlink for the fifth. Best choice for per-project skills that ship with a book.
**Cons:** still a symlink; still Windows-sensitive.

#### Layout C — Agent Plugins 1.0 package

Package the library once and let each client install it. See §12.

**Pros:** no symlinks, no per-agent paths, versioned distribution.
**Cons:** the newest option; Claude Code has its own plugin format and was not among
the clients named at the 1.0 launch.

!!! warning "Windows and symlinks"
    Symbolic links on Windows require either Developer Mode or elevated privileges, and
    `git config core.symlinks true`. On WSL the Linux-side symlinks work normally but are
    invisible to Windows-native agent installs. For Windows-first users, prefer Layout C,
    or a copy-on-install script with a `--check` mode that fails CI when the copies drift.

### Making the Install Script Multi-Agent

`scripts/bk-install-skills` currently targets `$HOME/.claude/skills` only. The portable
form is a loop over target roots:

```bash
# Every agent root that should see the library.
# .agents/skills covers Codex, Gemini CLI, Cursor, and Copilot in one shot.
TARGET_DIRS=(
  "$HOME/.claude/skills"     # Claude Code (does not read .agents/skills)
  "$HOME/.agents/skills"     # universal: Codex, Gemini CLI, Cursor, VS Code/Copilot
)

for TARGET_DIR in "${TARGET_DIRS[@]}"; do
  mkdir -p "$TARGET_DIR"
  for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    [ "$skill_name" = "archived" ] && continue
    ln -sfn "${skill_dir%/}" "$TARGET_DIR/$skill_name"
  done
done
```

The existing stale-link cleanup and broken-link audit should run per target root as well.

---

## 4. `CLAUDE.md` vs. `AGENTS.md`

Skills are only half the context an agent needs. The other half is the project instruction
file — and here the ecosystem split in two. Every major agent reads `AGENTS.md`; Claude
Code reads `CLAUDE.md`. They are two names for the same set of instructions.

!!! danger "Claude Code does not read `AGENTS.md` as a fallback"
    This is a widely repeated claim and it is wrong. Claude Code reads `CLAUDE.md`. If you
    want it to see `AGENTS.md`, you must arrange that explicitly using one of the options
    below.

### The Four Options

| Option | Mechanism | Windows-safe | Visible in the file tree | Drift-proof |
|--------|-----------|:------------:|:------------------------:|:-----------:|
| **1. Symbolic link** | `ln -s AGENTS.md CLAUDE.md` | Needs Developer Mode + `core.symlinks` | Shows as a link | Yes |
| **2. Hard link** | `ln AGENTS.md CLAUDE.md` | Works, but git cannot represent it — clones get two independent copies | Looks like a real file | Yes locally, **no** after clone |
| **3. Import directive** | `CLAUDE.md` contains only `@AGENTS.md` | Yes | Yes | Yes |
| **4. Copy** | Two real files kept in sync by hand or by a hook | Yes | Yes | **No** |

**Recommendation: Option 3.** A one-line `CLAUDE.md` is portable, visible, survives
cloning on every OS, and needs no filesystem features:

```markdown
# CLAUDE.md

@AGENTS.md
```

Make `AGENTS.md` the canonical file. Write it in vendor-neutral language — say "the agent",
not "Claude" — so it reads correctly no matter which tool loaded it.

### The Drift Failure Mode Is Real

Option 4 fails quietly and this repository is currently living proof. `CLAUDE.md` and
`AGENTS.md` are two independent files (different inodes), and the `AGENTS.md` copy was
produced by a mechanical find-and-replace of "Claude" → "Codex" that corrupted content
which had nothing to do with vendor naming:

| `CLAUDE.md` says | `AGENTS.md` says | Damage |
|------------------|------------------|--------|
| `claude.ai/code` | `Codex.ai/code` | Fabricated URL |
| `ibook-skills/` | `Codex-skills/` | Wrong repo name in the directory tree |
| `~/.claude/skills/` | `~/.Codex/skills/` | **Wrong install path** — the instruction is now non-executable |
| "300-600 concept learning graphs" | "200-concept learning graphs" | A drifted spec, unrelated to the rename |
| "copied to the AGENTS.md file" | "copied to the AGENTS.md file" | Sentence now says a file is copied to itself |

Any agent that reads `AGENTS.md` is being told to install skills into `~/.Codex/skills/`
and to generate 200 concepts instead of 300–600. Two files, one intent, no enforcement —
this is exactly what Option 3 prevents.

!!! tip "If you must keep two files, enforce it"
    Add a CI check that fails when the vendor-neutral content diverges, or a `Stop` hook
    that regenerates the copy from the canonical file. Never rely on a person remembering.

---

## 5. Invocation Differences

Even when a skill loads everywhere, users trigger it differently. Document all of these in
your README; do not assume the reader is on your platform.

| Platform | Explicit invocation | Automatic invocation | Session pinning |
|----------|--------------------|-----------------------|-----------------|
| **Claude Code** | `/skill-name` | Yes, by description match | — |
| **ChatGPT** | `@skill-name` | Yes | — |
| **Codex CLI** | `$skill-name` | Yes | — |
| **Gemini CLI** | — (model calls `activate_skill`, you approve the prompt) | Yes, with a confirmation showing purpose + directory access | — |
| **Cursor** | `/` menu | Yes | Option+Enter / Alt+Enter pins the skill as a Custom Mode for the conversation |
| **VS Code / Copilot** | `/skill-name`, with free text after it | Yes, unless `disable-model-invocation: true` | — |

Two consequences for skill authors:

1. **Never hard-code the sigil in your instructions.** Write "invoke the
   `microsim-generator` skill", not "run `/microsim-generator`". The former is true
   everywhere; the latter is wrong on four of six platforms.
2. **Gemini CLI's approval prompt is user-facing.** The `description` is not just a routing
   signal there — a human reads it before granting directory access. Descriptions that are
   vague or overreaching get denied.

---

## 6. Description Budget Engineering

Discovery-stage metadata is loaded for *every* skill, *every* session, on *every* platform.
It is the one cost you pay whether or not a skill is ever used, and clients enforce hard
caps on it.

| Client | Cap on discovery metadata | Behavior at the cap |
|--------|---------------------------|---------------------|
| **Codex** | 2% of the model's context window, or **8,000 characters** when the window is unknown | Descriptions are shortened first; excess skills are **omitted with a warning** |
| **Claude Code** | `description` + `when_to_use` truncated at **1,536 characters** per skill | Silent truncation — the tail of your description is simply gone |
| **Spec guidance** | ~100 tokens per skill | — |

### The Two Rules That Follow

**Rule 1 — Front-load the description.** Because truncation happens at the tail, the first
sentence must carry the primary use case. Trailing keyword lists are the first thing lost.

```yaml
# Good: primary use case first, keywords after
description: Generates a glossary from the learning graph's concept list with ISO 11179-compliant
  definitions (precise, concise, non-circular). Use after the learning graph concept list is finalized.

# Bad: the trigger condition is at the end, where truncation eats it
description: A comprehensive tool supporting many workflows for educational content teams who need
  consistent terminology across chapters, quizzes, and FAQs, with support for multiple standards
  including ISO 11179 ... use when generating a glossary.
```

**Rule 2 — Consolidate skills to protect the budget.** This is the real reason the
meta-skill router pattern matters. It is usually explained as a workaround for Claude Code's
30-skill ceiling, but Codex's 8,000-character floor is the tighter and more portable
constraint.

This library's current 14 loaded skills consume:

| Metric | Value |
|--------|-------|
| Total `name` + `description` characters at discovery | **4,083** |
| Codex's conservative floor | 8,000 |
| Headroom | ~49% |
| Largest single description (`microsim-generator`) | 517 chars |
| Smallest (`docx-to-web-publisher`) | 177 chars |

Comfortably inside the budget. The pre-consolidation catalog of 29 skills would have been
near or over it — the refactor described in
[Skill Refactor with Fable 5](../skill-refactor-fable-5.md) bought portability headroom as
a side effect, not just a Claude Code fix.

!!! note "Budget arithmetic to run before adding a skill"
    Target **≤ 350 characters** per description and **≤ 6,000 characters** total across the
    library. That leaves room for the user's own personal skills, the host's bundled skills,
    and any plugin skills — all of which share the same budget.

---

## 7. Capability Tiers: What Still Differs After the Skill Loads

Portability of the *format* is solved. Portability of the *capabilities the instructions
assume* is not. A skill can load perfectly and still produce garbage because the host agent
cannot do what step 4 asks for.

Classify every skill's requirements against these tiers.

### Tier 1 — Universal (assume freely)

Reading and writing files, running shell commands, editing code, searching the repository,
following multi-step Markdown instructions, invoking bundled `scripts/`. Every listed
client does these.

### Tier 2 — Common but not guaranteed (feature-detect)

| Capability | Notes |
|------------|-------|
| Web fetch / web search | Present in most, but sandbox and network policy vary. Gemini CLI and Codex both gate network access |
| Subagent / parallel execution | Claude Code, VS Code (`context: fork`, experimental), OpenHands, Mux. Absent in many CLIs |
| MCP server access | Widespread, but the connected server set is user-specific — never assume a given server exists |
| Long-context reasoning | Context windows differ by an order of magnitude across hosts |

### Tier 3 — Model-dependent and genuinely uneven

This is where most real breakage lives.

**Image understanding.** Claude's 5.x models remain markedly stronger at reading a rendered
screenshot and reasoning about layout — is the legend clipped, is the control panel
overlapping the canvas, is the label unreadable at this size. This capability underpins the
layout-reviewer workflow in
`skills/microsim-utils/references/visual-checklist.md`, which is the quality gate for every
MicroSim in this library. On agents with weaker vision, that skill degrades from "reviews
the screenshot and reports specific defects" to "confirms a file exists."

**Image generation.** Claude has no raster image generation — SVG only, which is
inappropriate for illustration, cover art, and mascot work. Claude Fable produces better
line art but at a token cost that makes it impractical at volume. Other platforms (ChatGPT,
Google Antigravity) have native raster generation. This is the largest capability gap in the
library, and it is handled architecturally rather than in-skill: see
[Delegating Image Generation to an External Agent](../imaging-agent-delegation.md), which
moves the work to a filesystem queue that any agent can service.

**Audio / TTS.** Depends entirely on configured API access (ElevenLabs), not on the host
agent. Genuinely portable, because it is a script calling an HTTP API — see §9.

### The Degradation Ladder

For any capability above Tier 1, write the skill to walk down this ladder rather than
failing:

1. **Declare it.** Use the spec's `compatibility` field so the requirement is visible before
   anything runs:
   ```yaml
   compatibility: Requires an agent with image understanding for the layout review step;
     falls back to a structural check without it. Needs Python 3.10+ and Chrome headless.
   ```
2. **Detect it.** Have the instructions probe for the capability — check for a binary,
   check whether an env var is set, attempt the read and branch on the result.
3. **Substitute.** Offer a lower-fidelity path: a structural check instead of a visual one,
   a placeholder image instead of a generated one, a text table instead of a chart.
4. **Delegate.** Hand the step to an agent that *can* do it, via a filesystem work queue.
5. **Announce and stop.** Emit an explicit, actionable message. Never silently skip a step
   and report success.

!!! warning "Silent degradation is the worst outcome"
    A skill that quietly omits the visual review and reports "done" is more damaging than one
    that refuses to run, because the missing quality gate is discovered by a reader, not by
    the author.

---

## 8. Writing Platform-Neutral Skill Bodies

Frontmatter portability is mechanical. Body portability is editorial. These are the rules
that matter most in practice.

| Do | Don't | Why |
|----|-------|-----|
| "the agent", "the assistant" | "Claude", "Codex" | The same file is read by every vendor's model |
| "invoke the `quiz-generator` skill" | "run `/quiz-generator`" | The invocation sigil differs on every platform (§5) |
| "read the project instruction file (`AGENTS.md` or `CLAUDE.md`)" | "read CLAUDE.md" | Half the ecosystem has no such file |
| "run `scripts/analyze-graph.py`" | "use the Read tool then compute..." | Tool names are not standardized; scripts are (§9) |
| "if a rendering step is unavailable, report which step was skipped" | assume the capability exists | Tier 3 capabilities are uneven (§7) |
| Relative paths from the skill root: `references/p5.md` | Absolute paths: `/Users/dan/...` | Skills are symlinked, copied, and packaged into different roots |
| Reference files one level deep | `references/sub/deep/chain.md` | The spec explicitly warns against deep reference chains |
| POSIX-portable shell, or Python | `sed -i ''` (BSD-only), zsh-isms | Agents run on macOS, Linux, WSL, and Windows |

### Tool Names Are Not Standardized

The spec's `allowed-tools` field takes a space-separated string like
`Bash(git:*) Bash(jq:*) Read` — but those tool *names* are Claude Code's. Another client
may call the same capability `shell`, `terminal`, or `execute`. The field is marked
**experimental** in the spec for exactly this reason.

Practical guidance: use `allowed-tools` for its permission benefit inside Claude Code if you
want it, but **never write a skill body that depends on a tool being named a particular
thing**. Describe the *action* ("read the file", "run the command"), not the *tool*.

### Model-Specific Prompting Doesn't Transfer

Phrasing tuned for one model family — extended-thinking cues, XML tag conventions,
"think step by step" scaffolds calibrated to a specific model's behavior — is a portability
liability. Prefer plain, numbered, imperative procedure. That is the style that survives
translation across model families, and it is also the style that survives a model upgrade
within one family.

---

## 9. Scripts Are the Portability Equalizer

The single most effective portability technique in this library: **when a step must produce
an exact output, make it a script rather than a prompt.**

`python analyze-graph.py learning-graph.csv quality-metrics.md` produces byte-identical
output under Claude, Gemini, Codex, and Cursor. The equivalent instruction — "compute the
quality metrics for this graph and write a report" — produces four different reports with
four different section orders and four different rounding conventions.

| Make it a script when | Keep it a prompt when |
|-----------------------|-----------------------|
| The output is validated (JSON schema, DAG check, quality score) | The output is prose |
| The step is deterministic | The step requires judgment |
| Correctness is checkable | "Correct" is a matter of taste |
| The step runs on every book | The step is one-off |

This is why `learning-graph-generator` ships `analyze-graph.py`, `csv-to-json.py`, and
`taxonomy-distribution.py`, and why six of the fourteen loaded skills carry a `scripts/`
directory. Each script is a portability guarantee.

**Script portability rules:**

- Declare dependencies in `compatibility:` and re-check them at the top of the script.
- Fail loudly with an actionable message; never exit 0 on a partial result.
- Prefer the standard library. Every dependency is a platform that might not have it.
- Use `#!/usr/bin/env python3`, not a hard-coded interpreter path.
- Take input and output paths as arguments. Never assume a working directory.

---

## 10. The Testing Matrix

Portability claims decay. Test them on a schedule.

### Conformance Checklist (per skill)

- [ ] `SKILL.md` exists and has valid YAML frontmatter
- [ ] `name` matches the parent directory name exactly
- [ ] `name` is lowercase alphanumeric + single hyphens, ≤ 64 chars
- [ ] `description` is non-empty, ≤ 1024 chars, and front-loads the primary use case
- [ ] Frontmatter contains **only** the six spec fields (extensions moved to `metadata:`)
- [ ] `SKILL.md` body is under 500 lines
- [ ] All file references are relative and one level deep
- [ ] No vendor names in the body except as explicit capability notes
- [ ] No invocation sigils (`/`, `@`, `$`) in the body
- [ ] `compatibility:` set if the skill needs anything beyond Tier 1
- [ ] Scripts are executable, dependency-checked, and argument-driven

### Platform Matrix (per release)

Track the actual state, not the aspiration:

| Skill | Claude Code | Codex | Gemini CLI | Cursor | Copilot |
|-------|:-----------:|:-----:|:----------:|:------:|:-------:|
| `course-description-analyzer` | Full | Full | Full | Full | Full |
| `learning-graph-generator` | Full | Full | Full | Full | Full |
| `microsim-generator` | Full | Full | Full | Full | Full |
| `microsim-utils` (layout review) | Full | Degraded — weaker vision | Degraded | Degraded | Degraded |
| `book-media-generator` (chapter images) | Delegated — no raster generation | Full | Full | Delegated | Delegated |

**Legend:** *Full* — produces the intended output. *Degraded* — runs, lower fidelity,
announces the shortfall. *Delegated* — hands the step to an external agent.
*Blocked* — cannot run; the skill says so and stops.

Re-run the matrix when a platform ships a major version, when a model family updates, and
before any release that claims cross-platform support.

---

## 11. Validation and CI

### Use the Reference Validator

The standard ships one:

```bash
skills-ref validate ./skills/microsim-generator
```

It checks frontmatter validity and naming conventions against the spec. Source:
[agentskills/agentskills/skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref).

### Add a Portability Lint

`skills-ref` validates the spec. It does not catch the *editorial* portability problems in
§8. This check does, and it is cheap enough to run on every commit:

```bash
#!/bin/bash
# scripts/bk-lint-portability — flag non-portable patterns across the skill library
SPEC_KEYS="name description license compatibility metadata allowed-tools"
fail=0

for f in skills/*/SKILL.md; do
  dir=$(basename "$(dirname "$f")")

  # 1. Frontmatter keys must be spec-only
  keys=$(awk 'NR==1&&/^---/{f=1;next} f&&/^---/{exit} f&&/^[a-zA-Z_-]+:/{sub(/:.*/,""); print}' "$f")
  for k in $keys; do
    case " $SPEC_KEYS " in
      *" $k "*) ;;
      *) echo "NON-SPEC KEY  $dir: '$k' — move to metadata:"; fail=1 ;;
    esac
  done

  # 2. name must match the directory
  nm=$(awk -F': *' '/^name:/{print $2; exit}' "$f")
  [ -n "$nm" ] && [ "$nm" != "$dir" ] && { echo "NAME MISMATCH $dir: name is '$nm'"; fail=1; }

  # 3. description length
  desc=$(awk -F': *' '/^description:/{sub(/^description: */,""); print; exit}' "$f")
  [ ${#desc} -gt 1024 ] && { echo "DESC TOO LONG $dir: ${#desc} chars"; fail=1; }
  [ ${#desc} -gt 350 ]  && echo "DESC BUDGET   $dir: ${#desc} chars (target 350)"

  # 4. body length
  lines=$(wc -l < "$f")
  [ "$lines" -gt 500 ] && echo "BODY LONG     $dir: $lines lines (target 500)"

  # 5. editorial portability
  grep -qE '(^|[^a-zA-Z])/[a-z][a-z0-9-]+ ' "$f" && echo "SIGIL?        $dir: looks like a '/command' reference"
  grep -qiE '\b(claude|codex|gemini|cursor) (should|will|must|can)\b' "$f" \
    && echo "VENDOR VOICE  $dir: addresses a specific vendor"
done

# 6. total discovery budget
total=$(for f in skills/*/SKILL.md; do
  awk 'NR==1&&/^---/{f=1;next} f&&/^---/{exit} f&&/^description:/{sub(/^description: */,""); print}' "$f"
done | wc -c)
echo "Discovery budget: $total chars (Codex floor: 8000)"
[ "$total" -gt 6000 ] && { echo "OVER BUDGET"; fail=1; }

exit $fail
```

Wire it into CI alongside `mkdocs build --strict`.

---

## 12. Packaging and Distribution: Agent Plugins 1.0

Symlinks solve the single-developer case. They do not solve distribution — handing this
library to a colleague, an institution, or a CI runner.

**Agent Plugins 1.0** landed on **6 August 2026**, published by a Technical Steering
Committee with Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel, with
Google joining as a Core Maintainer. It is a vendor-neutral package format that carries
Agent Skills **and** MCP server configuration in one directory.

```
ibook-skills-plugin/
├── plugin.json                  # Required manifest: identity + targeted spec version
├── mcp.json                     # Optional: MCP servers (stdio, Streamable HTTP, HTTP+SSE)
├── skills/
│   ├── learning-graph-generator/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── references/
│   └── microsim-generator/
│       └── SKILL.md
└── com.example.client/          # Client-specific extensions, reverse-domain namespaced
    └── hooks/
```

The reverse-domain namespace is the same discipline recommended for `metadata:` keys in §2:
**client-specific behavior lives in a clearly-marked side channel, and the portable core
stays clean.**

Clients supporting it at launch: ChatGPT, Codex, Cursor, GitHub Copilot, Kiro, and VS Code.
Normative details live in
[agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec).

!!! note "What this means for this library"
    A plugin build is the right eventual answer for distributing `ibook-skills` to other
    educators — it removes the symlink step, the Windows caveat, and the "which directory
    does my agent use" question in one move. Claude Code was not among the launch clients
    and has its own plugin format, so a dual build (Agent Plugins package + Claude Code
    plugin) is the realistic near-term target. Both can be generated from the same
    `skills/` directory, which is precisely why keeping that directory spec-clean matters.

---

## 13. Security and Trust

Portability cuts both ways: a format that any agent can load is a format that any agent can
be *attacked* through. The ecosystem's own assessment is blunt — distribution is solved,
quality and security are not.

A skill is executable instructions plus, frequently, executable scripts. Treat an installed
skill with the same scrutiny as an installed dependency.

- **Read `SKILL.md` and every script before installing a third-party skill.** There is no
  sandbox between a skill's instructions and your agent's tool permissions.
- **Pin to a commit, not a branch.** A skill that was safe at install time can change under
  you if it is symlinked to a moving target.
- **Watch `allowed-tools`.** Its purpose is to *pre-approve* tools — the field silently
  reduces the number of confirmation prompts a user sees. A skill requesting broad
  pre-approval deserves a close reading.
- **Prefer skills that declare `compatibility`.** Requiring network access is legitimate;
  requiring it without saying so is a smell.
- **Scope `metadata:` honestly.** It is free-form and unvalidated; do not put secrets in it.
- **Note what Gemini CLI gets right.** Its activation flow shows the user the skill's
  purpose and the directory access it wants, and requires approval. That is the right
  default, and it is worth writing descriptions that survive that scrutiny.

For a library distributed to educators — this one included — the security posture is part
of the product. Publish the license (`license:` is a spec field for a reason), publish the
repository, and keep the skills readable.

---

## 14. Portability Audit of This Repository

Applying everything above to `ibook-skills` as it stands today.

### Findings

| # | Finding | Severity | Detail |
|---|---------|:--------:|--------|
| 1 | **`model:` in 10 of 14 `SKILL.md` files** | High | A Claude Code extension, not a spec field. Blocks claude.ai upload, Skills API, and `package_skill.py` with a hard `Unexpected key(s)` error — and therefore blocks Cowork sessions, cloud sessions, and routines |
| 2 | **`AGENTS.md` has drifted from `CLAUDE.md`** | High | Separate inodes, mechanical find-and-replace damage: `~/.Codex/skills/`, `Codex.ai/code`, `Codex-skills/`, and a spec drift from "300-600 concepts" to "200-concept". Agents reading `AGENTS.md` get non-executable instructions |
| 3 | **`bk-install-skills` targets `~/.claude/skills` only** | Medium | Four of five major platforms read `~/.agents/skills`, which is never populated. Non-Claude use requires manual setup |
| 4 | **Empty `license:` in `book-chapter-generator`** | Low | Present but blank. Either populate it (the other nine use CC BY-NC 4.0) or remove the key |
| 5 | **Discovery budget is healthy** | — | 4,083 chars for name + description across 14 skills; ~49% headroom against Codex's 8,000-char floor |
| 6 | **`archived/` correctly excluded** | — | 19 archived skills are skipped by the installer. Correct: they would consume discovery budget on every platform for no benefit |
| 7 | **Six skills ship `scripts/`** | — | The strongest portability asset in the library (§9) |

### Recommended Actions, In Order

1. **Move `model:` into `metadata:`.** Fourteen files, one mechanical edit:
   ```yaml
   metadata:
     ibook.preferred-model: "sonnet"
   ```
   This unblocks every distribution path at once and costs nothing in Claude Code, which
   reads the skill from disk regardless.
2. **Collapse `CLAUDE.md` to `@AGENTS.md`** and repair `AGENTS.md` from the current
   `CLAUDE.md` content, rewriting vendor-specific phrasing by hand rather than by
   find-and-replace.
3. **Add `~/.agents/skills` to `bk-install-skills`** as a second target root (§3).
4. **Add `scripts/bk-lint-portability`** (§11) and run it in CI next to
   `mkdocs build --strict`.
5. **Fill in the platform matrix** (§10) with tested results rather than assumptions, and
   date it.
6. **Add `compatibility:` to the skills that need it** — anything invoking Chrome headless,
   Python with third-party packages, ElevenLabs, or image understanding.
7. **Evaluate an Agent Plugins 1.0 build** (§12) as the distribution path for other
   educators.

---

## 15. Reference Links

**The standard**

- [Agent Skills — Overview](https://agentskills.io/home)
- [Agent Skills — Specification](https://agentskills.io/specification)
- [Agent Skills — Client Showcase](https://agentskills.io/clients)
- [Agent Skills — Best Practices for Skill Creators](https://agentskills.io/skill-creation/best-practices)
- [Agent Skills — Optimizing Skill Descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- [agentskills/agentskills on GitHub](https://github.com/agentskills/agentskills)

**Packaging**

- [Agent Plugins](https://agent-plugins.org/)
- [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec)

**Per-platform skill documentation**

- [Claude Code](https://code.claude.com/docs/en/skills)
- [Claude Platform / Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [ChatGPT & Codex](https://developers.openai.com/codex/skills/)
- [Gemini CLI](https://geminicli.com/docs/cli/skills/)
- [Cursor](https://cursor.com/docs/context/skills)
- [VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

**Related appendices**

- [Skill Refactor with Fable 5](../skill-refactor-fable-5.md) — how 29 skills became 14
- [Delegating Image Generation to an External Agent](../imaging-agent-delegation.md) — the
  Tier 3 capability gap, solved architecturally
