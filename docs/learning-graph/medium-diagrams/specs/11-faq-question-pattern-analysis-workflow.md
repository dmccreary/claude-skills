# FAQ Question Pattern Analysis Workflow

**Chapter:** 11 - Educational Resources Assessment
**Generator:** mermaid-generator
**Match Score:** 95/100
**Difficulty:** Medium

## Specification

<summary>FAQ Question Pattern Analysis Workflow</summary>
    Type: workflow

    Purpose: Illustrate the systematic process of identifying common student questions from course materials and learning analytics

    Visual style: Flowchart with swim lanes separating automated analysis, human review, and validation steps

    Swimlanes:
    - Automated Analysis (Claude Skills)
    - Human Reviewer (Educator/Instructional Designer)
    - Validation & Refinement

    Steps:

    1. Start: "Course Materials Assembled"
       Hover text: "Course description, learning graph, glossary, chapter content, and MicroSim documentation compiled into corpus"
       Swimlane: Automated Analysis

    2. Process: "Extract Concept List"
       Hover text: "Parse learning graph to enumerate all concepts; identify which concepts appear in chapter content and which are referenced in glossary"
       Swimlane: Automated Analysis

    3. Process: "Analyze Concept Dependencies"
       Hover text: "Identify concepts with high in-degree (many prerequisites) that may generate prerequisite questions; flag concepts with zero dependencies as potential definition questions"
       Swimlane: Automated Analysis

    4. Process: "Search for Question Patterns"
       Hover text: "Scan corpus for existing questions, prompts, and interrogative structures; extract common patterns like 'What is...', 'How do I...', 'When should...'"
       Swimlane: Automated Analysis

    5. Process: "Generate Candidate Questions"
       Hover text: "Use Claude API to generate 5-10 questions per concept across definitional, procedural, troubleshooting, and comparative categories"
       Swimlane: Automated Analysis

    6. Decision: "Quality Threshold Met?"
       Hover text: "Check if questions are: (1) non-redundant, (2) answerable from course content, (3) aligned with reading level, (4) diverse across categories"
       Swimlane: Automated Analysis

    7a. Process: "Flag for Human Review" (if quality threshold not met)
        Hover text: "Questions lacking clarity, those answerable only with external knowledge, or redundant questions sent to human reviewer"
        Swimlane: Human Reviewer

    7b. Process: "Add to FAQ Database" (if quality threshold met)
        Hover text: "Approved questions added to structured FAQ with metadata: concept_id, category, difficulty_level, bloom_level"
        Swimlane: Automated Analysis

    8. Process: "Educator Review"
       Hover text: "Subject matter expert reviews flagged questions; edits for clarity, accuracy, and pedagogical appropriateness"
       Swimlane: Human Reviewer

    9. Process: "Generate Answers from Corpus"
       Hover text: "Claude generates comprehensive answers by retrieving relevant passages from course content; cites specific chapter sections"
       Swimlane: Automated Analysis

    10. Process: "Validate Answer Completeness"
        Hover text: "Check that answers: (1) directly address question, (2) stay within course scope, (3) reference relevant concepts, (4) match reading level"
        Swimlane: Validation & Refinement

    11. Decision: "Answer Complete?"
        Hover text: "Human reviewer assesses whether answer provides sufficient information without requiring external resources"
        Swimlane: Human Reviewer

    12a. Process: "Revise Answer" (if incomplete)
         Hover text: "Educator supplements or rewrites answer; may identify gap in course content requiring new chapter section"
         Swimlane: Human Reviewer

    12b. Process: "Approve FAQ Entry" (if complete)
         Hover text: "FAQ question-answer pair approved and added to /docs/faq.md with appropriate cross-references to chapters"
         Swimlane: Validation & Refinement

    13. Process: "Update FAQ Index"
        Hover text: "FAQ database updated with search keywords, concept tags, and navigation links; integrated into MkDocs site navigation"
        Swimlane: Automated Analysis

    14. End: "FAQ Published"
        Hover text: "FAQ accessible via search, concept page links, and dedicated FAQ section; analytics tracking which questions receive most views"
        Swimlane: Validation & Refinement

    Color coding:
    - Blue: Automated analysis steps
    - Orange: Human review required
    - Green: Approval/validation steps
    - Purple: Database updates
    - Gray: Decision points

    Annotations:
    - Bidirectional arrow between "Generate Answers" and "Validate Completeness" labeled "Iterative refinement loop"
    - Note attached to "Educator Review": "Typically 30-40% of auto-generated questions require human intervention"
    - Note attached to "Update FAQ Index": "Searchable database enables chatbot integration"

    Implementation: Mermaid.js flowchart rendered in MicroSim with interactive hover states