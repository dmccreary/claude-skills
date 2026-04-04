#!/usr/bin/env bash
# render-mascot-test.sh — Replace {MASCOT_NAME} in the mascot test template
# and write the result to docs/learning-graph/mascot-render-test.md
#
# Usage:
#   ./render-mascot-test.sh "Funcy"
#   ./render-mascot-test.sh "Professor Pixel"
#
# Must be run from the project root (where mkdocs.yml lives).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$SCRIPT_DIR/../references/assets/templates/docs/learning-graph/mascot-render-test.md"
OUTPUT="docs/learning-graph/mascot-render-test.md"

if [ $# -lt 1 ]; then
    echo "Usage: $(basename "$0") <mascot-name>"
    echo "Example: $(basename "$0") \"Funcy\""
    exit 1
fi

MASCOT_NAME="$1"

if [ ! -f "$TEMPLATE" ]; then
    echo "Error: Template not found at $TEMPLATE"
    exit 1
fi

mkdir -p "$(dirname "$OUTPUT")"

sed "s/{MASCOT_NAME}/$MASCOT_NAME/g" "$TEMPLATE" > "$OUTPUT"

echo "Created $OUTPUT with mascot name: $MASCOT_NAME"
