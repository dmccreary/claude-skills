---
description: List all available Claude skills
allowed-tools: Bash(./scripts/list-skills.sh:*)
---

Run the list-skills.sh script to display all available Claude skills with their names and descriptions.

Execute the following command:

```bash
./scripts/list-skills.sh
```

This script will:
- Check the personal skills directory (~/.claude/skills/)
- Extract the name and description from each SKILL.md file's YAML frontmatter
- Display results in a clean, readable format with emojis
- Show the total count of available skills