---
title: "Shortest Paths Algorithms"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

- Dijkstra’s shortest path first algorithm (1959)
- Bellman-Ford algorithm (1956)
- Floyd-Warshall algorithm (1962)
- A\* search (1968)

## Dijkstra’s shortest path first algorithm (1959)

Did it three times already.

## Bellman-Ford algorithm (1956)

- Slower than Dijkstra's, but more versatile
- Will cover later
- Probably, next year
- Please come back

## Floyd-Warshall algorithm (1962)

_Dynamic programming_ algorithm for finding the shortest paths between all pairs of vertices in a weighted graph with no negative cycles with $\Theta (|V|^{3})$ performance

### History

- Invented by Robert Floyd in 1962
- And by Stephen Warshall in 1962
- And by Bernard Roy in 1959
- Similar to Stephen Kleene's NFA to RE conversion algorithm from 1956
- Implementation by Peter Ingerman in 1962

### Algorithm

If the shortest path between vertices $i$ and $j$ exists, it either:

- goes through a vertex $k$ ($i \rightarrow k \rightarrow j$ via vertices in $\{1,...k-1\}$)
- does not go through a vertex $k$ (so, only using vertices in $\{1,...k-1\}$

$sp(i, j, 0) = w(i, j)$

$sp(i, j, k) = min(sp(i, j, k-1), sp(i, k, k-1) + sp(k, j, k-1))$

### Implementation. Initialization

```python
dist = {}
g = Graph()
n = len(g.vertices)
g.reset()  # set min distances to sys.maxsize
for edge in g.edges:
    dist[(edge.src, edge.dst)] = edge.weight
for vertex in g.vertices:
    dist((vertex, vertex)) = 0
```

### Implementation. Triple loop

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
```

### Comparison to repeated Dijkstra's

- Floyd-Warshall's performs better in dense graphs (large number of edges)
- Dijkstra's is $O(|E||V|+|V|^2\log{|V|})$
- Floyd-Warshall's is $O(|V|^3)$

## A\* search (1968)

- Graph traversal and path search algorithm
- Complete, optimal, and efficient
- Invented by Peter Hart, Nils Nilsson, and Bertram Raphael in 1968
- Uses heuristics to improve on Dijkstra's

## Summary

- Dijkstra’s shortest path first algorithm (1959)
- Bellman-Ford algorithm (1956)
- Floyd-Warshall algorithm (1962)
- A\* search (1968)

## Thank you

Got questions?

## References

- [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
- [Floyd–Warshall algorithm - Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
