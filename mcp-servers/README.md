# MCP Servers for Claude Skills

This directory contains Model Context Protocol (MCP) servers that extend Claude's capabilities with zero-token operations.

!!! Warning
  Claude has been unable to create a MCP that calls a UNIX shell script called list-skills.sh.
  Although it has generate a LOT of code in the skills-lister, it does not work.
  Our goal is to have the /skills command just list the skills installed in the $HOME/.claude/skills and $PROJECT/.claude/skills

## What is MCP?

The Model Context Protocol (MCP) allows Claude to interact with external tools and data sources without using tokens for data processing. MCP servers handle data operations directly and return only results to Claude.

## Available Servers

### skills-lister

Lists all available Claude skills from user and project directories with zero token usage.

**Features:**
- Executes `~/bin/list-skills.sh` directly
- Multiple output formats (names-only, json, full)
- Fast, efficient operation
- No file parsing in Claude

**Directory:** [skills-lister/](skills-lister/)

## Quick Start

### 1. Install MCP SDK

```bash
pip install mcp
```

### 2. Configure Claude

Add MCP servers to your Claude configuration:

**For Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

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

**For Claude Code** (`.claude/mcp.json` in your project or global config):

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "/absolute/path/to/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
```

### 3. Restart Claude

After configuration, restart Claude Desktop or restart your Claude Code session.

## Benefits Over Traditional Approach

| Approach | Token Usage | Speed | Flexibility |
|----------|-------------|-------|-------------|
| Direct file reading | 5,000+ tokens | Slow | Limited |
| Bash command | ~1,000 tokens | Medium | Good |
| MCP Server | **0 tokens** | **Fast** | **Excellent** |

## Development

Each MCP server is a self-contained Python package with:

```
server-name/
├── server.py              # Main MCP server implementation
├── pyproject.toml         # Python package configuration
├── README.md              # Server-specific documentation
├── .gitignore            # Python artifacts to ignore
└── claude_desktop_config.example.json  # Example configuration
```

### Creating a New MCP Server

1. Create a new directory under `mcp-servers/`
2. Implement the MCP protocol using the `mcp` Python SDK
3. Add documentation (README.md)
4. Test with Claude Desktop or Claude Code
5. Update this README to list the new server

### Testing

Each server can be tested independently:

```bash
cd mcp-servers/skills-lister
python3 server.py
```

MCP servers communicate via stdin/stdout using JSON-RPC protocol.

## Troubleshooting

### MCP server not showing up

1. Check JSON syntax in configuration file
2. Verify absolute paths to server.py files
3. Restart Claude after configuration changes
4. Check Claude logs for errors

### Import errors

Make sure the MCP SDK is installed:

```bash
pip install mcp
```

### Permission errors

Ensure server scripts are executable:

```bash
chmod +x mcp-servers/*/server.py
```

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/anthropics/mcp-python-sdk)
- [Claude Code Documentation](https://docs.claude.com/claude-code)

## Contributing

When adding new MCP servers:

1. Follow the existing directory structure
2. Include comprehensive README.md
3. Provide example configurations
4. Add .gitignore for build artifacts
5. Update this main README
6. Test with both Claude Desktop and Claude Code
