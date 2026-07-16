# Concept Classifier Route

**Route:** `microsim-generator` -> `concept-classifier`
**Framework:** data contract plus a legacy p5.js scaffold
**Publication status:** requires native controls and host-book validation

## Overview

The Concept Classifier route helps an author create a scenario-based learning activity in which learners apply explicit criteria to choose one defensible category. The durable part is the instructional loop: a realistic case, a category judgment, a misconception-derived distractor, a hint, and a contrastive explanation.

The old standalone `concept-classifier` skill was consolidated into `microsim-generator`. Do not install the archived skill or treat the bundled canvas UI as publication-ready.

## When To Use It

Use this route when:

- the learner is rehearsing a real classification decision;
- every category has observable inclusion and exclusion criteria;
- the context supports one defensible best answer;
- distractors represent known misconceptions; and
- feedback explains why the nearest alternative is wrong.

Use annotation, comparison, or discussion instead when categories overlap intrinsically or several answers remain equally defensible. If a single-answer activity needs an ambiguity or precedence policy, state that policy before writing scenarios.

## Authoring Contract

1. Name the learner decision and prerequisite concepts.
2. Define every category with observable criteria.
3. Map each distractor to a misconception.
4. Write enough reviewed scenarios for every category to appear as a correct answer.
5. Keep `questionsPerQuiz` at or below the scenario count.
6. Give every scenario two to four unique options, one exact answer, a non-revealing hint, and a contrastive explanation.
7. Validate the dataset before interface work.
8. Publish only with native keyboard-operable controls, visible focus, announced feedback, responsive text, and the host textbook's own browser and accessibility gates.

The executable validator is:

```bash
python3 skills/microsim-generator/scripts/validate_concept_classifier.py path/to/data.json
```

The complete schema and a copy-safe example live in `skills/microsim-generator/references/concept-classifier-guide.md`.

## Scoring

A correct answer remains correct even after a hint. Hint use may reduce points, but mastery messages use percent correct. The interface reports correctness and percentage of available points separately.

## Accessibility Boundary

The bundled p5.js scaffold draws answer choices on a canvas and handles them with pointer coordinates. `describe()` can label the canvas, but it does not turn those choices into keyboard or screen-reader controls. A learner-facing classifier must use real HTML controls and prove that long scenario, option, hint, and explanation text does not clip.

## Files

The routed assets live in:

```text
skills/microsim-generator/
├── references/concept-classifier-guide.md
├── scripts/validate_concept_classifier.py
├── tests/test_validate_concept_classifier.py
└── assets/concept-classifier/
    ├── concept-classifier-template.js
    ├── data-template.json
    ├── main-template.html
    └── index-template.md
```

Use `skills/microsim-generator/assets/templates/p5/metadata-template.json` for metadata. The host textbook's canonical concepts, learning graph, workbook behavior, and publication gate remain authoritative.

## Related Routes

- [MicroSim P5 Generator](./microsim-p5.md) for general p5.js simulations
- [Quiz Generator](../book/quiz-generator.md) for chapter multiple-choice assessment
