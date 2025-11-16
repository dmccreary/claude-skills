# FAQ Generator

This skill generates a comprehensive set of Frequently Asked Questions (FAQs) from course content, learning graphs, and glossary terms to help students understand common questions and prepare content for chatbot integration.

## Step 1: Assess Content Completeness

Calculates a content completeness score (1-100 scale) by evaluating required inputs: course description (25 points), learning graph with valid DAG structure (25 points), glossary with term count (15 points), total word count across all markdown files (20 points), and concept coverage percentage (15 points). Triggers user dialog if score is below 60 or critical inputs are missing.

## Step 2: Analyze Content for Question Opportunities

Reads and analyzes all content sources to identify common question patterns. Extracts questions from course description (scope, audience, outcomes, prerequisites), learning graph (definitions, relationships, prerequisites, progression), glossary (terminology, comparisons, examples), chapter content (themes, complex concepts, misconceptions, applications), and existing FAQ if present (preserving manual questions).

## Step 3: Generate Question Categories

Creates 6 standard categories with specific Bloom's Taxonomy distributions: Getting Started (10-15 questions, 60% Remember/40% Understand), Core Concepts (20-30 questions, distributed across Remember through Analyze), Technical Details (15-25 questions, terminology-focused), Common Challenges (10-15 questions, Apply/Analyze-heavy), Best Practices (10-15 questions, higher-order thinking), and Advanced Topics (5-10 questions, 60% Analyze/Evaluate/Create).

## Step 4: Generate Questions and Answers

Creates questions and answers following specific guidelines. Questions use level-2 headers, end with question marks, use glossary terminology, and stay concise (5-15 words). Answers are complete and standalone (100-300 words), include examples for 40% of entries, link to relevant sections (60%+ target), and are aligned with Bloom's Taxonomy levels (Remember, Understand, Apply, Analyze, Evaluate, Create).

## Step 5: Create FAQ File

Generates `docs/faq.md` with proper markdown structure using level-1 header for title, level-2 headers for categories and questions, body text for answers, markdown links to source content, and consistent formatting throughout. Organizes questions by the 6 standard categories with progressive difficulty.

## Step 6: Generate Chatbot Training JSON

Creates `docs/learning-graph/faq-chatbot-training.json` for RAG system integration. Each question entry includes unique ID, category, question text, full answer, Bloom's level, difficulty rating (easy/medium/hard), related concepts from learning graph, keywords for search optimization, source links, example presence flag, and word count.

## Step 7: Generate Quality Report

Creates `docs/learning-graph/faq-quality-report.md` with overall statistics (total questions, quality score, content completeness, concept coverage), category breakdown, Bloom's Taxonomy distribution analysis comparing actual vs target percentages, answer quality metrics (examples, links, length, completeness), organization quality assessment, and prioritized recommendations for improvement.

## Step 8: Generate Coverage Gaps Report

Creates `docs/learning-graph/faq-coverage-gaps.md` identifying concepts from the learning graph not covered in the FAQ. Prioritizes gaps into three categories: critical (high-centrality concepts with many dependencies), medium (moderate-centrality concepts), and low priority (leaf nodes or advanced concepts). Provides suggested questions for each gap.

## Step 9: Validate Output Quality

Performs comprehensive validation checks: uniqueness (scans for duplicate or near-duplicate questions), link validation (verifies all markdown links exist), Bloom's distribution (compares actual to target within ±10%), reading level (calculates Flesch-Kincaid grade level), answer completeness (ensures questions are fully addressed), and technical accuracy (cross-references with glossary and chapter content).

## Step 10: Update Navigation

Optionally updates `mkdocs.yml` if the FAQ is not already included. Reads the configuration file, checks if "FAQ: faq.md" exists in the nav section, adds it in an appropriate location (typically near end) if missing, and preserves existing navigation structure.
