# Testing Guide for skills-lister MCP Server

## Overview

This document describes how to test the skills-lister MCP server at various levels.

## Prerequisites

- Python 3.10+
- MCP SDK installed (`pip install mcp`)
- Shell script at `~/bin/list-skills.sh`
- Skills directories populated with SKILL.md files

## Test Levels

### 1. Shell Script Testing (Unit Level)

Test the underlying shell script directly:

```bash
# Test names-only output (fastest)
~/bin/list-skills.sh --names-only

# Expected: One skill name per line
# book-chapter-generator
# bubble-chart-generator
# ...

# Test JSON output
~/bin/list-skills.sh --json

# Expected: Valid JSON with total, user, project, skills array

# Test full output
~/bin/list-skills.sh

# Expected: Human-readable format with descriptions
```

**Validation checklist**:
- [ ] Script exits with status 0
- [ ] Output contains expected skill names
- [ ] JSON output is valid JSON
- [ ] Names-only output has one name per line
- [ ] Execution completes in <3 seconds

### 2. MCP Server Testing (Integration Level)

Test the MCP server in isolation:

#### Test 1: Server Starts Successfully

```bash
cd mcp-servers/skills-lister
python3 server.py &
SERVER_PID=$!

# Server should wait for input on stdin
sleep 1

# Check if process is running
ps -p $SERVER_PID > /dev/null && echo "Server started OK" || echo "Server failed to start"

# Cleanup
kill $SERVER_PID 2>/dev/null
```

**Expected**: Process starts and waits for input.

#### Test 2: Import Check

```bash
python3 -c "
import sys
sys.path.insert(0, 'mcp-servers/skills-lister')
try:
    import server
    print('✓ Server module imports successfully')
except ImportError as e:
    print(f'✗ Import failed: {e}')
    sys.exit(1)
"
```

**Expected**: No import errors.

#### Test 3: Tool Declaration

Test that the server declares its tools correctly (requires MCP testing framework):

```python
# test_tools.py
import asyncio
from server import app

async def test_list_tools():
    tools = await app.list_tools()
    assert len(tools) == 1
    assert tools[0].name == "list_skills"
    assert "format" in tools[0].inputSchema["properties"]
    print("✓ Tool declaration valid")

asyncio.run(test_list_tools())
```

#### Test 4: Tool Execution

```python
# test_execution.py
import asyncio
from server import app

async def test_call_tool():
    # Test names-only format
    result = await app.call_tool("list_skills", {"format": "names-only"})
    assert len(result) == 1
    assert result[0].type == "text"
    assert len(result[0].text) > 0
    print("✓ names-only format works")

    # Test json format
    result = await app.call_tool("list_skills", {"format": "json"})
    assert len(result) == 1
    import json
    data = json.loads(result[0].text)
    assert "total" in data
    assert "skills" in data
    print("✓ json format works")

asyncio.run(test_call_tool())
```

### 3. Claude Integration Testing (End-to-End)

Test with actual Claude integration:

#### Setup

1. Configure MCP server in Claude (see INSTALL.md)
2. Restart Claude
3. Open a new conversation

#### Test Cases

**Test 1: Direct MCP Call**

User message:
```
Can you list all available skills?
```

**Expected behavior**:
- Claude calls `list_skills` tool automatically
- Response appears in <1 second
- Lists all skill names
- Token usage: 0 tokens

**Validation**:
- [ ] Response is fast (<1 second)
- [ ] All skills are listed
- [ ] No errors in Claude logs
- [ ] Token counter shows 0 tokens used for tool call

**Test 2: Slash Command**

User command:
```
/skills
```

**Expected behavior**:
- Slash command expands to prompt
- Claude uses MCP tool if available
- Falls back to shell script if MCP unavailable
- Lists all skills

**Validation**:
- [ ] Command executes successfully
- [ ] Skills are listed
- [ ] Response is formatted nicely

**Test 3: Format Variations**

User message:
```
Can you list the skills in JSON format?
```

**Expected behavior**:
- Claude calls `list_skills` with `format: "json"`
- Returns structured JSON
- Includes metadata (total, user, project counts)

**Validation**:
- [ ] JSON output is valid
- [ ] Contains expected fields
- [ ] Counts are accurate

**Test 4: Error Handling**

Temporarily rename or move `~/bin/list-skills.sh`, then:

User message:
```
List the skills
```

**Expected behavior**:
- Claude calls MCP tool
- MCP server detects missing script
- Returns error message
- Claude presents user-friendly error

**Validation**:
- [ ] Error is caught gracefully
- [ ] Error message is clear
- [ ] No stack traces shown to user
- [ ] Claude suggests troubleshooting steps

### 4. Performance Testing

#### Latency Test

