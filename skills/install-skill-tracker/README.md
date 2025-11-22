# Claude Code Skill Tracker

A complete activity tracking system for Claude Code that automatically logs skill usage, execution duration, and user prompts to help identify patterns and opportunities for automation.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Data Format](#data-format)
- [Analysis & Reporting](#analysis--reporting)
- [Common Issues & Troubleshooting](#common-issues--troubleshooting)
- [Privacy & Security](#privacy--security)
- [Customization](#customization)

## Overview

The Skill Tracker system uses Claude Code's hooks mechanism to automatically collect telemetry data about skill usage without requiring any manual intervention. This data enables:

- **Pattern Discovery** - Identify frequently repeated workflows that could become new skills
- **Performance Analysis** - Track which skills take the most time and may need optimization
- **Productivity Metrics** - Quantify time saved through skill automation
- **Usage Insights** - Understand which skills provide the most value

### Key Features

- **Zero-overhead tracking** - Uses lightweight hooks that don't impact performance
- **Automatic correlation** - Links prompts to skill invocations via session IDs
- **Duration measurement** - Calculates precise execution time for each skill
- **Token usage tracking** - Captures input, output, and cache token metrics for cost analysis
- **Rich analytics** - Generates comprehensive reports with insights and suggestions
- **Privacy-first** - All data stored locally, never transmitted externally
- **JSONL format** - Industry-standard format for easy parsing and analysis

## Architecture

The tracking system consists of three components:

```
┌─────────────────┐
│  Claude Code    │
│                 │
│  User Prompts   │
└────────┬────────┘
         │
         ├──────────────────────────┐
         ↓                          ↓
┌────────────────┐         ┌────────────────┐
│ UserPromptSubmit│         │  Skill Tool    │
│     Hook        │         │   Invocation   │
└────────┬────────┘         └───────┬────────┘
         │                          │
         ↓                          ├──────────┐
┌────────────────┐                  ↓          ↓
│ track-prompts  │         ┌────────────┐ ┌────────────┐
│     .sh        │         │PreToolUse  │ │PostToolUse │
└────────┬────────┘         │   Hook     │ │   Hook     │
         │                  └─────┬──────┘ └──────┬─────┘
         │                        │               │
         ↓                        ↓               ↓
    prompts.jsonl          track-skill-    track-skill-
                           start.sh        end.sh
                                │               │
                                ↓               ↓
                           skill-usage.jsonl

         ┌──────────────────────┴──────────────────────┐
         ↓                                              ↓
    prompts.jsonl                               skill-usage.jsonl
         │                                              │
         └──────────────────┬───────────────────────────┘
                            ↓
                    analyze-skills.py
                            │
                            ↓
                    Analysis Report
```

### Component Breakdown

1. **Hook Scripts** (`.claude/hooks/`)
   - `track-prompts.sh` - Captures user prompts via UserPromptSubmit hook
   - `track-skill-start.sh` - Logs skill start time via PreToolUse hook
   - `track-skill-end.sh` - Logs skill completion and calculates duration via PostToolUse hook

2. **Log Files** (`.claude/activity-logs/`)
   - `prompts.jsonl` - One JSON object per line, each containing a user prompt with timestamp
   - `skill-usage.jsonl` - One JSON object per line, each containing a skill event (start/end)

3. **Analysis Script** (`.claude/scripts/`)
   - `analyze-skills.py` - Python script that processes logs and generates reports

## How It Works

### Data Flow

1. **Prompt Capture**
   ```
   User types prompt → UserPromptSubmit hook fires → track-prompts.sh logs to prompts.jsonl
   ```

2. **Skill Start Tracking**
   ```
   Skill invoked → PreToolUse hook fires → track-skill-start.sh:
     - Logs start event to skill-usage.jsonl
     - Creates temporary file with start timestamp
   ```

3. **Skill End Tracking**
   ```
   Skill completes → PostToolUse hook fires → track-skill-end.sh:
     - Reads start timestamp from temporary file
     - Calculates duration (end_time - start_time)
     - Logs end event with duration to skill-usage.jsonl
     - Deletes temporary file
   ```

4. **Session Correlation**
   ```
   All logs include session_id → analyze-skills.py joins prompts with skills
   ```

### Hook Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "command": "bash .claude/hooks/track-prompts.sh"
      }
    ],
    "PreToolUse": [
      {
        "command": "bash .claude/hooks/track-skill-start.sh",
        "matcher": {
          "tool_name": "Skill"
        }
      }
    ],
    "PostToolUse": [
      {
        "command": "bash .claude/hooks/track-skill-end.sh",
        "matcher": {
          "tool_name": "Skill"
        }
      }
    ]
  }
}
```

The `matcher` ensures we only track Skill tool usage, not other tools like Bash, Read, Edit, etc.

## Installation

Use the `install-skill-tracker` skill to automate setup:

```bash
# In Claude Code
/skill install-skill-tracker
```

Or install manually:

```bash
# Create directories
mkdir -p .claude/hooks .claude/scripts .claude/activity-logs

# Copy hook scripts
cp skills/install-skill-tracker/scripts/track-*.sh .claude/hooks/
chmod +x .claude/hooks/*.sh

# Copy analysis script
cp skills/install-skill-tracker/scripts/analyze-skills.py .claude/scripts/
chmod +x .claude/scripts/analyze-skills.py

# Copy configuration
cp skills/install-skill-tracker/assets/settings.json .claude/settings.json

# Add to .gitignore
echo ".claude/activity-logs/" >> .gitignore
```

## Data Format

### JSONL (JSON Lines) Format

**CRITICAL:** All log files use JSONL format, where each line is a complete, self-contained JSON object.

**Correct JSONL:**
```json
{"timestamp":"2025-11-22 07:04:33","session":"abc123","prompt":"run skill"}
{"timestamp":"2025-11-22 07:05:01","session":"abc123","prompt":"analyze logs"}
```

**Incorrect (Pretty-Printed JSON):**
```json
{
  "timestamp": "2025-11-22 07:04:33",
  "session": "abc123",
  "prompt": "run skill"
}
```

### Why JSONL?

JSONL format enables:
- **Streaming processing** - Parse one line at a time without loading entire file
- **Append-only writes** - Add new events without rewriting the file
- **Line-oriented tools** - Use `head`, `tail`, `grep` on JSON data
- **Simple parsing** - Read file line-by-line, parse each as JSON

### The jq -nc Flag

The hook scripts use `jq -nc` to generate compact JSON output:

```bash
jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg p "$PROMPT" \
  '{timestamp: $ts, prompt: $p}' >> prompts.jsonl
```

**Flags:**
- `-n` (null input) - Don't read stdin, use only --arg values
- `-c` (compact output) - **CRITICAL** - Output single-line JSON instead of pretty-printed

**Without `-c` flag, jq outputs pretty-printed JSON which breaks JSONL parsing!**

### prompts.jsonl Schema

```json
{
  "timestamp": "2025-11-22 07:04:33",  // Human-readable timestamp
  "epoch": "1763816673",                // Unix epoch for sorting/calculations
  "session": "9ff87af7-...",            // Session ID for correlation
  "prompt": "run the skill"             // User's prompt text
}
```

### skill-usage.jsonl Schema

**Start event:**
```json
{
  "timestamp": "2025-11-22 07:04:42",
  "epoch": "1763816682",
  "session": "9ff87af7-...",
  "skill": "book-metrics-generator",
  "event": "start"
}
```

**End event:**
```json
{
  "timestamp": "2025-11-22 07:04:51",
  "epoch": "1763816691",
  "session": "9ff87af7-...",
  "skill": "book-metrics-generator",
  "event": "end",
  "duration_seconds": "9",
  "input_tokens": 8,
  "output_tokens": 244,
  "total_tokens": 65971,
  "cache_read_tokens": 65327,
  "cache_creation_tokens": 392
}
```

**Token Fields (added in v1.2):**
- `input_tokens` - Direct API input tokens
- `output_tokens` - Generated response tokens
- `total_tokens` - Sum of all token types (input + output + cache)
- `cache_read_tokens` - Tokens read from prompt cache
- `cache_creation_tokens` - Tokens used to create cache entries

## Analysis & Reporting

### Running the Analysis Script

```bash
# Analyze current project logs
python .claude/scripts/analyze-skills.py

# Analyze logs from a different directory
python .claude/scripts/analyze-skills.py /path/to/logs
```

### Token Usage Analysis (NEW in v1.2)

View token usage for all skill executions:

```bash
# Display recent skill token usage
bash .claude/scripts/show-skill-tokens.sh

# Or make it executable and run directly
chmod +x .claude/scripts/show-skill-tokens.sh
.claude/scripts/show-skill-tokens.sh
```

**Sample Output:**
```
Skill Usage with Token Tracking
================================

2025-11-22 07:36:42  book-metrics-generator
  Duration: 0s
  Tokens: input=8, output=244, total=65971

2025-11-22 07:40:15  learning-graph-generator
  Duration: 134s
  Tokens: input=12000, output=8500, total=84200

Summary Statistics
==================
Total skill executions: 5
Total tokens used: 328,456
  Input: 60,024
  Output: 42,150
Average tokens per skill: 65,691
```

**Token Cost Estimation:**

Using this data, you can estimate API costs:
- Sonnet 4.5: $3 per million input tokens, $15 per million output tokens
- Example: 60K input + 42K output = $0.18 + $0.63 = $0.81 total

**Understanding Cache Tokens:**

Cache tokens significantly reduce costs:
- `cache_read_tokens` are charged at 10% of normal input rate ($0.30/M vs $3/M)
- `cache_creation_tokens` are charged at normal input rate
- High cache read counts indicate effective prompt caching

### Sample Report Output

```markdown
# Skill Usage Analysis Report

**Log directory:** `$HOME/project/.claude/activity-logs`
**Total skill invocations:** 15
**Analysis date:** 2025-11-22 14:30:00

## Most Used Skills

- **microsim-p5**: 7x
- **learning-graph-generator**: 5x
- **glossary-generator**: 3x

## Skill Performance (Average Duration)

- **learning-graph-generator**
  - Average: 2m 34s
  - Total time: 12m 50s
  - Invocations: 5x

- **microsim-p5**
  - Average: 1m 12s
  - Total time: 8m 24s
  - Invocations: 7x

## Common Prompts Leading to Skill Usage

3x: "create a new microsim for..."
2x: "generate the learning graph..."
2x: "update the glossary with..."

## Recent Skill Usage (Last 20)

| Timestamp | Skill | Duration | Prompt (truncated) |
|-----------|-------|----------|---------------------|
| 2025-11-22 14:25:33 | microsim-p5 | 1m 15s | create a bubble chart microsim for priority matrix... |
| 2025-11-22 14:12:41 | glossary-generator | 3m 42s | generate glossary from learning graph... |

## Insights & Suggestions

### Frequently Used Skills
- **microsim-p5** (7x): Could benefit from optimization or templates

### Slowest Skills
- **learning-graph-generator**: 12m 50s total (2m 34s avg)

### Total Time Automated
Skills have automated **45m 23s** of work
```

### Interpreting Results

**High Frequency Skills**
- Skills used 3+ times indicate valuable automation
- Consider creating variations or templates for common patterns

**High Duration Skills**
- Skills taking >2 minutes on average may benefit from optimization
- Consider caching, incremental updates, or parallelization

**Common Prompts**
- Repeated similar prompts suggest need for new specialized skills
- Look for patterns like "create X", "update Y", "analyze Z"

## Common Issues & Troubleshooting

### Issue: JSON Parsing Error

**Symptom:**
```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
```

**Cause:**
Hook scripts are using `jq -n` instead of `jq -nc`, causing pretty-printed JSON output that violates JSONL format.

**Solution:**
Update all hook scripts to use `jq -nc`:

```bash
# Fix existing hooks
sed -i '' 's/jq -n \\/jq -nc \\/' .claude/hooks/track-*.sh

# Fix existing log files
jq -c '.' .claude/activity-logs/prompts.jsonl > temp && mv temp .claude/activity-logs/prompts.jsonl
jq -c '.' .claude/activity-logs/skill-usage.jsonl > temp && mv temp .claude/activity-logs/skill-usage.jsonl
```

### Issue: No Data Logged

**Symptom:**
Running analysis shows "No skill usage data found yet."

**Diagnosis:**
```bash
# Check if directories exist
ls -la .claude/activity-logs/

# Check hook configuration
cat .claude/settings.json

# Check hook permissions
ls -l .claude/hooks/*.sh

# Verify hooks are executable
file .claude/hooks/*.sh
```

**Solution:**
```bash
# Ensure directories exist
mkdir -p .claude/activity-logs

# Make hooks executable
chmod +x .claude/hooks/*.sh

# Verify settings.json exists
test -f .claude/settings.json && echo "Settings found" || echo "Settings missing"
```

### Issue: Duration Shows "unknown"

**Symptom:**
Analysis report shows `Duration: unknown` for skills

**Cause:**
- Temporary start time file not created
- Start time file deleted before end hook runs
- Permissions issue preventing file creation

**Diagnosis:**
```bash
# Check for orphaned temp files
ls .claude/activity-logs/*.tmp

# Check permissions
ls -la .claude/activity-logs/
```

**Solution:**
- Ensure `.claude/activity-logs/` is writable
- Check that skill names don't contain special characters that break filenames
- Verify both PreToolUse and PostToolUse hooks are configured

### Issue: Hooks Not Executing

**Symptom:**
Log files not created when using skills

**Diagnosis:**
```bash
# Test hook manually
echo '{"prompt":"test","session_id":"test123"}' | bash .claude/hooks/track-prompts.sh

# Check for errors
echo '{"prompt":"test","session_id":"test123"}' | bash -x .claude/hooks/track-prompts.sh
```

**Solution:**
- Verify `jq` is installed: `which jq`
- Check hook script syntax: `bash -n .claude/hooks/track-prompts.sh`
- Ensure hooks are in `.claude/settings.json`
- Restart Claude Code to reload settings

## Privacy & Security

### Local Storage Only

All tracking data is stored locally in `.claude/activity-logs/`:
- No data transmission to external services
- No cloud sync or remote logging
- Complete control over your data

### Excluding from Git

The installation process adds `.claude/activity-logs/` to `.gitignore` to prevent:
- Committing sensitive prompt data
- Exposing project patterns
- Repository bloat from log files

### Deleting Logs

Remove all tracking data:
```bash
# Delete all logs
rm -rf .claude/activity-logs

# Delete specific log files
rm .claude/activity-logs/prompts.jsonl
rm .claude/activity-logs/skill-usage.jsonl
```

### Selective Logging

Disable specific hooks by commenting them out in `.claude/settings.json`:

```json
{
  "hooks": {
    // Disable prompt tracking
    // "UserPromptSubmit": [...],

    // Keep skill tracking enabled
    "PreToolUse": [...],
    "PostToolUse": [...]
  }
}
```

## Customization

### Global vs Project-Specific Tracking

**Current Setup:** Project-specific (logs in `.claude/activity-logs/`)

**For Global Tracking:**

1. Move settings to user-level config:
```bash
mv .claude/settings.json ~/.claude/settings.json
```

2. Update `LOG_DIR` in all hook scripts:
```bash
# Change from:
LOG_DIR="${CLAUDE_PROJECT_DIR:-.}/.claude/activity-logs"

# To:
LOG_DIR="$HOME/.claude/activity-logs"
```

3. Analysis script automatically finds global logs:
```bash
python ~/.claude/scripts/analyze-skills.py
```

### Tracking Additional Tools

To track all tool usage (not just skills), remove the `matcher`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "command": "bash .claude/hooks/track-tool-start.sh"
        // No matcher - tracks ALL tools
      }
    ]
  }
}
```

Update hook scripts to use `$TOOL_NAME` instead of `$SKILL_NAME`.

### Adding Custom Metadata

Extend hook scripts to capture additional context:

```bash
# In track-skill-end.sh, add project name
PROJECT_NAME=$(basename "$PWD")

jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg skill "$SKILL_NAME" \
  --arg project "$PROJECT_NAME" \
  '{timestamp: $ts, skill: $skill, project: $project}' >> "$LOG_FILE"
```

### Custom Analysis Queries

Query logs directly with `jq`:

```bash
# Count skills by name
jq -s 'group_by(.skill) | map({skill: .[0].skill, count: length})' \
  .claude/activity-logs/skill-usage.jsonl

# Find long-running skills (>60 seconds)
jq 'select(.event == "end" and (.duration_seconds | tonumber) > 60)' \
  .claude/activity-logs/skill-usage.jsonl

# Get unique prompts
jq -r '.prompt' .claude/activity-logs/prompts.jsonl | sort -u
```

## Version History

**v1.2** (2025-11-22)
- **NEW:** Added token usage tracking (input, output, cache metrics)
- **NEW:** Added `show-skill-tokens.sh` script for token analysis
- Extracts token data from Claude Code transcript files
- Tracks prompt cache efficiency with cache_read and cache_creation tokens
- Enables cost estimation and optimization insights

**v1.1** (2025-11-22)
- Fixed JSONL format bug by adding `-c` flag to all `jq` commands
- Added comprehensive troubleshooting section
- Documented data format requirements

**v1.0** (2025-11-20)
- Initial release
- Basic tracking and analysis functionality

## Resources

### Files in This Skill

```
install-skill-tracker/
├── README.md                    # This file
├── SKILL.md                     # Skill definition and installation workflow
├── scripts/
│   ├── track-prompts.sh        # Hook: Capture user prompts
│   ├── track-skill-start.sh    # Hook: Log skill start times
│   ├── track-skill-end.sh      # Hook: Log skill completion, duration, and tokens (v1.2)
│   ├── analyze-skills.py       # Analysis script for patterns and insights
│   └── show-skill-tokens.sh    # NEW v1.2: Display token usage and cost metrics
└── assets/
    ├── settings.json            # Template for .claude/settings.json
    └── README.md                # Documentation to copy to .claude/README.md
```

### External References

- [Claude Code Hooks Documentation](https://docs.anthropic.com/claude/docs/hooks)
- [JSONL Specification](https://jsonlines.org/)
- [jq Manual](https://stedolan.github.io/jq/manual/)

## Support

For issues or questions:
1. Check the [Troubleshooting](#common-issues--troubleshooting) section
2. Review the [Claude Code documentation](https://docs.anthropic.com/claude)
3. Open an issue in the repository
