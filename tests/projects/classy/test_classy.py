#!/usr/bin/env python3
"""
`classy` testing

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import importlib
import pathlib
import sys

import pytest
import toml

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.classy import classify, read_file


TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("filename"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, expected", get_cases("test_case"))
def test_read_file(filename, expected):
    """Testing the file reader"""
    relatives = read_file(filename)
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
def test_classifier(zoo, expected):
    """Testing the classifier"""
    assert classify(zoo) == expected


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, expected", get_cases("test_case"))
def test_classy(filename, expected):
    """Testing the output"""
    relatives = read_file(filename)
    assert classify(relatives) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
