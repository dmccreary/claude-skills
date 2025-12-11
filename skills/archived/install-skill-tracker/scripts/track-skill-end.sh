#!/bin/bash
# Track skill completion and calculate duration
# Logs are stored globally in ~/.claude/activity-logs/

HOOK_INPUT=$(cat)
TOOL_NAME=$(echo "$HOOK_INPUT" | jq -r '.tool_name')
SKILL_NAME=$(echo "$HOOK_INPUT" | jq -r '.tool_input.skill')
SESSION_ID=$(echo "$HOOK_INPUT" | jq -r '.session_id')
TRANSCRIPT_PATH=$(echo "$HOOK_INPUT" | jq -r '.transcript_path')
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
EPOCH=$(date '+%s')

# Create global log directory if it doesn't exist
LOG_DIR="$HOME/.claude/activity-logs"
mkdir -p "$LOG_DIR"

# Calculate duration if start time exists
TEMP_FILE="$LOG_DIR/skill-start-${SESSION_ID}-${SKILL_NAME}.tmp"
DURATION="unknown"
if [ -f "$TEMP_FILE" ]; then
  START_EPOCH=$(cat "$TEMP_FILE")
  DURATION=$((EPOCH - START_EPOCH))
  # Clean up temp file
  rm -f "$TEMP_FILE"
fi

# Extract token usage from transcript file (JSONL format)
INPUT_TOKENS="null"
OUTPUT_TOKENS="null"
TOTAL_TOKENS="null"
CACHE_READ_TOKENS="null"
CACHE_CREATION_TOKENS="null"

if [ -f "$TRANSCRIPT_PATH" ]; then
  # Get the last line from the JSONL file (most recent message)
  # Then extract usage data from .message.usage
  LAST_MESSAGE=$(tail -1 "$TRANSCRIPT_PATH" 2>/dev/null)

  if [ -n "$LAST_MESSAGE" ]; then
    INPUT_TOKENS=$(echo "$LAST_MESSAGE" | jq -r '.message.usage.input_tokens // null' 2>/dev/null)
    OUTPUT_TOKENS=$(echo "$LAST_MESSAGE" | jq -r '.message.usage.output_tokens // null' 2>/dev/null)
    CACHE_READ_TOKENS=$(echo "$LAST_MESSAGE" | jq -r '.message.usage.cache_read_input_tokens // null' 2>/dev/null)
    CACHE_CREATION_TOKENS=$(echo "$LAST_MESSAGE" | jq -r '.message.usage.cache_creation_input_tokens // null' 2>/dev/null)

    # Calculate total if both input and output are available
    if [ "$INPUT_TOKENS" != "null" ] && [ "$OUTPUT_TOKENS" != "null" ]; then
      TOTAL_TOKENS=$((INPUT_TOKENS + OUTPUT_TOKENS))

      # Add cache tokens if available for a complete picture
      if [ "$CACHE_READ_TOKENS" != "null" ]; then
        TOTAL_TOKENS=$((TOTAL_TOKENS + CACHE_READ_TOKENS))
      fi
      if [ "$CACHE_CREATION_TOKENS" != "null" ]; then
        TOTAL_TOKENS=$((TOTAL_TOKENS + CACHE_CREATION_TOKENS))
      fi
    fi
  fi
fi

# Log skill completion with duration, project, and token usage
LOG_FILE="$LOG_DIR/skill-usage.jsonl"
jq -nc \
  --arg ts "$TIMESTAMP" \
  --arg epoch "$EPOCH" \
  --arg sid "$SESSION_ID" \
  --arg proj "$PROJECT_DIR" \
  --arg skill "$SKILL_NAME" \
  --arg event "end" \
  --arg dur "$DURATION" \
  --argjson in_tok "${INPUT_TOKENS:-null}" \
  --argjson out_tok "${OUTPUT_TOKENS:-null}" \
  --argjson tot_tok "${TOTAL_TOKENS:-null}" \
  --argjson cache_read "${CACHE_READ_TOKENS:-null}" \
  --argjson cache_create "${CACHE_CREATION_TOKENS:-null}" \
  '{timestamp: $ts, epoch: $epoch, session: $sid, project: $proj, skill: $skill, event: $event, duration_seconds: $dur, input_tokens: $in_tok, output_tokens: $out_tok, total_tokens: $tot_tok, cache_read_tokens: $cache_read, cache_creation_tokens: $cache_create}' >> "$LOG_FILE"

# Allow normal completion (exit 0 = success)
exit 0
