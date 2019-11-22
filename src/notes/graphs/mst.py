#!/usr/bin/env python3
# encoding: UTF-8
"""Kruskal's minimum spanning tree algorithms"""

from collections import namedtuple
from pythonds3.graphs import Graph


def kruskal(g: Graph):
    """Kruska's algorithm"""
    pass


def main():
    """This is the main function"""
    g = Graph()
    g.add_edge("A", "B", 7)
    g.add_edge("A", "D", 5)
    g.add_edge("B", "A", 7)
    g.add_edge("B", "C", 8)
    g.add_edge("B", "D", 9)
    g.add_edge("B", "E", 7)
    g.add_edge("C", "B", 8)
    g.add_edge("C", "E", 5)
    g.add_edge("D", "A", 5)
    g.add_edge("D", "B", 9)
    g.add_edge("D", "E", 15)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "B", 7)
    g.add_edge("E", "C", 5)
    g.add_edge("E", "D", 15)
    g.add_edge("E", "F", 8)
    g.add_edge("E", "G", 9)
    g.add_edge("F", "D", 6)
    g.add_edge("F", "E", 8)
    g.add_edge("F", "G", 11)
    g.add_edge("G", "E", 9)
    g.add_edge("G", "F", 11)

    min_span_tree = kruskal(g)
    min_span_tree_weight = 0
    print("Edges of the minimum spanning tree")
    for edge in min_span_tree:
        print(edge)
        min_span_tree_weight += edge.weight
    print(f"Total weight of the tree is {min_span_tree_weight}")


if __name__ == "__main__":
    main()
