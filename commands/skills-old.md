---
description: List all available Claude skills
allowed-tools: Bash(~/bin/list-skills.sh:*)
---

Run the list-skills.sh script with --names-only flag to efficiently list all available Claude skills.

Execute the following command:

```bash
~/bin/list-skills.sh --names-only
```

This returns only skill names (one per line), minimizing token usage by ~95% compared to full descriptions.

Present the output to the user in a clean, readable format:
- Show the count of available skills
- List each skill name
- Keep the presentation concise

If the user wants more details about a specific skill, offer to read that skill's SKILL.md file.

Available output modes for reference:
- (no flag): Human-readable with descriptions (~5,063 chars)
- `--json`: Compact JSON format (~5,117 chars)
- `--names-only`: Just names (~267 chars) ← **Use this for /skills command**