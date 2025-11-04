---
name: course-description-analyzer
description: This skill analyzes or creates course descriptions for intelligent textbooks by checking for completeness of required elements (title, audience, prerequisites, topics, Bloom's Taxonomy outcomes) and providing quality scores with improvement suggestions. Use this skill when working with course descriptions in /docs/course-description.md that need validation or creation for learning graph generation.
---

# Course Description Analyzer

## Overview

Analyze or create high-quality course descriptions that contain all necessary elements for generating comprehensive learning graphs with 200+ concepts. Check the `/docs/course-description.md` file for completeness, quality, and alignment with 2001 Bloom's Taxonomy learning outcomes.

## Workflow Decision Tree

Start by checking if `/docs/course-description.md` exists:

- **File does not exist** → Follow **Creation Workflow** (Step 1)
- **File exists** → Follow **Analysis Workflow** (Step 2)

## Step 1: Course Description Creation

Use this workflow when `/docs/course-description.md` does not exist.

### 1.1 Gather Course Information

Ask the user the following questions sequentially (not all at once):

1. **What is the title of the course?**

2. **What is the target audience of the course?**
   - Options: elementary, junior high, high school, college undergraduate, graduate students, adult continuing education, professional development, or other

3. **What are the prerequisites for this course?**
   - If none, explicitly state "None"

4. **What are the main subjects/topics covered by this course?**
   - Request a list of major topics

5. **What are the learning outcomes organized by the 2001 Bloom's Taxonomy?**
   - Explain that after this course, students will be able to demonstrate competencies at each level:
     - **Remember**: Retrieve, recognize, and recall relevant knowledge
     - **Understand**: Construct meaning from instructional messages
     - **Apply**: Carry out or use procedures in given situations
     - **Analyze**: Break material into parts and determine relationships
     - **Evaluate**: Make judgments based on criteria and standards
     - **Create**: Put elements together to form coherent wholes; includes capstone projects

### 1.2 Generate Course Description

Use the template from `assets/course-description-template.md` and populate it with the user's responses. Create the file at `/docs/course-description.md`.

Ensure the generated file includes:
- Clear course title
- Target audience specification
- Prerequisites (or "None")
- Comprehensive list of main topics
- Section for topics NOT covered (to set boundaries)
- Detailed learning outcomes organized by all six Bloom's Taxonomy levels
- Descriptive text explaining why the course is important

### 1.3 After Creation

After creating the file, automatically proceed to **Step 2 (Analysis Workflow)** to validate the newly created course description and provide a quality score.

## Step 2: Course Description Analysis

Use this workflow when `/docs/course-description.md` exists.

### 2.1 Read the Course Description

Read `/docs/course-description.md` and analyze its contents against the quality criteria.

### 2.2 Course Description Quality Scoring System

Evaluate the course description using this 100-point scoring system:

| Element | Points | Criteria |
|---------|--------|----------|
| **Title** | 5 | Clear, descriptive course title present |
| **Target Audience** | 5 | Specific audience identified (e.g., "college undergraduate") |
| **Prerequisites** | 5 | Prerequisites listed or explicitly stated as "None" |
| **Main Topics Covered** | 10 | Comprehensive list of topics (ideally 5-10 topics) |
| **Topics Excluded** | 5 | Clear boundaries set for what's NOT covered |
| **Learning Outcomes Header** | 5 | Clear statement: "After this course, students will be able to..." |
| **Remember Level** | 10 | Multiple specific outcomes for remembering/recalling |
| **Understand Level** | 10 | Multiple specific outcomes for understanding/explaining |
| **Apply Level** | 10 | Multiple specific outcomes for applying/using |
| **Analyze Level** | 10 | Multiple specific outcomes for analyzing/breaking down |
| **Evaluate Level** | 10 | Multiple specific outcomes for evaluating/judging |
| **Create Level** | 10 | Multiple specific outcomes for creating/synthesizing; includes capstone ideas |
| **Descriptive Context** | 5 | Additional context about course importance, relevance, or value |

**Scoring Guidelines:**
- Award full points if element is complete and high-quality
- Award partial points if element is present but incomplete or vague
- Award 0 points if element is missing
- For Bloom's Taxonomy levels, require at least 3 specific, actionable outcomes for full points

### 2.3 Gap Analysis

Identify missing or weak elements:
- List each element that scored less than full points
- Explain what is missing or insufficient
- Indicate how the absence impacts learning graph generation

### 2.4 Improvement Suggestions

Provide specific, actionable recommendations:
- For missing elements: Suggest what should be added
- For weak elements: Provide examples of how to strengthen them
- For Bloom's Taxonomy outcomes: Recommend specific verbs and topics
- Prioritize suggestions that will have the most impact on reaching the goal of generating 200 concepts

### 2.5 Assessment Report

Generate a comprehensive report with:

1. **Overall Score**: X/100
2. **Quality Rating**:
   - 90-100: Excellent - Ready for learning graph generation
   - 75-89: Good - Minor improvements recommended
   - 60-74: Adequate - Several improvements needed
   - 40-59: Fair - Significant gaps to address
   - 0-39: Poor - Major revision required

3. **Detailed Scoring Breakdown**: Show points earned for each element
4. **Gap Analysis**: List of missing or weak elements
5. **Improvement Suggestions**: Prioritized recommendations
6. **Next Steps**:
   - If score ≥ 75: Ready to proceed with learning graph generation
   - If score < 75: Recommend addressing specific gaps before generating learning graph

### 2.6 Concept Generation Readiness

Assess whether the course description contains sufficient detail to generate 200 concepts:
- Evaluate topic breadth and depth
- Check if Bloom's Taxonomy outcomes suggest diverse concept types
- Estimate potential concept count based on current content
- Recommend additions if concept generation may fall short

### Add course-description.md to mkdocs.yml Navigation

After the course-description.md file has been added to the /docs direction,
ask the user if the new file should be added to the mkdocs.yml file.
If the answer is yes, place the new file after the about.md file.

## Best Practices

When using this skill:

1. **Be thorough**: Don't skip Bloom's Taxonomy levels—all six are essential for comprehensive learning
2. **Be specific**: Vague outcomes like "understand the material" won't support quality learning graphs
3. **Use action verbs**: Each outcome should start with a measurable verb (list, explain, apply, analyze, evaluate, design, etc.)
4. **Think concepts**: Each topic and outcome should suggest multiple learnable concepts
5. **Set boundaries**: Topics excluded are as important as topics covered for scope management

## Resources

### assets/

- `course-description-template.md`: Template structure for creating new course descriptions with all required sections and Bloom's Taxonomy framework
