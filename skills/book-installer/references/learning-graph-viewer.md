---
name: install-learning-graph-viewer
description: This skill installs an interactive learning graph viewer application into an intelligent textbook project. Use this skill when working with a textbook that has a learning-graph.json file and needs a visual, interactive graph exploration tool with search, filtering, and statistics capabilities.
---
# Install Learning Graph Viewer

## Overview

Installs a complete interactive graph viewer into `/docs/sims/graph-viewer/` by copying 4 template files and replacing the TITLE placeholder. Total install time: under 2 minutes.

**Template files are in this skill at:** `references/learning-graph-viewer-templates/`

## Step 1: Verify Prerequisites

```bash
ls docs/learning-graph/learning-graph.json
```

If missing, run the `learning-graph-generator` skill first.

### Validate classifierName Values

```bash
python3 -c "
import json
with open('docs/learning-graph/learning-graph.json') as f:
    data = json.load(f)
issues = []
for gid, ginfo in data['groups'].items():
    name = ginfo.get('classifierName', '')
    if name == gid:
        issues.append(f'  {gid}: classifierName equals ID - needs human-readable name')
    else:
        print(f'  OK: {gid} -> {name}')
if issues:
    print('FIX REQUIRED:')
    for i in issues: print(i)
"
```

If any classifierName equals its ID, fix taxonomy-names.json and regenerate learning-graph.json before proceeding.

## Step 2: Copy Template Files

```bash
SKILL_DIR="$HOME/.claude/skills/book-installer/references/learning-graph-viewer-templates"
mkdir -p docs/sims/graph-viewer
cp "$SKILL_DIR/local.css"  docs/sims/graph-viewer/local.css
cp "$SKILL_DIR/script.js"  docs/sims/graph-viewer/script.js
cp "$SKILL_DIR/index.md"   docs/sims/graph-viewer/index.md
cp "$SKILL_DIR/main.html"  docs/sims/graph-viewer/main.html
```

## Step 3: Replace TITLE Placeholder

Extract the course title from learning-graph.json and replace TITLE in main.html:

```bash
TITLE=$(python3 -c "import json; print(json.load(open('docs/learning-graph/learning-graph.json'))['metadata']['title'])")
sed -i '' "s/TITLE/$TITLE/g" docs/sims/graph-viewer/main.html
echo "Title set to: $TITLE"
```

Verify the replacement worked:

```bash
grep "<title>" docs/sims/graph-viewer/main.html
```

## Step 4: Reorder Groups to Match Taxonomy (Optional but Recommended)

The legend order in the sidebar matches the groups key order in learning-graph.json. Reorder to match concept-taxonomy.md:

```bash
cd docs/learning-graph
python3 -c "
import json, re
with open('concept-taxonomy.md') as f:
    text = f.read()
ordered_ids = re.findall(r'^#{1,6}[^(]+\(([A-Z]{2,8})\)', text, re.MULTILINE)
with open('learning-graph.json') as f:
    data = json.load(f)
ordered_groups = {}
for key in ordered_ids:
    if key in data['groups']:
        ordered_groups[key] = data['groups'][key]
for key in data['groups']:
    if key not in ordered_groups:
        ordered_groups[key] = data['groups'][key]
data['groups'] = ordered_groups
with open('learning-graph.json', 'w') as f:
    json.dump(data, f, indent=2)
print('Groups reordered to match concept-taxonomy.md')
for k in data['groups']:
    print(f'  {k}: {data[\"groups\"][k][\"classifierName\"]}')
"
cd ../..
```

## Step 5: Add Fullscreen Link to Learning Graph Index

Add this markdown to `docs/learning-graph/index.md` right after the level-1 heading:

```markdown
[Open Learning Graph Viewer Fullscreen](../sims/graph-viewer/main.html){ .md-button .md-button--primary }

<iframe src="../sims/graph-viewer/main.html" width="100%" height="600px" frameborder="0"></iframe>
```

## Step 6: Update mkdocs.yml Navigation

Add the graph viewer to the MicroSims section in `mkdocs.yml`:

```yaml
nav:
  # ... existing nav ...
  - MicroSims:
    - Learning Graph Viewer: sims/graph-viewer/index.md
```

## Step 7: Inform the User

Tell the user to test at:
```
http://127.0.0.1:8000/REPO_NAME/sims/graph-viewer/main.html
```

Where REPO_NAME is the git repository name.

## File Structure Created

```
docs/sims/graph-viewer/
├── main.html      # vis-network viewer (TITLE replaced with course name)
├── script.js      # Graph loading, search, filtering, highlighting
├── local.css      # Sidebar layout, search, legend, stats styling
└── index.md       # MkDocs page with iframe embed + fullscreen link
```

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Legend shows IDs like "FOUND" | classifierName not set | Fix taxonomy-names.json, regenerate JSON |
| Colors don't match legend | groups not passed to vis-network | Verify script.js builds visGroups from JSON |
| Graph keeps spinning | Physics timeout missing | script.js disables physics after 5s (built-in) |
| Checkbox toggling slow | Per-item DataSet.update() calls | Use batched array update (built-in) |
| Graph not loading | Wrong JSON path | script.js expects `../../learning-graph/learning-graph.json` |

## Dependencies

- vis-network.js (CDN: `https://unpkg.com/vis-network/standalone/umd/vis-network.min.js`)
- learning-graph.json at `docs/learning-graph/learning-graph.json`
