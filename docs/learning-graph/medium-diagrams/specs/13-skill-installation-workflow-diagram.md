# Skill Installation Workflow Diagram

**Chapter:** 13 - Dev Tools Version Control Deployment
**Generator:** timeline-generator
**Match Score:** 97/100
**Difficulty:** Medium

## Specification

<summary>Skill Installation Workflow Diagram</summary>
    Type: diagram

    Purpose: Show the relationship between project skills directory, global skills directory, and Claude Code's skill discovery

    Components to show:
    - Project repository structure (left side):
      ```
      ~/Documents/textbook-project/
      ├── skills/
      │   ├── glossary-generator/
      │   │   ├── SKILL.md
      │   │   └── templates/
      │   ├── quiz-generator/
      │   │   └── SKILL.md
      │   └── learning-graph-generator/
      │       ├── SKILL.md
      │       └── scripts/
      └── scripts/
          └── install-claude-skills.sh
      ```

    - Global skills directory (center):
      ```
      ~/.claude/skills/
      ├── glossary-generator -> ~/Documents/textbook-project/skills/glossary-generator
      ├── quiz-generator -> ~/Documents/textbook-project/skills/quiz-generator
      └── learning-graph-generator -> ~/Documents/textbook-project/skills/learning-graph-generator
      ```

    - Claude Code (right side):
      - Search icon looking in ~/.claude/skills/
      - Successfully finding skills via symlinks
      - Loading SKILL.md files

    Connections:
    - Dashed arrows from global skills to project skills (labeled "symlink")
    - Solid arrow from install-claude-skills.sh to global skills (labeled "creates")
    - Solid arrow from Claude Code to global skills (labeled "reads from")

    Annotations:
    - Label on project skills: "Original files (version controlled)"
    - Label on global skills: "Symlinks (not version controlled)"
    - Label on symlinks: "Points to original, no duplication"
    - Callout: "When original files update, changes immediately available to Claude"

    Visual style: System architecture diagram with clear flow
    Color scheme:
    - Project files: Blue
    - Symlinks: Orange (with dotted line style)
    - Claude Code: Purple

    Implementation: SVG diagram with labeled components and directional arrows