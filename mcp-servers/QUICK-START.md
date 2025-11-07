# MCP Server Quick Start Guide

Get up and running with MCP servers in 5 minutes.

## What You'll Get

A zero-token skill lister that makes `/skills` command instant and free.

## Prerequisites

```bash
python3 --version  # Must be 3.10+
```

## Installation (3 steps)

### 1. Install MCP SDK

```bash
pip install mcp
```

### 2. Run Setup Script

```bash
cd mcp-servers/skills-lister
./setup.sh
```

The script will:
- Check Python version
- Install MCP SDK (if needed)
- Make scripts executable
- Generate configuration
- Optionally create `.claude/mcp.json`

### 3. Configure Claude

**For Claude Desktop:**

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "/FULL/PATH/TO/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
```

**For Claude Code:**

The setup script can create `.claude/mcp.json` for you, or create it manually:

```bash
mkdir -p .claude
cat > .claude/mcp.json << 'EOF'
{
  "mcpServers": {
    "skills-lister": {
      "command": "python3",
      "args": [
        "/FULL/PATH/TO/mcp-servers/skills-lister/server.py"
      ]
    }
  }
}
EOF
```

Replace `/FULL/PATH/TO/` with the actual absolute path!

## Restart Claude

**Claude Desktop:** Quit and relaunch

**Claude Code:** Exit and start new session

## Test It

Ask Claude:
```
Can you list the available skills?
```

You should see the skills list appear instantly with **0 tokens used**.

## Before vs After

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Tokens | 5,000+ | 0 | 100% reduction |
| Time | 3-5 sec | <1 sec | 5x faster |
| Cost | ~$0.015 | $0 | Free! |

## Troubleshooting

### "Script not found"

```bash
ls -l ~/bin/list-skills.sh
# If missing:
cp scripts/list-skills.sh ~/bin/
chmod +x ~/bin/list-skills.sh
```

### "Module not found: mcp"

```bash
pip install mcp
```

### Server not appearing

1. Check JSON syntax (use a validator)
2. Use absolute paths (no `~`)
3. Restart Claude after config changes
4. Check Claude logs for errors

### Still having issues?

See detailed documentation:
- [INSTALL.md](INSTALL.md) - Full installation guide
- [skills-lister/README.md](skills-lister/README.md) - Server documentation
- [README.md](README.md) - Overview and architecture

## Next Steps

Once working, you can:
1. Create more MCP servers for other operations
2. Customize output formats
3. Add search/filter capabilities
4. Build tool integrations

## Key Files

```
mcp-servers/
├── QUICK-START.md          ← You are here
├── INSTALL.md              ← Detailed setup
├── README.md               ← Overview
└── skills-lister/
    ├── setup.sh            ← Run this first
    ├── server.py           ← MCP server
    └── README.md           ← Server docs
```

## Support

- Issues: [GitHub Issues](https://github.com/dmccreary/claude-skills/issues)
- MCP Docs: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- Claude Code: [claude.ai/code](https://claude.ai/code)
