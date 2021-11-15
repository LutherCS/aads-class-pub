---
title: "Convex hull"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

- Convex hull
- Gift wrapping
- Graham scan

## Convex hull

- The smallest convex set of points that contains a shape.
- One of the fundamental problems of computational geometry.
- Usually $n$ is the number of points and $h$ is the number of _extreme_ points.
- Can be solved in $O(n\log{n})$ time for 2-dimensional space.
- Output-sensitive complexity of $O(n\log{h})$.

## Algorithms

- Gift wrapping (1970-73) with the complexity of $O(nh)$ and $\Theta(n^2)$ in the worst case.
- Graham scan (1972) with the complexity of $O(n\log{n})$ and $O(n)$ if points are sorted.
- Quickhull (1977-78) with the complexity of $O(n\log{n})$ and $O(n^2)$ in the worst case.
- Kirkpatrick–Seidel algorithm (1986) is an _optimal_ output-sensitive algorithm with the complexity of $O(n\log{h})$.
- Chan's algorithm (1996) is a simpler optimal algorithm with the complexity of $O(n\log{h})$.

### Gift wrapping

1. Pick some point $p_0$ on the hull. Leftmost-lowest point is guaranteed to be on the hull. Set $i$ to 0, so $i+1$ is 1.
2. Find a point $p_{i+1}$ so that all other points are on the right of the line $p_{i}p_{i+1}$ (initially, $p_0p_1$).
   - compare _polar angles_ of all points with respect to $p_i$
3. Add $p_{i+1}$ to the hull and set $i$ to $i+1$
4. Repeat steps 2-3 until some step $h$ selects $p_0$ as $p_h$.

### Graham scan

1. Find the lowest-leftmost point ($p_0$) in the set ($O(n)$ operation). It is guaranteed to be on the hull.
2. Sort the points in the set by the angle between $p_0p_i$ and the X axis ($O(n\log{n})$ operation).
3. Starting with $p_0$ and $p_1$, continue through the sorted list and for each point $p_{i+2}$ determine if getting from $p_ip_{i+1}$ to $p_{i+2}$ requires a _left_ or a _right_ turn.
   - in case of a right turn, remove $p_{i+1}$ from the hull and look at points $p_{i-1}p_{i}$ until left turn is found.

### Left turn vs right turn

Calculate z-coordinate of the cross product of two vectors, two vectors $\overrightarrow {P_{1}P_{2}}$ and $\overrightarrow {P_{1}P_{3}}$ as follows:

$$z = (x_{2}-x_{1})(y_{3}-y_{1})-(y_{2}-y_{1})(x_{3}-x_{1})$$

- If the result is 0, the points are collinear
- If it is positive, the three points constitute a "left turn" or counter-clockwise orientation
- otherwise a "right turn" or clockwise orientation

## Summary

- Convex hull
- Gift wrapping
- Graham scan

## Thank you

Got questions?

## References

- [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
- [Convex hull - Wikipedia](https://en.wikipedia.org/wiki/Convex_hull)
- [Convex hull algorithms - Wikipedia](https://en.wikipedia.org/wiki/Convex_hull_algorithms)
