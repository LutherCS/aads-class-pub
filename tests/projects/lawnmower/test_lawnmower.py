#!/usr/bin/env python3
"""
Testing the Lawn Mower
@author: Roman Yasinovskyy
@date: 2020
"""

import pathlib
import pytest
import toml
from src.projects.lawnmower import evaluate

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("data"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data_file, expected_file", get_cases("test_case"))
def test_evaluate(data_file, expected_file):
    """Testing the output"""
    with open(expected_file) as f:
        expected = "\n".join([x.strip() for x in f.readlines()])
    assert evaluate(data_file) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_lawnmower.py"])
