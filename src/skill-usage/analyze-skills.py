#!/usr/bin/env python3
"""Analyze skill usage logs to identify patterns, performance metrics, and token usage."""

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import sys
from io import StringIO

def load_jsonl(filepath):
    """Load JSONL file into list of dicts."""
    if not filepath.exists():
        return []
    with open(filepath) as f:
        return [json.loads(line) for line in f if line.strip()]

def format_duration(seconds):
    """Format duration in human-readable format."""
    if seconds == "unknown" or seconds is None:
        return "unknown"
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}m {secs}s"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"

def format_tokens(count):
    """Format token count with K/M suffix."""
    if count is None or count == "null":
        return "N/A"
    count = int(count)
    if count >= 1_000_000:
        return f"{count/1_000_000:.1f}M"
    elif count >= 1_000:
        return f"{count/1_000:.1f}K"
    return str(count)

def correlate_prompts_with_skills(prompts, skill_events):
    """Match user prompts with skill invocations by session ID and timestamp."""
    # Index prompts by session and epoch for better matching
    prompts_by_session = defaultdict(list)
    for prompt in prompts:
        prompts_by_session[prompt['session']].append({
            'epoch': int(prompt['epoch']),
            'prompt': prompt['prompt'],
            'timestamp': prompt['timestamp']
        })

    # Sort prompts by epoch within each session
    for session in prompts_by_session:
        prompts_by_session[session].sort(key=lambda x: x['epoch'])

    # Correlate skill events with nearest preceding prompt
    correlated = []
    for event in skill_events:
        if event['event'] != 'end':
            continue

        session = event['session']
        skill_epoch = int(event['epoch'])

        # Find the most recent prompt before this skill event
        best_prompt = "Unknown prompt"
        session_prompts = prompts_by_session.get(session, [])
        for p in reversed(session_prompts):
            if p['epoch'] <= skill_epoch:
                best_prompt = p['prompt']
                break

        correlated.append({
            'skill': event['skill'],
            'prompt': best_prompt,
            'duration': event.get('duration_seconds', 'unknown'),
            'timestamp': event['timestamp'],
            'session': session,
            'input_tokens': event.get('input_tokens'),
            'output_tokens': event.get('output_tokens'),
            'total_tokens': event.get('total_tokens'),
            'cache_read_tokens': event.get('cache_read_tokens'),
            'cache_creation_tokens': event.get('cache_creation_tokens')
        })

    return correlated

