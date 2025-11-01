# AI Prompts Guide for Intelligent Textbook Creation

This reference provides the complete collection of AI prompts used in the intelligent textbook creation workflow.

## Learning Graph Creation Workflow (Sequential Prompts)

### Prompt 00: Course Description

Use this comprehensive template to define your course scope:

```markdown
# Generating a Course Description

## Core Information

**Title:** [Insert your textbook title here]

**Summary:** [Provide a 2-3 sentence overview of what this textbook covers and its unique approach]

**Intended Audience:** [Specify target learners - e.g., "High school seniors", "Undergraduate CS majors", "Working professionals transitioning to data science"]

**Prerequisites:**
- [List specific knowledge requirements]
- [Include both conceptual and technical prerequisites]
- [Mention any required tools or software]

**Learning Objectives (Using Bloom's 2005 Taxonomy):**

### Remember (Recall facts and basic concepts)
Students will be able to:
- Define [key terms and concepts]
- List [important elements, principles, or components]
- Identify [fundamental patterns or structures]

### Understand (Explain ideas or concepts)
Students will be able to:
- Explain [core principles in their own words]
- Summarize [key processes or methodologies]
- Compare and contrast [related concepts]

### Apply (Use information in new situations)
Students will be able to:
- Solve [specific types of problems]
- Demonstrate [practical skills]
- Use [tools, techniques, or frameworks]

### Analyze (Draw connections among ideas)
Students will be able to:
- Analyze [complex systems or scenarios]
- Differentiate between [competing approaches or solutions]
- Examine [cause-and-effect relationships]

### Evaluate (Justify a decision or course of action)
Students will be able to:
- Evaluate [solutions, designs, or approaches]
- Critique [theories, methodologies, or implementations]
- Assess [quality, effectiveness, or appropriateness]

### Create (Produce original work)
Students will be able to:
- Design [original solutions or systems]
- Develop [new applications or implementations]
- Construct [working prototypes or models]

## Concepts Covered
1. **Foundation Concepts:** [List 5-10 fundamental concepts]
2. **Core Concepts:** [List 10-15 main concepts]
3. **Advanced Concepts:** [List 5-10 advanced topics]

## Concepts Explicitly Excluded
- [List topics that might be expected but are intentionally omitted]
- [Explain briefly why each is excluded]

## Capstone Projects
1. **Project Name:** [Title]
   - **Description:** [2-3 sentences about the project]
   - **Skills Demonstrated:** [List 3-5 key skills]
   - **Deliverables:** [What students will produce]

## Interactive Elements (MicroSims)
- **Estimated Number of MicroSims:** [Provide a range]
- **Types of Simulations:** [e.g., "Interactive visualizations", "Problem-solving scenarios"]
- **Primary Library:** [e.g., "p5.js", "vis.js"]

## Assessment Strategy
- **Formative Assessments:** [How students check understanding during learning]
- **Summative Assessments:** [How final competency is measured]
- **Self-Assessment Tools:** [Quizzes, reflection prompts, etc.]

## Learning Path Structure
- **Estimated Chapters:** [Number]
- **Estimated Total Concepts:** [Number, typically 150-250]
- **Estimated Completion Time:** [Hours or weeks]
- **Suggested Pace:** [e.g., "2-3 concepts per week"]

## Real-World Applications
After completing this textbook, students will be able to:
- [Specific job-relevant task 1]
- [Specific job-relevant task 2]
- [Industry or field application]

## Success Metrics
Students will know they have mastered the material when they can:
- [Observable, measurable outcome 1]
- [Observable, measurable outcome 2]
- [Observable, measurable outcome 3]

## Technical Requirements
- **Software/Tools Needed:** [List any required software]
- **Hardware Requirements:** [Minimum specifications if applicable]
- **Internet Connectivity:** [Required/Recommended/Optional]

## Glossary Scope
- **Estimated Number of Terms:** [Provide a range]
- **Term Categories:** [e.g., "Technical terms", "Domain-specific concepts"]
```

**Usage Instructions:**
- Replace all bracketed placeholders with specific information
- Be as detailed and specific as possible
- Example: Instead of "Students will solve problems", write "Students will solve differential equations using the separation of variables method"

---

### Prompt 02: Enumerate Concepts

**Recommended Prompt:**

```
You are an expert at generating concept lists for online training courses.

I am writing a book on the topic of [YOUR TOPIC]. I want a hands-on course
that walks [TARGET AUDIENCE] through each of the steps to create [DESIRED OUTCOME].

I want you to list the 150-250 most important concepts in this course.
Just return a simple ordered list in markdown with no other content.

Here is a list of concepts I've identified, listed roughly from core concepts
to most advanced topics:

[PASTE YOUR INITIAL CONCEPT LIST HERE]

Please review this list and:
1. Add other concepts that are required for a newcomer
2. Ensure concepts progress from foundational to advanced
3. Use Title Case for all concept labels
4. Return only a numbered markdown list
```

