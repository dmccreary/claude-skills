# Learning Graph Generator

This skill generates a comprehensive learning graph from a course description, including 200 concepts with dependencies, taxonomy categorization, and quality validation reports.

## Step 0: Setup

Ensures the proper directory structure exists and prepares the working environment. Creates the `/docs/learning-graph` directory and copies necessary Python programs from the skill package. Verifies that mkdocs.yml and the docs directory are present.

## Step 1: Course Description Quality Assessment

Analyzes the course description to ensure it has sufficient content to generate 200 high-quality concepts. Verifies required elements (title, prerequisites, audience, objectives, outcomes) and assesses depth, breadth, and granularity. Generates a quality score (1-100) and provides detailed feedback. Asks user for approval before proceeding.

## Step 2: Generate Concept Labels

Creates 200 concept labels from the course content. Each label must be in Title Case with a maximum length of 32 characters. Labels should be clear, specific, and pedagogically sound. Saves the numbered list to `concept-list.md` and prompts user to review before continuing.

## Step 3: Generate Dependency Graph

Creates a CSV file mapping learning dependencies between concepts. Each concept gets a ConceptID, ConceptLabel, and Dependencies (pipe-delimited list). Ensures the graph is a Directed Acyclic Graph (DAG) with no cycles or self-dependencies. Converts CSV to JSON format using the `csv-to-json.py` program.

## Step 4: Learning Graph Quality Validation

Performs comprehensive quality checks using the `analyze-graph.py` program. Verifies DAG structure, checks for self-dependencies, identifies foundational concepts, orphaned nodes, and disconnected subgraphs. Generates quality metrics report including indegree analysis and dependency chain statistics. Provides a quality score (1-100).

## Step 5: Create Concept Taxonomy

Develops a categorical taxonomy with approximately 12 categories for organizing concepts. Categories should evenly distribute concepts (no category exceeding 30% of total). Creates clear category names with 3-5 letter abbreviations (TaxonomyID). Saves taxonomy definitions to `concept-taxonomy.md`.

## Step 6: Add Taxonomy to CSV

Updates the learning graph CSV file by adding a TaxonomyID column. Assigns the appropriate TaxonomyID to each concept based on the taxonomy created in Step 5. Uses "MISC" for concepts without a clear category match. The `add-taxonomy.py` program can assist with this substitution.

## Step 7: Taxonomy Distribution Report

Generates a distribution analysis showing concept counts and percentages for each category. Uses the `taxonomy-distribution.py` program to create a markdown table. Identifies over-represented categories and suggests alternative categorization if needed. Saves results to `taxonomy-distribution.md`.

## Step 8: Create Index File

Creates a new `index.md` file in the learning-graph directory from the `index-template.md` template. Customizes the file by replacing placeholder values (like TEXTBOOK_NAME) with appropriate values specific to the intelligent textbook.

## Step 9: Completion

Informs the user that the learning graph generation is complete and lists all generated files: course description assessment, concept list, learning graph CSV and JSON, concept taxonomy, quality metrics report, and taxonomy distribution report.
