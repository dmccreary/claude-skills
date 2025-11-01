# ISO 11179 Metadata Registry Standards for Definitions

This reference provides detailed guidance on creating definitions that comply with ISO/IEC 11179 metadata registry standards.

## The Four Core Criteria

### 1. Precision

A definition is precise when it accurately and specifically captures the concept's meaning without ambiguity.

**Guidelines:**

- State exactly what the concept is, not what it does or how it's used
- Include the essential characteristics that distinguish it from other concepts
- Use terminology appropriate for the target audience
- Avoid generic or vague language

**Examples:**

❌ **Not Precise:** "Learning Graph - A useful tool for education"

✓ **Precise:** "Learning Graph - A directed graph of concepts that reflects the order concepts should be learned to master a new concept"

❌ **Not Precise:** "API - A way to connect programs"

✓ **Precise:** "API - A set of protocols and tools that defines how software components should interact"

### 2. Conciseness

A definition is concise when it conveys the meaning efficiently without unnecessary words.

**Guidelines:**

- Target 20-50 words for most definitions
- Remove filler words and redundant phrases
- Use active voice when possible
- Get to the core meaning quickly
- Avoid examples in the definition itself (add them separately)

**Examples:**

❌ **Not Concise:** "A learning graph is a type of specialized graph structure that is commonly used in educational contexts and learning management systems to represent the various relationships and dependencies that exist between different concepts that students need to learn"

✓ **Concise:** "A directed graph of concepts that reflects the order concepts should be learned to master a new concept"

❌ **Not Concise:** "Scaffolding is an instructional method where educators and teachers provide support and assistance to learners and students at the beginning stages of the learning process, and then gradually remove this support as the learners gain more confidence"

✓ **Concise:** "An instructional strategy where support is provided to learners at the beginning and gradually removed as they gain confidence and competence"

### 3. Distinctiveness

A definition is distinct when it is unique and clearly differentiates the concept from related concepts.

**Guidelines:**

- Highlight what makes this concept different from similar concepts
- Avoid copying definitions from other sources verbatim
- Ensure no two definitions in your glossary are too similar
- Include distinguishing characteristics

**Examples:**

Two related but distinct concepts:

✓ **Learning Graph:** "A directed graph of concepts that reflects the order concepts should be learned to master a new concept"

✓ **Concept Dependency:** "A prerequisite relationship between two concepts where one must be understood before the other can be learned effectively"

(Note: These are distinct - one is the overall structure, the other is a relationship within that structure)

❌ **Not Distinct:** Having both "Learning Graph" and "Knowledge Graph" with nearly identical definitions

### 4. Non-Circularity

A definition is non-circular when it does not reference the term being defined or create circular chains of dependencies.

**Guidelines:**

- Do not use the term itself in the definition
- Do not reference terms that themselves reference this term
- Use simpler, more fundamental terms in definitions
- Ensure all referenced terms are either defined elsewhere or commonly understood

**Examples:**

❌ **Circular:** "Learning Graph - A graph that represents learning"

✓ **Non-Circular:** "Learning Graph - A directed graph of concepts that reflects the order concepts should be learned"

❌ **Circular Chain:**
- "Prerequisite - A concept that must be learned before a dependent concept"
- "Dependent Concept - A concept that requires prerequisites"

✓ **Non-Circular:**
- "Prerequisite - A concept that must be understood before another concept can be learned effectively"
- "Dependent Concept - A concept that requires prior knowledge of other concepts"

## Additional ISO 11179 Principle

### 5. Unencumbered with Business Rules

Definitions should describe what something *is*, not how it *should be used* or what *rules apply* to it.

**Guidelines:**

- Avoid prescriptive language (must, should, required)
- Describe the concept, not policies or procedures
- Separate the definition from usage rules
- Focus on the concept's nature, not its governance

**Examples:**

❌ **Contains Business Rules:** "Prerequisite - A concept that students must complete before advancing to the next level"

