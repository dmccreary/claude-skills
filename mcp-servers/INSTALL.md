# MCP Server Installation Guide

This guide walks you through installing and configuring MCP servers for Claude.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Claude Desktop or Claude Code CLI

## Step 1: Install MCP SDK

```bash
pip install mcp
```

To verify installation:

```bash
python3 -c "import mcp; print('MCP SDK installed successfully')"
```

## Step 2: Locate Your Claude Configuration File

### Claude Desktop

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

### Claude Code CLI

**Project-specific** (recommended):
```
.claude/mcp.json
```

**Global** (all projects):
```
~/.claude/mcp.json
```

## Step 3: Configure MCP Servers

### For Claude Desktop

Create or edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "/ABSOLUTE/PATH/TO/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
```

**Important:** Replace `/ABSOLUTE/PATH/TO/` with the actual path to this repository.

Example for macOS:
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

### For Claude Code CLI

**IMPORTANT**: Claude Code MCP integration requires tools to be exposed with an `mcp__` prefix (e.g., `mcp__list_skills`). As of this writing, Claude Code's MCP integration may not be fully operational.

Create `.claude/mcp.json` in your project root:

```bash
mkdir -p .claude
cat > .claude/mcp.json << 'EOF'
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "/ABSOLUTE/PATH/TO/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
EOF
```

**Note**: Even with proper configuration, you may need to check if your version of Claude Code supports MCP servers. Run the diagnostic to verify:

```bash
cd mcp-servers/skills-lister
./check-mcp-status.sh
```

## Step 4: Make Scripts Executable

```bash
chmod +x mcp-servers/skills-lister/server.py
chmod +x ~/bin/list-skills.sh
```

## Step 5: Restart Claude

**Claude Desktop:** Quit and relaunch the application

**Claude Code:** Exit and start a new session

## Step 6: Verify Installation

Ask Claude to list skills:

```
Can you list the available skills?
```

**Expected behavior if MCP is working:**
- Claude should use the MCP `list_skills` tool automatically
- Zero token usage
- No shell script fallback message

**Current state in Claude Code (as of writing):**
- MCP tools may not be exposed with the required `mcp__` prefix
- The `/skills` command will explain the issue and provide manual commands
- This is a limitation of Claude Code's MCP integration, not the server itself

To verify if MCP is actually working, look for tools starting with `mcp__` in Claude's available tools list.

## Troubleshooting

### "Script not found" error

Verify the shell script exists:

```bash
ls -l ~/bin/list-skills.sh
```

If missing, copy it from the repository:

```bash
cp scripts/list-skills.sh ~/bin/
chmod +x ~/bin/list-skills.sh
```

### "Module not found: mcp" error

The MCP SDK isn't installed. Run:

```bash
pip install mcp
```

If using a virtual environment, make sure it's activated first.

### MCP server not appearing in Claude

1. Check JSON syntax with a validator
2. Verify absolute paths (no `~`, use full paths)
3. Check Claude logs for errors:
   - **macOS:** `~/Library/Logs/Claude/`
   - **Windows:** `%APPDATA%\Claude\Logs\`
   - **Linux:** `~/.local/share/Claude/logs/`

4. Ensure Python 3.10+ is available:

```bash
python3 --version
```

### Permission denied errors

Make all scripts executable:

```bash
find mcp-servers -name "*.py" -type f -exec chmod +x {} \;
```

### Testing the server directly

Test that the MCP server can run:

```bash
cd mcp-servers/skills-lister
python3 server.py
```

Press `Ctrl+D` to send EOF and exit. If it waits for input, the server is working correctly.

## Advanced Configuration

### Multiple MCP Servers

You can configure multiple MCP servers in the same file:

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": ["/path/to/skills-lister/server.py"]
    },
    "another-server": {
      "command": "python3",
      "args": ["/path/to/another-server/server.py"]
    }
  }
}
```

### Using Virtual Environments

If you use a Python virtual environment:

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "/path/to/venv/bin/python3",
      "args": [
        "/path/to/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
```

### Environment Variables

You can pass environment variables to MCP servers:

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": ["/path/to/server.py"],
      "env": {
        "CUSTOM_VAR": "value"
      }
    }
  }
}
```

## Uninstallation

To remove MCP servers:

1. Remove the server entry from your configuration file
2. Restart Claude
3. Optionally uninstall the MCP SDK:

```bash
pip uninstall mcp
```

## Getting Help

- **MCP Documentation:** https://modelcontextprotocol.io/
- **Claude Code Issues:** https://github.com/anthropics/claude-code/issues
- **This Repository:** https://github.com/dmccreary/claude-skills/issues
