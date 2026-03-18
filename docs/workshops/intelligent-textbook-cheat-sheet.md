# Intelligent Textbook Workshop - Quick Reference

## 1. Setup Commands
```bash
# Clone the repository
git clone https://github.com/dmccreary/claude-skills
cd claude-skills

# Set environment variable (add to ~/.bashrc or ~/.zshrc)
export BK_HOME=$HOME/Documents/ws/claude-skills
export PATH="$HOME/.local/bin:$PATH"

# Reload shell config
source ~/.bashrc   # or source ~/.zshrc

# Install scripts and skills
$BK_HOME/scripts/bk-install-scripts
bk-install-skills

# Verify installation
bk                        # Show main menu
bk-list-skills            # List available skills
```

## 2. Bloom's Taxonomy (2001) - 6 Cognitive Levels
| Level | Name | Color | Verbs |
|-------|------|-------|-------|
| 1 | **Remember** | Red | Define, list, recall, identify |
| 2 | **Understand** | Orange | Summarize, explain, classify |
| 3 | **Apply** | Yellow | Implement, solve, use |
| 4 | **Analyze** | Green | Differentiate, compare, organize |
| 5 | **Evaluate** | Blue | Judge, critique, assess |
| 6 | **Create** | Purple | Design, construct, develop |

## 3. The 12-Step Intelligent Textbook Workflow
| Step | Task | Skill Command |
|------|------|---------------|
| 1 | Course Description | `/skill course-description-analyzer` |
| 2 | Bloom's Integration | (manual in course-description.md) |
| 3 | Concept Enumeration | `/skill learning-graph-generator` |
| 4 | Dependencies (DAG) | (included in step 3) |
| 5 | Taxonomy Categories | (included in step 3) |
| 6 | Graph Visualization | (JSON output from step 3) |
| 7 | Chapter Structure | `/skill book-chapter-generator` |
| 8 | Chapter Content | `/skill chapter-content-generator` |
| 9 | MicroSim Creation | `/skill microsim-p5` |
| 10 | Glossary & FAQ | `/skill glossary-generator` then `/skill faq-generator` |
| 11 | Quality Metrics | `/skill book-metrics-generator` |
| 12 | Site Deployment | `mkdocs gh-deploy` |

## 4. Key File Locations
```
docs/
├── course-description.md          # Your course description (create first!)
├── glossary.md                    # Generated glossary
├── learning-graph/
│   ├── learning-graph.csv         # Concept list with dependencies
│   ├── learning-graph.json        # vis-network visualization data
│   └── quality-metrics.md         # Graph quality report
├── chapters/                      # Generated chapter content
│   └── 01-introduction/index.md
└── sims/                          # MicroSims (interactive simulations)
    └── [sim-name]/main.html
```

## 5. MkDocs Commands
```bash
mkdocs serve              # Preview locally at http://localhost:8000
mkdocs build --strict     # Build for production (check for errors)
mkdocs gh-deploy          # Deploy to GitHub Pages
```

## 6. ISO 11179 Definition Standards (Glossary Quality)
Definitions must be: **Precise** | **Concise** | **Distinct** | **Non-circular** | **No business rules**

## 7. Learning Graph Quality Targets
- Quality score: **≥70/100**
- Dependencies per concept: **2-4 average**
- No taxonomy category: **>30%** of concepts
- **Zero** circular dependencies (must be a DAG)
- All concepts connected (no orphaned nodes, i.e., no completely disconnected concepts)

## 8. Quick Reference: Visualization Skills
| Type | Skill | Use For |
|------|-------|---------|
| Animation | `microsim-p5` | Interactive simulations |
| Charts | `chartjs-generator` | Bar, line, pie charts |
| Flows | `mermaid-generator` | Flowcharts, process diagrams |
| Timeline | `timeline-generator` | Chronological events |
| Sets | `venn-diagram-generator` | Set relationships |
| Maps | `map-generator` | Geographic visualizations |
| Networks | `vis-network` | Concept graphs, dependencies |

## 9. Troubleshooting
| Issue | Solution |
|-------|----------|
| Skills not found | Run `bk-install-skills` |
| Learning graph fails | Add more detail to course description |
| Quality score <70 | Refine concept dependencies |
| Circular dependencies | Edit CSV manually to break cycles |
| MicroSim won't render | Check browser console for JS errors |

## 10. Essential Skill Invocation Pattern
```
/skill [skill-name]
```
Example: `/skill learning-graph-generator`

**Workshop support:** https://github.com/dmccreary/claude-skills/issues
