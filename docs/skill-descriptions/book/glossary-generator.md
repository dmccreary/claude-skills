# Glossary Generator

This skill automatically generates a comprehensive glossary of terms from a learning graph's concept list, ensuring each definition follows ISO 11179 metadata registry standards (precise, concise, distinct, non-circular, and free of business rules).

## Step 1: Validate Input Quality

Assesses the quality of the concept list before generating definitions. Checks for duplicate concept labels (target: 100% unique), verifies Title Case formatting (target: 95%+ compliance), validates length constraints (target: 98% under 32 characters), and assesses concept clarity. Calculates a quality score (1-100 scale) and triggers user dialog if score is below 70 or issues are found.

## Step 2: Read Course Context

Reads the course description file and other markdown files in `/docs/**/*.md` to understand target audience, course objectives, prerequisites, and learning outcomes. This context ensures definitions use appropriate terminology and example complexity for the intended learners.

## Step 3: Generate Definitions

Creates ISO 11179-compliant definitions for each concept following four criteria worth 25 points each: Precision (accurately captures the concept's meaning in course context), Conciseness (20-50 words target length), Distinctiveness (unique and distinguishable from other concepts), and Non-circularity (avoids referencing undefined terms or circular chains).

## Step 4: Add Examples

Includes relevant examples for 60-80% of terms. Each example starts with "**Example:**" followed by a concrete illustration from the course domain in 1-2 sentences. Examples clarify concepts without adding confusion, using appropriate complexity for the target audience.

## Step 5: Add Cross-References

Adds references to related terms where appropriate. Uses "See also:" for related concepts and "Contrast with:" for opposing concepts. Ensures all cross-referenced terms exist in the glossary and limits cross-references to 1-3 per term.

## Step 6: Create Glossary File

Generates `docs/glossary.md` with level-4 headers (####) for term names, sorted alphabetically (case-insensitive). Each entry contains the definition in body text, followed by optional examples marked with "**Example:**". Maintains consistent spacing and formatting throughout.

## Step 7: Generate Quality Report

Creates `docs/learning-graph/glossary-quality-report.md` with ISO 11179 compliance metrics for each definition. Reports overall quality metrics including average definition length, percentage meeting all four criteria, circular definitions found, example coverage, and cross-reference statistics. Includes readability metrics (Flesch-Kincaid grade level) and recommendations for improvement.

## Step 8: Validate Output

Performs final validation checks: verifies 100% alphabetical ordering, validates all cross-references point to existing terms, ensures all concepts from input list are included, confirms markdown syntax renders correctly, and checks for zero circular definitions. Success criteria include overall quality score > 85/100 and proper mkdocs rendering.

## Step 9: Update Navigation

Optionally updates `mkdocs.yml` if it doesn't already include the glossary. Reads the configuration file, checks if "Glossary: glossary.md" exists in the nav section, adds it in an appropriate location if missing, and preserves existing navigation structure.

## Step 10: Generate Cross-Reference Index

Optionally creates `docs/learning-graph/glossary-cross-ref.json` for semantic search features. Produces a JSON file mapping each term to related terms, contrasts, and categories, enabling future capabilities like semantic search, concept relationship visualization, and automated suggestion of related terms.
