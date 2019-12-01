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

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/exercises/partition/")
DATA_DIR = pathlib.Path("data/exercises/partition/")
FILE_PUBLIC = pathlib.Path("test_partition_public.toml")

if "tests" not in THIS_DIR.parts:
    FILE_PUBLIC = THIS_DIR / TEST_DIR / FILE_PUBLIC

all_test_cases = toml.load(FILE_PUBLIC)

TIME_LIMIT = 1
DATA = [
    (v.get("data"), v.get("expected"))
    for v in all_test_cases.get("case_public").get("success").values()
]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("data_file, expected", DATA)
def test_partition(data_file, expected):
    """Testing the output"""
    vertices, edges = read_xml(data_file)
    partition = Partition(len(vertices))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
    assert partition.forest == expected


if __name__ == "__main__":
    pytest.main(["-v", "test_partition.py"])
