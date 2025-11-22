# Skills Lister MCP Server

An MCP (Model Context Protocol) server that efficiently lists Claude skills with zero token usage by executing a shell script directly.

## Features

- **Zero-token operation**: Executes `~/bin/list-skills.sh` directly without using LLM tokens
- **Multiple output formats**:
  - `names-only` (default): Just skill names, ~267 chars
  - `json`: Structured JSON with metadata, ~5,117 chars
  - `full`: Human-readable with descriptions, ~5,063 chars
- **Fast execution**: Direct shell script execution, no file parsing in Python
- **Works with both skill directories**:
  - User global: `~/.claude/skills`
  - Project local: `.claude/skills`

## Installation

### Prerequisites

1. Python 3.10 or higher
2. The `list-skills.sh` script installed at `~/bin/list-skills.sh`
3. MCP Python SDK

### Install MCP SDK

```bash
pip install mcp
```

### Install the Server

From the `mcp-servers/skills-lister` directory:

```bash
pip install -e .
```

## Configuration

### For Claude Desktop

Add to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**Linux**: `~/.config/Claude/claude_desktop_config.json`

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

Add to your project's MCP configuration (`.claude/mcp.json` or global config):

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

## Usage

Once configured, the MCP server provides a `list_skills` tool that Claude can call automatically.

### Examples

**List skill names only (most efficient):**
```
Tool: list_skills
Arguments: { "format": "names-only" }
```

**Get structured JSON data:**
```
Tool: list_skills
Arguments: { "format": "json" }
```

**Get full human-readable output:**
```
Tool: list_skills
Arguments: { "format": "full" }
```

### Sample Output

**names-only format:**
```
book-chapter-generator
bubble-chart-generator
chapter-content-generator
course-description-analyzer
...
```

**json format:**
```json
{
  "total": 16,
  "user": 16,
  "project": 0,
  "skills": [
    {
      "name": "book-chapter-generator",
      "description": "Generates chapter structure for intelligent textbooks",
      "location": "user"
    },
    ...
  ]
}
```

## Architecture

```
User Request
    ↓
Claude Code/Desktop
    ↓
MCP Protocol
    ↓
skills-lister MCP Server
    ↓
subprocess.run()
    ↓
~/bin/list-skills.sh
    ↓
Shell script reads SKILL.md files
    ↓
Returns formatted output
```

## Token Efficiency

- **Traditional approach**: Claude reads multiple files, uses ~5,000+ tokens
- **This MCP approach**: Zero tokens used, shell script handles all processing
- **Speedup**: Near-instantaneous response, no LLM processing needed

## Troubleshooting

### Script not found error

Ensure `~/bin/list-skills.sh` exists and is executable:

```bash
chmod +x ~/bin/list-skills.sh
```

### Permission errors

Make sure the server script is executable:

```bash
chmod +x /path/to/mcp-servers/skills-lister/server.py
```

### MCP not showing up in Claude

1. Restart Claude Desktop/Code after configuration changes
2. Check the logs for errors (location varies by platform)
3. Verify JSON configuration syntax is valid

## Development

### Testing the server directly

```bash
cd mcp-servers/skills-lister
python3 server.py
```

The server communicates via stdin/stdout using JSON-RPC, so direct testing requires sending properly formatted MCP messages.

### Testing the shell script

```bash
~/bin/list-skills.sh --names-only
~/bin/list-skills.sh --json
~/bin/list-skills.sh
```

## License

Same as parent repository (see root LICENSE file).

## Related Files

- Shell script: `~/bin/list-skills.sh`
- Slash command: `$HOME/Documents/ws/claude-skills/commands/skills.md`
- Skills directory: `~/.claude/skills/` and `.claude/skills/`
