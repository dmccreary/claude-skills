#!/bin/bash

# validate-learning-graph.sh
# Validates a learning graph JSON file against the learning-graph-schema.json
# Usage: ./validate-learning-graph.sh <path-to-learning-graph.json>

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCHEMA_FILE="$SCRIPT_DIR/learning-graph-schema.json"

# Check if a file was provided
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: No learning graph file specified${NC}"
    echo "Usage: $0 <path-to-learning-graph.json>"
    echo ""
    echo "Example:"
    echo "  $0 ../../docs/vis/combined-viewer/learning-graph.json"
    exit 1
fi

# Get the input file
INPUT_FILE="$1"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${RED}Error: File not found: $INPUT_FILE${NC}"
    exit 1
fi

# Check if schema file exists
if [ ! -f "$SCHEMA_FILE" ]; then
    echo -e "${RED}Error: Schema file not found: $SCHEMA_FILE${NC}"
    exit 1
fi

echo -e "${YELLOW}Validating learning graph...${NC}"
echo "Input file: $INPUT_FILE"
echo "Schema file: $SCHEMA_FILE"
echo ""

# Run Python validation on the input file against the schema
python3 "$SCRIPT_DIR/validate-learning-graph.py" "$INPUT_FILE" "$SCHEMA_FILE"

# Capture exit code
EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ Learning graph is valid!${NC}"
else
    echo -e "${RED}✗ Learning graph validation failed${NC}"
fi

exit $EXIT_CODE
