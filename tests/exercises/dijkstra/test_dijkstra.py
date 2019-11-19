#!/usr/bin/env python3
# encoding: UTF-8
"""
@author: Roman Yasinovskyy
@date: 2019
@module: exercises.dijkstra
"""

import pytest
from src.exercises.dijkstra import read_toml, find_path

TIME_LIMIT = 1

NETWORK = [("t", 4), ("u", 3), ("v", 0), ("w", 4), ("x", 3), ("y", 8), ("z", 11)]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("vertex, distance", NETWORK)
def test_dijkstra(vertex, distance):
    """Testing the output"""
    g = read_toml("data/exercises/dijkstra/network.toml")
    find_path(g, "v")
    assert g.get_vertex(vertex).distance == distance


if __name__ == "__main__":
    pytest.main(["test_dijkstra.py"])
