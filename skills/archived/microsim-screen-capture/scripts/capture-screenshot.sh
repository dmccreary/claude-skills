#!/bin/bash
# Screenshot capture script for MicroSims using Chrome headless mode
# Usage: ./capture_screenshot.sh <microsim-directory-path>

set -e

if [ $# -eq 0 ]; then
    echo "Error: MicroSim directory path is required"
    echo "Usage: $0 <microsim-directory-path>"
    exit 1
fi

MICROSIM_DIR="$1"

# Validate directory exists
if [ ! -d "$MICROSIM_DIR" ]; then
    echo "Error: Directory does not exist: $MICROSIM_DIR"
    exit 1
fi

# Validate main.html exists
if [ ! -f "$MICROSIM_DIR/main.html" ]; then
    echo "Error: main.html not found in $MICROSIM_DIR"
    exit 1
fi

# Extract MicroSim name from directory path
MICROSIM_NAME=$(basename "$MICROSIM_DIR")

# Construct paths
MAIN_HTML_PATH="$MICROSIM_DIR/main.html"
OUTPUT_IMAGE="$MICROSIM_DIR/${MICROSIM_NAME}.png"

# Get absolute path for file:// URL
ABSOLUTE_PATH=$(cd "$MICROSIM_DIR" && pwd)/main.html

# Chrome paths to try (in order of preference)
CHROME_PATHS=(
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    "/usr/bin/google-chrome"
    "/usr/bin/chromium"
    "google-chrome"
    "chromium"
)

# Find Chrome
CHROME_BIN=""
for path in "${CHROME_PATHS[@]}"; do
    if [ -f "$path" ] || command -v "$path" &> /dev/null; then
        CHROME_BIN="$path"
        break
    fi
done

if [ -z "$CHROME_BIN" ]; then
    echo "Error: Chrome/Chromium not found. Please install Google Chrome."
    exit 1
fi

echo "📸 Capturing screenshot of MicroSim: $MICROSIM_NAME"
echo "   Source: $ABSOLUTE_PATH"
echo "   Output: $OUTPUT_IMAGE"

# Capture screenshot using Chrome headless mode
# Key flags:
#   --headless=new: Use new headless mode
#   --disable-gpu: Disable GPU acceleration for consistency
#   --screenshot: Capture screenshot
#   --window-size: Set viewport size
#   --hide-scrollbars: Remove scrollbars from capture
#   --disable-web-security: Allow loading external resources (CDNs)
#   --allow-file-access-from-files: Allow file:// URLs to load resources
#   --timeout: Give JavaScript time to load and render

"$CHROME_BIN" \
    --headless=new \
    --disable-gpu \
    --screenshot="$OUTPUT_IMAGE" \
    --window-size=1200,800 \
    --hide-scrollbars \
    --disable-web-security \
    --allow-file-access-from-files \
    --timeout=5000 \
    "file://$ABSOLUTE_PATH" \
    2>&1 | grep -v "CVDisplayLink" | grep -v "SharedImageManager" || true

# Verify screenshot was created
if [ -f "$OUTPUT_IMAGE" ]; then
    SIZE=$(ls -lh "$OUTPUT_IMAGE" | awk '{print $5}')
    echo "✅ Screenshot captured successfully: $OUTPUT_IMAGE ($SIZE)"
else
    echo "❌ Failed to capture screenshot"
    exit 1
fi
