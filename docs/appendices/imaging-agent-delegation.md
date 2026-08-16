# Delegating Image Generation to an External Agent

*A case study in handing work to a tool you cannot drive — and getting it back verified.*

## The Capability Gap

Claude Code can write prose, code, SVG, and p5.js sketches. It cannot generate a raster illustration. An intelligent textbook needs plenty of them: chapter headers, cover art, mascot poses, and — most demanding of all — the annotation-free background images that interactive infographic overlays are drawn on top of.

The tools that *do* generate those images live outside the harness. ChatGPT's desktop app, Google Antigravity, Midjourney, and every other image model sit on the far side of a boundary Claude Code cannot reach across. There is no MCP server for "make me a picture of a breadboard."

This appendix documents a working solution built for the [Beginning Electronics](https://github.com/dmccreary/beginning-electronics) textbook: a filesystem work queue that lets any external image agent discover tasks, work them, and signal completion back to Claude — with automated acceptance checks so bad output does not silently reach the book.

The reference implementation lives at `image-tasks/` in that repository. Everything below generalizes to any intelligent textbook project.

## The Finding That Shaped Everything Else

The two tools in play had wildly different capability profiles, and that difference turned out to be the whole design problem.

| Tool | Filesystem | Shell | Realistic mode of participation |
|---|---|---|---|
| **Google Antigravity** | Yes | Yes | Fully agentic — reads the queue, claims a task, writes the file, all unattended |
| **ChatGPT desktop** | No (sandboxed) | No | **Human courier** — you paste a prompt, it returns an image, you save the file |

The temptation is to build two integrations. That is the wrong instinct. An agentic tool and a human dragging a PNG out of a chat window have exactly one capability in common:

> **Something can save a file to a path.**

So that became the entire protocol.

### The filename is the message

> Save the finished image to `image-tasks/inbox/<task-id>.png`

Nothing else is required. No form, no JSON sidecar, no commit, no API call, no metadata to remember. The task ID *is* the filename, so the drop carries its own routing information.

This single decision is what makes the system work across such different tools. A fully autonomous agent and a distracted human get the same instruction, and neither needs an adapter. Everything downstream — validation, receipt-writing, notification, compression, installation into the repo — keys off that one file appearing.

**The general principle:** when designing a handoff to a tool you cannot drive, find the least-capable participant you intend to support and make *their* minimum action the entire contract. Building for the capable tool first and bolting on a fallback produces two code paths that drift apart.

## Directory Layout

```
image-tasks/
  README.md      # the agent-facing contract — point external tools here
  QUEUE.md       # generated dashboard, human-readable at a glance
  bin/igq        # the CLI
  tasks/*.md     # one task = YAML accept-criteria + markdown prompt
  inbox/         # THE DROP ZONE
  receipts/      # per-delivery JSON check results
  archive/       # previous versions, rollback safety
```

The queue lives at the repository root, **not** under `docs/`. Anything under `docs/` gets published by MkDocs, and a work queue is not book content.

`README.md` is the most important file. It is written *to the external agent*, not to the human maintainer — the opening line is "You are an image-generation agent," and it states the one rule before anything else. When you point ChatGPT or Antigravity at this system, you point it at that file.

## The Task Specification

Each task is a single markdown file: YAML frontmatter for the machine, body for the prompt.

```yaml
---
id: rgb-led-breadboard-circuit
title: RGB LED breadboard wiring diagram
status: open            # open | claimed | delivered | accepted | rejected
priority: 1
output: docs/kits/rgb-led/rgb-circuit.png   # where accept installs it
prompt_file: docs/img/mascot/image-prompts.md#2-welcome-pose   # optional
accept:
  format: png
  width: 1200           # or min_width / min_height
  height: 900
  aspect: "4:3"
  max_kb: 500
  alpha: required       # required | forbidden | any
  transparent_corners: true
  trim_border_px: 4
  no_text: true         # flags for human review; not machine-checkable
---

Everything below the frontmatter is the prompt, verbatim.
```

Two design notes worth stealing:

**`output:` makes acceptance mechanical.** The task declares where the image belongs, so installing it is not a judgment call at accept time. This also means the queue can report exactly which book pages are still waiting on art.

**`prompt_file:` indexes rather than duplicates.** This was a direct response to what the survey found (below): the project already had good image prompts scattered across three different conventions. A task can point at an existing prompt file and an optional heading anchor, and the CLI inlines that section into the brief. The agent still receives one self-contained block; the prompt keeps living where it already lived. **Do not migrate existing prompts into a new format — index them.**

## What the Survey Found

Before building anything, it is worth auditing what a project already has. The audit of Beginning Electronics turned up more than expected, and several findings changed the design.

**Prompts already existed in three separate conventions.** A single big `docs/img/cover-image-prompt.md`, a multi-pose `docs/img/mascot/image-prompts.md` explicitly written so that "any single one" could be pasted into an image tool, and a per-simulation `docs/sims/{id}/image-prompt.md` mandated by the microsim-generator skill. All three were good. None knew about the others. This is what motivated `prompt_file:` indirection.

**Provenance was already being lost.** Of ten interactive-overlay MicroSims, all ten had their background image — but only **two** had an `image-prompt.md`. The other eight had an image nobody could regenerate, revise, or restyle, because the prompt that produced it existed only in some past chat window. This is the quiet failure mode of ad-hoc image generation, and it is not visible until you need a variant.

> **The prompt is a source artifact. Commit it next to the image it produced.**

**A referenced script did not exist.** `docs/img/mascot/image-prompts.md` instructed users to run `src/image-utils/trim-padding-from-image.py` after saving each pose. That file had never been written. Seven mascot images were nonetheless correctly trimmed, so the step had been done by hand or by a since-deleted script — meaning the documented workflow could not actually be followed by the next person.

**Acceptance criteria were already formalized, just not enforced.** A test page at `docs/learning-graph/mascot-test.md` ran browser-side pixel checks asserting RGBA transparency, transparent corners, and a **4px content border** at alpha threshold 10. Those assertions were a specification nobody had connected to the generation step. Lifting them into `accept:` criteria cost almost nothing and made the pipeline enforce what the test page merely reported.

**Image weight was unmanaged.** 50 PNGs in `docs/` exceeded 400 KB, totalling **63 MB**, with a single 8.8 MB file. One image that *had* been optimized sat at 308 KB against siblings at 1.2–1.9 MB. Compression belongs in the accept step, not in a cleanup task nobody schedules.

## Acceptance: What a Machine Can Check

The queue validates every delivery automatically and writes a JSON receipt.

| Check | Catches |
|---|---|
| `format` | JPEG delivered when PNG was required |
| `width`/`height`, `min_width`/`min_height` | Wrong canvas size |
| `aspect` (+ tolerance) | Correct pixels, wrong shape |
| `alpha: required` | **Fake transparency** — a white or black background baked into pixels |
| `transparent_corners` | A drawn checkerboard "transparency" pattern |
| `trim_border_px` | Untrimmed padding that renders the subject tiny |
| `max_kb` | Unoptimized output |

`alpha: required` deserves emphasis. Image models frequently return a *flattened* image when asked for a transparent background — sometimes with a literal checkerboard pattern drawn into the pixels, having learned that transparency "looks like" a checkerboard. Both failures are invisible in a thumbnail and obvious in production. The check is two lines against the alpha channel's extrema, and it catches the single most common delivery defect.

### And what it cannot

`no_text: true` is the most-violated requirement in the whole system and **no automated check can catch it.**

Overlay infographics need annotation-free backgrounds because the textbook renders labels itself, in HTML, on top of the image. Baked-in text collides with the overlay and makes the image unusable. Image models are strongly biased toward adding labels to anything that looks like a diagram, and they do it even when told not to.

So `no_text` does not attempt a machine check. It flags the task for human review in the receipt. The honest design move is to **mark the gap rather than fake a check** — an OCR pass would produce false confidence on stylized art, and a receipt claiming "no text detected" is worse than one saying "a human must look at this."

### Validate the validator

Before trusting the checker, run it against files already known to be correct. The trim-border logic was verified against the seven existing mascot PNGs; all seven reported exactly 4px, matching the independently-written browser test. That agreement — two implementations, written at different times, arriving at the same number — is what justified trusting the checker on files nobody had inspected.

**Never ship an acceptance check you have not seen produce a `PASS` on known-good input and a `FAIL` on known-bad.** A check that only ever passes is indistinguishable from a check that is broken.

### Compression as part of acceptance

PIL's `FASTOCTREE` quantizer is the only one that preserves an alpha channel, which makes it the right default for this pipeline. Flat vector illustrations — exactly the house style for educational diagrams — quantize to a 256-color palette with no visible loss, typically 60–80% smaller. The accept step keeps the palette version only if it is genuinely smaller, and re-validates against `max_kb` afterward.

## Notification: Three Channels, One Trigger

All three fire from the same file drop. Which one is right depends on whether Claude happens to be running.

**Claude is live in a session.** Claude arms a persistent `Monitor` on the inbox and is notified in-conversation within seconds of a file appearing. Zero setup, but it ends with the session.

**Claude is not running.** `igq watch` polls the inbox, validates arrivals, appends to `NOTIFY.md`, and raises a desktop notification. A `--wake` flag additionally launches headless `claude -p` to review and install unattended.

`--wake` is **off by default, deliberately.** It spends tokens autonomously with no human present. Defaulting a convenience feature to "spend money without asking" is a decision the user should make explicitly, not one that arrives as a side effect of using the tool.

**Nothing is running.** The file sits in `inbox/`, and `igq status` reports it on the next run. Because the queue is only files on disk, no delivery is ever lost — the durable state *is* the filesystem, and the notification channels are conveniences layered on top. Build it in that order and the system degrades gracefully instead of dropping work.

### Feedback has to reach the next attempt

Rejections recorded feedback into the task file — and the brief did not show it. The next agent to pick up the task would receive the identical prompt that had just failed, and would very likely repeat the mistake.

The fix: `igq brief` now leads with a **READ FIRST — a previous attempt was rejected** block listing every prior rejection reason before the requirements or the prompt.

**A rejection loop that does not feed back into the next brief is not a loop, it is a treadmill.** If you build a reject path, trace the feedback all the way to where the next attempt actually reads it.

## Crossing Machines Through Git

For a project worked from more than one computer, the queue should travel.

**Tracked:** `tasks/` (including each task's `status`, `claimed_by`, and rejection `feedback`), `receipts/`, `QUEUE.md`, `README.md`, and the CLI. Accepted images travel too, since they are installed into `docs/`.

**Not tracked:** `inbox/`, `archive/`, `NOTIFY.md` — unreviewed binaries and rollback copies do not belong in history.

That split is right, but it creates two states that will confuse anyone who hits them cold, so the tool detects both:

- **Claimed on another machine.** Claims record `platform.node()`, so a task claimed on the desktop reads as such from the laptop, with a `--force` takeover available.
- **Delivered elsewhere.** Because `inbox/` is local, a task whose *committed* status says `delivered` may have no file on this machine. Rather than leaving you wondering, `igq status` names the machine and offers the three ways out.

The practical rule: **accept before you switch machines.** Once accepted, the image is in `docs/` and travels with everything else. A delivery left sitting in the inbox does not.

Two mechanical details that are easy to miss:

**Empty directories need a `.gitkeep`.** `inbox/` is gitignored and `receipts/` is often empty, so neither survives a clone without one. The first `igq scan` on a fresh machine would otherwise fail or write to the wrong place.

**Pin LF explicitly on every file the tool writes.** Task files are rewritten on every status change and are committed. Python's default text mode on Windows translates `\n` to `\r\n`, so a mixed Mac/Windows pair would rewrite the *entire* task file in every diff — landing precisely on the cross-machine workflow the design exists to serve. `open(path, "w", encoding="utf-8", newline="\n")` at every write site.

## Windows

The tooling shells out to POSIX utilities for clipboard and desktop notifications, and had not been tested on native Windows. Rather than half-working, both entry points exit immediately with instructions to install **Windows Subsystem for Linux**.

Two implementation details matter:

**Put the guard above every other import.** Otherwise the first thing a Windows user encounters is `Pillow is required` — a dependency error that sends them installing packages that were never the problem. The platform check should run before anything that could fail for an unrelated reason.

```python
import os
import sys

if sys.platform == "win32" or os.name == "nt":
    sys.exit("...install WSL, then run from the WSL shell...")

import argparse  # noqa: E402  (kept below the platform guard on purpose)
```

**WSL passes through correctly.** Python under WSL reports `sys.platform == "linux"`, so the guard stays silent there — which is the entire point of directing people to WSL rather than simply refusing.

## Verification Pitfalls

Three mistakes made while building this are worth recording, because all three produced *confident, wrong* intermediate results.

**A zsh glob failure silently corrupted a survey.** `ls dir/*.png dir/*.jpg` aborts entirely under zsh when either pattern matches nothing — it does not just skip that pattern. An audit built on that idiom reported ten simulations as missing their images when in fact all ten had them. Use `find` for existence surveys, and be suspicious of a result where *everything* is missing.

**Relative-path resolution produced false positives.** A naive image-reference scan flagged seven mascot images as broken because it resolved MkDocs directory-URL-relative paths as file-relative. The files were fine. Any link checker must model the rendered URL structure, not the source tree.

**A platform simulation broke the thing it was testing.** Patching `os.name = "nt"` to fake Windows caused `shutil` to attempt `import nt` and blow up before the guard under test ever ran. The traceback looked like a bug in the guard; it was an artifact of the test. Restructuring so the guard sits above the imports made it both better code *and* actually testable.

The common thread: **when a check reports something surprising, suspect the check before the code.** All three of these produced plausible-looking output that would have led to real wasted work — in the first case, regenerating ten images that already existed.

## Command Reference

| Command | Purpose |
|---|---|
| `igq list` | Show open tasks |
| `igq status` | Counts, inbox contents, cross-machine warnings |
| `igq brief <id>` | Print the full copy-paste prompt (`--copy` for clipboard) |
| `igq claim <id> --agent NAME` | Mark a task as being worked |
| `igq deliver <id> <file>` | Copy a finished image into the inbox and check it |
| `igq scan` | Validate the inbox, write receipts, notify |
| `igq accept <id>` | Compress and install into the repo (`--all` for every pass) |
| `igq reject <id> --reason "..."` | Return to the queue with feedback |
| `igq new <id> --title ... --output ...` | Create a task |
| `igq queue` | Regenerate `QUEUE.md` |
| `igq watch` | Poll the inbox (`--wake` to launch headless Claude) |
| `igq optimize docs/img` | Shrink oversized PNGs already in the repo |

## House Rules for Textbook Image Prompts

Findings about the prompts themselves, which apply to any educational illustration:

**State the negative constraints explicitly and specifically.** "No text" is insufficient. The working formulation enumerates: no letters, numbers, labels, titles, arrows, callout lines, legends, watermarks, or logos. Models satisfy the letter of a short prohibition and violate its spirit.

**Prohibit things that contradict the pedagogy, not just things that look wrong.** The Beginning Electronics prompts forbid microcontrollers, Arduino boards, and source code because the course deliberately contains no programming — an Arduino in a header image misrepresents the book. They forbid soldering irons, solder, smoke, and mains wiring because it is a no-soldering, low-voltage course and those images contradict its safety message. These are *content* constraints, and no generic style guide would supply them.

**Allow narrow exceptions rather than forking the system.** One task in the seeded queue is a schematic where three labels (`Vs`, `R`, `Vf`) are genuinely necessary. It sets `no_text: false` and enumerates the complete list of permitted symbols, with an instruction to omit them entirely rather than render them illegibly. The same queue handles annotation-free overlay backgrounds and labeled schematics without a second mechanism.

**Specify position and proportion, not just content.** Percentage-based positioning ("centered at 40% from left"), explicit relative sizing ("the largest montage element"), and stated margins ("at least 40 pixels of clear margin, since social platforms crop edges") produce dramatically more usable output than a list of objects.

**Name the audience in the prompt.** "Drawn for beginning electronics students in grades 5–12 who will copy this wiring hole-for-hole" changes the output more than any style adjective, because it tells the model what the image is *for*.

## What Transfers

Strip out the electronics and the reusable design is:

1. **Find the least-capable participant and make their minimum action the whole protocol.** Here, a filename.
2. **Durable state is files on disk.** Notifications are a convenience layer; the system must work when every convenience is off.
3. **Machine-check what you can, and explicitly mark what you cannot.** A flagged gap beats a fake check.
4. **Validate the validator against known-good input** before trusting it on unknown input.
5. **Commit the prompt beside the artifact.** An image without its prompt cannot be revised.
6. **Trace the feedback path** — a rejection that does not reach the next attempt is a treadmill.
7. **Suspect the check before the code** when a result surprises you.
