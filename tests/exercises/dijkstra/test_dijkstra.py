#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: exercises.dijkstra
"""

import pathlib
import pytest
from src.exercises.dijkstra import read_toml, find_path

THIS_DIR = pathlib.Path(".")
TEST_DIR = pathlib.Path("tests/exercisesw/dijkstra/")
DATA_DIR = pathlib.Path("data/exercises/dijkstra/")

TIME_LIMIT = 1


@pytest.mark.timeout(TIME_LIMIT)
def test_dijkstra():
    """Testing the output"""
    g = read_toml("data/exercises/dijkstra/network.toml")
    find_path(g, "v")


if __name__ == "__main__":
    pytest.main(["test_dijkstra.py"])
