---
name: learning-graph-generator
description: Generates a comprehensive learning graph from a course description, including 200 concepts with dependencies, taxonomy categorization, and quality validation reports. Use this when the user wants to create a structured knowledge graph for educational content.
---

# Learning Graph Generator

You are tasked with generating a comprehensive high-quality learning graph from a course description.
A learning graph is the foundational data structure for intelligent textbooks that can recommend learning paths.
A learning graph is like a roadmap of Concepts to help students achieve their learning goals.
A learning graph is an DAG Concept graph.  Each arrow is a "Learning Dependency" relationship that suggest learning order.

Follow these steps carefully:

## Markdown Generation Rules

1. Always place a blank line before any markdown list.  This is required by the mkdocs markdown tools.

## Mkdocs Navigation Rules

After you add a markdown file (any file with an extenion `.md`) make sure to add that file
to the navigation structure in the mkdocs.yml file.  Here is an example of the nav section
for the learning graph section:

```yml
  - Learning Graph:
    - Introduction: learning-graph/index.md
    - Course Description Assessment: learning-graph/course-description-assessment.md
    - Concept Enumeration: learning-graph/list-concepts.md
    - Graph Quality Analysis: learning-graph/graph-quality-analysis.md
    - Concept Taxonomy: learning-graph/concept-taxonomy.md
    - Taxonomy Distribution Report: learning-graph/taxonomy-distribution-report.md
```

## Step 0: Setup

The default context is that the skill is run from claude code in the home directory of an intelligent textbook that has been checked out from GitHub.
There should be a docs directory with a standard mkdocs.yml file in the home git directory.
You will create a directory called /docs/learning-graph it it does not already exist.  
The path is relative to the git home directory.  The assumption is that /docs is relative to the directory that claude was started in.

`mkdir -p docs/learning-graph; cd docs/learning-graph`

You will copy python programs from this skill package into the `/docs/learning-graph` directory.  
You will execute python from that directory.

If you do not see the `docs` directory and the `mkdocs.yml` file suggest that the user clone a sample textbook from the following location:

`git clone https://github.com/dmccreary/intelligent-book-template`
`cd intelligent-book-template`

## Step 1: Course Description Quality Assessment

First, analyze the provided course description at [course-description.md](../course-description.md) to ensure it has enough content to generate 200 high-quality concepts:

1. Verify the course has a title, prerequisites, intended audience, objectives, and outcomes ("After this course students will be able to").  If these fields are missing ask the user for this information. 
1. Examine the depth and breadth of topics covered
2. Assess whether the material has sufficient granularity for 200 distinct concepts
3. Check for diverse topic areas and learning objectives
4. Provide detailed feedback to the user about:
   - List the expected content that you found
   - Estimated number of concepts you can derive
   - Compare this concept number with similar courses
   - Describe areas where the course description is strong
   - Any gaps or areas that might be under-represented
   - Suggest how the 2001 Bloom taxonomy (remember, understand, apply, analyze, evaluate, create) could improve the outcomes descriptions
   - Objective overall quality assessment on a scale of (1-poor to 100-perfect)
   - Suggest that the user does not proceed unless a quality score is 70 or above

Save this report to [course-description-assessment.md](./course-description-assessment.md)

5. **Ask the user if you should proceed** with generating the learning graph

## Step 2: Generate Concept Labels

Once approved, generate 200 concept labels from the course content:

**Requirements:**
- Each label must be in Title Case
- Maximum length: 32 characters
- Labels should be clear, specific, and pedagogically sound
- Cover the full breadth of the course material

**Output:**
- Save the numbered list to [concept-list.md](./concept-list.md)
- Format: Simple numbered list (1-200) in a markdown file
- Make sure that each number is unique so it can be used as a ConceptID
- Inform the user the file has been created
- Tell the user they should view the list and add and remove concepts now
- Tell the user it is best review the concept list before the next steps

## Step 3: Generate Dependency Graph

Create a CSV file mapping dependencies between concepts:

**Format:**
- Filename: [learning-graph.csv](./learning-graph.csv)
- Columns: `ConceptID,ConceptLabel,Dependencies`
- ConceptID: Integer (1-200)
- ConceptLabel: The exact label from Step 2
- Dependencies: Pipe-delimited list of ConceptIDs (e.g., "1|3|7")

**Dependency Rules:**
- Foundational/prerequisite concepts have NO dependencies (empty Dependencies field)
- All other concepts must have at least one dependency
- No concept can depend on itself
- The graph must be a Directed Acyclic Graph (DAG) - no cycles
- Create meaningful learning pathways, not just linear chains
- Consider prerequisite relationships carefully
- Next, run the csv-to-json.py program.  
- `python csv-to-json.py learning-graph.csv learning-graph.json`
It will read the [learning-graph.csv](./learning-graph.csv) and return a [learning-graph.json](./learning-graph.json) file in vis-network.js format

