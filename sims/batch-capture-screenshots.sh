#!/bin/bash
# Batch Screenshot Capture for MicroSims
# Captures screenshots for all MicroSims that don't have PNG images

SIMS_DIR="/Users/dan/Documents/ws/claude-skills/docs/sims"
CAPTURE_SCRIPT="/Users/dan/.claude/skills/microsim-screen-capture/scripts/capture_screenshot.sh"

# List of MicroSims needing screenshots
MICROSIMS=(
  "adding-taxonomy-workflow"
  "average-dependencies-distribution"
  "book-levels"
  "chapter-index-structure"
  "chapter-organization-workflow"
  "claude-code-timeline"
  "concept-length-histogram"
  "course-description-quality-workflow"
  "dag-validation-algorithm"
  "faq-pattern-analysis"
  "git-workflow-skill-development"
  "graph-viewer"
  "learning-graph-json-schema"
  "linear-chain-vs-network"
  "microsim-file-relationship-diagram"
  "mkdocs-build-process"
  "mkdocs-github-pages-deployment"
  "orphaned-nodes-identification"
  "p5js-architecture"
  "security-zones-diagram"
  "skill-directory-structure"
  "skill-installation-workflow"
  "taxonomy-distribution-pie"
  "terminal-workflow-textbook"
  "test-world-cities"
)

echo "========================================"
echo "Batch MicroSim Screenshot Capture"
echo "========================================"
echo "Total MicroSims to process: ${#MICROSIMS[@]}"
echo ""

SUCCESS_COUNT=0
FAIL_COUNT=0

for microsim in "${MICROSIMS[@]}"; do
  microsim_path="$SIMS_DIR/$microsim"

  echo "----------------------------------------"
  echo "Processing: $microsim"
  echo "----------------------------------------"

  if [ ! -d "$microsim_path" ]; then
    echo "✗ ERROR: Directory not found: $microsim_path"
    ((FAIL_COUNT++))
    continue
  fi

  if [ ! -f "$microsim_path/main.html" ]; then
    echo "✗ ERROR: main.html not found in $microsim"
    ((FAIL_COUNT++))
    continue
  fi

  # Run capture script
  bash "$CAPTURE_SCRIPT" "$microsim_path"

  if [ $? -eq 0 ]; then
    echo "✓ Screenshot captured successfully"
    ((SUCCESS_COUNT++))
  else
    echo "✗ Screenshot capture failed"
    ((FAIL_COUNT++))
  fi

  echo ""
done

echo "========================================"
echo "SUMMARY"
echo "========================================"
echo "✓ Successful: $SUCCESS_COUNT"
echo "✗ Failed: $FAIL_COUNT"
echo "Total: ${#MICROSIMS[@]}"
echo "========================================"
