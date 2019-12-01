#!/usr/bin/env python
"""Implementation of the Partition data structure"""

from xml.dom import minidom
from collections import namedtuple

Vertex = namedtuple("Vertex", ["id", "x", "y", "key"])
Edge = namedtuple("Edge", ["src", "dst", "weight"])


class Partition:
    def __init__(self, size):
        self._forest = [x for x in range(size)]

    @property
    def forest(self):
        """Return the forest"""
        return self._forest

    def add(self, e: Edge):
        """
        Add an edge to the partition

        Find the root of the source vertex tree
        Find the root of the destination vertex tree
        If they are different, set root of the destination vertex tree to the root of the source vertex tree
        """
        raise NotImplementedError

    def _find_root(self, node: int) -> int:
        """
        Find root of a node

        The root of a tree is a node that has its value matching the index in the forest
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Stringify the forest"""
        return str(self._forest)

    def __iter__(self):
        """Iterate over the forest"""
        return iter(self._forest)


def read_xml(filename: str) -> tuple:
    """Read XML representation of the graph"""
    vertices = {}  # {int: Vertex}
    edges = []  # [Edge]

    xml_doc = minidom.parse(filename)
    xml_graph = xml_doc.getElementsByTagName("Graph")[0]
    xml_vertices = xml_graph.getElementsByTagName("Vertices")[0].getElementsByTagName(
        "Vertex"
    )
    xml_edges = xml_graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")

    # TODO: Add all vertices from the XML file to the dictionary of vertices

    # TODO: Add all edges from the XML file to the list of edges

    return vertices, edges


def main():
    """Main function"""
    vertices, edges = read_xml("data/exercises/partition/neia.xml")
    partition = Partition(len(vertices))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
        print(", ".join([f"{x:2}" for x in partition]))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    print(partition.forest)


if __name__ == "__main__":
    main()
