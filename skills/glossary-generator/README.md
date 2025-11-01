# Glossary Generator Skill

Automatically generate comprehensive glossaries for intelligent textbooks with ISO 11179-compliant definitions.

## Overview

This skill converts concept lists from learning graphs into properly formatted glossary entries. Each definition follows ISO 11179 metadata registry standards ensuring precision, conciseness, distinctiveness, and non-circularity.

## Installation

To use this skill with Claude Code or Claude.ai:

1. Install the skill by providing the path to this directory
2. The skill will be available for Claude to use when generating glossaries

## Usage

**Trigger Phrases:**

- "Generate a glossary from my concept list"
- "Create a glossary for the textbook"
- "Build a glossary from the learning graph concepts"

**Prerequisites:**

- Learning graph concept list exists (e.g., `docs/learning-graph/02-concept-list-v1.md`)
- Course description file exists (`docs/course-description.md`)
- Concepts have been reviewed and approved

**Typical Workflow:**

1. User asks Claude to generate a glossary
2. Skill validates the concept list quality
3. Skill reads course context
4. Skill generates ISO 11179-compliant definitions
5. Skill creates `docs/glossary.md` with alphabetically sorted entries
6. Skill generates quality report

## Output Files

### Required

- **`docs/glossary.md`** - Complete glossary with ISO-compliant definitions
  - Alphabetically sorted terms
  - Level-4 headers for each term
  - Examples for 60-80% of terms
  - Cross-references to related terms

### Recommended

- **`docs/learning-graph/glossary-quality-report.md`** - Quality assessment
  - ISO 11179 compliance scores per definition
  - Overall quality metrics
  - Recommendations for improvement
  - Circular dependency detection

### Optional

- **`docs/learning-graph/glossary-cross-ref.json`** - Semantic search data
  - JSON mapping of term relationships
  - Category assignments
  - Related/contrasting terms

## Quality Standards

### ISO 11179 Criteria (100 point scale)

Each definition scored on four 25-point criteria:

1. **Precision (25 pts):** Accurately captures concept meaning
2. **Conciseness (25 pts):** Brief definitions (20-50 words target)
3. **Distinctiveness (25 pts):** Unique and distinguishable from related concepts
4. **Non-circularity (25 pts):** No circular dependencies or self-references

### Success Thresholds

- **85-100:** Excellent, publication ready
- **70-84:** Good, minor refinements beneficial
- **55-69:** Adequate, improvements needed
- **Below 55:** Requires revision

### Overall Glossary Metrics

- Zero circular definitions (required)
- 100% alphabetical ordering (required)
- All concepts from input list included (required)
- 60-80% of terms include examples (target)
- Markdown renders correctly in mkdocs (required)

## Skill Contents

```
glossary-generator/
├── SKILL.md                              # Main skill instructions
├── README.md                             # This file
└── references/
    └── iso-11179-standards.md            # Detailed ISO 11179 guidance
```

## Example Input

**Concept List** (`docs/learning-graph/02-concept-list-v1.md`):

```markdown
1. Learning Graph
2. Concept Dependency
3. Scaffolding
4. Bloom's Taxonomy
...
```

## Example Output

**Glossary** (`docs/glossary.md`):

```markdown
# Glossary of Terms

#### Bloom's Taxonomy

A hierarchical classification of educational learning objectives consisting of six cognitive levels: Remember, Understand, Apply, Analyze, Evaluate, and Create.

**Example:** When designing quiz questions, use Bloom's Taxonomy to ensure a balanced distribution across cognitive levels rather than focusing only on memorization.

#### Concept Dependency

A prerequisite relationship between two concepts where one must be understood before the other can be learned effectively.

**Example:** In a programming course, "Variables" has a concept dependency relationship with "Functions" because understanding variables is required before learning about function parameters.

...
```

## Quality Report Example

**Quality Report** (`docs/learning-graph/glossary-quality-report.md`):

```markdown
# Glossary Quality Report

Generated: 2025-01-31

## Overall Statistics

- **Total Terms:** 187
- **Overall Quality Score:** 89/100
- **Terms Meeting All Criteria:** 172 (92%)
- **Circular Definitions:** 0
- **Example Coverage:** 71%

## ISO 11179 Compliance

- **Precision:** 91% (avg 22.8/25 pts)
- **Conciseness:** 88% (avg 22.0/25 pts)
- **Distinctiveness:** 94% (avg 23.5/25 pts)
- **Non-Circularity:** 100% (avg 25.0/25 pts)

## Recommendations

### High Priority (3 terms)

- **API:** Definition too vague, needs more precision
- **Framework:** Too long (78 words), needs condensing
- **Module:** Similar to "Component", needs distinction

...
```

## References

### ISO 11179 Standards

The skill includes detailed guidance on ISO/IEC 11179 metadata registry standards in `references/iso-11179-standards.md`. This reference covers:

- The four core criteria with examples
- Common patterns by concept type
- Quality checklists
- Scoring rubrics
- Definition templates
- Common pitfalls to avoid

Claude will reference this document as needed when generating definitions.

## Best Practices

### For Users

1. **Review concept list first** - Ensure concepts are finalized before generating glossary
2. **Provide course context** - Complete course description helps with appropriate examples
3. **Review quality report** - Use recommendations to improve lower-scoring definitions
4. **Iterate as needed** - Refine definitions based on quality scores

### For Definitions

1. **Target 20-50 words** - Sweet spot for most concepts
2. **Include examples** - Especially for abstract concepts
3. **Use cross-references** - Link related terms (but ensure they exist)
4. **Match audience level** - Use appropriate complexity for target audience
5. **Avoid jargon** - Unless necessary and defined elsewhere

## Troubleshooting

### "Quality score is low (<70)"

**Cause:** Concept list has duplicates, formatting issues, or unclear concepts

**Solution:**
- Review concept list for duplicates
- Fix Title Case formatting
- Ensure concepts are under 32 characters
- Clarify ambiguous concept labels

### "Circular definitions detected"

**Cause:** Definitions reference each other or undefined terms

**Solution:**
- Review quality report for specific circular chains
- Use simpler, more fundamental terms
- Ensure all referenced terms are defined

### "Missing examples"

**Cause:** Not enough examples generated (below 60% target)

**Solution:**
- Re-run with emphasis on examples for abstract concepts
- Manually add examples to complex or important concepts
- Ensure course description provides good context

## Version History

- **v1.0** (2025-01-31) - Initial release
  - ISO 11179 compliance
  - Quality scoring and reporting
  - Cross-reference generation
  - Example coverage

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or improvements:

1. Review the detailed specification in `/docs/skills/glossary-generator.md`
2. Check the ISO 11179 reference guide
3. Examine quality reports for specific guidance
4. Iterate based on feedback

## Related Skills

- **Learning Graph** - Generates the concept list used as input
- **Chapter Content Generator** - Uses glossary for consistent terminology
- **FAQ Generator** - References glossary for technical questions
- **Concept Validator** - Validates glossary coverage of all concepts
