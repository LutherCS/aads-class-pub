#!/usr/bin/env python3
"""
Testing the project *subarray*
@author: Roman Yasinovskyy
@date: 2020
"""

import pathlib

import pytest
import toml
from src.projects.subarray import kadane

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("data"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", get_cases("test_case"))
def test_classy(data, expected):
    """Testing the implementation"""
    assert kadane(data) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_subarray.py"])
