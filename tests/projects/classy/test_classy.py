#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.classy
"""

import pathlib
import pytest
import toml
from src.projects.classy import read_file, classify

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/projects/classy/")
DATA_DIR = pathlib.Path("data/projects/classy/")
FILE_PUBLIC = pathlib.Path("test_classy_public.toml")
FILE_SECRET = pathlib.Path("test_classy_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
PEOPLE = [
    (v.get("data"), v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    PEOPLE.extend(
        [
            (v.get("data"), v.get("expected"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", PEOPLE)
def test_read_file(data, expected):
    """Testing the file reader"""
    relatives = read_file(DATA_DIR / pathlib.Path(data))
    assert len(relatives) == len(expected)


@pytest.mark.timeout(TIME_LIMIT)
def test_classifier():
    """Testing the classifier"""
    zoo = {
        "Aardvark": "upper",
        "Beaver": "upper-upper",
        "Cheetah": "middle-upper",
        "Dolphin": "upper",
        "Elephant": "upper-middle-upper"
    }
    assert classify(zoo) == ["Beaver", "Elephant", "Aardvark", "Cheetah", "Dolphin"]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", PEOPLE)
def test_classy(data, expected):
    """Testing the output"""
    relatives = read_file(DATA_DIR / pathlib.Path(data))
    assert classify(relatives) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_classy.py"])
