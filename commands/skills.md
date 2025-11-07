---
description: List all available Claude skills
---

List all available Claude skills efficiently using the best available method.

## Instructions

1. **Check if MCP server is available**:
   - Look for MCP tools that start with `mcp__` prefix in your available tools list
   - Specifically check for: `mcp__list_skills` or similar

2. **If MCP is available**: Call the tool with format "names-only" for fastest response:
   ```
   Tool: mcp__list_skills
   Arguments: { "format": "names-only" }
   ```
   This uses **0 tokens** (ideal).

3. **If MCP is NOT available**: Execute the shell script directly:
   ```bash
   ~/bin/list-skills.sh --names-only
   ```
   This uses approximately **~67 tokens** to display the output (still very efficient).

4. **Present the results**:
   - Show the count of available skills
   - List each skill name (bullet points)
   - Show the actual token cost: "**Token cost:** ~67 tokens" (or "0 tokens" if MCP was used)
   - Keep the presentation concise

5. **If the user wants more details** about a specific skill, offer to read that skill's SKILL.md file

## MCP Tool Formats

The `list_skills` MCP tool supports three output formats:

- **"names-only"** (default, ~267 chars): Just skill names - fastest and most token-efficient
- **"json"** (~5,117 chars): Structured JSON with metadata, counts, and locations
- **"full"** (~5,063 chars): Human-readable format with descriptions

## Token Efficiency Comparison

| Method | Tokens Used | Speed | Notes |
|--------|-------------|-------|-------|
| MCP Server | **0 tokens** | **<1 sec** | Best option (requires setup) |
| Shell Script (via Claude) | **~67 tokens** | ~2 sec | Efficient fallback |
| Direct Reading | 5,000+ tokens | 3-5 sec | NEVER use this method |

**Strategy**: Try MCP first (0 tokens), fall back to shell script (~67 tokens) if MCP unavailable.

## Setup Required

For zero-token operation, the MCP server must be configured in Claude's settings.

If not configured, see: [mcp-servers/QUICK-START.md](../mcp-servers/QUICK-START.md)

Quick setup:
```bash
cd mcp-servers/skills-lister
./setup.sh
```

## Example Usage

**User asks:** "What skills are available?"

**If MCP configured (tools with `mcp__` prefix available):**
```
[Call mcp__list_skills tool with format: "names-only"]
[Present results: Found 16 skills: skill1, skill2, ...]
**Token cost:** 0 tokens ✅
```

**If MCP not configured (no `mcp__` tools available):**
```
[Execute: ~/bin/list-skills.sh --names-only]
[Present results: Found 16 skills: skill1, skill2, ...]
**Token cost:** ~67 tokens
```

## Note for Claude

- **Check for MCP tools FIRST** - Look for tools starting with `mcp__` prefix (0 tokens if available)
- **If MCP unavailable** - Execute the shell script directly (~67 tokens - still very efficient)
- **NEVER read skill files directly** - This would use 5,000+ tokens
- **Always report the actual token cost** in your response
- **Keep output concise** - User just wants to see the list

## Why MCP May Not Work in Claude Code

MCP (Model Context Protocol) servers require tools to be exposed with an `mcp__` prefix (e.g., `mcp__list_skills`).

**The Issue**: Even with correct configuration, Claude Code may not be exposing MCP tools with the required prefix. This is a Claude Code integration issue, not a server configuration issue.

**What This Means**:
- ✅ The MCP server (`skills-lister`) is correctly implemented
- ✅ Configuration file (`.claude/mcp.json`) is valid
- ✅ Python dependencies are installed
- ❌ Claude Code is not exposing tools with `mcp__` prefix

**How to Verify**: Check if any tools starting with `mcp__` appear in Claude's available tools list. If none exist, MCP integration is not operational.

**For detailed technical explanation**, see: [mcp-servers/MCP-PREFIX-ISSUE.md](../mcp-servers/MCP-PREFIX-ISSUE.md)

**To diagnose configuration issues**, run:
```bash
~/Documents/ws/claude-skills/mcp-servers/skills-lister/check-mcp-status.sh
```

## Legacy Behavior

The old version of this command that reads files directly is preserved in [skills-old.md](skills-old.md) for reference.
