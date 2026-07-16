# Concept Classifier Quiz Guide

> Formerly the standalone skill `concept-classifier`.

## Overview

This guide creates interactive classification quiz MicroSims. Students are presented with scenarios, examples, or descriptions and must classify them into the correct category from multiple choice options. Use the pattern to teach discrimination between categories, not merely to make recall practice look interactive.

The bundled p5.js files are legacy scaffolding, not publication-ready proof. In particular, the canvas-drawn answer choices are not native keyboard or screen-reader controls. A published classifier must expose each choice as a real HTML button, preserve a visible focus state, announce the result and explanation, and pass the host textbook's own accessibility and browser gates.

## When to Use This Guide

Use this guide when you need to create a quiz where students must:

- **Identify types or categories** - e.g., identify which cognitive bias is shown, which logical fallacy is used, which literary device is present
- **Classify examples** - e.g., classify animals into taxonomic groups, chemical reactions by type, historical events by era
- **Recognize patterns** - e.g., recognize which design pattern is used, which musical form is playing, which art movement a painting belongs to
- **Match scenarios to concepts** - e.g., match business scenarios to management theories, symptoms to conditions, code snippets to algorithms

Use a classifier only when every category has observable decision criteria and each assessed scenario has one defensible best answer under the stated context. Do not force intrinsically overlapping, contested, or open-ended judgments into a single-answer quiz. Use a comparison, annotation, or discussion activity instead.

Before generating files, record:

- the learner decision the classifier rehearses;
- the observable criteria that separate each category;
- the prerequisite concepts learners need;
- the misconception represented by each distractor;
- the policy for ambiguous or boundary cases; and
- the feedback or artifact retained after the attempt.

## Features

- **Scenario-based questions** with detailed descriptions
- **Multiple choice answers** (typically 4 options per question)
- **Hint system** that reduces points but helps struggling students
- **Automatic explanations** shown after each answer
- **Score tracking** with visual progress indicator
- **Randomized question selection** from a larger pool
- **Encouraging feedback messages** for both correct and incorrect answers
- **Animated mascot character** that reacts to answers
- **End screen** with performance summary and tips
- **Fully configurable** via data.json file

## Data Structure

All quiz content is stored in a `data.json` file for easy editing. The following is an intentionally small but valid two-category dataset. The bundled starter below expands the same contract to four categories, four scenarios, and a quiz length of four.

```json
{
  "title": "Quiz Title Here",
  "description": "Brief description of what this quiz tests",
  "config": {
    "questionsPerQuiz": 2,
    "pointsCorrect": 10,
    "pointsWithHint": 5,
    "scenarioLabel": "SCENARIO",
    "instructionText": "Select the correct category for this scenario",
    "correctAnswerField": "correctAnswer"
  },
  "scenarios": [
    {
      "id": 1,
      "scenario": "Description of the scenario or example to classify...",
      "correctAnswer": "Category A",
      "options": ["Category A", "Category B"],
      "explanation": "Category A is correct because [criterion]. Unlike Category B, this case [distinguishing feature].",
      "hint": "Compare the defining criteria for Category A and Category B."
    },
    {
      "id": 2,
      "scenario": "A contrasting scenario whose defining feature satisfies Category B...",
      "correctAnswer": "Category B",
      "options": ["Category A", "Category B"],
      "explanation": "Category B is correct because [criterion]. Unlike Category A, this case [distinguishing feature].",
      "hint": "Identify the one feature that rules out Category A."
    }
  ],
  "encouragingMessages": {
    "correct": [
      "Excellent!",
      "Well done!",
      "Great job!",
      "You got it!",
      "Perfect!"
    ],
    "incorrect": [
      "Not quite—now you know for next time!",
      "Good try! This one is tricky.",
      "Learning from mistakes makes us better!",
      "Keep practicing!",
      "Almost! Now you'll remember it."
    ]
  },
  "categoryDescriptions": {
    "Category A": "Observable inclusion and exclusion criteria for Category A",
    "Category B": "Observable inclusion and exclusion criteria for Category B"
  },
  "endScreen": {
    "tipsTitle": "Tips for Success:",
    "tips": [
      "First tip for students...",
      "Second tip for students...",
      "Third tip for students..."
    ],
    "performanceMessages": {
      "excellent": {
        "threshold": 90,
        "message": "Outstanding!",
        "subMessage": "You have excellent classification skills."
      },
      "good": {
        "threshold": 70,
        "message": "Great Job!",
        "subMessage": "You classified most items correctly."
      },
      "fair": {
        "threshold": 50,
        "message": "Good Progress!",
        "subMessage": "Keep practicing to improve."
      },
      "needsWork": {
        "threshold": 0,
        "message": "Keep Learning!",
        "subMessage": "Practice makes perfect."
      }
    }
  }
}
```

