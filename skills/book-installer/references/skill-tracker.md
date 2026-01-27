---
name: install-skill-tracker
description: This skill installs a complete Claude Code skill tracking system using hooks to automatically log skill usage, execution duration, token usage, and user prompts for later analysis. Use this skill when setting up activity tracking in a Claude Code project to identify patterns, monitor costs, and discover opportunities for new skills.
---

# Install Skill Tracker

## Overview

This skill automates the installation of a **global** skill tracking system for Claude Code. The system uses Claude Code hooks installed in `~/.claude/` to automatically log all skill invocations across **all projects**, including their duration, token usage, and the prompts that triggered them. This data enables pattern analysis to identify frequently repeated workflows that could become new skills.

**Key Feature:** Global installation means skill usage is tracked across all your Claude Code projects in a single centralized log, making it easy to analyze your total skill usage patterns and costs.

## When to Use This Skill

Use this skill when:
- Setting up skill usage tracking that works across all your Claude Code projects
- Wanting to analyze which skills are used most frequently across your entire workflow
- **Measuring how long each skill takes** to identify optimization opportunities
- Monitoring API costs and token usage across all skill executions
- Identifying time-consuming skills that may need optimization
- Discovering patterns in work that could be automated with new skills
- Tracking productivity gains and cost efficiency from skill automation
- Understanding prompt cache effectiveness and optimization opportunities

**Why Timing Matters:** Understanding how long skills take helps you:
- Identify slow skills that need optimization
- Estimate total time saved through automation
- Make informed decisions about which skills to invest in improving
- Track productivity improvements over time

## Installation Workflow

### Step 1: Create Global Directory Structure

Create the necessary directories in your home `.claude` folder:

```bash
mkdir -p ~/.claude/hooks ~/.claude/scripts ~/.claude/activity-logs
```

### Step 2: Install Hook Scripts

Copy the hook scripts from this skill's `scripts/` directory to `~/.claude/hooks/`:

- **track-prompts.sh** - Logs user prompts with timestamps and session IDs
- **track-skill-start.sh** - Logs when skills begin execution
- **track-skill-end.sh** - Logs skill completion and calculates duration

Make the hook scripts executable:

```bash
chmod +x ~/.claude/hooks/*.sh
```

### Step 3: Install Analysis Scripts

Copy the analysis scripts from this skill's `scripts/` directory to `~/.claude/scripts/`:

- **analyze-skills.py** - Processes logs and generates usage reports
- **show-skill-tokens.sh** - Displays token usage and cost metrics

Make the analysis scripts executable:

```bash
chmod +x ~/.claude/scripts/analyze-skills.py
chmod +x ~/.claude/scripts/show-skill-tokens.sh
```

### Step 4: Configure Global Hooks

Copy the `settings.json` template from this skill's `assets/` directory to `~/.claude/settings.json`. This configuration registers three hooks that will run for all projects:

- **UserPromptSubmit** - Captures all user prompts
- **PreToolUse** (Skill matcher) - Logs skill start times
- **PostToolUse** (Skill matcher) - Logs skill completion times

**Important:** If you already have a `~/.claude/settings.json` file, merge the hooks configuration rather than overwriting.

### Step 5: Add Documentation

Copy the `README.md` from this skill's `assets/` directory to `~/.claude/README.md`. This provides documentation on:
- What data gets tracked
- How the tracking system works
- How to analyze the logs
- Customization options
- Troubleshooting guide

### Step 6: Verify Installation

Confirm all files are in place:

```bash
ls -la ~/.claude/hooks/
ls -la ~/.claude/scripts/
cat ~/.claude/settings.json
```

### Step 7: Test Timing Data Collection

**IMPORTANT:** After installation, verify that timing data is being collected correctly by running a skill and checking the logs.

1. Run any skill (e.g., a simple one like `glossary-generator`)
2. Check that the skill-usage.jsonl contains timing data:

```bash
tail -5 ~/.claude/activity-logs/skill-usage.jsonl
```

3. Run the analysis report to verify timing appears:

```bash
bk-analyze-skill-usage
```

Look for these timing metrics in the report:
- **Time from Prompt** column in Recent Skill Usage table
- **Avg Time** column in Token Usage by Skill table
- **Timing Summary** section with total and average time

If timing shows "N/A" or "0s", see the Troubleshooting section below.

## Using the Tracking System

### Automatic Logging

After installation, the tracking system operates automatically across all projects:
1. Use skills normally through Claude Code in any project
2. Each skill invocation is logged with timestamp, duration, token usage, and triggering prompt
3. Logs accumulate in `~/.claude/activity-logs/` as JSONL files (centralized for all projects)

**What Gets Tracked (v2.1):**
- Skill name and invocation time
- **Timing metrics:**
  - Time from prompt submission to skill completion
  - Duration between start and end events
  - Session activity timeline (time between prompts)
- Token usage metrics:
  - Input tokens (new content)
  - Output tokens (generated response)
  - Cache read tokens (from prompt cache)
  - Cache creation tokens (creating cache entries)
  - Total tokens (sum of all above)
- User prompt that triggered the skill
- Session ID for correlation
- Project directory (for filtering by project if needed)

### Analyzing Usage Data

Run the analysis scripts to generate insights:

**Pattern and Performance Analysis:**
```bash
~/.claude/scripts/analyze-skills.py
```

**Token Usage and Cost Analysis (v1.2):**
```bash
~/.claude/scripts/show-skill-tokens.sh
```

