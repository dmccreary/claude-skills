#!/bin/bash
# Track skill invocation start time
# Logs are stored globally in ~/.claude/activity-logs/

HOOK_INPUT=$(cat)
TOOL_NAME=$(echo "$HOOK_INPUT" | jq -r '.tool_name')
SKILL_NAME=$(echo "$HOOK_INPUT" | jq -r '.tool_input.skill')
SESSION_ID=$(echo "$HOOK_INPUT" | jq -r '.session_id')
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
EPOCH=$(date '+%s')

# Create global log directory if it doesn't exist
LOG_DIR="$HOME/.claude/activity-logs"
mkdir -p "$LOG_DIR"

# Log skill start with timestamp and project
LOG_FILE="$LOG_DIR/skill-usage.jsonl"
jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg epoch "$EPOCH" \
  --arg sid "$SESSION_ID" \
  --arg proj "$PROJECT_DIR" \
  --arg skill "$SKILL_NAME" \
  --arg event "start" \
  '{timestamp: $ts, epoch: $epoch, session: $sid, project: $proj, skill: $skill, event: $event}' >> "$LOG_FILE"

# Create a temporary file to track start time for duration calculation
TEMP_FILE="$LOG_DIR/skill-start-${SESSION_ID}-${SKILL_NAME}.tmp"
echo "$EPOCH" > "$TEMP_FILE"

# Allow the skill to execute (exit 0 = success)
exit 0
