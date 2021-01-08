---
title: "Splay tree"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

* Properties
* Rotation
* Splaying
* Performance

## Properties

* Invented in 1985 by Daniel Sleator and Robert Tarjan
* Has (amortized) $\Theta(\log{n})$ complexity for insertion, lookup, and removal
* Prioritizes recency of access (read or write)
* *Splay tree* maintains balance that is *good enough* without storing *balance* explicitly
* Relies on *spatial locality*
* Used to implement caching or garbage collectors

## Rotation

* *zig* (right)
* *zag* (left)
* *zig-zig* (right-right, left-left)
* *zig-zag* (right-left, left-right)

### Right-right

![Right-right](images/splayrightright.png)

### Left-left

![Left-left](images/splayleftleft.png)

### Right-left

![Right-left](images/splayrightleft.png)

### Left-right

![Left-right](images/splayleftright.png)

## Splaying

![Splay tree example](images/splaysample.png)

## Performance

![Splay tree vs AVL tree](images/splayvsavl.png)

## Summary

* Properties
* Rotation
* Splaying
* Performance

## Thank you

Got questions?

## References

* [Sleator, Daniel D.; Tarjan, Robert E. (1985). "Self-Adjusting Binary Search Trees" (PDF)](https://www.cs.cmu.edu/~sleator/papers/self-adjusting.pdf)
* [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
* [Splay tree - Wikipedia](https://en.wikipedia.org/wiki/Splay_tree)