## File Structure

Each Concept Classifier MicroSim creates these files:

```
/docs/sims/$MICROSIM_NAME/
├── index.md           # Documentation page with iframe embed
├── main.html          # HTML wrapper loading p5.js
├── $MICROSIM_NAME.js  # p5.js quiz logic
├── data.json          # Quiz questions and configuration
└── metadata.json      # Dublin Core metadata
```

## URI Scheme for Discoverability

All MicroSim HTML files include this schema meta tag for global discoverability:

```html
<meta name="schema" content="https://dmccreary.github.io/intelligent-textbooks/ns/microsim/v1">
```

This enables counting and discovery of MicroSims across GitHub. See the [URI Scheme documentation](https://dmccreary.github.io/intelligent-textbooks/uri-scheme/) for details.

## Customization Options

### Visual Customization

The JavaScript file contains configurable parameters:

```javascript
// Canvas dimensions
let canvasWidth = 800;
let drawHeight = 480;
let controlHeight = 50;

// Colors (can be customized)
// Drawing area: 'aliceblue' with 'silver' border
// Correct answer: green tones
// Incorrect answer: orange/red tones
// Mascot: pink brain character (can be replaced)
```

### Mascot Character

The default mascot is an animated brain character with three expressions:

- **neutral** - default state
- **happy** - when answer is correct
- **thinking** - when hint is used or answer is incorrect

You can customize or replace the `drawMascotCharacter()` function to use a different mascot appropriate to your subject domain.

### Question Count

The bundled data template contains four sample scenarios, covers every defined category once, and therefore sets `questionsPerQuiz` to four. After adding a reviewed production pool, choose a quiz length that does not exceed that pool:

```json
"config": {
  "questionsPerQuiz": 10
}
```

Keep this choice in `data.json`; do not create a second question-count authority by hardcoding the slice in JavaScript.

## Example Use Cases

### 1. Cognitive Bias Quiz (Ethics/Psychology)
Students read scenarios demonstrating cognitive biases and must identify which bias is shown.

### 2. Logical Fallacy Identifier (Philosophy/Critical Thinking)
Students analyze arguments and identify which logical fallacy is present.

### 3. Literary Device Recognizer (English/Literature)
Students read passages and identify metaphors, similes, personification, etc.

### 4. Chemical Reaction Classifier (Chemistry)
Students read reaction descriptions and classify as synthesis, decomposition, single replacement, etc.

### 5. Historical Era Matcher (History)
Students read about events or artifacts and match them to the correct historical period.

### 6. Design Pattern Identifier (Computer Science)
Students read code scenarios and identify which software design pattern applies.

### 7. Musical Form Quiz (Music)
Students listen to or read about musical pieces and identify the form (sonata, rondo, theme and variations, etc.).

### 8. Art Movement Classifier (Art History)
Students view or read about artworks and classify them into movements (Impressionism, Cubism, etc.).

## Implementation Steps

1. **Name the learner decision** - State what a learner should be able to distinguish after the activity and where that judgment is used.

2. **Define category criteria** - Give every category observable inclusion and exclusion criteria. Reject the format if boundary cases cannot be handled honestly.

3. **Create scenarios** - Write enough scenarios to cover every category and misconception. Prefer realistic cases with source or authoring provenance.

4. **Design distractors from misconceptions** - Each wrong option should diagnose a plausible confusion, not merely make the answer list longer.

5. **Write contrastive explanations** - Explain both why the selected category fits and why the nearest alternative does not.

6. **Add hints** - Guide attention to the distinguishing evidence without naming the answer.

7. **Validate the dataset** - Run the bundled validator before browser testing:

   ```bash
   python3 skills/microsim-generator/scripts/validate_concept_classifier.py \
     docs/sims/<name>/data.json
   ```

8. **Build accessible controls** - Use native buttons, keyboard navigation, visible focus, and an announced feedback region. Do not publish the mouse-only canvas choices unchanged.

9. **Test the learning interaction** - Verify answer identity, hint scoring, explanations, restart behavior, narrow layouts, keyboard use, screen-reader output, and the host project's publication gates.

## Best Practices

### Writing Good Scenarios

- **Be specific** - Scenarios should clearly demonstrate one category
- **Avoid ambiguity** - Each scenario should have one clearly correct answer
- **Label boundary cases** - If the real domain permits overlap, state the assumption that makes one answer best or move the case to a discussion activity
- **Use realistic examples** - Real-world scenarios are more memorable
- **Vary difficulty** - Mix easy and challenging scenarios
- **Keep length manageable** - Scenarios should fit in the display area (roughly 2-4 sentences)

### Writing Good Distractors (Wrong Answers)

- **Make them plausible** - Wrong answers should be reasonable alternatives
- **Avoid obviously wrong options** - Each option should require thought
- **Use common misconceptions** - Include options that represent typical errors
- **Make distractors diagnostic** - Be able to name the misconception each distractor reveals
- **Keep similar length** - Options should be roughly equal in length

### Writing Good Explanations

- **Explain the "why"** - Don't just state the answer, explain the reasoning
- **Contrast the nearest alternative** - Tell the learner what evidence rules out the most plausible distractor
- **Reference key features** - Point out what makes this scenario fit the category
- **Keep it concise** - 2-3 sentences is ideal
- **Educational tone** - Use this as a teaching moment

## Template Files

Template files live in this skill's `assets/concept-classifier/` directory:

- `concept-classifier-template.js` - Generalized p5.js quiz logic
- `data-template.json` - Example data structure with placeholders
- `main-template.html` - HTML wrapper
- `index-template.md` - Documentation page template

Use `assets/templates/p5/metadata-template.json` for the required `metadata.json`; the classifier asset directory does not carry a second metadata authority.

## Data Quality Contract

The validator rejects datasets that would otherwise fail silently or teach the wrong distinction:

- missing titles, descriptions, scenarios, feedback messages, or category definitions;
- a `questionsPerQuiz` larger than the scenario pool;
- duplicate scenario IDs, duplicate answer options, or fewer than two/more than four choices that the fixed legacy layout cannot render safely;
- a correct answer that is not one of the options;
- options with no category description;
- hint points outside the range from zero to the full-credit score; and
- missing or non-descending performance thresholds.

Validation proves structural consistency, not instructional truth. A subject-matter reviewer must still inspect category criteria, scenario provenance, ambiguity, distractor diagnoses, and explanations.

## Bloom's Taxonomy Level

This quiz format can address **Application (Level 3)** when learners apply explicit criteria to genuinely new scenarios. Recalling memorized labels from rehearsed examples remains Remember or Understand regardless of the interface.

## Integration with MkDocs

After creating the MicroSim, add it to `mkdocs.yml`:

```yaml
nav:
  - MicroSims:
    - Your Quiz Name: sims/your-quiz-name/index.md
```

## Technical Notes

- **Framework**: p5.js 1.11.10
- **Responsive**: The legacy scaffold changes width but retains a fixed height; the published activity must prove that scenario, option, hint, and explanation text do not clip at supported widths
- **Data loading**: Uses p5.js `loadJSON()` in `preload()`
- **Accessibility**: `describe()` labels the canvas but does not make canvas-drawn choices operable; native controls and announced feedback are required
- **Browser support**: Modern browsers (Chrome, Firefox, Safari, Edge)

The end screen reports both percent correct and percentage of available points. Performance messages use percent correct; hint-reduced points remain a separate coaching signal and never turn a correct answer into a failed mastery tier.

## Conclusion

The Concept Classifier pattern is useful when the learning objective is a real discrimination task and the category boundary is teachable. Separating content from logic makes reuse easier, while the validator and publication gates keep structural convenience from replacing instructional judgment.