**Expected Output Format:**
```
1. Foundation Concept A
2. Foundation Concept B
3. Basic Term X
4. Intermediate Skill Y
5. Advanced Technique Z
...
150. Capstone Application
```

**Tips:**
- Start with 20-30 concepts you know are important
- Let AI expand to full 150-250 range
- Review for completeness and ordering
- Iterate if needed

---

### Prompt 03: Create Dependency Graph

**Recommended Prompt:**

```
I have a list of [NUMBER] concepts for a course on [YOUR TOPIC].

I need you to create a CSV file that maps the prerequisite dependencies
between these concepts to form a Directed Acyclic Graph (DAG).

**CSV Format:**
- Column 1: ConceptID (integer, 1-N)
- Column 2: ConceptLabel (exact text from concept list)
- Column 3: Dependencies (pipe-delimited list of ConceptIDs that are prerequisites)

**Rules:**
1. Foundation concepts have empty Dependencies column
2. Each concept can depend on multiple prerequisites (use | delimiter: "1|2|5")
3. No circular dependencies allowed (must be a DAG)
4. All referenced ConceptIDs must exist
5. Dependencies should only reference concepts that come earlier in the learning sequence

**Concepts:**
[PASTE YOUR ENUMERATED CONCEPT LIST HERE]

Return only the CSV data, no explanations.
```

**Expected Output:**
```csv
ConceptID,ConceptLabel,Dependencies
1,Foundation Concept A,
2,Foundation Concept B,
3,Basic Term X,1|2
4,Intermediate Skill Y,3
5,Advanced Technique Z,3|4
```

**Validation Checks:**
- No concept depends on itself
- No circular chains (A→B→C→A)
- All dependency IDs exist
- Foundation concepts clearly identified (empty Dependencies)

---

### Prompt 04: Create Taxonomy

**Recommended Prompt:**

```
I have created a learning graph with [NUMBER] concepts for a course on [YOUR TOPIC].

I need you to create a 10-12 category taxonomy system to organize these concepts
into thematic groups.

**Requirements:**
1. Create 10-12 taxonomy categories that cover all concept types
2. Category 1 should always be "Foundation Concepts"
3. Other categories should represent thematic areas (e.g., "Terms & Definitions", "Advanced Techniques")
4. Assign each concept to exactly one primary category
5. Add a TaxonomyID column to the existing CSV
6. Generate an HTML legend with color codes for each taxonomy

**Current CSV:**
[PASTE YOUR DEPENDENCY GRAPH CSV HERE]

**Suggested Taxonomy Structure:**
1. Foundation Concepts
2. Terms & Definitions
3. [Domain-Specific Category 1]
4. [Domain-Specific Category 2]
...
10. Advanced Applications & Future

Return:
1. Updated CSV with TaxonomyID column
2. HTML legend table with taxonomy names and colors
```

**Expected Output:**

**Updated CSV:**
```csv
ConceptID,ConceptLabel,Dependencies,TaxonomyID
1,Foundation Concept A,,1
2,Foundation Concept B,,1
3,Basic Term X,1|2,2
4,Setup Process,1,3
5,Advanced Technique,3|4,10
```

**HTML Legend:**
```html
<table>
  <tr><td bgcolor="#FF6B6B">1 - Foundation Concepts</td></tr>
  <tr><td bgcolor="#4ECDC4">2 - Terms & Definitions</td></tr>
  <tr><td bgcolor="#45B7D1">3 - Setup & Configuration</td></tr>
  ...
  <tr><td bgcolor="#FFA07A">10 - Advanced Applications</td></tr>
</table>
```

---

## Additional Content Generation Prompts

### Generate Glossary Terms

**Prompt:**

```
Create ISO 11179-compliant glossary definitions for the following concepts:

[PASTE CONCEPT LIST]

For each concept, provide:
1. **Term**: Concept name
2. **Definition**: Clear 1-2 sentence definition
3. **Context**: When/where this concept is used
4. **Example**: Practical example
5. **Related Terms**: Links to 2-3 related concepts

Format as markdown with this structure:

## [Concept Name]

**Definition:** [Clear definition]

**Context:** [Usage context]

**Example:** [Practical example]

**Related:** [Concept 1], [Concept 2], [Concept 3]
```

---

### Generate Chapter Content

**Prompt:**

```
I am writing a chapter on [TOPIC] for an intelligent textbook.

**Learning Objectives for this chapter:**
- [Objective 1]
- [Objective 2]
- [Objective 3]

**Target Audience:** [Description]

**Prerequisites:** [List prerequisite concepts]

**Key Concepts to Cover:**
[List concepts from learning graph]

Please generate:
1. Chapter introduction (2-3 paragraphs)
2. Section outline with subsections
3. Detailed content for each section
4. Code examples (if applicable)
5. Formative assessment questions
6. Summary and key takeaways
7. Suggestions for related MicroSims

Use clear, accessible language and include practical examples.
```

