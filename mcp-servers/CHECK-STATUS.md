# MCP Server Status Check

## How to Tell if MCP Server is Running

### Method 1: Look for the Fallback Message (Easiest)

Run `/skills` and check the output:

**❌ MCP NOT Running:**
```
⏺ I don't have access to the list_skills MCP tool,
  so I'll use the shell script fallback:
⏺ Bash(~/bin/list-skills.sh --names-only)
```
You see "fallback" message and Bash command.

**✅ MCP IS Running:**
```
⏺ Available Claude Skills
  Found 16 skills: ...
```
No "fallback" message, no Bash command shown, instant results.

### Method 2: Check Configuration Files

```bash
# Project-specific config
ls -la $HOME/Documents/ws/claude-skills/.claude/mcp.json

# Global config
ls -la ~/.claude/mcp.json
```

**Your Status:**
- ✅ Project config exists: `$HOME/Documents/ws/claude-skills/.claude/mcp.json`
- ❌ Global config: Not found (not needed if project config exists)

### Method 3: Validate Configuration

```bash
# Check JSON is valid
python3 -c "import json; json.load(open('$HOME/Documents/ws/claude-skills/.claude/mcp.json'))"

# View configuration
cat $HOME/Documents/ws/claude-skills/.claude/mcp.json
```

**Your Config Status:**
```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "$HOME/Documents/ws/claude-skills/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
```
✅ Valid JSON
✅ Correct structure
✅ Path is absolute

### Method 4: Verify Prerequisites

```bash
# Check Python version (need 3.10+)
python3 --version

# Check MCP SDK installed
python3 -c "import mcp; print('✅ MCP SDK installed')"

# Check server file exists and is executable
ls -lh $HOME/Documents/ws/claude-skills/mcp-servers/skills-lister/server.py

# Check shell script exists
ls -lh ~/bin/list-skills.sh
```

**Your Status:**
- ✅ Python: Installed
- ✅ MCP SDK: Installed
- ✅ server.py: Exists and is executable (3.8K, rwxr-xr-x)
- ✅ Shell script: Exists at ~/bin/list-skills.sh

### Method 5: Test Server Manually

```bash
cd $HOME/Documents/ws/claude-skills/mcp-servers/skills-lister
python3 server.py
```

**Expected behavior:**
- Server starts and waits for input (cursor hangs)
- No error messages
- Press `Ctrl+D` or `Ctrl+C` to exit

**If you see errors:**
- Check import errors → Install MCP: `pip install mcp`
- Check file not found → Verify paths in config

### Method 6: Check Claude Code Startup

When you start Claude Code in this project, it should:
1. Load the `.claude/mcp.json` configuration
2. Initialize the MCP server
3. Make `list_skills` tool available

**To see startup logs** (if Claude Code shows them):
- Look for "Loading MCP servers..."
- Look for "skills-lister: connected" or similar

### Method 7: Diagnostic Script

Run this comprehensive check:

```bash
#!/bin/bash
echo "=== MCP Server Status Check ==="
echo ""

echo "1. Configuration file:"
if [ -f "$HOME/Documents/ws/claude-skills/.claude/mcp.json" ]; then
    echo "   ✅ Found at: $HOME/Documents/ws/claude-skills/.claude/mcp.json"
    if python3 -c "import json; json.load(open('$HOME/Documents/ws/claude-skills/.claude/mcp.json'))" 2>/dev/null; then
        echo "   ✅ Valid JSON"
    else
        echo "   ❌ Invalid JSON"
    fi
else
    echo "   ❌ Not found"
fi
echo ""

echo "2. MCP SDK:"
if python3 -c "import mcp" 2>/dev/null; then
    echo "   ✅ Installed"
else
    echo "   ❌ Not installed (run: pip install mcp)"
fi
echo ""

echo "3. Server file:"
if [ -f "$HOME/Documents/ws/claude-skills/mcp-servers/skills-lister/server.py" ]; then
    echo "   ✅ Found"
    if [ -x "$HOME/Documents/ws/claude-skills/mcp-servers/skills-lister/server.py" ]; then
        echo "   ✅ Executable"
    else
        echo "   ⚠️  Not executable (run: chmod +x server.py)"
    fi
else
    echo "   ❌ Not found"
fi
echo ""

echo "4. Shell script:"
if [ -f ~/bin/list-skills.sh ]; then
    echo "   ✅ Found at ~/bin/list-skills.sh"
else
    echo "   ❌ Not found at ~/bin/list-skills.sh"
fi
echo ""

echo "5. Test import server module:"
if python3 -c "import sys; sys.path.insert(0, '$HOME/Documents/ws/claude-skills/mcp-servers/skills-lister'); import server" 2>/dev/null; then
    echo "   ✅ Server module imports successfully"
else
    echo "   ❌ Import error"
fi
echo ""

echo "=== Summary ==="
echo ""
echo "If all checks pass, the MCP server should work."
echo "If Claude Code still shows 'fallback' message:"
echo "  1. Restart Claude Code (exit and relaunch)"
echo "  2. Make sure you're in the correct project directory"
echo "  3. Check Claude Code logs for errors"
echo ""
```

Save this as `check-mcp-status.sh` and run it:

```bash
cd $HOME/Documents/ws/claude-skills/mcp-servers/skills-lister
chmod +x check-mcp-status.sh
./check-mcp-status.sh
```

## Your Current Status Summary

Based on the checks run:

### Configuration ✅
- ✅ Config file exists: `.claude/mcp.json`
- ✅ JSON is valid
- ✅ Structure is correct
- ✅ Path is absolute

### Prerequisites ✅
- ✅ Python 3.10+ installed
- ✅ MCP SDK installed
- ✅ server.py exists and is executable
- ✅ Shell script exists

### What This Means

**Everything is configured correctly!**

If you're still seeing the "fallback" message, it means:
1. **Claude Code hasn't loaded the MCP config yet**
   - Solution: Restart Claude Code completely

2. **You're in a different session/project**
   - Solution: Make sure you're in the `$HOME/Documents/ws/claude-skills` directory

3. **Claude Code is caching the old state**
   - Solution: Exit completely and start fresh

## Next Steps

### If Still Seeing Fallback Message:

1. **Exit Claude Code completely**
   ```
   Exit the current session entirely
   ```

2. **Restart Claude Code in this project**
   ```bash
   cd $HOME/Documents/ws/claude-skills
   # Start Claude Code here
   ```

3. **Test with `/skills`**
   - Should NOT see "fallback" message
   - Should be instant (<1 sec)
   - Should use 0 tokens

### If Still Not Working:

Check Claude Code startup logs for:
- MCP server initialization messages
- Any error messages about skills-lister
- Permission or path errors

## Expected Behavior After Restart

**Before (current):**
```
/skills
⏺ I don't have access to the list_skills MCP tool...
⏺ Bash(~/bin/list-skills.sh --names-only)
[~1,000 tokens used]
```

**After (with MCP working):**
```
/skills
⏺ Available Claude Skills
  Found 16 skills: ...
[0 tokens used, <1 second]
```

The key difference: **No "fallback" message = MCP is working!**
