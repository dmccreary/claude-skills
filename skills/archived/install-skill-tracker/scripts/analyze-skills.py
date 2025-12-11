#!/usr/bin/env python3
"""Analyze skill usage logs to identify patterns, performance metrics, and token usage."""

import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import sys

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

def analyze_skill_usage(log_dir):
    """Analyze skill usage patterns and generate report."""
    log_dir = Path(log_dir)

    # Load logs
    prompts = load_jsonl(log_dir / "prompts.jsonl")
    skill_events = load_jsonl(log_dir / "skill-usage.jsonl")

    if not skill_events:
        print("No skill usage data found yet.")
        print(f"Logs will be created in: {log_dir}")
        print("\nUse skills in Claude Code and they'll be tracked automatically.")
        return

    # Correlate prompts with skills
    correlated = correlate_prompts_with_skills(prompts, skill_events)

    print("# Skill Usage Analysis Report\n")
    print(f"**Log directory:** `{log_dir}`")
    print(f"**Total skill invocations:** {len(correlated)}")
    print(f"**Analysis date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Skill frequency analysis
    skill_counts = Counter(entry['skill'] for entry in correlated)
    print("## Most Used Skills\n")
    for skill, count in skill_counts.most_common():
        print(f"- **{skill}**: {count}x")

    # Token usage analysis (NEW)
    print("\n## Token Usage by Skill\n")
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

    print("| Skill | Invocations | Total Tokens | Cache Read | Cache Creation |")
    print("|-------|-------------|--------------|------------|----------------|")

    # Sort by total tokens descending
    sorted_skills = sorted(skill_tokens.items(), key=lambda x: x[1]['total'], reverse=True)
    for skill, data in sorted_skills:
        print(f"| {skill} | {data['count']}x | {format_tokens(data['total'])} | {format_tokens(data['cache_read'])} | {format_tokens(data['cache_creation'])} |")

    # Cache efficiency summary
    if total_tokens_all > 0:
        cache_hit_ratio = (total_cache_read / total_tokens_all) * 100 if total_tokens_all else 0
        print(f"\n**Token Summary:**")
        print(f"- Total tokens processed: {format_tokens(total_tokens_all)}")
        print(f"- Cache reads: {format_tokens(total_cache_read)} ({cache_hit_ratio:.1f}% of total)")
        print(f"- Cache creations: {format_tokens(total_cache_creation)}")
        print(f"- Estimated cost savings from cache: ~${total_cache_read * 0.00000015:.2f}")

    # Duration analysis (with note about what it measures)
    print("\n## Skill Loading Times\n")
    print("*Note: Duration measures skill loading time, not actual work time.*\n")

    skill_durations = defaultdict(list)
    for entry in correlated:
        dur = entry['duration']
        if dur != 'unknown' and dur is not None:
            try:
                skill_durations[entry['skill']].append(int(dur))
            except (ValueError, TypeError):
                pass

    if skill_durations:
        skill_avg_durations = []
        for skill, durations in skill_durations.items():
            if durations:
                avg = sum(durations) / len(durations)
                total = sum(durations)
                skill_avg_durations.append((skill, avg, total, len(durations)))

        skill_avg_durations.sort(key=lambda x: x[2], reverse=True)

        for skill, avg, total, count in skill_avg_durations:
            print(f"- **{skill}**")
            print(f"  - Average: {format_duration(avg)}")
            print(f"  - Total time: {format_duration(total)}")
            print(f"  - Invocations: {count}x")
    else:
        print("No duration data available.")

    # Common prompts that trigger skills
    print("\n## Common Prompts Leading to Skill Usage\n")
    prompt_counts = Counter(entry['prompt'][:100] for entry in correlated if entry['prompt'] != "Unknown prompt")
    shown = 0
    for prompt, count in prompt_counts.most_common(10):
        if count > 1 or shown < 5:
            truncated = prompt[:80] + "..." if len(prompt) > 80 else prompt
            print(f"{count}x: \"{truncated}\"")
            shown += 1
        if shown >= 10:
            break

    # Detailed log
    print("\n## Recent Skill Usage (Last 20)\n")
    print("| Timestamp | Skill | Tokens | Prompt (truncated) |")
    print("|-----------|-------|--------|---------------------|")
    for entry in sorted(correlated, key=lambda x: x['timestamp'], reverse=True)[:20]:
        tokens = format_tokens(entry.get('total_tokens'))
        prompt_short = entry['prompt'][:50].replace('|', '\\|').replace('\n', ' ')
        print(f"| {entry['timestamp']} | {entry['skill']} | {tokens} | {prompt_short}... |")

    # Efficiency suggestions
    print("\n## Insights & Suggestions\n")

    # Find frequently used skills
    frequent_skills = [s for s, c in skill_counts.items() if c >= 3]
    if frequent_skills:
        print("### Frequently Used Skills")
        print("These skills are used often - consider:")
        for skill in frequent_skills[:5]:
            count = skill_counts[skill]
            tokens = skill_tokens[skill]['total']
            print(f"- **{skill}** ({count}x, {format_tokens(tokens)} tokens): Could benefit from optimization or templates")

    # Find token-heavy skills
    if sorted_skills:
        print("\n### Most Token-Intensive Skills")
        print("These skills consume the most tokens:")
        for skill, data in sorted_skills[:3]:
            avg_tokens = data['total'] / data['count'] if data['count'] > 0 else 0
            print(f"- **{skill}**: {format_tokens(data['total'])} total ({format_tokens(avg_tokens)} avg per use)")

    # Cache optimization opportunities
    if total_tokens_all > 0:
        print("\n### Cache Efficiency")
        if cache_hit_ratio > 70:
            print(f"✅ Good cache utilization ({cache_hit_ratio:.1f}% cache hits)")
        elif cache_hit_ratio > 40:
            print(f"⚠️ Moderate cache utilization ({cache_hit_ratio:.1f}% cache hits)")
            print("   Consider reusing context across skill invocations")
        else:
            print(f"❌ Low cache utilization ({cache_hit_ratio:.1f}% cache hits)")
            print("   Significant optimization opportunity - try batching related skill uses")

    print(f"\n### Total Resources Used")
    print(f"- Total tokens: **{format_tokens(total_tokens_all)}**")
    print(f"- Estimated API cost: **${total_tokens_all * 0.000003:.2f}** (at $3/1M tokens)")

def main():
    """Main entry point."""
    # Default log directory - use global ~/.claude/activity-logs
    log_dir = Path.home() / ".claude" / "activity-logs"

    # Allow override from command line
    if len(sys.argv) > 1:
        log_dir = Path(sys.argv[1])

    if not log_dir.exists():
        print(f"Log directory not found: {log_dir}")
        print("\nHooks will create this directory on first skill usage.")
        print("\nTip: You can specify a log directory as an argument:")
        print(f"  {sys.argv[0]} /path/to/.claude/activity-logs")
        return

    analyze_skill_usage(log_dir)

if __name__ == "__main__":
    main()
