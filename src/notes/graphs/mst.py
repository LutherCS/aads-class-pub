#!/usr/bin/env python3
# encoding: UTF-8
"""Kruskal's minimum spanning tree algorithms"""

from collections import namedtuple
from pythonds3.graphs import Graph


def kruskal(g: Graph):
    """Kruskal's algorithm"""
    Edge = namedtuple("Edge", ["src", "dst", "weight"])
    vertices = [set(v) for v in g.get_vertices()]

    edges = [Edge(e[0][0], e[0][1], e[1]) for e in g._edges.items()]
    edges.sort(key=lambda edge: edge.weight, reverse=True)

    min_span_tree = set()
    min_span_tree_size = len(vertices) - 1

    while len(min_span_tree) < min_span_tree_size:
        candidate = edges.pop()
        for v_set in vertices:
            if candidate.src in v_set:
                src_set = v_set
                break
        # else:
        #     src_set = set()
        for v_set in vertices:
            if candidate.dst in v_set:
                dst_set = v_set
                break
        # else:
        #     dst_set = set()
        if src_set != dst_set:
            min_span_tree.add(candidate)
            src_set.update(dst_set)
            vertices.remove(dst_set)
            yield candidate
        # return min_span_tree


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
