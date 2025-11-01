# Quiz Generator Skill

Automatically generate interactive multiple-choice quizzes for textbook chapters with Bloom's Taxonomy alignment and mkdocs-material question admonition formatting.

## Overview

This skill converts chapter content into high-quality multiple-choice quiz questions. Questions are aligned to learning graph concepts, distributed across Bloom's Taxonomy cognitive levels, and formatted using mkdocs-material question admonitions with upper-alpha (A, B, C, D) answer choices.

## Installation

To use this skill with Claude Code or Claude.ai:

1. Install the skill by providing the path to this directory
2. The skill will be available for Claude to use when generating quizzes

## Usage

**Trigger Phrases:**

- "Generate a quiz for Chapter 3"
- "Create quiz questions for my chapter"
- "Build a quiz from this content"
- "Generate quizzes for all chapters"

**Prerequisites:**

- Chapter content exists (1000+ words per chapter recommended)
- Learning graph created (`docs/learning-graph/03-concept-dependencies.csv`)
- Glossary available (`docs/glossary.md`) - recommended
- Course description with learning outcomes - optional

**Typical Workflow:**

1. User asks Claude to generate quiz for specific chapter
2. Skill assesses content readiness (score 1-100)
3. Skill determines chapter type and Bloom's distribution
4. Skill generates 8-12 questions using question admonition format
5. Skill creates quiz markdown and metadata files
6. Skill updates quiz bank and generates quality report

## Question Format

All questions use the mkdocs-material question admonition format:

```markdown
#### 1. What is the primary purpose of a learning graph?

<div class="upper-alpha" markdown>
1. To create visual decorations for textbooks
2. To map prerequisite relationships between concepts
3. To generate random quiz questions
4. To organize files in a directory structure
</div>

??? question "Show Answer"
    The correct answer is **B**. A learning graph is a directed graph that maps prerequisite relationships between concepts, showing which concepts must be learned before others.

    **Concept Tested:** Learning Graph

    **See:** [Learning Graph Concept](../concepts/learning-graph.md)
```

**Key Formatting Elements:**