```bash
time python3 -c "
import asyncio
from server import app

async def measure():
    import time
    start = time.time()
    await app.call_tool('list_skills', {'format': 'names-only'})
    end = time.time()
    print(f'Execution time: {(end-start)*1000:.0f}ms')

asyncio.run(measure())
"
```

**Expected**: <1000ms (preferably <500ms)

#### Throughput Test

```bash
# Test 10 concurrent calls
python3 -c "
import asyncio
from server import app
import time

async def call():
    return await app.call_tool('list_skills', {'format': 'names-only'})

async def measure():
    start = time.time()
    tasks = [call() for _ in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f'10 calls in {(end-start)*1000:.0f}ms')
    print(f'Average: {(end-start)*100:.0f}ms per call')

asyncio.run(measure())
"
```

**Expected**: All calls complete successfully, average <1000ms per call

### 5. Regression Testing

After making changes, verify:

#### Checklist

- [ ] Shell script still works standalone
- [ ] Server starts without errors
- [ ] All three formats (names-only, json, full) work
- [ ] Error handling works correctly
- [ ] Performance is acceptable (<1s)
- [ ] Claude integration works
- [ ] Documentation is up-to-date

#### Quick Regression Test Script

```bash
#!/bin/bash
# regression-test.sh

echo "=== Skills Lister Regression Tests ==="
echo ""

# Test 1: Shell script
echo "Test 1: Shell script (names-only)"
if ~/bin/list-skills.sh --names-only > /dev/null 2>&1; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
    exit 1
fi

# Test 2: Shell script JSON
echo "Test 2: Shell script (json)"
if ~/bin/list-skills.sh --json | python3 -m json.tool > /dev/null 2>&1; then
    echo "✓ PASS (valid JSON)"
else
    echo "✗ FAIL (invalid JSON)"
    exit 1
fi

# Test 3: Python imports
echo "Test 3: Python imports"
if python3 -c "import sys; sys.path.insert(0, 'mcp-servers/skills-lister'); import server" 2>/dev/null; then
    echo "✓ PASS"
else
    echo "✗ FAIL"
    exit 1
fi

# Test 4: Server tool declaration
echo "Test 4: Tool declaration"
python3 << 'EOF'
import sys
import asyncio
sys.path.insert(0, 'mcp-servers/skills-lister')
from server import app

async def test():
    tools = await app.list_tools()
    assert len(tools) == 1
    assert tools[0].name == "list_skills"
    print("✓ PASS")

asyncio.run(test())
EOF

echo ""
echo "=== All Tests Passed ==="
```

Make it executable and run:
```bash
chmod +x regression-test.sh
./regression-test.sh
```

## Common Issues and Solutions

### Issue: "Module not found: mcp"

**Solution**:
```bash
pip install mcp
```

### Issue: "Script not found at ~/bin/list-skills.sh"

**Solution**:
```bash
cp scripts/list-skills.sh ~/bin/
chmod +x ~/bin/list-skills.sh
```

### Issue: Server hangs on startup

**Cause**: MCP servers use stdin/stdout for communication

**Solution**: This is normal behavior. Server waits for JSON-RPC input. Test with Claude integration instead.

### Issue: JSON parsing error

**Cause**: Shell script output is not valid JSON

**Solution**:
```bash
# Test JSON output
~/bin/list-skills.sh --json | python3 -m json.tool
```

If invalid, check for stray output in shell script.

### Issue: Performance slower than expected

**Cause**: Many skills or slow file I/O

**Solutions**:
1. Add caching layer
2. Pre-generate skill index
3. Use SSD for faster I/O

## Continuous Integration

### GitHub Actions Workflow (Future)

```yaml
# .github/workflows/test-mcp.yml
name: MCP Server Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install mcp

      - name: Run tests
        run: |
          cd mcp-servers/skills-lister
          ./regression-test.sh
```

## Test Coverage Goals

- **Shell script**: 100% (all output modes)
- **MCP server**: 80%+ (all tool calls, error handling)
- **Integration**: Manual testing until automated framework available
- **Performance**: <1s response time, 0 token usage

## Reporting Issues

When reporting issues, include:

1. **Environment**:
   - OS and version
   - Python version
   - MCP SDK version
   - Claude version

2. **Test that failed**:
   - Which test case
   - Expected vs actual behavior
   - Error messages/logs

3. **Reproduction steps**:
   - Exact commands run
   - Configuration used
   - Any modifications made

4. **Logs**:
   - Claude logs (if applicable)
   - Server stderr output
   - Shell script output

## Next Steps

After all tests pass:

1. Deploy to production (configure in Claude)
2. Monitor for issues
3. Collect user feedback
4. Plan improvements based on usage patterns

## References

- [MCP Testing Documentation](https://github.com/anthropics/mcp-python-sdk/tree/main/tests)
- [Python unittest framework](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/)
