#!/bin/bash
# uncomment-images.sh — Remove HTML comment wrappers from image references
# in a story index.md file.
#
# Usage: uncomment-images.sh <path-to-index.md>
#
# Converts lines like:
#   <!-- ![Cover image](./cover.png) -->
#   <!-- ![](./panel-01.png) -->
# Into:
#   ![Cover image](./cover.png)
#   ![](./panel-01.png)
#
# Only affects lines matching the pattern <!-- ![...](...) -->
# Other HTML comments are left untouched.

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <path-to-index.md>"
    echo "Example: $0 docs/stories/dragon-layoffs/index.md"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "Error: File not found: $FILE"
    exit 1
fi

# Count commented images before
BEFORE=$(grep -c '<!-- !\[' "$FILE" 2>/dev/null || true)

if [ "$BEFORE" -eq 0 ]; then
    echo "No commented-out images found in $FILE"
    exit 0
fi

# Remove <!-- ... --> wrapper around image markdown references
# Handles both ![alt text](path) and ![](path) forms
sed -i '' 's|<!-- \(!\[.*\](\.\/[^)]*)\) -->|\1|g' "$FILE"

# Count remaining commented images after
AFTER=$(grep -c '<!-- !\[' "$FILE" 2>/dev/null || true)
UNCOMMENTED=$((BEFORE - AFTER))

echo "Uncommented $UNCOMMENTED image(s) in $FILE"
if [ "$AFTER" -gt 0 ]; then
    echo "Warning: $AFTER commented image(s) remain (may have unexpected formatting)"
fi