---

### Generate Quality Metrics

**Prompt:**

```
Assess the following intelligent textbook content across these dimensions:

**Content to Assess:**
[PASTE CHAPTER OR SECTION]

**Assessment Dimensions:**
1. **Clarity**: Is the content clear and understandable?
2. **Accuracy**: Is the information technically correct?
3. **Completeness**: Does it cover all necessary aspects?
4. **Engagement**: Is it engaging and well-structured?
5. **Bloom's Coverage**: Which Bloom's levels are addressed?
6. **Accessibility**: Is it accessible to the target audience?

For each dimension, provide:
- Score (1-10)
- Justification
- Specific improvement suggestions
```

---

### Generate FAQ

**Prompt:**

```
Create a Frequently Asked Questions (FAQ) section for a chapter on [TOPIC].

**Concepts covered:** [List concepts]

**Target audience:** [Description]

Generate 10-15 questions that:
1. Address common misconceptions
2. Clarify complex concepts
3. Provide practical guidance
4. Link to prerequisite knowledge
5. Suggest further learning paths

Format:
### Q: [Question]
**A:** [Clear, concise answer with examples]
```

---

## Using the Prompts Effectively

### Sequential Workflow

Follow this order for creating a complete learning graph:

```
1. Course Description (Prompt 00)
   ↓
2. Enumerate Concepts (Prompt 02)
   ↓
3. Dependency Graph (Prompt 03)
   ↓
4. Taxonomy (Prompt 04)
   ↓
5. Glossary Generation
   ↓
6. Chapter Content Generation
```

### Iteration Guidelines

- **Don't expect perfection on first try**: Run prompts 2-3 times, refining each iteration
- **Review AI output carefully**: Fact-check technical accuracy
- **Customize for your domain**: Modify prompts with domain-specific terminology
- **Maintain consistency**: Use the same concept labels across all prompts
- **Validate dependencies**: Manually check that the learning graph makes pedagogical sense

### Best Practices

1. **Provide Context**: The more context you give the AI, the better the output
2. **Be Specific**: Vague prompts produce vague results
3. **Iterate**: Generate, review, refine, repeat
4. **Combine Manual + AI**: Use AI for first draft, refine manually
5. **Preserve Structure**: Maintain CSV format, concept numbering, etc.

### Common Issues

**Issue**: AI generates circular dependencies
**Solution**: Explicitly state "no circular dependencies" and validate output

**Issue**: Too many or too few concepts
**Solution**: Specify exact range (e.g., "exactly 150 concepts")

**Issue**: Inconsistent concept labels
**Solution**: Provide exact concept list in subsequent prompts

**Issue**: Taxonomy doesn't fit domain
**Solution**: Provide example categories relevant to your field

---

## Prompt Customization Examples

### For Computer Science Course

```
Topic: "Building Web Applications with React and Node.js"
Concepts: 180
Audience: "Intermediate programmers with JavaScript knowledge"
Taxonomy Categories:
1. Foundation Concepts
2. JavaScript & ES6 Fundamentals
3. React Components & Hooks
4. State Management
5. Backend with Node.js & Express
6. Database Integration
7. Authentication & Security
8. Testing & Debugging
9. Deployment & DevOps
10. Advanced Patterns & Best Practices
```

### For Mathematics Course

```
Topic: "Calculus I: Limits, Derivatives, and Integrals"
Concepts: 200
Audience: "High school seniors or college freshmen with Algebra II background"
Taxonomy Categories:
1. Foundation Concepts (Algebra review)
2. Functions & Graphs
3. Limits & Continuity
4. Derivatives - Rules & Techniques
5. Applications of Derivatives
6. Integration - Rules & Techniques
7. Applications of Integration
8. Transcendental Functions
9. Numerical Methods
10. Advanced Topics & Series
```

### For Business Course

```
Topic: "Digital Marketing Analytics"
Concepts: 150
Audience: "Marketing professionals with basic statistics knowledge"
Taxonomy Categories:
1. Foundation Concepts (Marketing & Analytics basics)
2. Web Analytics Platforms
3. Metrics & KPIs
4. Data Collection & Tracking
5. Campaign Analysis
6. A/B Testing & Experimentation
7. Attribution Modeling
8. Visualization & Reporting
9. Tools & Technologies
10. Strategy & Optimization
```

---

## Summary

This prompt collection enables:
- **Structured content generation** following learning science principles
- **Consistent terminology** across the textbook
- **Dependency-driven** learning paths
- **Scalable creation** of educational content
- **Quality assessment** built into the workflow

Use these prompts as templates, customize for your domain, and iterate to create comprehensive, high-quality intelligent textbooks.
