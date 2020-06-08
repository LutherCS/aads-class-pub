#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: project.partition
"""

import pathlib
import pytest
import toml
from src.exercises.partition import Partition, read_xml

TIME_LIMIT = 1


def get_cases(category: str):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield (case.get("filename"), case.get("expected"))


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename, expected", get_cases("test_case"))
def test_partition(filename, expected):
    """Testing the output"""
    vertices, edges = read_xml(filename)
    partition = Partition(len(vertices))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
    assert partition.forest == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_partition.py"])