✓ **Unencumbered:** "Prerequisite - A concept that must be understood before another concept can be learned effectively"

❌ **Contains Business Rules:** "MicroSim - An interactive simulation that must include user controls and visual feedback"

✓ **Unencumbered:** "MicroSim - A small-scale, embedded interactive simulation designed to illustrate a concept within educational content"

## Definition Template

Use this template as a starting point:

```
A [fundamental category/type] that [essential characteristic] [distinguishing feature].
```

**Examples:**

- "A **directed graph** that **reflects concept prerequisites** **for learning**"
- "An **instructional strategy** where **support is gradually reduced** **as competence increases**"
- "A **small-scale simulation** that **illustrates a concept** **within educational content**"

## Quality Checklist

Before finalizing a definition, verify:

- [ ] **Precise:** Accurately captures the concept's specific meaning?
- [ ] **Concise:** Uses 20-50 words (or fewer if appropriate)?
- [ ] **Distinct:** Clearly different from related concepts?
- [ ] **Non-Circular:** Doesn't reference itself or create circular chains?
- [ ] **Unencumbered:** Free of business rules and prescriptive requirements?
- [ ] **Clear:** Understandable by the target audience?
- [ ] **Grammatically Correct:** Proper sentence structure?
- [ ] **Terminology:** Uses terms defined elsewhere or commonly understood?

## Common Patterns by Concept Type

### Objects/Entities

Pattern: "A [type] that [essential characteristic]"

Example: "A directed graph that represents concept dependencies"

### Processes/Actions

Pattern: "The process of [action] to [purpose]"

Example: "The process of gradually reducing instructional support as learners gain competence"

### Properties/Attributes

Pattern: "The [quality/characteristic] of [entity] with respect to [dimension]"

Example: "The degree to which instructional content builds upon prior knowledge"

### Relationships

Pattern: "The relationship between [entity A] and [entity B] where [characteristic]"

Example: "The relationship between two concepts where one must be understood before the other"

## Word Count Guidelines

- **Minimum:** 10 words (most concepts need at least this much)
- **Target:** 20-50 words (sweet spot for most definitions)
- **Maximum:** 75 words (beyond this, consider breaking into multiple sentences or adding detail as an example)
- **Simple Concepts:** 10-25 words may suffice
- **Complex Concepts:** 30-50 words may be necessary
- **Very Complex:** 50-75 words, but consider if an example would be better

## Readability Targets

- **Grade Level:** Match the target audience
  - High School: Grade 9-10 (Flesch-Kincaid)
  - Undergraduate: Grade 12-14
  - Graduate: Grade 14-16
  - Professional: Grade 14-18
- **Sentence Structure:** Prefer simple, direct sentences
- **Jargon:** Use only when necessary for precision and when terms are defined elsewhere
- **Active Voice:** Preferred when natural

## Example Workflow

1. **Draft:** Write initial definition without worrying about criteria
2. **Review Precision:** Does it accurately capture the meaning?
3. **Review Conciseness:** Can any words be removed?
4. **Review Distinctiveness:** How is it different from related concepts?
5. **Review Non-Circularity:** Any circular references?
6. **Review Business Rules:** Any prescriptive language?
7. **Revise:** Make necessary changes
8. **Validate:** Check against full checklist
9. **Add Example:** If concept is abstract or could benefit from illustration

## Scoring Rubric

Each criterion worth 25 points:

**20-25 points:** Fully meets criterion, no issues
**15-19 points:** Mostly meets criterion, minor issues
**10-14 points:** Partially meets criterion, notable issues
**5-9 points:** Minimally meets criterion, major issues
**0-4 points:** Fails to meet criterion

**Overall Quality Score:**

- **85-100:** Excellent, ready for publication
- **70-84:** Good, minor refinements beneficial
- **55-69:** Adequate, notable improvements needed
- **40-54:** Poor, requires substantial revision
- **Below 40:** Unacceptable, complete rewrite needed
