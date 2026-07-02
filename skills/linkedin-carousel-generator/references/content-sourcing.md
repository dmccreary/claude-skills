# Content Sourcing Map

Exactly where each of the 12 slides' text and images come from. When in doubt, pull from the
canonical file listed here rather than re-deriving a number by hand — this keeps the carousel
consistent with `linkedin-announcement-generator` and `readme-generator`, which read the same
sources.

| # | Slide | Text source | Field(s) / section | Image source |
|---|-------|-------------|---------------------|---------------|
| 1 | Cover | `mkdocs.yml` | `site_name`, `site_description` | `docs/img/cover.png` (optional) + mascot `welcome.png` |
| 2 | Why This Book | `docs/about.md` | "Why This Intelligent Textbook" section — condense to 2-3 sentences, don't paste the whole section | mascot `welcome.png` or `thinking.png` |
| 3 | Learning Graph | `docs/learning-graph/book-metrics.json` + `docs/learning-graph/index.md` | `metrics.concepts`, taxonomy category count and edge count (from the index.md prose, since these aren't always in book-metrics.json) | Cropped `docs/sims/graph-viewer/*.png` screenshot |
| 4 | Coverage Summary | `mkdocs.yml` nav + `book-metrics.json` | `metrics.chapters`, `metrics.concepts`; hand-pick 4-6 chapter titles from the nav that best represent breadth (intro, a signature mid-book topic, an advanced topic) | none (big-numbers pattern) |
| 5 | Engagement Strategy | `CLAUDE.md` / `CONTENT-GENERATION-GUIDELINES.md` | The project's hands-on interaction loop (e.g. "Read → Run → Modify" for Skulpt-based books) — describe the project's actual mechanism, don't assume every project uses Skulpt | none (icon-row pattern) |
| 6 | Mascot Summary | `docs/img/mascot/character-sheet.md` | The "Pose Set" table — use every pose that exists in the project's `docs/img/mascot/` directory (commonly 6-7: welcome, thinking, tip, warning, encouraging, celebration, and optionally neutral) | Each pose's PNG |
| 7 | MicroSim Count | `docs/learning-graph/book-metrics.json` | `metrics.microsims` | Screenshot of the user-confirmed flagship MicroSim |
| 8 | Supplementary Content | `docs/learning-graph/book-metrics.json` | `metrics.glossaryTerms`, `metrics.faqs`, `metrics.quizQuestions`, `metrics.references` (or `metrics.chapterReferences` if per-chapter references aren't aggregated) | none (icon-row pattern) |
| 9 | License | `docs/license.md` | License type and short rights summary (share/adapt/attribution terms) | `docs/img/license.png` |
| 10 | Adaptivity | Project's own skill usage (course-description → learning-graph-generator → chapter-content-generator pipeline) | Describe the pipeline conceptually — name the actual skills used if this project used them | Simple 3-4 box pipeline diagram, or omit image and use icon-row |
| 11 | Continuous Enrichment | No canonical file — this is a forward-looking capability statement | Phrase as "can be configured to..." not as a description of an already-running system, unless the project genuinely has this (e.g. `register-book-analytics` wired up + a documented A/B process) | none, or a simple feedback-loop icon |
| 12 | Closing CTA | `mkdocs.yml` | `site_url`, `repo_url` | mascot `celebration.png` |

## Extraction one-liners

```bash
# mkdocs.yml site metadata + theme palette
python3 - <<'PY'
import yaml
d = yaml.safe_load(open("mkdocs.yml"))
print("site_name:", d.get("site_name"))
print("site_description:", d.get("site_description"))
print("site_url:", d.get("site_url"))
print("repo_url:", d.get("repo_url"))
print("primary:", d.get("theme", {}).get("palette", {}).get("primary"))
print("accent:", d.get("theme", {}).get("palette", {}).get("accent"))
PY

# canonical book metrics
python3 - <<'PY'
import json
m = json.load(open("docs/learning-graph/book-metrics.json"))["metrics"]
print(json.dumps(m, indent=2))
PY
```

## Handling missing content gracefully

- No `docs/img/cover.png` → skip the cover image, lean on the title/subtitle typography instead
- No taxonomy `color-config.json` → skip the color legend on slide 3, keep the concept/edge counts
- Fewer than 6 mascot poses → show only the poses that exist; never invent a pose or role
- `metrics.diagrams` or `metrics.equations` is 0 → omit that stat from slide 8 rather than
  displaying "0"
- No flagship MicroSim confirmed by the user → default to the one with the most visually
  distinctive output (turtle-graphics drawing, chart, network diagram) over a plain form
