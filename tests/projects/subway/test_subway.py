#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.subway
"""

import pathlib
import pytest
import toml
from src.projects.subway import read_file, find_path

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/projects/subway/")
DATA_DIR = pathlib.Path("data/projects/subway/")
FILE_PUBLIC = pathlib.Path("test_subway_public.toml")
FILE_SECRET = pathlib.Path("test_subway_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
STATIONS = [
    (v.get("data"), v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    STATIONS.extend(
        [
            (v.get("data"), v.get("expected"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", STATIONS)
def test_subway(data, expected):
    """Testing the output"""
    g, src, dst = read_file(DATA_DIR / pathlib.Path(data))
    assert find_path(g, src, dst) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_subway.py"])
