#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2021
@module: project.anomalycounter
"""

import pathlib
import pytest
import toml
from src.projects.anomalycounter import count


DATA_DIR = pathlib.Path("data/projects/anomalycounter/")
TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("data"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data, expected", get_cases("test_case"))
def test_anomalycounter(data, expected):
    """Testing the output"""
    assert count(DATA_DIR / pathlib.Path(data)) == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_anomalycounter.py"])
