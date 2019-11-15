#!/usr/bin/env python3
# encoding: UTF-8
"""Graphs and graphing algorithms demo"""


# from notes_graphs import *
import Graph as graph
from sys import stdout
import random


def main():
    """Main function"""
    print("Testing Graphs")
    g = graph.Graph()
    for i in range(6):
        g.add_vertex(i)
    print("Graph vertices")
    print(g.vertices)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    print("Graph vertices")
    print(g.vertices)

    print("\nGraph vertices roll call")
    for i in range(6):
        if i in g:
            print("Vertex {} is in the graph".format(i))

    print("\nGraph edges")
    # Using the iterator
    for v in g:
        for w in v.get_neighbors():
            print("({} - {} : {})".format(v.get_key(), w.get_key(), v.get_weight(w)))


    print("\nNetwork graph demo")
    net_graph = graph.Graph()
    net_graph.read_file("src/notes/graphs/graph_1.txt")
    net_graph.reset_distances()
    start_vertex = "x"
    net_graph.dijkstra(net_graph.get_vertex(start_vertex), 1)
    print("All paths")
    for v in net_graph.get_vertices() - {start_vertex}:
        net_graph.traverse(start_vertex, v)


if __name__ == "__main__":
    main()
