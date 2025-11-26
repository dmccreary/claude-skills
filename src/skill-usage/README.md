# Skill Usage Analysis Tools

This directory contains scripts for analyzing Claude Code skill usage data.

## Scripts

### analyze-skills.py

Python script that analyzes skill usage logs and generates comprehensive reports including:

- Skill invocation frequency
- Token usage by skill (total, cache read, cache creation)
- Cache efficiency metrics
- Prompt correlation (matches prompts to skill invocations)
- Cost estimation

**Usage:**
```bash
# Via the bk-analyze-skill-usage wrapper (recommended)
bk-analyze-skill-usage

# Direct invocation
python3 analyze-skills.py [log-directory]
```

### show-skill-tokens.sh

Bash script for quick token usage summary.

**Usage:**
```bash
./show-skill-tokens.sh [log-directory]
```

## Data Format

The scripts read from `.claude/activity-logs/` which contains:

- `skill-usage.jsonl` - Skill start/end events with token data
- `prompts.jsonl` - User prompts with session IDs

## Installation

These scripts are the canonical source. The `install-skill-tracker` skill copies hook scripts to projects, but analysis scripts are run from this central location via `bk-analyze-skill-usage`.

## Related Files

- `$BK_HOME/scripts/bk-analyze-skill-usage` - Shell wrapper that invokes analyze-skills.py
- `$BK_HOME/skills/install-skill-tracker/` - Skill that installs tracking hooks in projects
