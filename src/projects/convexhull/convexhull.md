# Convex Hull

Idea: <https://open.kattis.com/problems/convexhull2>

Finding the convex hull of a set of points is an important problem that is often part of a larger problem and there are many algorithms for solving this task.

The task itself can be divided into two sub-tasks:

1. First, given a set of points, find a subset of those points that, when joined with line segments, form a convex polygon that encloses all of the original points.
2. Second, output the points of the convex hull in order, walking counter-clockwise around the polygon.

In this assignment, the first sub-task has already been done for you, and your program should complete the second sub-task with an additional third sub-task of measuring the length of the convex hull. That is, given the points that are known to lie on the convex hull, output them in order walking counter-clockwise around the hull.

The input files (found in *data/projects/convexhull/*) contains *all* the points in the following format: (x-coordinate, y-coordinate, letter). Letter "Y" indicates that the point *is* on the convex hull of all the points, and "N" indicates that it *is not*.

Function `get_convex` returns the list of points on the hull in counter-clockwise order around the hull, starting with the leftmost-lowest point (lowest x- and y- coordinates). If multiple points have the same x-coordinate, order them by y-coordinate.

Function `measure_convex` returns the length of the convex hull found by `get_convex`.
