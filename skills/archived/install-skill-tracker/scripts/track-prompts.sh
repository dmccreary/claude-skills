#!/bin/bash
# Track user prompts to correlate with skill usage
# Logs are stored globally in ~/.claude/activity-logs/

HOOK_INPUT=$(cat)
PROMPT=$(echo "$HOOK_INPUT" | jq -r '.prompt')
SESSION_ID=$(echo "$HOOK_INPUT" | jq -r '.session_id')
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
EPOCH=$(date '+%s')

# Create global log directory if it doesn't exist
LOG_DIR="$HOME/.claude/activity-logs"
mkdir -p "$LOG_DIR"

# Log prompt with session ID and project for correlation
LOG_FILE="$LOG_DIR/prompts.jsonl"
jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg epoch "$EPOCH" \
  --arg sid "$SESSION_ID" \
  --arg proj "$PROJECT_DIR" \
  --arg p "$PROMPT" \
  '{timestamp: $ts, epoch: $epoch, session: $sid, project: $proj, prompt: $p}' >> "$LOG_FILE"

# Allow the prompt to continue (exit 0 = success)
exit 0
