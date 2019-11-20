#!/usr/bin/env python3
# encoding: UTF-8
"""Graphs and graphing algorithms"""


import heapq
import sys
from sys import stdout


class Vertex:
    """Graph vertex"""

    def __init__(self, key):
        """Graph constructor"""
        # Vertex name
        self._key = key
        # Adjacent vertices
        self._neighbors = {}
        # Distance to the source
        self._distance = sys.maxsize
        # Predecessor
        self._previous = None
        # Color (for BFS)
        self._color = "white"
        # Discovery time (for DFS)
        self._discovered = 0
        # Closing time (for DFS)
        self._finalized = 0

    @property
    def key(self):
        """Get node key"""
        return self._key

    def get_neighbor(self, other: "Vertex"):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other: "Vertex", weight=0):
        """Add neighbor"""
        self._neighbors[other] = weight

    @property
    def neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.keys()

    @property
    def distance(self):
        """Get distance"""
        return self._distance

    @distance.setter
    def distance(self, new_value):
        """Set distance"""
        self._distance = new_value

    @property
    def previous(self):
        """Get previous"""
        return self._previous

    @previous.setter
    def previous(self, new_value):
        """Set previous"""
        self._previous = new_value

    @property
    def color(self):
        """Get color"""
        return self._color

    @color.setter
    def color(self, new_value):
        """Get color"""
        self._color = new_value

    @property
    def discovered(self):
        """Get discovery time"""
        return self._discovered

    @discovered.setter
    def discovered(self, new_value):
        """Set discovery time"""
        self._discovered = new_value

    @property
    def finalized(self):
        """Get finish time"""
        return self._finalized

    @finalized.setter
    def finalized(self, new_value):
        """Set finish time"""
        self._finalized = new_value

    def get_weight(self, other: "Vertex"):
        """Get edge weight"""
        return self._neighbors[other]

    def __repr__(self):
        """Return a vertex"""
        return f"Vertex({self._key})"

    def __str__(self):
        """Print a vertex"""
        return (
            "Neighbors of "
            + str(self._key)
            + ": "
            + str([x.key for x in self._neighbors])
        )

    def __lt__(self, other: "Vertex"):
        return self._key < other.key


class Graph:
    """Graph class"""

    def __init__(self):
        """Create a new, empty graph"""
        self._vertices = {}
        self._time = 0

    def add_vertex(self, key):
        """Add an instance of Vertex to the graph"""
        new_vertex = Vertex(key)
        self._vertices[key] = new_vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)
        self._vertices[from_vertex].neighbor = self._vertices[to_vertex], weight

    def get_vertex(self, key):
        """Find the vertex in the graph named vert_key"""
        return self._vertices.get(key, None)

    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        return self._vertices.keys()

    def reset_distances(self):
        """Reset distances to test Dijkstra's"""
        for v in self:
            v.distance = 255

    def __contains__(self, key):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        return key in self._vertices

    def __iter__(self):
        """Iterator"""
        return iter(self._vertices.values())

    def __len__(self):
        """Graph's size"""
        return len(self._vertices)

    def bfs(self, start):
        """Breadth First Search"""
        pass

    def dfs(self):
        """Depth First Search"""
        pass

    def dijkstra(self, start: Vertex) -> None:
        """Dijkstra's shortest path algorithm"""
        start.distance = 0
        known = [[start.distance, start]]
        visited = set()
        heapq.heapify(known)
        while known:
            current_vertex = heapq.heappop(known)[1]
            for next_vertex in current_vertex.neighbors:
                new_distance = current_vertex.distance + current_vertex.get_weight(
                    next_vertex
                )
                if new_distance < next_vertex.distance:
                    next_vertex.distance = new_distance
                    next_vertex.previous = current_vertex
                    found = False
                    for v in known:
                        if v[1].key == next_vertex.key:
                            v[0] = next_vertex.distance
                            heapq.heapify(known)
                            found = True
                    if not found:
                        heapq.heappush(known, [next_vertex.distance, next_vertex])


    def traverse(self, src, dst):
        """Traverse a graph"""
        pass

    def read_file(self, filename):
        """Read the graph from a file"""
        pass


def main():
    pass


if __name__ == "__main__":
    main()
