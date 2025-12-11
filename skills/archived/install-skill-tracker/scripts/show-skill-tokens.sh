#!/bin/bash
# Display skill usage with token information
# Uses global log directory ~/.claude/activity-logs/

LOG_FILE="$HOME/.claude/activity-logs/skill-usage.jsonl"

if [ ! -f "$LOG_FILE" ]; then
  echo "No skill usage log found at: $LOG_FILE"
  exit 1
fi

echo "Skill Usage with Token Tracking"
echo "================================"
echo ""

# Show recent skill executions with token data
jq -r '
  select(.event == "end") |
  "\(.timestamp)  \(.skill)\n" +
  "  Duration: \(.duration_seconds)s\n" +
  "  Tokens: input=\(.input_tokens // "N/A"), output=\(.output_tokens // "N/A"), total=\(.total_tokens // "N/A")\n"
' "$LOG_FILE" | tail -20

echo ""
echo "Summary Statistics"
echo "=================="

# Calculate total tokens across all skills
jq -s '
  map(select(.event == "end" and .total_tokens != null)) |
  {
    total_executions: length,
    total_tokens: (map(.total_tokens) | add // 0),
    total_input_tokens: (map(.input_tokens) | add // 0),
    total_output_tokens: (map(.output_tokens) | add // 0),
    avg_tokens_per_skill: ((map(.total_tokens) | add // 0) / (length | if . == 0 then 1 else . end))
  } |
  "Total skill executions: \(.total_executions)\n" +
  "Total tokens used: \(.total_tokens)\n" +
  "  Input: \(.total_input_tokens)\n" +
  "  Output: \(.total_output_tokens)\n" +
  "Average tokens per skill: \(.avg_tokens_per_skill | floor)"
' "$LOG_FILE"
