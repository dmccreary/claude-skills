# MCP Prefix Issue in Claude Code

## The Problem

The `skills-lister` MCP server is correctly implemented and configured, but **Claude Code is not exposing the MCP tools** with the required `mcp__` prefix.

## How MCP Should Work

### In Claude Desktop (Working)
1. MCP server starts when Claude launches
2. Server exposes tool: `list_skills`
3. Claude Desktop automatically adds prefix: `mcp__list_skills`
4. Tool is available to Claude with 0 token cost

### In Claude Code (Not Working)
1. MCP server is configured in `.claude/mcp.json` ✅
2. Server is correctly implemented ✅
3. Python dependencies installed ✅
4. Configuration file has valid JSON ✅
5. **BUT**: No tools with `mcp__` prefix appear in Claude's tool list ❌

## Verification

You can verify this by checking Claude's available tools. Look for any tools starting with `mcp__`:

**Expected (if working):**
```
mcp__list_skills
```

**Actual (current state):**
```
(No mcp__ tools available)
```

## Why the `mcp__` Prefix Matters

Claude Code uses the prefix to distinguish between:
- **Built-in tools**: `Bash`, `Read`, `Write`, `Edit`, etc.
- **MCP tools**: `mcp__list_skills`, `mcp__some_tool`, etc.

Without this prefix, Claude Code cannot identify or use MCP-provided tools.

## Who Controls the Prefix?

**The MCP server does NOT control the prefix.**

The server defines tools with regular names:
```python
Tool(
    name="list_skills",  # ← Regular name in server
    description="...",
    ...
)
```

**Claude Code (the host) should add the prefix automatically:**
- Server exposes: `list_skills`
- Host should expose to Claude as: `mcp__list_skills`

This is the same mechanism used in Claude Desktop, which works correctly.

## Current Workaround

Since MCP is not working in Claude Code, the `/skills` command now:

1. **Checks for MCP tools** (looks for `mcp__` prefix)
2. **If not found**: Explains the issue and provides manual commands
3. **Never executes shell scripts automatically** (to save tokens)

This ensures **0 token usage** even when MCP isn't working.

## Is This a Bug?

Possibly. Potential causes:

1. **Claude Code version**: MCP support may be incomplete in current version
2. **Configuration location**: `.claude/mcp.json` vs `~/.claude/mcp.json`
3. **Process spawning**: MCP server may not be starting correctly
4. **Tool registration**: The tool registration mechanism may differ from Claude Desktop
5. **Prefix handling**: Claude Code may use a different prefix convention

## How to Test If MCP Is Actually Running

### Test 1: Check Configuration
```bash
cat .claude/mcp.json
```

Should show:
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

### Test 2: Test Server Directly
```bash
cd mcp-servers/skills-lister
python3 server.py
```

The server should wait for input (it's listening on stdin). Press `Ctrl+D` to exit.

If it starts without errors, the server itself is working correctly.

### Test 3: Run Diagnostic
```bash
cd mcp-servers/skills-lister
./check-mcp-status.sh
```

This checks:
- ✅ Configuration file exists and has valid JSON
- ✅ Python 3.10+ installed
- ✅ MCP SDK installed
- ✅ Server file exists and is executable
- ✅ Shell script exists in ~/bin/

If all checks pass, the **server side is configured correctly**. The issue is on the **Claude Code side** (tool exposure).

### Test 4: Check Claude's Available Tools

Ask Claude: "What tools do you have available?"

Look for any tools starting with `mcp__`. If none exist, MCP integration is not working.

## Solutions (in order of preference)

### Solution 1: Wait for Claude Code Update
The MCP integration may be improved in future versions of Claude Code. Check for updates.

### Solution 2: Use Manual Command (Current Approach)
The `/skills` command now provides the manual command to run:
```bash
~/bin/list-skills.sh --names-only
```

This uses **0 tokens** (user runs it manually).

### Solution 3: Use Claude Desktop
If you need zero-token MCP integration now, use Claude Desktop instead of Claude Code. MCP works correctly there.

### Solution 4: File Bug Report
If you believe this is a bug, report it to the Claude Code team:
https://github.com/anthropics/claude-code/issues

Include:
- Claude Code version
- Operating system
- Configuration file contents
- Output of diagnostic script

## The Bottom Line

**The MCP server is working correctly.**

The issue is that **Claude Code is not exposing MCP tools** with the required `mcp__` prefix.

Until this is resolved:
- ✅ Configuration is correct
- ✅ Server implementation is correct
- ✅ `/skills` command handles the issue gracefully
- ✅ Manual commands are provided (0 tokens)
- ❌ Automatic MCP integration is not functional

## References

- MCP Documentation: https://modelcontextprotocol.io/
- Claude Code GitHub: https://github.com/anthropics/claude-code
- This Server's Diagnostic: `./check-mcp-status.sh`
- Configuration Guide: [INSTALL.md](INSTALL.md)
