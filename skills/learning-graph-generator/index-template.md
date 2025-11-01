# Learning Graph for TEXTBOOK_NAME

This section contains the learning graph for this textbook.  A learning graph is
a graph of concepts used in this textbook.  Each concept is represented by a
node in a network graph.  Concepts are connected by directed edges that indicate
what concepts each node depends on before that concept is understood by the student.

A learning graph is the foundational data structure for intelligent textbooks that can recommend learning paths.
A learning graph is like a roadmap of concepts to help students arrive at their learning goals.

At the left of the learning graph are prerequisite or foundational concepts.  They
have no outbound edges.  They only have inbound edges for other concepts that depend on
understanding these foundational prerequisite concepts.  At the far right
we have the most advanced concepts in the course.  To master these concepts you
must understand all the concepts that they point to.

Here are other files used by the learning graph.

## Course Description

We use the [Course Description](../course-description.md) as
the source document for the concepts that are included in this course.
The course description uses the 2001 Bloom taxonomy to order learning objectives.

## List of Concepts

We use generative AI to convert the course description into a [Concept List](./concept-list.md).
Each concept is in the form of a short Title Case label with most labels under 32 characters long.

## Concept Dependency List

We next use generative AI to create a Directed Acyclic Graph (DAG).  DAGs do not have cycles where
concepts depend on themselves.  We provide the DAG in two formats.  One is a [CSV file](learning-graph.csv) and the other
format is a [JSON file](learning-graph.json) that uses the vis-network JavaScript library format.  The vis-network format uses `nodes`, `edges` and `metadata`
elements with edges containing `from` and `to` properties.  This makes it easy for you to view and edit the learning
graph using an editor built with the vis-network tools.

## Analysis & Documentation

### Course Description Quality Assessment

This report rates the overall quality of the course description for the purpose of generating a learning graph.

- Course description fields and content depth analysis
- Validates course description has sufficient depth for generating 200 concepts
- Compares course description against similar courses
- Identifies content gaps and strengths
- Suggests areas of improvement
[Vew the Course Description Quality Assessment](course-description-assessment.md)

### Learning Graph Quality Validation

This report gives you an overall assessment of the quality of the learning graph.
It uses graph algorithms to look for specific quality patterns in the graph.

- Graph structure validation - all concepts are connected
- DAG validation (no cycles detected)
- Foundational concepts: 10 entry points
- Indegree distribution analysis
- Longest dependency chains
- Connectivity: percent of nodes connected to the main cluster

[View the Learning Graph Quality Validation](quality-metrics.md)

### Concept Taxonomy

In order to see patterns in the learning graph, it is useful to assign colors
to each concept based on the concept type.  We use generative AI to
create about a dozen categories for our concepts and then place each concept
into a single primary classifier.

- A concept classifier taxonomy with approximately 12 categories (+/- 1 or 2)
- Category organization - foundational elements first, course capstone project ideas last
- Balanced categories (3.5% - 15% each)
- All categories under 30% threshold
- Pedagogical flow recommendations
- Clear 3-5 letter abbreviations for use in CSV file
- A Miscellaneous (MOSC) category is sometimes added
[View the Concept Taxonomy](concept-taxonomy.md)

### Taxonomy Distribution

This reports shows how many concepts fit into each category of the taxonomy.
Our goal is a somewhat balanced taxonomy where each category holds an
equal number of concepts.  We also don't want any category to contain
over 30% of our concepts.

- Statistical breakdown
- Detailed concept listing by category
- Visual distribution table
- Balance verification

[View the Taxonomy Distribution Report](./taxonomy-distribution.md)