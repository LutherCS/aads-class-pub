---
title: "Graph"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

- ADT
- Implementation
- Algorithms
- Problems

## ADT

- _Graph_ is an abstract data type that implements the mathematical concept
- Set of vertices and edges
  - an edge may be directed or undirected
- Graphs are studied in discrete math and graph theory. The word _graph_ was first used in this sense by James Joseph Sylvester in 1878.

## Implementation

Graphs can be represented as either _adjacency matrix_ or _adjacency list_

### Factors to consider

- Size (vertices and edges) of the problem (graph)
- Density
  - matrix grows quadratically as number of vertices increases
  - list grows quadratically if the graph is dense
- Algorithms
  - DFS are easier to implement using a matrix
  - operation `__contains__` is easier to implement using a list
- Frequency of modification
  - Add/remove edge
  - Modify vertex attributes

### Python implementation

- `pythonds3.graphs`
- `networkx`

## Algorithms

- Bellman-Ford algorithm (1956)
- Kruskal’s algorithm (1956)
- Prim’s algorithm (1957)
- Dijkstra’s shortest path first algorithm (1959)
- Floyd-Warshall algorithm (1962)
- A\* search (1968)
- PageRank (1998)

## Problems

- Network flow problem
- Travelling salesman problem
- Minimum spanning tree

## Summary

- ADT
- Implementation
- Algorithms
- Problems

## Thank you

Got questions?

## References

- [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
- [Algorithm Repository](http://algorist.com/problems/Graph_Data_Structures.html)
- [Graph (abstract data type) - Wikipedia](<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>)
- [networkx/networkx: Official NetworkX source code repository.](https://github.com/networkx/networkx)
