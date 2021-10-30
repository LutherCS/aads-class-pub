#!/usr/bin/env python3
"""
`exam_strategy` testing

@authors: Roman Yasinovskyy
@version: 2021.10
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.exam_strategy import pick_questions_to_answer


DATA_DIR = pathlib.Path("data/projects/exam_strategy/")
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), encoding="utf-8") as file:
        all_cases = toml.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, selected",
    get_cases("test_case", "filename", "selected"),
)
def test_selection(filename: str, selected: list[int]):
    """Testing the selection"""
    result = pick_questions_to_answer(DATA_DIR / pathlib.Path(filename))
    assert result[0] == selected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, total_val", get_cases("test_case", "filename", "total_val")
)
def test_total_value(filename: str, total_val: int):
    """Testing the total value calculated"""
    result = pick_questions_to_answer(DATA_DIR / pathlib.Path(filename))
    assert result[1] == total_val


if __name__ == "__main__":
    pytest.main(["-v", __file__])
