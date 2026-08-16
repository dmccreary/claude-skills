# Book Appendices

Supplementary case studies and deep-dive write-ups that don't fit the main chapter sequence but are useful reference material for understanding how this repository works and evolved.

- [Skill Refactor with Fable 5](./skill-refactor-fable-5.md) — a case study on how the intelligent-textbook skill library evolved since Claude Skills launched in October 2025, why it periodically needs re-architecting, and how a 29-skill, over-budget catalog was consolidated to 14 skills through an agent-authored, human-reviewed, phase-by-phase refactor.
- [Delegating Image Generation to an External Agent](./imaging-agent-delegation.md) — how to hand image work to a tool Claude Code cannot drive (ChatGPT desktop, Google Antigravity) and get it back verified: a filesystem work queue whose entire protocol is a filename, automated acceptance checks, notification channels that degrade gracefully, and what a machine can and cannot validate about a generated illustration.
