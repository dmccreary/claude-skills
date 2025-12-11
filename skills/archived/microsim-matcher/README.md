# MicroSim Matcher Skill

Intelligently matches diagram specifications to the most appropriate MicroSim generator skill.

## Overview

The microsim-matcher skill analyzes diagram, chart, or simulation specifications and returns a ranked list of recommended MicroSim generator skills with match scores (0-100) and detailed reasoning. This helps users quickly identify the best tool for creating educational visualizations.

## Features

- **9 MicroSim Generators Supported**: Evaluates all available generators in the repository
- **Intelligent Scoring**: 0-100 scale based on data type, interactivity, visual style, and trigger words
- **Detailed Reasoning**: Each recommendation includes clear explanation of score
- **Version Checking**: Automatically detects if reference files are outdated
- **Auto-Update**: Optional script flag to download latest matching criteria

## Quick Start

### Basic Usage

```bash
# Invoke the skill through Claude Code
# Provide a diagram specification file or description
```

### Version Check

Before using the skill, check if your reference files are up-to-date:

```bash
# Check version
python scripts/check-version.py

# Auto-update if outdated
python scripts/check-version.py --update
```

## File Structure

```
microsim-matcher/
├── SKILL.md                     # Main skill workflow (7 steps)
├── README.md                    # This file
├── references/
│   └── matching-criteria.md    # Detailed generator profiles (650+ lines)
└── scripts/
    └── check-version.py        # Version checking utility
```

## Supported MicroSim Generators

The skill evaluates matches against these 9 generators:

1. **microsim-p5** - Custom animations, simulations (p5.js)
2. **chartjs-generator** - Statistical charts (bar, line, pie, etc.)
3. **math-function-plotter-plotly** - Mathematical function plots
4. **mermaid-generator** - Flowcharts, diagrams, workflows
5. **vis-network** - Network graphs (nodes/edges)
6. **timeline-generator** - Chronological timelines
7. **map-generator** - Geographic visualizations (Leaflet.js)
8. **venn-diagram-generator** - Set relationships (2-4 sets)
9. **bubble-chart-generator** - Priority matrices

## Scoring Methodology

Each generator receives a score from 0-100 based on:

| Factor | Weight | Description |
|--------|--------|-------------|
| Data Type Match | 40 points | Does data structure align? |
| Interactivity Match | 25 points | Do interaction needs match? |
| Visual Style Match | 25 points | Does visual output align? |
| Trigger Words | 10 points | Contains relevant keywords? |

**Score Interpretation:**
- **90-100**: Perfect match - Primary use case
- **70-89**: Strong match - Well-suited
- **50-69**: Moderate match - Could work but not optimal
- **30-49**: Weak match - Significant limitations
- **0-29**: Poor match - Not recommended

## Example Output

```
MicroSim Generator Recommendations:

1. timeline-generator (Score: 98/100)
   Reason: Perfect match for chronological events with specific dates.
   Features zoom, filtering, event details - all requested features.

2. chartjs-generator (Score: 35/100)
   Reason: Could show as line chart but lacks timeline-specific
   features (zoom to dates, event panels, chronological navigation).

3. microsim-p5 (Score: 45/100)
   Reason: Custom development possible but timeline-generator
   provides all features out-of-the-box.

Recommendation: Use timeline-generator (98/100)
```

## Version Checking

### Why Version Checking Matters

The `matching-criteria.md` file contains scoring guidelines for all generators. When new generators are added or existing ones are updated, this file changes. Using outdated criteria can lead to:

- Missing recommendations for new generators
- Incorrect scoring for updated generators
- Poor recommendations overall

### How Version Checking Works

The `check-version.py` script:

1. Gets local file modification timestamp
2. Queries GitHub API for latest commit date
3. Compares timestamps
4. Warns if GitHub version is newer

### Version Check Commands

```bash
# Basic check (shows output)
python scripts/check-version.py

# Quiet mode (exit code only)
python scripts/check-version.py --quiet
echo $?  # 0=up-to-date, 1=outdated, 2=error

# Auto-update mode
python scripts/check-version.py --update
```

### GitHub API Reference

The script uses this GitHub API endpoint:
```
https://api.github.com/repos/dmccreary/claude-skills/commits?path=skills/microsim-matcher/references/matching-criteria.md&page=1&per_page=1
```

Latest reference file:
```
https://github.com/dmccreary/claude-skills/blob/main/skills/microsim-matcher/references/matching-criteria.md
```

## Workflow Steps

The skill follows a 7-step process:

1. **Step 0**: Check for reference file updates (version check)
2. **Step 1**: Read and parse diagram specification
3. **Step 2**: Extract key characteristics (data type, interactivity, visual style)
4. **Step 3**: Load MicroSim generator capabilities
5. **Step 4**: Score each generator (0-100)
6. **Step 5**: Rank by score (highest first)
7. **Step 6**: Format output with reasoning

## Maintenance

### Keeping Files Up-to-Date

**For users:**
```bash
# Check for updates before starting new project
python scripts/check-version.py

# Or pull latest from GitHub
git pull origin main
```

**For maintainers:**

When adding new generators:
1. Update `references/matching-criteria.md` with new generator profile
2. Update `SKILL.md` generator list (update count from 9)
3. Add to "Recent Updates" section in matching-criteria.md
4. Commit and push to GitHub
5. Users will be notified via version check

### Recent Updates

See `references/matching-criteria.md` for detailed update history.

## Troubleshooting

### Version Check Fails

**Error: "Network error"**
- Check internet connection
- GitHub API may be down (try again later)
- Firewall blocking API access

**Error: "Local file not found"**
- Run from repository root: `python skills/microsim-matcher/scripts/check-version.py`
- Or navigate to skill directory first

### Poor Recommendations

**Generator scores seem wrong:**
- Check if reference file is outdated (`python scripts/check-version.py`)
- Update to latest: `python scripts/check-version.py --update`
- Review specification - may be unclear or ambiguous

**Multiple generators score high:**
- This is normal for some specifications
- Review reasoning to understand trade-offs
- Consider splitting into multiple MicroSims

## Contributing

To add support for a new MicroSim generator:

1. Add generator profile to `references/matching-criteria.md`:
   - Primary use cases
   - Data types
   - Interactivity level
   - Trigger words
   - Scoring guidelines (when to score high/low)
   - Strengths and limitations

2. Update `SKILL.md`:
   - Add to "Available MicroSim Generators" list
   - Update generator count
   - Add example recommendations

3. Add to "Recent Updates" section with date

4. Test with sample specifications

5. Submit PR to repository

## License

Same license as the claude-skills repository.

## References

- **Main Skill**: `SKILL.md`
- **Matching Criteria**: `references/matching-criteria.md`
- **Version Check**: `scripts/check-version.py`
- **GitHub Repository**: https://github.com/dmccreary/claude-skills
- **MicroSim Overview**: `/docs/skill-descriptions/microsims/index.md`

## Support

For issues or questions:
- Check GitHub repository issues
- Review MicroSim generator documentation
- Run version check to ensure up-to-date files
