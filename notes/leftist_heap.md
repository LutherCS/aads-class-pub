---
title: "Leftist heap"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

- Leftist heap definition
- Leftist heap implementation
- Insertion
- Removal
- Merging

## Leftist heap ADT

### Leftist

![Karl Marx and Friedrich Engels](images/kmfe.jpg)

### Leftist heap (tree)

![Leftist tree](images/leftist_heap.png)

### Leftist tree properties

- Invented in 1972 by Clark Crane
- Binary tree with left subtree _usually_ taller than the right one
- Merging of two heaps is $O(log(n))$ (improvement over _binary heap_'s $O(n)$)
- Every node keeps track of the _s-value_ (null path length)
- The shortest path to an external node is always on the right

## Leftist tree definition

1. Either $T=\emptyset$; or
2. $T={R,T_L,T_R}$, where $T_L$ and $T_R$ are leftist trees which have _s-value_ $d_L$ and $d_R$, such that $d_L \ge d_R$

## Leftist heap vs leftist tree

Leftist heap is a heap-ordered leftist tree

Rule #2 may be violated after the insertion, that is _s-value_ of the right subtree of a certain node may become larger than the _s-value_ of the left subtree

In that case, _swap left and right subtrees of the node_.

## Implementation

Implemented with links (pointers), based on `BinaryTree`

### Class BinaryTree

```python
class BinaryTree:
    """Binary tree class"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None
```

### Class LeftistHeap

```python
class LeftistHeap(BinaryTree):
    """Leftist tree class"""

    def __init__(self):
        super().__init__(None)
        self._svalue = 0
```

## Insertion

In order to insert an element `e` into leftist heap `h`, create a new leftist heap of one element (`e`) and merge it into `h1`

## Removal

In order to remove an element from the leftist heap `h`, remove its root and merge left and right subtrees into a new leftist heap.

## Merging leftist heaps

Merging heaps `h1` and `h2` keeps `h1` _leftist_ and `h2` empty

1. If `h1` is empty, swap `h1` and `h2`
2. Assume the _root_ of `h2` is greater than _root_ of `h1`
3. Recursively merge `h2` with the _right_ subtree of `h1`
4. Swap left and right subtrees if _s-value_ constrain is violated
5. If the _root_ of `h2` is smaller than the _root_ of `h1`, swap and proceed

$O(log(n))$ operation

### Merging example start

![Two leftist heaps](images/HBLT_1.jpg)

### Merging example result

![Two leftist heaps](images/HBLT_9.jpg)

## Summary

- Leftist heap definition
- Leftist heap implementation
- Insertion
- Removal
- Merging

## Thank you

Got questions?

## References

- [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
- [Leftist tree - Wikipedia](https://en.wikipedia.org/wiki/Leftist_tree)
- [Weight-biased leftist trees and modified skip lists](https://www.cise.ufl.edu/~sahni/papers/wblt.pdf)