Verify that the file [learning-graph.json](./learning-graph.json) is present and is a valid JSON file.

## Step 4: Learning Graph Quality Validation

Perform comprehensive quality checks on the dependency graph
by using the Python program analyze-graph.py in this skill.
It will do the following checks:

1. **Verify DAG structure**: Ensure no cycles exist
2. **Check for self-dependencies**: No concept should depend on itself
3. **Foundational concepts**: Identify concepts with zero dependencies
4. **Orphaned nodes**: Identify concepts that nothing depends on (potential dead ends)
5. **Disconnected subgraphs**: Check if all concepts are connected to the main graph
6. **Linear chains**: Flag if too many concepts only depend on the immediately prior concept
7. **Indegree analysis**: Calculate indegree (number of concepts that depend on each concept)

Shell command `python analyze-graph.py learning-graph.csv quality-metrics.md`

Verify the report has been written to [quality-metrics.md](./quality-metrics.md)

**Generate quality metrics report:**
- Total concepts with zero dependencies - outbound arrows (foundational prerequisites)
- Total concepts with 1+ dependencies
- Average number of dependencies per concept
- Maximum dependency chain length
- Number of orphaned nodes
- Number of disconnected subgraphs
- Top 10 concepts with highest indegree (most depended-upon concepts)

Give the user a general quality score on a scale of 1 (poor) to 100 (perfect).
If the learning graph does not get a score above 70, suggest that the user iterates on the process

## Step 5: Create Concept Taxonomy

Develop a categorical taxonomy for organizing concepts:

**Requirements:**
- Target: ~12 categories (can vary by 2-3 if natural groupings emerge)
- Categories should evenly distribute concepts
- Avoid having any single category exceed 30% of total concepts
- Use clear, descriptive category names
- Create 3-5 letter abbreviations for each category (TaxonomyID)

**Output:**
- Save taxonomy to [concept-taxonomy.md](./concept-taxonomy.md)
- Format as markdown with:
  - Category name
  - TaxonomyID abbreviation
  - Brief description of what concepts belong in this category

## Step 6: Add Taxonomy to CSV

Update the dependencies CSV file:

1. Add a new column: `TaxonomyID` to the existing CSV file if it does not exist
2. For each concept, assign the best matching TaxonomyID
3. Use "MISC" for concepts without a clear category match
4. Save the updated file to [learning-graph.csv](./learning-graph.csv)

You can use the Python Program add-taxonomy.py as a template
that will do the substitution.

**Final CSV columns:** `ConceptID,ConceptLabel,Dependencies,TaxonomyID`

## Step 7: Taxonomy Distribution Report

Generate a distribution analysis:

1. Count concepts in each category
2. Calculate percentages
3. Identify over-represented categories (>30%)
4. Suggest alternative categorization if needed

Use the python report in this skill called taxonomy-distribution.py

**Output:**
- Save to [taxonomy-distribution.md](./taxonomy-distribution.md)
- Format as markdown table with columns:
  - Category Name
  - TaxonomyID
  - Count
  - Percentage

## Step 8: Create new index.md from index-template.md

Create a new `index.md` file in the learning-graph directory from the file index-template.md in this skill.
Customize the new index.md file to reflect the name of this intelligent book.  Look for values in all uppercase (TEXTBOOK_NAME)
and replace them with the appropriate values.

## Step 9: Completion

Inform the user that the learning graph generation is complete! Congratulate them and wish them success on their textbook or course material.

**Files created:**
- [course-description-assessment.md](./course-description-assessment.md) - quality assessment of the course description
- [concept-list.md](./concept-list.md) - Numbered list of 200 concepts
- [learning-graph.csv](./learning-graph.csv) - Full dependency graph with taxonomy
- [learning-graph.json](./learning-graph.json) - Full dependency graph in vis-network.js JSON format
- [concept-taxonomy.md](./concept-taxonomy.md) - Category definitions
- [quality-metrics.md](./quality-metrics.md) - Quality validation report
- [taxonomy-distribution.md](./taxonomy-distribution.md) - Category distribution analysis

---

## Important Notes

- Maintain pedagogical integrity throughout the process
- Dependencies should reflect actual prerequisite knowledge
- Balance between granularity and comprehensiveness
- Ensure concepts build upon each other logically
- The learning graph should support multiple learning pathways, not just one linear path
