# Quiz Generator

This skill generates interactive multiple-choice quizzes for each chapter of an intelligent textbook, with questions aligned to specific concepts from the learning graph and distributed across Bloom's Taxonomy cognitive levels to assess student understanding effectively.

## Step 1: Assess Content Readiness

Calculates content readiness score (1-100) for each target chapter based on five quality checks: chapter word count (20 points for 2000+ words), example coverage (20 points for 60%+ concepts with examples), glossary coverage (20 points for 80%+ chapter concepts defined), concept clarity (20 points for clear explanations), and learning graph alignment (20 points for all concepts mapped). Triggers user dialog if score is below 60 or critical content is missing.

## Step 2: Determine Target Distribution

Sets target Bloom's Taxonomy distribution based on chapter type (introductory, intermediate, or advanced). Introductory chapters focus heavily on Remember (40%) and Understand (40%) with minimal higher-order thinking. Intermediate chapters balance Remember (25%), Understand (30%), and Apply (30%) with some Analyze (15%). Advanced chapters emphasize Apply (25%), Analyze (25%), Evaluate (10%), and Create (5%) with less emphasis on lower levels. Target question count is 8-12 per chapter (default: 10).

## Step 3: Identify Concepts to Test

Analyzes chapter content and learning graph to prioritize concepts into three tiers. Priority 1 (must test) includes high-centrality concepts, concepts in chapter title/introduction, dedicated sections, and emphasized key terms. Priority 2 (should test) includes supporting concepts with substantial explanation, concepts with examples, and prerequisites. Priority 3 (may test) covers peripheral concepts mentioned briefly. Aims for 80%+ coverage of Priority 1 concepts.

## Step 4: Generate Questions by Bloom's Level

Creates questions using the mkdocs-material question admonition format with upper-alpha list styling. Each question uses level-4 header with number, `<div class="upper-alpha" markdown>` wrapper, numbered list (1-4) for options, and `??? question "Show Answer"` admonition. Questions are written according to Bloom's level: Remember (definitions/facts), Understand (explanations/relationships), Apply (scenarios), Analyze (patterns/causes), Evaluate (judgments), and Create (design solutions).

## Step 5: Write Quality Distractors

Ensures each incorrect answer option is plausible, uses related terminology, has similar length to correct answer, and addresses common misconceptions. Avoids obviously wrong answers, "all/none of the above" options, jokes, grammatical inconsistencies, and overlapping answers. Uses common distractor patterns including partial truth, reversals, similar terminology, and typical student errors.

## Step 6: Write Explanations

Creates explanations (50-100 words target) that clearly state the correct answer letter, explain why it's correct, reference chapter content or concept definitions, and optionally explain why distractors are incorrect. Each explanation includes the concept tested and a link to the relevant chapter section for additional detail.

## Step 7: Ensure Answer Balance

Verifies correct answers are distributed evenly across A, B, C, D options (target: 25% each, ±5% acceptable). Avoids predictable patterns like consecutive same letters, alternating sequences, or position bias. Generates random sequence, shuffles for each question, and adjusts if distribution is imbalanced.

## Step 8: Create Quiz File

Generates quiz as either a separate file (`docs/[section]/[chapter-name]-quiz.md`) or embedded at the end of the chapter file. Uses consistent formatting with level-4 headers for questions, horizontal rules (---) between questions, sequential numbering, and proper markdown rendering. Includes introductory text explaining the quiz purpose.

## Step 9: Generate Metadata File

Creates `docs/learning-graph/quizzes/[chapter-name]-quiz-metadata.json` containing chapter information, file paths, generation date, content readiness score, quality score, detailed question data (ID, number, text, correct answer, Bloom's level, difficulty, concept tested, links, distractor quality), answer distribution statistics, Bloom's distribution breakdown, and concept coverage metrics.

## Step 10: Generate Quiz Bank

Creates or updates `docs/learning-graph/quiz-bank.json` aggregating all questions across chapters. Each entry includes unique ID, chapter reference, question text, all options, correct answer, explanation, Bloom's level, difficulty, concept, source links, and tags. Supports LMS export, quiz randomization, alternative versions, chatbot integration, and study app integration.

## Step 11: Generate Quality Report

Creates `docs/learning-graph/quiz-generation-report.md` with overall statistics (total chapters, questions, averages, quality score), per-chapter summary table, Bloom's Taxonomy distribution analysis comparing actual vs target, answer balance statistics, concept coverage metrics, question quality analysis (well-formed questions, distractor quality, explanations, valid links), and prioritized recommendations for improvement.

## Step 12: Validate Quality

Performs comprehensive validation across 10 criteria: no ambiguity (one correct answer, clear question), distractor quality (plausible and educational), grammar and clarity (professional writing), answer balance (distributed across options), Bloom's distribution (matches target within ±15%), concept coverage (75%+ major concepts), no duplicates (unique questions), explanation quality (teaching value, proper length), link validation (all links work), and bias check (no cultural, gender, or accessibility issues).

## Step 13: Generate Alternative Questions

Optionally creates `docs/learning-graph/quizzes/alternative-questions.json` with 2-3 alternative questions per concept. Each alternative tests the same concept at the same Bloom's level but with different phrasing. Supports quiz randomization, test variations (A/B versions), practice mode with different questions each time, and adaptive difficulty adjustments.