The analysis reports include:
- **Skill frequency** - Most commonly used skills
- **Timing metrics** - Time from prompt to completion, average time per skill
- **Timing summary** - Total time spent in skills, average time per skill
- **Session activity timeline** - Time gaps between prompts to understand work patterns
- **Token usage metrics** - Input/output/cache tokens per skill
- **Cost estimation** - Calculate API costs based on token usage
- **Cache efficiency** - Identify cache hit rates and optimization opportunities
- **Prompt patterns** - Common prompts that trigger skills
- **Usage history** - Recent skill invocations with timing and token details
- **Insights** - Suggestions for optimization and new skill opportunities

### Example Analysis Output

```
# Skill Usage Analysis Report

**Total skill invocations:** 15

## Token Usage by Skill

| Skill | Invocations | Total Tokens | Avg Time | Cache Read | Cache Creation |
|-------|-------------|--------------|----------|------------|----------------|
| learning-graph-generator | 5x | 420.5K | 2m 34s | 380.2K | 15.3K |
| microsim-p5 | 7x | 168.7K | 1m 12s | 145.6K | 8.1K |
| glossary-generator | 3x | 45.2K | 45s | 38.9K | 2.4K |

## Timing Summary

| Metric | Value |
|--------|-------|
| Total time in skills | 45m 23s |
| Average time per skill | 3m 1s |
| Skills with timing data | 15 of 15 |

## Recent Skill Usage

| Timestamp | Skill | Tokens | Time from Prompt | Prompt (truncated) |
|-----------|-------|--------|------------------|---------------------|
| 2025-12-03 14:25:33 | microsim-p5 | 24.1K | 1m 15s | create a bubble chart microsim... |
| 2025-12-03 14:12:41 | glossary-generator | 15.1K | 42s | generate glossary from learning... |

## Session Activity Timeline

| Timestamp | Time Since Previous | Prompt (truncated) |
|-----------|---------------------|---------------------|
| 2025-12-03 14:25:33 | 12m 52s | create a bubble chart microsim... |
| 2025-12-03 14:12:41 | 3m 15s | generate glossary from learning... |

## Insights

### Most Token-Intensive Skills
- **learning-graph-generator**: 420.5K total (84.1K avg)

### Cache Efficiency
✅ Good cache utilization (89.2% cache hits)
```

## Log Data Format

The system creates two JSONL log files in `~/.claude/activity-logs/`:

### prompts.jsonl
Logs user prompts with session correlation:
```json
{"timestamp": "2025-11-22 14:23:45", "epoch": "1732299825", "session": "abc123", "project": "/path/to/project", "prompt": "create a learning graph"}
```

### skill-usage.jsonl
Logs skill start/end events with duration and token usage:
```json
{"timestamp": "2025-11-22 14:23:46", "epoch": "1732299826", "session": "abc123", "project": "/path/to/project", "skill": "learning-graph-generator", "event": "start"}
{"timestamp": "2025-11-22 14:26:20", "epoch": "1732299980", "session": "abc123", "project": "/path/to/project", "skill": "learning-graph-generator", "event": "end", "duration_seconds": "154", "input_tokens": 12000, "output_tokens": 8500, "total_tokens": 84200, "cache_read_tokens": 62400, "cache_creation_tokens": 1300}
```

## Customization Options

### Tracking Additional Metrics

Extend the hook scripts to capture:
- All tool usage (not just skills)
- Error rates and failures
- Custom metadata fields
- Project-specific context

Hooks receive full JSON context via stdin with tool names, parameters, and outputs.

## Privacy & Security

All tracking data is stored locally:
- No data transmission to external services
- Logs remain in `~/.claude/activity-logs/`
- Stored in your home directory, not in project directories

To delete all tracking data:
```bash
rm -rf ~/.claude/activity-logs
```

## Troubleshooting

### JSON Parsing Errors

**IMPORTANT FIX (v1.1):** The hook scripts now use `jq -nc` instead of `jq -n` to generate compact JSON output. This is **critical** for proper JSONL format.

If you encounter errors like:
```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
```

Your existing log files may have pretty-printed JSON. Fix with:
```bash
jq -c '.' ~/.claude/activity-logs/prompts.jsonl > temp && mv temp ~/.claude/activity-logs/prompts.jsonl
jq -c '.' ~/.claude/activity-logs/skill-usage.jsonl > temp && mv temp ~/.claude/activity-logs/skill-usage.jsonl
```

### Hooks Not Executing

Verify hook configuration:
```bash
cat ~/.claude/settings.json
```

Check script permissions:
```bash
ls -l ~/.claude/hooks/*.sh
```

### No Log Files Created

Ensure directories exist:
```bash
mkdir -p ~/.claude/activity-logs
```

Use a skill to trigger logging, then check:
```bash
ls -la ~/.claude/activity-logs/
```

### Analysis Shows No Data

Logs are created only after skill usage. Run any skill first, then execute the analysis script.

### Detailed Troubleshooting

For comprehensive troubleshooting, see the [README.md](./README.md) in this skill directory, which includes:
- JSONL format requirements and the `-c` flag fix
- Common issues and solutions
- Hook debugging techniques
- Custom analysis queries

## Resources

This skill includes:

### scripts/
- **track-prompts.sh** - Bash hook to log user prompts
- **track-skill-start.sh** - Bash hook to log skill start times
- **track-skill-end.sh** - Bash hook to log skill completion, duration, and tokens (v1.2)
- **analyze-skills.py** - Python script to analyze logs and generate reports
- **show-skill-tokens.sh** - Bash script to display token usage and cost metrics (v1.2)

### assets/
- **settings.json** - Hook configuration template for `.claude/settings.json`
- **README.md** - Complete documentation for the tracking system
