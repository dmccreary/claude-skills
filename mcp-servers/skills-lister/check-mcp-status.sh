#!/bin/bash
# MCP Server Status Diagnostic Script

echo "╔════════════════════════════════════════════╗"
echo "║   MCP Server Status Check                  ║"
echo "║   skills-lister diagnostic                 ║"
echo "╚════════════════════════════════════════════╝"
echo ""

PROJECT_DIR="$HOME/Documents/ws/claude-skills"
CONFIG_FILE="$PROJECT_DIR/.claude/mcp.json"
SERVER_FILE="$PROJECT_DIR/mcp-servers/skills-lister/server.py"
SHELL_SCRIPT="$HOME/bin/list-skills.sh"

CHECKS_PASSED=0
CHECKS_TOTAL=0

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check function
check() {
    ((CHECKS_TOTAL++))
    if [ $1 -eq 0 ]; then
        echo -e "   ${GREEN}✅${NC} $2"
        ((CHECKS_PASSED++))
        return 0
    else
        echo -e "   ${RED}❌${NC} $2"
        if [ -n "$3" ]; then
            echo -e "      ${YELLOW}→${NC} $3"
        fi
        return 1
    fi
}

warn() {
    echo -e "   ${YELLOW}⚠️${NC}  $1"
    if [ -n "$2" ]; then
        echo -e "      ${YELLOW}→${NC} $2"
    fi
}

echo "1. Configuration File"
echo "   ─────────────────"
if [ -f "$CONFIG_FILE" ]; then
    check 0 "Config exists: $CONFIG_FILE"

    if python3 -c "import json; json.load(open('$CONFIG_FILE'))" 2>/dev/null; then
        check 0 "Valid JSON syntax"
    else
        check 1 "Invalid JSON syntax" "Fix JSON errors in $CONFIG_FILE"
    fi

    # Check if skills-lister is configured
    if grep -q "skills-lister" "$CONFIG_FILE"; then
        check 0 "skills-lister configured"
    else
        check 1 "skills-lister not found in config" "Add skills-lister to mcpServers"
    fi
else
    check 1 "Config not found" "Run ./setup.sh to create configuration"
fi
echo ""

echo "2. Python Environment"
echo "   ──────────────────"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Python version: $PYTHON_VERSION"

if python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
    check 0 "Python 3.10+ installed"
else
    check 1 "Python 3.10+ required" "Install Python 3.10 or higher"
fi

if python3 -c "import mcp" 2>/dev/null; then
    check 0 "MCP SDK installed"
else
    check 1 "MCP SDK not installed" "Run: pip install mcp"
fi
echo ""

echo "3. Server Files"
echo "   ────────────"
if [ -f "$SERVER_FILE" ]; then
    check 0 "server.py exists"

    if [ -x "$SERVER_FILE" ]; then
        check 0 "server.py is executable"
    else
        warn "server.py not executable" "Run: chmod +x $SERVER_FILE"
    fi

    # Test import
    if python3 -c "import sys; sys.path.insert(0, '$(dirname $SERVER_FILE)'); import server" 2>/dev/null; then
        check 0 "server.py imports successfully"
    else
        check 1 "server.py import error" "Check for syntax errors or missing dependencies"
    fi
else
    check 1 "server.py not found" "Verify installation in mcp-servers/skills-lister/"
fi
echo ""

echo "4. Shell Script"
echo "   ────────────"
if [ -f "$SHELL_SCRIPT" ]; then
    check 0 "list-skills.sh exists: $SHELL_SCRIPT"

    if [ -x "$SHELL_SCRIPT" ]; then
        check 0 "list-skills.sh is executable"
    else
        warn "list-skills.sh not executable" "Run: chmod +x $SHELL_SCRIPT"
    fi

    # Test execution
    if "$SHELL_SCRIPT" --names-only > /dev/null 2>&1; then
        check 0 "Shell script executes successfully"
    else
        check 1 "Shell script execution failed" "Test manually: $SHELL_SCRIPT --names-only"
    fi
else
    check 1 "list-skills.sh not found" "Copy from scripts/: cp scripts/list-skills.sh ~/bin/"
fi
echo ""

echo "5. Skills Directories"
echo "   ──────────────────"
if [ -d "$HOME/.claude/skills" ]; then
    SKILL_COUNT=$(find "$HOME/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
    check 0 "User skills directory exists (~/.claude/skills)"
    echo "      Found $SKILL_COUNT skills"
else
    warn "User skills directory not found" "No skills in ~/.claude/skills (optional)"
fi

if [ -d "$PROJECT_DIR/.claude/skills" ]; then
    SKILL_COUNT=$(find "$PROJECT_DIR/.claude/skills" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
    check 0 "Project skills directory exists (.claude/skills)"
    echo "      Found $SKILL_COUNT skills"
else
    warn "Project skills directory not found" "No skills in .claude/skills (optional)"
fi
echo ""

echo "╔════════════════════════════════════════════╗"
echo "║   Summary                                  ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo "   Checks passed: $CHECKS_PASSED / $CHECKS_TOTAL"
echo ""

if [ $CHECKS_PASSED -eq $CHECKS_TOTAL ]; then
    echo -e "${GREEN}✅ All checks passed!${NC}"
    echo ""
    echo "   MCP server should be working."
    echo ""
    echo "   If Claude Code still shows 'fallback' message:"
    echo "   1. Exit Claude Code completely"
    echo "   2. Start Claude Code in: $PROJECT_DIR"
    echo "   3. Run: /skills"
    echo "   4. Should see NO 'fallback' message and 0 tokens used"
    echo ""
elif [ $CHECKS_PASSED -gt $((CHECKS_TOTAL * 3 / 4)) ]; then
    echo -e "${YELLOW}⚠️  Most checks passed, but some issues found.${NC}"
    echo ""
    echo "   Review the warnings above and fix any issues."
    echo "   MCP server may still work with minor warnings."
    echo ""
else
    echo -e "${RED}❌ Several checks failed.${NC}"
    echo ""
    echo "   Fix the errors above before MCP server will work."
    echo "   Common fixes:"
    echo "   - Install MCP SDK: pip install mcp"
    echo "   - Run setup: ./setup.sh"
    echo "   - Check file permissions: chmod +x server.py"
    echo ""
fi

echo "╔════════════════════════════════════════════╗"
echo "║   Quick Tests                              ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo "Test shell script directly:"
echo "   $SHELL_SCRIPT --names-only"
echo ""
echo "Test MCP server manually:"
echo "   cd $(dirname $SERVER_FILE)"
echo "   python3 server.py"
echo "   (Press Ctrl+D to exit)"
echo ""
echo "View configuration:"
echo "   cat $CONFIG_FILE"
echo ""
echo "Full documentation:"
echo "   cat $PROJECT_DIR/mcp-servers/ENABLE-MCP.md"
echo ""