- Level-4 header (####) with question number
- `<div class="upper-alpha" markdown>` wrapper for upper-alpha styling
- Numbered list (1, 2, 3, 4) that renders as A, B, C, D
- `??? question "Show Answer"` admonition
- Indented answer block (4 spaces)
- "The correct answer is **[LETTER]**." statement
- Concept tested and source link

## Output Files

### Required (Per Chapter)

**1. Quiz Markdown File**

Location options:
- Separate: `docs/[section]/[chapter-name]-quiz.md`
- Embedded: Appended to chapter file

Content:
- 8-12 multiple choice questions
- Question admonition format
- Complete explanations
- Links to chapter sections

**2. Quiz Metadata JSON**

Location: `docs/learning-graph/quizzes/[chapter-name]-quiz-metadata.json`

Contains:
- Question metadata (Bloom's level, difficulty, concept)
- Answer distribution statistics
- Bloom's distribution
- Concept coverage
- Quality scores

### Recommended (Aggregate)

**3. Quiz Bank JSON**

Location: `docs/learning-graph/quiz-bank.json`

Contains:
- All questions from all chapters
- Searchable by concept, Bloom's level, difficulty
- Ready for LMS export or chatbot integration

**4. Quality Report**

Location: `docs/learning-graph/quiz-generation-report.md`

Contains:
- Overall statistics
- Per-chapter quality scores
- Bloom's Taxonomy distribution
- Answer balance analysis
- Concept coverage
- Recommendations

### Optional

**5. Alternative Question Bank**

Location: `docs/learning-graph/quizzes/alternative-questions.json`

Contains:
- 2-3 alternative questions per concept
- For quiz randomization or variations

**6. Study Guide**

Location: `docs/[section]/[chapter-name]-study-guide.md`

Contains:
- Key concepts to review
- Practice questions
- Links to chapter sections

## Quality Standards

### Content Readiness Score (1-100)

Assesses whether chapter content is sufficient for quality quiz:

- **90-100:** Rich content (2000+ words, examples, clear concepts)
- **70-89:** Good content (1000-2000 words, some examples)
- **50-69:** Basic content (500-1000 words, limited examples)
- **Below 50:** Insufficient content

### Quiz Quality Score (1-100)

Five components:

1. **Question Quality (30 pts):** Clear, unambiguous, well-formed
2. **Bloom's Distribution (25 pts):** Matches target for chapter type
3. **Concept Coverage (20 pts):** Tests 75%+ of major concepts
4. **Answer Balance (15 pts):** Correct answers evenly distributed
5. **Pedagogical Value (10 pts):** Explanations teach, links provided

### Bloom's Taxonomy Targets

**Introductory Chapters:**
- 40% Remember, 40% Understand, 15% Apply, 5% Analyze

**Intermediate Chapters:**
- 25% Remember, 30% Understand, 30% Apply, 15% Analyze

**Advanced Chapters:**
- 15% Remember, 20% Understand, 25% Apply, 25% Analyze, 10% Evaluate, 5% Create

### Success Criteria

- Overall quality score > 70/100
- 8-12 questions generated
- Bloom's distribution within ±15% of target
- 75%+ concept coverage
- Answer balance within 20-30% per option (A, B, C, D)
- 100% questions have explanations
- No duplicate questions
- All links valid

## Skill Contents

```
quiz-generator/
├── SKILL.md                              # Main skill instructions
├── README.md                             # This file
└── references/
    └── distractor-writing-guide.md       # Detailed distractor guidance
```

## Example Output

**Quiz File** (`docs/concepts/learning-graph-quiz.md`):

```markdown
# Quiz: Learning Graphs

Test your understanding of learning graphs with these questions.

---

#### 1. What is the primary purpose of a learning graph?

<div class="upper-alpha" markdown>
1. To create visual decorations for textbooks
2. To map prerequisite relationships between concepts
3. To generate random quiz questions
4. To organize files in a directory structure
</div>

??? question "Show Answer"
    The correct answer is **B**. A learning graph is a directed graph that maps prerequisite relationships between concepts, ensuring students learn foundational concepts before advanced ones.

    **Concept Tested:** Learning Graph

    **See:** [Learning Graph Concept](../concepts/learning-graph.md)

---

#### 2. Which data structure prevents cycles in a learning graph?

<div class="upper-alpha" markdown>
1. Linked list
2. Directed acyclic graph
3. Directed cyclic graph
4. Undirected graph
</div>

??? question "Show Answer"
    The correct answer is **B**. A directed acyclic graph (DAG) is specifically designed to prevent cycles, which is essential for learning graphs because circular dependencies would create impossible prerequisite chains.

    **Concept Tested:** Directed Acyclic Graph

    **See:** [Learning Graph Structure](../concepts/learning-graph.md#structure)

---

[Continue with remaining questions...]
```

**Quality Report** (excerpt):

```markdown
# Quiz Generation Quality Report

## Chapter: Learning Graphs

- **Total Questions:** 10
- **Overall Quality Score:** 82/100
- **Content Readiness:** 88/100

## Bloom's Taxonomy Distribution

| Level | Actual | Target | Deviation |
|-------|--------|--------|-----------|
| Remember | 20% | 25% | -5% ✓ |
| Understand | 30% | 30% | 0% ✓ |
| Apply | 30% | 25% | +5% ✓ |
| Analyze | 20% | 15% | +5% ✓ |

**Bloom's Score:** 24/25 (excellent)

## Answer Balance

- A: 20% (2/10)
- B: 30% (3/10)
- C: 30% (3/10)
- D: 20% (2/10)

**Balance Score:** 14/15 (good)

## Concept Coverage

- **Total Concepts:** 12
- **Tested Concepts:** 10
- **Coverage:** 83%

**Coverage Score:** 17/20 (good)
```

## References

### Distractor Writing Guide

The skill includes comprehensive guidance on writing quality distractors in `references/distractor-writing-guide.md`. This reference covers:

- The four qualities of effective distractors (plausibility, educational value, discrimination, fairness)
- Distractor construction patterns
- Common mistakes to avoid
- Quality checklist
- Examples by Bloom's level
- Revision strategies

Claude will reference this document when creating answer options.

## Best Practices

### For Users

1. **Ensure sufficient content** - 1000+ words per chapter for quality quizzes
2. **Review generated quizzes** - Check for accuracy and appropriate difficulty
3. **Validate links** - Ensure all references point to correct sections
4. **Test rendering** - Preview questions in mkdocs to verify formatting
5. **Iterate as needed** - Refine based on quality report recommendations

### For Quiz Generation

1. **Balance Bloom's levels** - Don't over-focus on Remember/Understand
2. **Create quality distractors** - All wrong answers should be plausible
3. **Write teaching explanations** - Don't just confirm, explain why
4. **Vary correct answer position** - Avoid patterns (all C's, alternating, etc.)
5. **Link to sources** - Reference chapter sections for deeper learning
6. **Test major concepts** - Focus on important concepts, not trivial details

## Troubleshooting

### "Content readiness score is low (<60)"

**Cause:** Chapter has insufficient content for quality quiz

**Solution:**
- Write more chapter content (target: 1000+ words)
- Add examples for key concepts
- Ensure concepts are clearly explained
- Verify glossary coverage

### "Bloom's distribution is imbalanced"

**Cause:** Too many questions at one cognitive level

**Solution:**
- Review chapter type (introductory, intermediate, advanced)
- Check target distribution for that chapter type
- Add more higher-level questions (Apply, Analyze, Evaluate)
- Reduce excessive Remember/Understand questions

### "Answer balance is poor"

**Cause:** Correct answers clustered on one option (e.g., all B's)

**Solution:**
- Randomize correct answer placement
- Target: 25% each for A, B, C, D (±5% acceptable)
- Avoid patterns (A-B-A-B, all C's, etc.)
- Check after each question added

### "Question admonition not rendering"

**Cause:** Formatting error in markdown

**Solution:**
- Verify `<div class="upper-alpha" markdown>` wrapper present
- Check numbered list uses 1, 2, 3, 4 (not A, B, C, D)
- Ensure closing `</div>` tag exists
- Verify 4-space indentation in answer block
- Check blank lines before and after div

### "Distractors are too obvious"

**Cause:** Wrong answers not plausible

**Solution:**
- Review distractor writing guide
- Use related terminology
- Base on common misconceptions
- Ensure similar length to correct answer
- Avoid nonsense or joke options

## Version History

- **v1.0** (2025-01-31) - Initial release
  - Question admonition format with upper-alpha styling
  - Bloom's Taxonomy distribution
  - Quality distractor analysis
  - LMS-ready JSON export
  - Comprehensive quality scoring

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or improvements:

1. Review detailed specification in `/docs/skills/quiz-generator.md`
2. Check distractor writing guide for answer option help
3. Examine quality reports for specific guidance
4. Test question rendering in mkdocs preview

## Related Skills

- **Learning Graph** - Generates concept dependencies used for question selection
- **Glossary Generator** - Creates glossary referenced for terminology questions
- **Chapter Content Generator** - Produces content analyzed for quiz questions
- **FAQ Generator** - Creates FAQ questions (complementary to quiz questions)
- **Concept Validator** - Validates quiz coverage of all concepts
