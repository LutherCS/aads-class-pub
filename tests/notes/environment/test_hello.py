#!/usr/bin/env python3
"""
`hello` testing

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import pathlib

import pytest
import toml
from src.notes.environment import greet

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("data"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", get_cases("test_case_success"))
def test_greet(data, expected):
    """Testing the output"""
    assert greet(data) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", get_cases("test_case_error"))
def test_greet_err(data, expected):
    """Testing the exception"""
    with pytest.raises(TypeError) as exc:
        greet(data)
    assert str(exc.value) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
