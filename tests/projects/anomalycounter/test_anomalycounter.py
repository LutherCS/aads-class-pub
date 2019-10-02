#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.anomalycounter
"""

import pathlib
import pytest
import toml
from src.projects.anomalycounter import count

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/projects/anomalycounter/")
DATA_DIR = pathlib.Path("data/projects/anomalycounter/")
FILE_PUBLIC = pathlib.Path("test_anomalycounter_public.toml")
FILE_SECRET = pathlib.Path("test_anomalycounter_secret.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC
    FILE_SECRET = THIS_DIR / TEST_DIR / FILE_SECRET

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
IMAGES = [
    (v.get("data"), v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]

if FILE_SECRET.exists():
    all_test_cases.update(toml.load(FILE_SECRET))
    IMAGES.extend(
        [
            (v.get("data"), v.get("expected"))
            for v in all_test_cases.get("case_secret").get("success").values()
        ]
    )


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", IMAGES)
def test_anomalycounter(data, expected):
    """Testing the output"""
    assert count(DATA_DIR / pathlib.Path(data)) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_anomalycounter.py"])