def generate_report(log_dir, project_dir=None):
    """Generate skill usage report and return as string."""
    log_dir = Path(log_dir)
    output = StringIO()

    def write(text=""):
        output.write(text + "\n")

    # Load logs
    prompts = load_jsonl(log_dir / "prompts.jsonl")
    skill_events = load_jsonl(log_dir / "skill-usage.jsonl")

    if not skill_events:
        write("No skill usage data found yet.")
        write(f"Logs will be created in: {log_dir}")
        write("\nUse skills in Claude Code and they'll be tracked automatically.")
        return output.getvalue(), False

    # Correlate prompts with skills
    correlated = correlate_prompts_with_skills(prompts, skill_events)

    write("# Skill Usage Report")
    write()
    write(f"**Project:** {project_dir.name if project_dir else 'Unknown'}<br/>")
    write(f"**Log directory:** `{log_dir}`<br/>")
    write(f"**Total skill invocations:** {len(correlated)}<br/>")
    write(f"**Report generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    write()

    # Skill frequency analysis
    skill_counts = Counter(entry['skill'] for entry in correlated)
    write("## Skill Usage Summary")
    write()
    for skill, count in skill_counts.most_common():
        write(f"- **{skill}**: {count}x")

    # Token usage analysis
    write()
    write("## Token Usage by Skill")
    write()
    skill_tokens = defaultdict(lambda: {
        'input': 0, 'output': 0, 'total': 0,
        'cache_read': 0, 'cache_creation': 0, 'count': 0
    })

    total_tokens_all = 0
    total_cache_read = 0
    total_cache_creation = 0

    for entry in correlated:
        skill = entry['skill']
        skill_tokens[skill]['count'] += 1

        if entry.get('total_tokens') and entry['total_tokens'] != 'null':
            tokens = int(entry['total_tokens'])
            skill_tokens[skill]['total'] += tokens
            total_tokens_all += tokens

        if entry.get('input_tokens') and entry['input_tokens'] != 'null':
            skill_tokens[skill]['input'] += int(entry['input_tokens'])

        if entry.get('output_tokens') and entry['output_tokens'] != 'null':
            skill_tokens[skill]['output'] += int(entry['output_tokens'])

        if entry.get('cache_read_tokens') and entry['cache_read_tokens'] != 'null':
            cache_read = int(entry['cache_read_tokens'])
            skill_tokens[skill]['cache_read'] += cache_read
            total_cache_read += cache_read

        if entry.get('cache_creation_tokens') and entry['cache_creation_tokens'] != 'null':
            cache_create = int(entry['cache_creation_tokens'])
            skill_tokens[skill]['cache_creation'] += cache_create
            total_cache_creation += cache_create

    write("| Skill | Invocations | Total Tokens | Cache Read | Cache Creation |")
    write("|-------|-------------|--------------|------------|----------------|")

    # Sort by total tokens descending
    sorted_skills = sorted(skill_tokens.items(), key=lambda x: x[1]['total'], reverse=True)
    for skill, data in sorted_skills:
        write(f"| {skill} | {data['count']}x | {format_tokens(data['total'])} | {format_tokens(data['cache_read'])} | {format_tokens(data['cache_creation'])} |")

    # Cache efficiency summary
    cache_hit_ratio = 0
    if total_tokens_all > 0:
        cache_hit_ratio = (total_cache_read / total_tokens_all) * 100
        write()
        write("## Token Summary")
        write()
        write(f"| Metric | Value |")
        write(f"|--------|-------|")
        write(f"| Total tokens processed | {format_tokens(total_tokens_all)} |")
        write(f"| Cache reads | {format_tokens(total_cache_read)} ({cache_hit_ratio:.1f}%) |")
        write(f"| Cache creations | {format_tokens(total_cache_creation)} |")
        write(f"| Estimated API cost | ${total_tokens_all * 0.000003:.2f} |")

    # Common prompts that trigger skills
    write()
    write("## Common Prompts")
    write()
    prompt_counts = Counter(entry['prompt'][:100] for entry in correlated if entry['prompt'] != "Unknown prompt")
    shown = 0
    for prompt, count in prompt_counts.most_common(10):
        if count > 1 or shown < 5:
            truncated = prompt[:80] + "..." if len(prompt) > 80 else prompt
            write(f"- {count}x: \"{truncated}\"")
            shown += 1
        if shown >= 10:
            break

    # Recent skill usage table
    write()
    write("## Recent Skill Usage")
    write()
    write("| Timestamp | Skill | Tokens | Prompt (truncated) |")
    write("|-----------|-------|--------|---------------------|")
    for entry in sorted(correlated, key=lambda x: x['timestamp'], reverse=True)[:20]:
        tokens = format_tokens(entry.get('total_tokens'))
        prompt_short = entry['prompt'][:50].replace('|', '\\|').replace('\n', ' ')
        write(f"| {entry['timestamp']} | {entry['skill']} | {tokens} | {prompt_short}... |")

    # Insights
    write()
    write("## Insights")
    write()

    # Find frequently used skills
    frequent_skills = [s for s, c in skill_counts.items() if c >= 3]
    if frequent_skills:
        write("### Frequently Used Skills")
        write()
        for skill in frequent_skills[:5]:
            count = skill_counts[skill]
            tokens = skill_tokens[skill]['total']
            write(f"- **{skill}** ({count}x, {format_tokens(tokens)} tokens)")
        write()

    # Token-heavy skills
    if sorted_skills:
        write("### Most Token-Intensive Skills")
        write()
        for skill, data in sorted_skills[:3]:
            avg_tokens = data['total'] / data['count'] if data['count'] > 0 else 0
            write(f"- **{skill}**: {format_tokens(data['total'])} total ({format_tokens(avg_tokens)} avg)")
        write()

    # Cache efficiency
    if total_tokens_all > 0:
        write("### Cache Efficiency")
        write()
        if cache_hit_ratio > 70:
            write(f"✅ Good cache utilization ({cache_hit_ratio:.1f}% cache hits)")
        elif cache_hit_ratio > 40:
            write(f"⚠️ Moderate cache utilization ({cache_hit_ratio:.1f}% cache hits)")
        else:
            write(f"❌ Low cache utilization ({cache_hit_ratio:.1f}% cache hits)")

    return output.getvalue(), True

def analyze_skill_usage(log_dir, output_file=None, project_dir=None):
    """Analyze skill usage patterns and generate report."""
    report, success = generate_report(log_dir, project_dir)

    # Always print to stdout
    print(report)

    # Write to file if specified
    if output_file and success:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(report)
        print(f"\n📄 Report saved to: {output_path}")

    return success

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze skill usage logs')
    parser.add_argument('log_dir', nargs='?', help='Log directory path')
    parser.add_argument('-o', '--output', help='Output markdown file path')
    parser.add_argument('-p', '--project', help='Project directory (for context)')

    args = parser.parse_args()

    # Determine log directory
    if args.log_dir:
        log_dir = Path(args.log_dir)
    else:
        log_dir = Path.cwd() / ".claude" / "activity-logs"

    # Determine project directory
    if args.project:
        project_dir = Path(args.project)
    elif args.log_dir:
        # Assume log_dir is inside project/.claude/activity-logs
        project_dir = Path(args.log_dir).parent.parent.parent
    else:
        project_dir = Path.cwd()

    # Determine output file
    output_file = None
    if args.output:
        output_file = args.output
    else:
        # Default: write to project's docs/learning-graph/skill-usage.md
        default_output = project_dir / "docs" / "learning-graph" / "skill-usage.md"
        if default_output.parent.exists():
            output_file = default_output

    if not log_dir.exists():
        print(f"Log directory not found: {log_dir}")
        print("\nHooks will create this directory on first skill usage.")
        print("\nTip: You can specify a log directory as an argument:")
        print(f"  {sys.argv[0]} /path/to/.claude/activity-logs")
        return

    analyze_skill_usage(log_dir, output_file, project_dir)

if __name__ == "__main__":
    main()
