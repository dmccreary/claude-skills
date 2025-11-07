#!/usr/bin/env python3
"""
MCP Server for listing Claude skills
Provides zero-token skill listing by executing shell script directly
"""

import json
import subprocess
import os
from pathlib import Path
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

app = Server("skills-lister")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="list_skills",
            description="List all available Claude skills from both user (~/.claude/skills) and project (.claude/skills) directories. Returns skill names only for efficient token usage.",
            inputSchema={
                "type": "object",
                "properties": {
                    "format": {
                        "type": "string",
                        "enum": ["names-only", "json", "full"],
                        "description": "Output format: 'names-only' (just names), 'json' (structured data), or 'full' (human-readable with descriptions)",
                        "default": "names-only"
                    }
                },
                "required": []
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name != "list_skills":
        raise ValueError(f"Unknown tool: {name}")

    # Get format from arguments (default to names-only)
    output_format = arguments.get("format", "names-only")

    # Construct path to the shell script
    script_path = os.path.expanduser("~/bin/list-skills.sh")

    # Check if script exists
    if not os.path.exists(script_path):
        return [TextContent(
            type="text",
            text=f"Error: Script not found at {script_path}"
        )]

    # Build command with appropriate flag
    cmd = [script_path]
    if output_format == "json":
        cmd.append("--json")
    elif output_format == "names-only":
        cmd.append("--names-only")
    # For 'full', no flag needed

    try:
        # Execute the shell script
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )

        output = result.stdout.strip()

        # Format the response based on output type
        if output_format == "json":
            # Validate JSON and pretty-print if requested
            try:
                parsed = json.loads(output)
                formatted_output = json.dumps(parsed, indent=2)
                return [TextContent(
                    type="text",
                    text=formatted_output
                )]
            except json.JSONDecodeError:
                return [TextContent(
                    type="text",
                    text=output
                )]
        else:
            # Return raw output for names-only or full format
            return [TextContent(
                type="text",
                text=output
            )]

    except subprocess.TimeoutExpired:
        return [TextContent(
            type="text",
            text="Error: Script execution timed out after 10 seconds"
        )]
    except subprocess.CalledProcessError as e:
        return [TextContent(
            type="text",
            text=f"Error executing script:\n{e.stderr}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Unexpected error: {str(e)}"
        )]

async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
