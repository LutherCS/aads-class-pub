"""Graphs and graphing algorithms"""
#!/usr/bin/env python3
# encoding: UTF-8


import heapq
import sys
from sys import stdout
import time
import colorama


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

    @property
    def neighbor(self, other):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    @neighbor.setter
    def neighbor(self, other, weight=0):
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
    def distance(self, distance):
        """Set distance"""
        self._distance = distance

    @property
    def previous(self):
        """Get previous"""
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Set previous"""
        self._previous = previous

    @property
    def color(self):
        """Get color"""
        return self._color

    @color.setter
    def color(self, color):
        """Get color"""
        self._color = color

    @property
    def discovered(self):
        """Get discovery time"""
        return self._discovered

    @discovered.setter
    def discovered(self, t):
        """Set discovery time"""
        self._discovered = t

    @property
    def finilized(self):
        """Get finish time"""
        return self._finalized

    @finilized.setter
    def set_finish(self, t):
        """Set finish time"""
        self._finalized = t

    @property
    def edge(self, other):
        """Get edge weight"""
        return self._neighbors[other]

    def __repr__(self):
        """Return a vertex"""
        return (
            "Neighbors of "
            + str(self._key)
            + ": "
            + str([x.key for x in self._neighbors])
        )

    def __str__(self):
        """Print a vertex"""
        return (
            "Neighbors of "
            + str(self.key)
            + ": "
            + str([x.key for x in self.neighbors])
        )

    def __lt__(self, other):
        return self.key < other.key


class Graph:
    """Graph class"""

    def __init__(self):
        """Create a new, empty graph"""
        pass

    def add_vertex(self, key):
        """Add an instance of Vertex to the graph"""
        pass

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        pass

    def get_vertex(self, key):
        """Find the vertex in the graph named vert_key"""
        pass

    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        pass

    def reset_distances(self):
        """Reset distances to test Dijkstra's"""
        pass

    def __contains__(self, key):
        """Return True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise"""
        pass

    def __iter__(self):
        """Iterator"""
        pass

    def __len__(self):
        """Graph's size"""
        return len(self.vertices)

    def bfs(self, start):
        """Breadth First Search"""
        pass

    def dfs(self):
        pass

    def dfs_visit(self, start):
        pass

    def dijkstra(self, start, debug=False):
        """Dijkstra's shortest path algorithm"""
        pass

    def traverse(self, src, dst):
        """Traverse a graph"""
        pass

    def read_txt_file(self, filename):
        """Read the graph from a file"""
        with open(filename, "r") as f:
            for raw_line in f:
                line = raw_line.split()
                if len(line) == 1:
                    src = line[0]
                elif len(line) == 2:
                    self.add_edge(src, line[0], int(line[1]))
