#!/usr/bin/env python3
"""
`classy` testing

@authors: Roman Yasinovskyy
@version: 2024.9
"""

import importlib
import pathlib
import sys
from typing import Generator

import pytest
import tomllib

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.classy import classify, read_file


DATA_DIR = pathlib.Path("data/projects/classy/")
TIME_LIMIT = 1


def get_cases(category: str, *attribs: str) -> Generator:
    """Get test cases from the TOML file"""
    with open(pathlib.Path(__file__).with_suffix(".toml"), "rb") as file:
        all_cases = tomllib.load(file)
        for case in all_cases[category]:
            yield tuple(case.get(a) for a in attribs)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, expected", get_cases("test_case", "filename", "expected")
)
def test_read_file(filename: str, expected: list[str]):
    """Testing the file reader"""
    relatives = read_file(DATA_DIR / pathlib.Path(filename))
    assert len(relatives) == len(expected)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "zoo, expected",
    [
        ({"Ant": "upper", "Bee": "middle", "Cat": "lower"}, ["Ant", "Bee", "Cat"]),
        ({"Dog": "middle", "Elk": "upper", "Frog": "lower"}, ["Elk", "Dog", "Frog"]),
        (
            {
                "Aardvark": "upper",
                "Beaver": "upper-upper",
                "Cheetah": "middle-upper",
                "Dolphin": "upper",
                "Elephant": "upper-middle-upper",
            },
            ["Beaver", "Elephant", "Aardvark", "Cheetah", "Dolphin"],
        ),
    ],
)
def test_classifier(zoo: dict[str, str], expected: list[str]):
    """Testing the classifier"""
    assert classify(zoo) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "filename, expected", get_cases("test_case", "filename", "expected")
)
def test_classy(filename: str, expected: list[str]):
    """Testing the output"""
    relatives = read_file(DATA_DIR / pathlib.Path(filename))
    assert classify(relatives) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
