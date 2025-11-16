# Course Description Analyzer

The course-description-analyzer skill is an autonomous agent that validates
and creates course descriptions for intelligent textbook projects. It
ensures course descriptions contain all necessary elements to support the
generation of comprehensive learning graphs with 200+ concepts.

## Key Capabilities

Dual-mode operation:

1. **Creation Mode** - Guides users through creating a new
/docs/course-description.md file by asking sequential questions about the
course
2. **Analysis Mode** - Evaluates an existing course description against quality
criteria

## Required Elements Checked

The skill validates that course descriptions include:

- Clear course title and target audience
- Prerequisites (or explicit "None")
- Comprehensive list of main topics (5-10 topics)
- Topics NOT covered (scope boundaries)
- Learning outcomes for all six 2001 Bloom's Taxonomy levels:
- Remember, Understand, Apply, Analyze, Evaluate, Create (with capstone
projects)

## Quality Assessment System

Uses a 100-point scoring rubric that evaluates:
- Basic metadata (title, audience, prerequisites): 15 points
- Topics covered and excluded: 15 points
- Bloom's Taxonomy outcomes (all 6 levels): 60 points
- Descriptive context: 10 points

## Quality ratings:
- 90-100: Excellent (ready for learning graph generation)
- 75-89: Good (minor improvements needed)
- 60-74: Adequate (several improvements needed)
- Below 60: Significant revision required

## Output Deliverables

The skill generates a comprehensive assessment report with:
- Overall score and quality rating
- Detailed scoring breakdown by element
- Gap analysis identifying missing/weak components
- Prioritized improvement suggestions
- Concept generation readiness assessment
- Recommendation on whether to proceed with learning graph generation

## Integration

After creating or analyzing a course description, the skill optionally adds
the file to mkdocs.yml navigation (after about.md). If the score is ≥75,
it indicates readiness to proceed with the learning-graph-generator skill.

This skill is typically the first step in the intelligent textbook creation
workflow, ensuring a solid foundation before generating learning graphs.

[Sample Execution Log of Course Description Analyzer](../prompts/course-description-skill.md)