#!/usr/bin/env python3
"""Validate the structural contract of a concept-classifier dataset."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def is_number(value: Any) -> bool:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def require_text(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path} must be a non-empty string")


def require_text_list(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{path} must be a non-empty list")
        return
    for index, item in enumerate(value):
        require_text(item, f"{path}[{index}]", errors)


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root must be an object"]

    require_text(data.get("title"), "title", errors)
    require_text(data.get("description"), "description", errors)

    config = data.get("config")
    if not isinstance(config, dict):
        errors.append("config must be an object")
        config = {}

    questions_per_quiz = config.get("questionsPerQuiz")
    if not isinstance(questions_per_quiz, int) or isinstance(questions_per_quiz, bool) or questions_per_quiz < 1:
        errors.append("config.questionsPerQuiz must be a positive integer")

    points_correct = config.get("pointsCorrect")
    points_with_hint = config.get("pointsWithHint")
    if not is_number(points_correct) or points_correct <= 0:
        errors.append("config.pointsCorrect must be greater than zero")
    if not is_number(points_with_hint) or points_with_hint < 0:
        errors.append("config.pointsWithHint must be zero or greater")
    elif is_number(points_correct) and points_with_hint > points_correct:
        errors.append("config.pointsWithHint must not exceed config.pointsCorrect")
    require_text(config.get("scenarioLabel"), "config.scenarioLabel", errors)
    require_text(config.get("instructionText"), "config.instructionText", errors)
    require_text(config.get("correctAnswerField"), "config.correctAnswerField", errors)

    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        errors.append("scenarios must be a non-empty list")
        scenarios = []
    elif isinstance(questions_per_quiz, int) and questions_per_quiz > len(scenarios):
        errors.append("config.questionsPerQuiz must not exceed the scenario count")

    seen_ids: set[Any] = set()
    used_categories: set[str] = set()
    correct_categories: set[str] = set()
    answer_field = config.get("correctAnswerField", "correctAnswer")
    if not isinstance(answer_field, str) or not answer_field:
        answer_field = "correctAnswer"

    for index, scenario in enumerate(scenarios):
        path = f"scenarios[{index}]"
        if not isinstance(scenario, dict):
            errors.append(f"{path} must be an object")
            continue
        scenario_id = scenario.get("id")
        if (
            not isinstance(scenario_id, (str, int))
            or isinstance(scenario_id, bool)
            or (isinstance(scenario_id, str) and not scenario_id.strip())
        ):
            errors.append(f"{path}.id must be a string or integer")
        elif scenario_id in seen_ids:
            errors.append(f"{path}.id duplicates {scenario_id!r}")
        else:
            seen_ids.add(scenario_id)
        require_text(scenario.get("scenario"), f"{path}.scenario", errors)
        require_text(scenario.get("explanation"), f"{path}.explanation", errors)
        require_text(scenario.get("hint"), f"{path}.hint", errors)
        require_text(scenario.get(answer_field), f"{path}.{answer_field}", errors)

        options = scenario.get("options")
        require_text_list(options, f"{path}.options", errors)
        if isinstance(options, list):
            if not 2 <= len(options) <= 4:
                errors.append(f"{path}.options must contain between 2 and 4 choices")
            comparable = [item.strip().casefold() for item in options if isinstance(item, str)]
            if len(comparable) != len(set(comparable)):
                errors.append(f"{path}.options must be unique ignoring case and surrounding whitespace")
            for option_index, option in enumerate(options):
                if isinstance(option, str) and option != option.strip():
                    errors.append(f"{path}.options[{option_index}] must not have surrounding whitespace")
            answer = scenario.get(answer_field)
            if isinstance(answer, str) and answer not in options:
                errors.append(f"{path}.{answer_field} must appear exactly in options")
            elif isinstance(answer, str) and answer.strip():
                correct_categories.add(answer)
            used_categories.update(item for item in options if isinstance(item, str) and item.strip())

    descriptions = data.get("categoryDescriptions")
    if not isinstance(descriptions, dict) or not descriptions:
        errors.append("categoryDescriptions must be a non-empty object")
        descriptions = {}
    for category in sorted(used_categories):
        require_text(descriptions.get(category), f"categoryDescriptions[{category!r}]", errors)
    if descriptions:
        uncovered = sorted(set(descriptions) - correct_categories)
        if uncovered:
            errors.append(f"every category must appear as a correct answer; uncovered: {uncovered}")

    messages = data.get("encouragingMessages")
    if not isinstance(messages, dict):
        errors.append("encouragingMessages must be an object")
    else:
        require_text_list(messages.get("correct"), "encouragingMessages.correct", errors)
        require_text_list(messages.get("incorrect"), "encouragingMessages.incorrect", errors)

    end_screen = data.get("endScreen")
    if not isinstance(end_screen, dict):
        errors.append("endScreen must be an object")
        end_screen = {}
    require_text(end_screen.get("tipsTitle"), "endScreen.tipsTitle", errors)
    require_text_list(end_screen.get("tips"), "endScreen.tips", errors)

    performance = end_screen.get("performanceMessages")
    levels = ("excellent", "good", "fair", "needsWork")
    thresholds: list[float] = []
    if not isinstance(performance, dict):
        errors.append("endScreen.performanceMessages must be an object")
    else:
        for level in levels:
            item = performance.get(level)
            if not isinstance(item, dict):
                errors.append(f"endScreen.performanceMessages.{level} must be an object")
                continue
            threshold = item.get("threshold")
            if not is_number(threshold) or not 0 <= threshold <= 100:
                errors.append(f"endScreen.performanceMessages.{level}.threshold must be between 0 and 100")
            else:
                thresholds.append(float(threshold))
            require_text(item.get("message"), f"endScreen.performanceMessages.{level}.message", errors)
            require_text(item.get("subMessage"), f"endScreen.performanceMessages.{level}.subMessage", errors)
        if len(thresholds) == len(levels) and not all(
            left > right for left, right in zip(thresholds, thresholds[1:])
        ):
            errors.append("performance thresholds must descend: excellent > good > fair > needsWork")
        if (
            isinstance(performance.get("needsWork"), dict)
            and performance["needsWork"].get("threshold") != 0
        ):
            errors.append("endScreen.performanceMessages.needsWork.threshold must equal 0")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.dataset.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}")
        return 1

    errors = validate(data)
    if errors:
        for error in errors:
            print(f"INVALID: {error}")
        return 1
    print(f"VALID: {args.dataset} ({len(data['scenarios'])} scenarios)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
