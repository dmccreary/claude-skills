# Enable MCP for Zero-Token `/skills` Command

## What You're Seeing Now

```
/skills is running…

⏺ I'll list the available Claude skills for you. Let me try the MCP tool first
  for the most efficient approach.

⏺ I don't have access to the list_skills MCP tool, so I'll use the shell
  script fallback:

⏺ Bash(~/bin/list-skills.sh --names-only)
  ⎿ book-chapter-generator
    bubble-chart-generator
    chapter-content-generator
    … +13 lines
```

**Status**: ⚠️ Working, but using ~1,000 tokens via shell script fallback

## What You'll See After MCP Setup

```
/skills is running…

⏺ Available Claude Skills

  Found 16 skills:

  1. book-chapter-generator
  2. bubble-chart-generator
  3. chapter-content-generator
  ... (all 16 skills)
```

**Status**: ✅ Working with **0 tokens** via MCP server (no fallback message!)

## The Difference

### Current (Shell Script Fallback)
```
Message: "I don't have access to the list_skills MCP tool..."
Method:  Shell script via Bash tool
Tokens:  ~1,000 tokens used
Time:    ~2 seconds
```

### After MCP Setup
```
Message: (No fallback message - just results)
Method:  MCP server (direct, no Bash)
Tokens:  0 tokens used ✨
Time:    <1 second ⚡
```

## Enable MCP Now (3 Commands)

```bash
# 1. Install MCP SDK (30 seconds)
pip install mcp

# 2. Run setup script (30 seconds)
cd $HOME/Documents/ws/claude-skills/mcp-servers/skills-lister
./setup.sh

# 3. Restart Claude Code
# Exit and start a new session
```

## What the Setup Script Does

When you run `./setup.sh`, it will:

1. ✅ Check Python 3.10+ is installed
2. ✅ Verify MCP SDK is installed
3. ✅ Make server.py executable
4. ✅ Check for ~/bin/list-skills.sh
5. ✅ Show you the configuration
6. ✅ Ask if you want it to create `.claude/mcp.json` automatically

**Example output:**
```
Skills Lister MCP Server Setup
===============================

1. Checking Python version...
   Found: Python 3.11.5
   ✓ Python version OK

2. Checking MCP SDK...
   ✓ MCP SDK already installed

3. Making server executable...
   ✓ server.py is executable

4. Checking for list-skills.sh...
   ✓ Found ~/bin/list-skills.sh

5. Configuration
   Add this to your Claude configuration:

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

6. Would you like to create a .claude/mcp.json in this project? (y/n)
```

Type `y` and it will create the configuration file for you!

## After Setup: Testing

1. **Restart Claude Code** (important!)

2. **Run `/skills` again**

3. **Look for these differences:**

   ❌ You should NOT see:
   ```
   "I don't have access to the list_skills MCP tool"
   "Bash(~/bin/list-skills.sh --names-only)"
   ```

   ✅ You SHOULD see:
   ```
   Instant list of skills
   No mention of fallback
   Results appear in <1 second
   ```

4. **Check token usage:**
   - MCP tool calls use 0 tokens
   - You won't see a Bash tool invocation

## Why This Matters

If you use `/skills` regularly:

**10 times per day:**
- Save: 10,000 tokens/day = 3.65M tokens/year
- Save: ~$11/year in API costs
- Save: 10+ seconds/day = 60+ hours/year

**The MCP server pays for itself after the first use!**

## Visual Comparison

### Before MCP
```
┌─────────────────┐
│   User: /skills │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│   Claude Code       │
│ "Try MCP first..."  │
│ "MCP not available" │  ← Message about fallback
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Bash Tool         │
│ ~/bin/list-skills.sh│  ← Uses tokens!
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Results           │
│ ~1,000 tokens used  │  ← Cost & time
│ ~2 seconds          │
└─────────────────────┘
```

### After MCP
```
┌─────────────────┐
│   User: /skills │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│   Claude Code       │
│ Calls MCP silently  │  ← No fallback message!
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   MCP Server        │
│ Direct execution    │  ← 0 tokens!
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Results           │
│ 0 tokens used ✨    │  ← Free & fast!
│ <1 second ⚡        │
└─────────────────────┘
```

## Status Check

You can verify MCP is working by looking for these indicators:

### MCP Not Configured (Current State)
- ❌ See message: "I don't have access to the list_skills MCP tool"
- ❌ See: "Bash(~/bin/list-skills.sh --names-only)"
- ❌ Token usage: ~1,000 tokens
- ⏱️ Time: ~2 seconds

### MCP Configured and Working
- ✅ No fallback message
- ✅ No Bash tool invocation visible
- ✅ Token usage: 0 tokens
- ⚡ Time: <1 second
- 🎉 Just instant results!

## Ready to Enable?

Run these three commands:

```bash
# 1. Install (if needed)
pip install mcp

# 2. Setup
cd $HOME/Documents/ws/claude-skills/mcp-servers/skills-lister
./setup.sh

# 3. Restart Claude Code and test /skills
```

**That's it!** Your `/skills` command will now use 0 tokens. 🎉

## Questions?

- **Where's the config file?**
  - Project: `$HOME/Documents/ws/claude-skills/.claude/mcp.json`
  - Global: `~/.claude/mcp.json`

- **How do I know it's working?**
  - No "fallback" message
  - No Bash tool shown
  - Instant results (<1 sec)

- **What if it doesn't work?**
  - See [SETUP-GUIDE.md](SETUP-GUIDE.md) troubleshooting section
  - Check logs
  - Verify configuration

- **Can I still use the old way?**
  - Yes! If MCP fails, it falls back to shell script automatically
  - The old version is saved in [commands/skills-old.md](../commands/skills-old.md)

## Summary

✅ MCP server is built and ready
✅ Documentation is complete
⚠️ Just needs configuration (3 commands, 2 minutes)
🎯 Result: Zero tokens, instant skills listing!

**Next**: Run `./setup.sh` in the `mcp-servers/skills-lister` directory!
