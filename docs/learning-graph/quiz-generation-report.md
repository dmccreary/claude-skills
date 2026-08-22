# Quiz Generation Quality Report

Generated: 2025-11-08

## Overall Statistics

- **Total Chapters:** 13
- **Total Questions:** 130
- **Avg Questions per Chapter:** 10.0
- **Overall Quality Score:** 88.5/100

## Per-Chapter Summary

| Chapter | Title | Questions | Quality Score | Concept Coverage |
|---------|-------|-----------|---------------|------------------|
| 1 | Introduction to AI and Intelligent Textbooks | 10 | 88/100 | 67% (10/15) |
| 2 | Getting Started with Claude and Skills | 10 | 90/100 | 56% (10/18) |
| 3 | Course Design and Educational Theory | 10 | 89/100 | 59% (10/17) |
| 4 | Introduction to Learning Graphs | 10 | 88/100 | 83% (10/12) |
| 5 | Concept Enumeration and Dependencies | 10 | 87/100 | 56% (10/18) |
| 6 | Learning Graph Quality and Validation | 10 | 85/100 | 63% (10/16) |
| 7 | Taxonomy and Data Formats | 10 | 86/100 | 45% (10/22) |
| 8 | MkDocs Platform and Documentation | 10 | 89/100 | 100% (10/10) |
| 9 | Claude Skills Architecture and Development | 10 | 90/100 | 59% (13/22) |
| 10 | Content Creation Workflows | 10 | 88/100 | 69% (11/16) |
| 11 | Educational Resources and Assessment | 10 | 89/100 | 50% (8/16) |
| 12 | Interactive Elements and MicroSims | 10 | 90/100 | 47% (8/17) |
| 13 | Development Tools, Version Control, and Deployment | 10 | 91/100 | 44% (8/18) |

**Average Concept Coverage:** 61.3%

## Bloom's Taxonomy Distribution (Overall)

| Level | Actual | Percentage | Target Range | Status |
|-------|--------|------------|--------------|--------|
| Remember | 39 | 30.0% | 20-40% | ✓ Excellent |
| Understand | 43 | 33.1% | 25-35% | ✓ Excellent |
| Apply | 33 | 25.4% | 20-30% | ✓ Excellent |
| Analyze | 14 | 10.8% | 10-20% | ✓ Good |
| Evaluate | 1 | 0.8% | 5-10% | ⚠ Low |
| Create | 0 | 0.0% | 0-5% | ✓ Acceptable |

**Bloom's Distribution Score:** 23/25 (excellent)

### Analysis

The overall Bloom's distribution is excellent for an intermediate-level textbook:
- Strong foundation in Remember and Understand levels (63.1% combined)
- Good representation of Apply level (25.4%)
- Adequate Analyze level coverage (10.8%)
- Low Evaluate level coverage (0.8%) - only 1 question across all chapters
- No Create level questions - acceptable for this content level

The distribution aligns well with an intermediate technical textbook where students need solid foundational knowledge (Remember/Understand) with practical application skills (Apply) and some analytical thinking (Analyze).

## Answer Balance (Overall)

| Answer | Count | Percentage | Target | Status |
|--------|-------|------------|--------|--------|
| A | 6 | 4.6% | 25% | ❌ Severely Low |
| B | 78 | 60.0% | 25% | ❌ Severely High |
| C | 40 | 30.8% | 25% | ⚠ Moderately High |
| D | 6 | 4.6% | 25% | ❌ Severely Low |

**Answer Balance Score:** 5/15 (poor distribution)

### Critical Issue: Answer Distribution Imbalance

There is a **severe imbalance** in answer distribution:
- **B is correct 60% of the time** (78/130 questions) - should be ~25%
- **A and D are each correct only 4.6% of the time** (6/130 each) - should be ~25%
- **C is correct 30.8% of the time** (40/130) - slightly high

This pattern is problematic because:
1. Students may recognize that B is disproportionately correct
2. Test-taking strategies (favoring B when guessing) become more effective than knowledge
3. Assessment validity is compromised

**Affected Chapters:**
- Chapters 4-7: Heavy B bias (6-7 out of 10)
- Chapters 8-10: Heavy B bias (7 out of 10)
- Chapters 11-13: Extreme B bias (6-9 out of 10)
- Chapter 13 has 9/10 questions with B as correct answer

## Question Quality Analysis

- **Well-formed questions:** 98% (127/130)
- **Quality distractors:** 89% avg (range: 0.85-0.93)
- **Clear explanations:** 100% (130/130)
- **Valid links:** 100% (130/130)
- **Proper formatting:** 100% (all use mkdocs-material admonitions correctly)

**Question Quality Score:** 29/30 (excellent)

### Quality Highlights

**Strengths:**
- All questions use proper mkdocs-material question admonition format
- All explanations start with "The correct answer is **[LETTER]**."
- All include "Concept Tested:" and "See:" reference fields
- Explanations average 70 words (target: 50-100)
- Distractors are plausible and test understanding
- No grammatical errors detected

**Minor Issues:**
- 3 questions have slightly ambiguous wording (could be clarified)
- Some explanations could be more concise

## Concept Coverage

- **Total Concepts Across All Chapters:** 217
- **Tested Concepts:** 133
- **Overall Coverage:** 61.3%

**Coverage Score:** 16/20 (good)

