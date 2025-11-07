#!/bin/bash
# Quick setup script for skills-lister MCP server

set -e

echo "Skills Lister MCP Server Setup"
echo "==============================="
echo ""

# Check Python version
echo "1. Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found: Python $PYTHON_VERSION"

REQUIRED_VERSION="3.10"
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
    echo "   ❌ Error: Python 3.10 or higher required"
    exit 1
fi
echo "   ✓ Python version OK"
echo ""

# Check if MCP is installed
echo "2. Checking MCP SDK..."
if python3 -c "import mcp" 2>/dev/null; then
    echo "   ✓ MCP SDK already installed"
else
    echo "   Installing MCP SDK..."
    pip install mcp
    echo "   ✓ MCP SDK installed"
fi
echo ""

# Make server executable
echo "3. Making server executable..."
chmod +x server.py
echo "   ✓ server.py is executable"
echo ""

# Check for list-skills.sh
echo "4. Checking for list-skills.sh..."
if [ -f ~/bin/list-skills.sh ]; then
    echo "   ✓ Found ~/bin/list-skills.sh"
    chmod +x ~/bin/list-skills.sh
else
    echo "   ⚠️  Warning: ~/bin/list-skills.sh not found"
    echo "   Please ensure the script is installed at ~/bin/list-skills.sh"
fi
echo ""

# Get absolute path to server.py
SERVER_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/server.py"

echo "5. Configuration"
echo "   Add this to your Claude configuration:"
echo ""
echo "   For Claude Desktop:"
echo "   ~/Library/Application Support/Claude/claude_desktop_config.json"
echo ""
echo "   For Claude Code:"
echo "   .claude/mcp.json"
echo ""
echo "   Configuration snippet:"
echo "   {"
echo "     \"mcpServers\": {"
echo "       \"skills-lister\": {"
echo "         \"command\": \"python3\","
echo "         \"args\": ["
echo "           \"$SERVER_PATH\""
echo "         ]"
echo "       }"
echo "     }"
echo "   }"
echo ""

# Offer to create Claude Code config
echo "6. Would you like to create a .claude/mcp.json in this project? (y/n)"
read -r RESPONSE
if [[ "$RESPONSE" =~ ^[Yy]$ ]]; then
    # Go to repository root
    REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
    mkdir -p "$REPO_ROOT/.claude"

    # Create mcp.json
    cat > "$REPO_ROOT/.claude/mcp.json" << EOF
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "$SERVER_PATH"
      ]
    }
  }
}
EOF
    echo "   ✓ Created $REPO_ROOT/.claude/mcp.json"
    echo ""
fi

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Restart Claude Desktop or Claude Code"
echo "2. Test by asking Claude to list skills"
echo ""
echo "For more information, see:"
echo "- README.md (server documentation)"
echo "- ../INSTALL.md (detailed installation guide)"
