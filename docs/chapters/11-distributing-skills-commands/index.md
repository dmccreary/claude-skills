---
title: Distributing Skills and Building Commands
description: Covers installing skills globally or per-project with symbolic links, invoking skills and commands, the ibook runbook, and cross-platform graceful degradation.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 14:35:00
version: 0.09
---

# Distributing Skills and Building Commands

## Summary

This chapter covers packaging a skill and installing it globally or per-project with symbolic links, including cleaning up stale links and listing what is currently available. It then covers creating Claude commands and ordered runbooks, such as the `/ibook` command, that chain multiple skills together. Students will be able to install a skill library and invoke a skill by name or slash command after this chapter.

## Concepts Covered

This chapter covers the following 20 concepts from the learning graph:

1. Symbolic Link Installation
2. Cross-Platform Skill Testing
3. Error Analysis in Skills
4. Global Skill Installation
5. bk-install-skills Script
6. Graceful Capability Degradation
7. Improving Skill Quality
8. Project-Specific Skills
9. Stale Symlink Cleanup
10. Listing Available Skills
11. Image Understanding Dependency
12. bk Command Family
13. Invoking a Skill
14. Slash Command Invocation
15. Claude Command
16. Command Definition File
17. Skills Versus Commands
18. Runbook Command
19. ibook Runbook
20. Read-Only State Detection

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [10. Building and Testing Portable Skills](../10-building-testing-portable-skills/index.md)

---

!!! mascot-welcome "Let's get your skills actually installed."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A packaged skill sitting in a repository doesn't do anything until an agent can find it. This chapter covers installing skills, invoking them, and the runbook command that ties this whole library together. Right tool, right task!

## Installing Skills: Global vs Project-Specific

Rather than copying a skill's folder to where an agent looks for it, this project uses **symbolic link installation**: installing a skill by creating a filesystem pointer to its source folder, so edits to the source take effect immediately without a separate copy step going stale. Where you point that link determines its scope. **Global skill installation** places skills where every project on a machine can use them, while **project-specific skills** are installed inside one project so they apply only to that book — typically because they encode subject-specific knowledge, like this library's own breadboard-simulation skill for an electronics textbook.

The **bk-install-skills script** is the utility that creates those links from the skill repository into an agent's skills directory and removes links whose targets no longer exist — that removal step is **stale symlink cleanup**: clearing pointers that reference deleted or renamed skills, preventing a load error the next time the agent starts. Once installed, **listing available skills** means displaying the skills an agent can currently use, along with their summaries, so you can confirm installation actually worked.

## Invoking a Skill

**Invoking a skill** means causing its instructions to load and run, either by describing the task in prose or by naming the skill explicitly. The explicit route is **slash command invocation**: triggering a skill or command by typing its name after a forward slash rather than describing the task, the fastest and least ambiguous way to reach for a specific tool by name.

## Skills Versus Commands

Not everything you invoke by name is a skill. A **Claude command** is a named, reusable instruction file invoked directly by the user, typically to run a fixed procedure rather than an open-ended task, declared in a **command definition file**: the markdown file that declares a command's name and description and contains the steps it performs.

!!! mascot-thinking "A skill is selected for you; a command is chosen by you."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    This is **skills versus commands**: the distinction between a capability an agent selects automatically based on your request, and a procedure you invoke explicitly by name. A skill answers "what does this request need?" A command answers "run exactly this, now." Once you see that split, deciding whether to write a skill or a command for a new tool gets much easier.

## Runbooks: The ibook Command

Some commands don't perform work at all — they tell you what to do next. A **runbook command** reports the ordered steps of a process and identifies which step comes next, without performing the steps itself. The **ibook runbook** is this library's own instance: the command that inspects a textbook project and reports how far the build pipeline has progressed and which skill to run next. It can do that safely because of **read-only state detection**: inspecting a project to determine its progress without altering any file, so a status report can never cause damage — you can run `/ibook` as often as you like just to check in.

## The bk Command Family

Beyond skills and commands, this project installs a set of short shell utilities: the **bk command family**, the set of installed command-line utilities, each prefixed for recognition, that perform book maintenance tasks such as capturing a MicroSim screenshot or generating book metrics. You've already met the pattern behind them in Chapter 3's shell script wrapper — a short, memorable name standing in for a longer, more exact command.

## Cross-Platform Testing and Graceful Degradation

Chapter 10 introduced skill portability as a claim you verify, not one you assume. **Cross-platform skill testing** is running the same skill on several agent platforms and comparing results to find behavior that depends on one vendor. When a platform genuinely lacks something Claude has, the right response is **graceful capability degradation**: designing a skill so that when a platform lacks a capability, it produces a reduced but still useful result rather than failing outright. The single most common capability gap is an **image understanding dependency**: a skill's reliance on a model's ability to interpret pictures, which is the capability most likely to be missing on non-Claude platforms.

!!! mascot-tip "Design the fallback before you need it."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    If a skill uses image understanding to review a MicroSim's layout, write its instructions so that on a platform without that capability, it still runs the text-based checks and clearly reports which checks it had to skip — rather than crashing or silently producing an incomplete result.

## When Things Break: Error Analysis and Improvement

When a skill run doesn't go as expected, **error analysis in skills** means examining the failed run to determine whether the fault lies in the description, the instructions, a script, or the environment — the same categories as Chapter 10's skill failure modes, applied to one specific incident instead of the general pattern. Once you know where the fault actually is, **improving skill quality** means revising the skill in response to that measured defect, then re-running the benchmark to confirm the change actually helped.

!!! mascot-warning "Don't guess at the cause — isolate it."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    It's tempting to rewrite an entire skill's instructions the moment something goes wrong. Resist that — check the description first (did it even trigger?), then the instructions, then any script it calls, then the environment. Fixing the wrong layer wastes a revision and doesn't fix the actual defect.

## Key Takeaways

- **Symbolic link installation**, scoped either **globally** or per-project, is installed and maintained by **bk-install-skills**, including **stale symlink cleanup** and **listing available skills**.
- **Invoking a skill** can happen by description or by **slash command**; a **Claude command**, defined in a **command definition file**, is a different, explicitly-chosen tool — that's **skills versus commands**.
- A **runbook command** like the **ibook runbook** reports progress using **read-only state detection**, safely, as often as you like.
- The **bk command family** wraps common book-maintenance tasks in short, memorable names.
- **Cross-platform testing** verifies **portability**; **graceful capability degradation** — especially around the common **image understanding dependency** — keeps a skill useful even where a capability is missing; **error analysis** and **improving skill quality** close the loop when something breaks.

!!! mascot-celebration "Your library is installed, invokable, and self-diagnosing."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Installed globally or per-project, invoked by name, checked with a runbook that never breaks anything just by looking — that's a skill library someone else could actually pick up and use. Right tool, right task!