### Coverage by Chapter Type

**Introductory Chapters (1-3):**
- Average coverage: 60.7%
- Target: 75-85%
- Status: ⚠ Below target

**Intermediate Chapters (4-10):**
- Average coverage: 67.9%
- Target: 65-75%
- Status: ✓ Good

**Advanced Chapters (11-13):**
- Average coverage: 47.0%
- Target: 60-70%
- Status: ⚠ Below target

### High-Priority Untested Concepts

Based on concept centrality in the learning graph, these high-priority concepts should have quiz questions:

- **Chapter 1:** Anthropic Claude Pro Account, Level 4: Adaptive Content, Level 5: AI Personalization
- **Chapter 7:** Data formats, CSV structure, JSON schema
- **Chapter 11:** Reference management, citation formats
- **Chapter 12:** p5.js library specifics, canvas controls
- **Chapter 13:** Git workflow, deployment processes

## Recommendations

### High Priority (Address Immediately)

1. **Fix Answer Distribution Imbalance**
   - Redistribute correct answers to achieve ~25% for each option (A, B, C, D)
   - Focus especially on chapters 8-13 where B bias is extreme
   - This can be done by reassigning which distractor is correct without rewriting questions
   - Target: Each letter correct 30-35 times (out of 130 total)

2. **Add Evaluate-Level Questions**
   - Current: Only 1 question (0.8%)
   - Target: 6-13 questions (5-10%)
   - Add 5-12 more Evaluate-level questions across chapters
   - Focus on advanced chapters (11-13) where critical judgment is appropriate

3. **Improve Coverage for Advanced Chapters**
   - Chapters 11-13 have <50% concept coverage
   - Add 2-3 questions per chapter to test high-priority untested concepts
   - Consider 12-question quizzes for these content-rich chapters

### Medium Priority (Address in Next Revision)

1. **Enhance Coverage for Introductory Chapters**
   - Chapters 1-3 below target 75-85% coverage
   - Add alternative questions for key concepts (Levels of Intelligence, Claude features)
   - Consider supplemental "quick check" quizzes for foundational concepts

2. **Add Create-Level Questions**
   - Currently: 0 questions (0.0%)
   - Target: 3-6 questions (2-5%) for advanced chapters
   - Example: "Design a MicroSim that demonstrates..." or "Create a workflow for..."
   - Appropriate only for chapters 11-13

3. **Clarify Ambiguous Questions**
   - Review 3 flagged questions for wording clarity
   - Ensure single defensible correct answer for each
   - Get peer review on borderline cases

### Low Priority (Future Enhancement)

1. **Create Alternative Question Bank**
   - Develop 2-3 alternative questions per major concept
   - Enable quiz randomization and test variations
   - Support practice mode with different questions each attempt

2. **Export to LMS Formats**
   - Generate Moodle XML export
   - Create Canvas-compatible QTI packages
   - Enable integration with institutional learning platforms

3. **Add Difficulty Progression**
   - Consider progressive difficulty within each quiz
   - Start with easier Remember questions, end with harder Analyze questions
   - Supports confidence-building and natural flow

## Quiz File Locations

**Quiz Markdown Files:**
```
docs/chapters/01-intro-ai-intelligent-textbooks/quiz.md
docs/chapters/02-getting-started-ibook-skills/quiz.md
docs/chapters/03-course-design-educational-theory/quiz.md
docs/chapters/04-intro-learning-graphs/quiz.md
docs/chapters/05-concept-enumeration-dependencies/quiz.md
docs/chapters/06-learning-graph-quality-validation/quiz.md
docs/chapters/07-taxonomy-data-formats/quiz.md
docs/chapters/08-mkdocs-platform-documentation/quiz.md
docs/chapters/09-ibook-skills-architecture-development/quiz.md
docs/chapters/10-content-creation-workflows/quiz.md
docs/chapters/11-educational-resources-assessment/quiz.md
docs/chapters/12-interactive-elements-microsims/quiz.md
docs/chapters/13-dev-tools-version-control-deployment/quiz.md
```

**Metadata Files:**
```
docs/learning-graph/quizzes/chapter-01-quiz-metadata.json
docs/learning-graph/quizzes/chapter-02-quiz-metadata.json
... (through chapter-13)
```

**Aggregated Data:**
```
docs/learning-graph/quiz-bank.json
```

## Success Criteria Met

✓ Overall quality score > 70/100 (actual: 88.5/100)
✓ 8-12 questions per chapter (actual: 10 per chapter)
✓ Bloom's distribution within ±15% of target (actual: excellent match)
✗ Answer balance within 20-30% per option (actual: severe imbalance)
✓ 100% questions have explanations
✓ No duplicate questions
✓ All links valid
⚠ 75%+ concept coverage (actual: 61.3% overall, varies by chapter)

## Overall Assessment

**Score: 83/100**

The quiz generation project successfully created 130 high-quality questions across 13 chapters with excellent Bloom's distribution, proper formatting, and comprehensive explanations. The primary weakness is the severe answer distribution imbalance (60% B answers), which should be corrected before deploying quizzes to students. Concept coverage is good for intermediate chapters but needs improvement for introductory and advanced chapters.

With the recommended corrections to answer distribution and addition of Evaluate-level questions, this quiz set will provide robust assessment capabilities for the intelligent textbook.
