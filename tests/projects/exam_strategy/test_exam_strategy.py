#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.exam_strategy
"""

import pathlib
import pytest
import toml
from src.projects.exam_strategy import pick_questions_to_answer


DATA_DIR = pathlib.Path("data/projects/exam_strategy/")
TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("filename"), case.get("selected"), case.get("total_val"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, selected, total_val", get_cases("test_case"))
def test_selection(filename, selected, total_val):
    """Testing the output"""
    result = pick_questions_to_answer(DATA_DIR / pathlib.Path(filename))
    assert result[0] == selected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, selected, total_val", get_cases("test_case"))
def test_total_value(filename, selected, total_val):
    """Testing the output"""
    result = pick_questions_to_answer(DATA_DIR / pathlib.Path(filename))
    assert result[1] == total_val


if __name__ == "__main__":
    pytest.main(["-v", "test_exam_strategy.py"])
