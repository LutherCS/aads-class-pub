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

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/projects/exam_strategy/")
DATA_DIR = pathlib.Path("data/projects/exam_strategy/")
FILE_PUBLIC = pathlib.Path("test_exam_strategy_public.toml")
FILE_SECRET = pathlib.Path("test_exam_strategy_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
QUESTIONS = [
    (v.get("filename"), v.get("selected"), v.get("total_val"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    QUESTIONS.extend(
        [
            (v.get("filename"), v.get("selected"), v.get("total_val"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, selected, total_val", QUESTIONS)
def test_exam_strategy(filename, selected, total_val):
    """Testing the output"""
    result = pick_questions_to_answer(DATA_DIR / pathlib.Path(filename))
    assert result[0] == selected
    assert result[1] == total_val


if __name__ == "__main__":
    pytest.main(["-v", "test_exam_strategy.py"])
