# Concept Classifier Quiz Generator

**Name:** concept-classifier
**Width Responsive:** Yes
**Framework:** p5.js 1.11.10

## Overview

The Concept Classifier skill creates interactive classification quiz MicroSims where students read scenarios, examples, or descriptions and must classify them into the correct category from multiple choice options. All quiz content is stored in a separate `data.json` file for easy editing without modifying code.

## When to Use This Skill

Use this skill when you need to create a quiz where students must:

- **Identify types or categories** - e.g., cognitive biases, logical fallacies, literary devices
- **Classify examples** - e.g., animals into taxonomic groups, chemical reactions by type
- **Recognize patterns** - e.g., design patterns, musical forms, art movements
- **Match scenarios to concepts** - e.g., business scenarios to management theories

## Features

- Scenario-based questions with detailed descriptions
- Multiple choice answers (typically 4 options)
- Hint system that reduces points but helps struggling students
- Automatic explanations shown after each answer
- Score tracking with visual progress indicator
- Randomized question selection from a larger pool
- Encouraging feedback messages for correct and incorrect answers
- Animated mascot character that reacts to answers
- End screen with performance summary and customizable tips
- Fully configurable via `data.json` file

## Data Structure

```json
{
  "title": "Quiz Title",
  "description": "Quiz description",
  "config": {
    "questionsPerQuiz": 10,
    "pointsCorrect": 10,
    "pointsWithHint": 5,
    "scenarioLabel": "SCENARIO",
    "instructionText": "Select the correct category",
    "correctAnswerField": "correctAnswer"
  },
  "scenarios": [
    {
      "id": 1,
      "scenario": "Description of scenario...",
      "correctAnswer": "Category Name",
      "options": ["Category A", "Category B", "Category C", "Category D"],
      "explanation": "Why this answer is correct...",
      "hint": "A helpful hint..."
    }
  ],
  "encouragingMessages": {
    "correct": ["Excellent!", "Well done!"],
    "incorrect": ["Good try!", "Keep learning!"]
  },
  "endScreen": {
    "tipsTitle": "Tips:",
    "tips": ["Tip 1", "Tip 2", "Tip 3"],
    "performanceMessages": {
      "excellent": { "threshold": 90, "message": "Outstanding!" },
      "good": { "threshold": 70, "message": "Great Job!" },
      "fair": { "threshold": 50, "message": "Good Progress!" },
      "needsWork": { "threshold": 0, "message": "Keep Learning!" }
    }
  }
}
```

## File Structure

```
/docs/sims/$MICROSIM_NAME/
├── index.md           # Documentation with iframe embed
├── main.html          # HTML wrapper loading p5.js
├── $MICROSIM_NAME.js  # p5.js quiz logic
├── data.json          # Quiz questions and configuration
└── metadata.json      # Dublin Core metadata
```

## Example Use Cases

1. **Cognitive Bias Quiz** - Identify which bias is shown in scenarios
2. **Logical Fallacy Identifier** - Classify arguments by fallacy type
3. **Literary Device Recognizer** - Identify metaphors, similes, etc.
4. **Chemical Reaction Classifier** - Classify by reaction type
5. **Historical Era Matcher** - Match events to time periods
6. **Design Pattern Identifier** - Identify software patterns
7. **Musical Form Quiz** - Classify musical pieces by form
8. **Art Movement Classifier** - Match artworks to movements

## Bloom's Taxonomy Level

This quiz format primarily addresses **Application (Level 3)** - students apply their knowledge of categories to analyze new scenarios.

## Customization

### Visual Elements
- Canvas dimensions (default: 800×530)
- Color scheme (drawing area, buttons, feedback)
- Mascot character (default: animated brain)

### Quiz Behavior
- Number of questions per quiz
- Points for correct answers (with/without hint)
- Custom labels and instruction text
- Performance thresholds and messages

### Content
- Add scenarios to `data.json` without code changes
- Customize encouraging messages
- Set topic-specific tips for end screen

## Best Practices

### Writing Good Scenarios
- Be specific - scenarios should clearly demonstrate one category
- Avoid ambiguity - one obviously correct answer
- Use realistic examples - real-world scenarios are memorable
- Vary difficulty - mix easy and challenging
- Keep manageable length - 2-4 sentences

### Writing Good Distractors
- Make them plausible but distinguishable
- Use common misconceptions
- Keep similar length to correct answer

### Writing Good Explanations
- Explain the "why" not just state the answer
- Reference key distinguishing features
- Keep concise (2-3 sentences)

## Related Skills

- [MicroSim P5 Generator](./microsim-p5.md) - General p5.js simulations
- [Quiz Generator](../textbook-generation/quiz-generator.md) - Multiple choice quizzes for chapters

## Template Location

Templates are located in:
```
/skills/concept-classifier/templates/
├── concept-classifier-template.js
├── data-template.json
├── main-template.html
└── index-template.md
```
