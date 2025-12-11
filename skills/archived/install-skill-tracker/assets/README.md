# Claude Code Skill Tracking System (Global)

This directory contains hooks and scripts to automatically track skill usage in Claude Code across **all projects**.

## What Gets Tracked

The tracking system logs:
- **User prompts** that trigger skills
- **Skill names** being invoked
- **Start and end times** for each skill
- **Duration** of skill execution
- **Session IDs** to correlate prompts with skills
- **Project directory** to identify which project triggered each skill
- **Token usage** (input, output, cache read, cache creation)

## Files

```
~/.claude/
├── settings.json                 # Hook configuration (global)
├── hooks/
│   ├── track-prompts.sh         # Logs user prompts
│   ├── track-skill-start.sh     # Logs skill start time
│   └── track-skill-end.sh       # Logs skill completion and duration
├── scripts/
│   ├── analyze-skills.py        # Analyzes logs and generates reports
│   └── show-skill-tokens.sh     # Displays token usage metrics
└── activity-logs/               # Created automatically
    ├── prompts.jsonl            # User prompt log (JSONL)
    ├── skill-usage.jsonl        # Skill timing log (JSONL)
    └── skill-start-*.tmp        # Temporary files for duration tracking
```

## How It Works

1. **When you submit a prompt** → `track-prompts.sh` logs it with session ID and project
2. **When a skill starts** → `track-skill-start.sh` logs start time and project
3. **When a skill completes** → `track-skill-end.sh` logs end time, duration, and tokens
4. **All data is correlated** by session ID to match prompts with skills

## Usage

### Normal Usage (Automatic)

The hooks run automatically whenever you use skills in Claude Code in **any project**. Just work normally and data will accumulate in `~/.claude/activity-logs/`.

### Analyzing Your Data

Run the analysis script to see insights across all projects:

```bash
~/.claude/scripts/analyze-skills.py
```

This generates a report showing:
- Most frequently used skills
- Average and total duration for each skill
- Common prompts that trigger skills
- Recent skill usage history
- Efficiency insights and suggestions

### Example Output

```
# Skill Usage Analysis Report

**Total skill invocations:** 15

## Most Used Skills

- **learning-graph-generator**: 5x
- **glossary-generator**: 3x
- **microsim-p5**: 7x

## Skill Performance (Average Duration)

- **learning-graph-generator**
  - Average: 2m 34s
  - Total time: 12m 50s
  - Invocations: 5x

## Insights & Suggestions

### Frequently Used Skills
- **microsim-p5** (7x): Could benefit from optimization or templates

### Total Time Automated
Skills have automated **45m 23s** of work
```

## Log Format

### prompts.jsonl
```json
{"timestamp": "2025-11-22 14:23:45", "epoch": "1732299825", "session": "abc123", "project": "/path/to/project", "prompt": "create a learning graph"}
```

### skill-usage.jsonl
```json
{"timestamp": "2025-11-22 14:23:46", "epoch": "1732299826", "session": "abc123", "project": "/path/to/project", "skill": "learning-graph-generator", "event": "start"}
{"timestamp": "2025-11-22 14:26:20", "epoch": "1732299980", "session": "abc123", "project": "/path/to/project", "skill": "learning-graph-generator", "event": "end", "duration_seconds": "154", "input_tokens": 12000, "output_tokens": 8500, "total_tokens": 84200}
```

## Customization

### Add Additional Tracking

You can extend the hooks to track:
- Tool usage (not just skills)
- Error rates
- Custom metadata

Just modify the hook scripts to capture additional fields from the JSON input.

### Filter by Project

Since logs include the project directory, you can filter analysis by project:

```bash
# View skills used in a specific project
jq 'select(.project | contains("my-project"))' ~/.claude/activity-logs/skill-usage.jsonl
```

## Privacy & Data

All logs are stored **locally** in `~/.claude/activity-logs/`. No data is sent externally.

To delete logs:
```bash
rm -rf ~/.claude/activity-logs
```

## Troubleshooting

### Hooks not running?

Check hook configuration:
```bash
cat ~/.claude/settings.json
```

Verify scripts are executable:
```bash
ls -l ~/.claude/hooks/*.sh
```

### No log files created?

Run a skill and check for errors:
```bash
ls -la ~/.claude/activity-logs/
```

Check if directory was created:
```bash
mkdir -p ~/.claude/activity-logs
```

### Analysis script shows no data?

Ensure you've run at least one skill since installing the hooks. The logs are only created when skills are actually used.

## Next Steps

1. **Use skills normally** - The tracking happens automatically across all projects
2. **Review weekly** - Run `~/.claude/scripts/analyze-skills.py` to see patterns
3. **Identify opportunities** - Find repetitive tasks that could become new skills
4. **Optimize workflows** - Use insights to improve your skill usage

For more information about hooks, see the [Claude Code hooks documentation](https://github.com/anthropics/claude-code/tree/main/examples/hooks).
