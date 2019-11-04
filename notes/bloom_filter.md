---
title: "Bloom filter"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

* Data lookup
* Checking for membership
* Time vs space complexity

## Membership

* Use *HashSet*
* Fast: $O(1)$
* Huge: $O(n)$

## Bloom filter

Probabilistic data structure to determine if an item belongs to a set (collection)

## False positives vs false negatives

* False **positive**: an item **not in** a collection reported **present**
* False **negative**: an item **in** a collection reported as **absent**
* Bloom filter may report false **positive** but never false **negative**

## Spell checker

It is acceptable for an automated spell checker to miss a missspelled [sic] word but it should not mark valid words as misspelled.

## Bloom filter properties

* A fixed-size *bit vector*
  * filter size $m$ is a function of the dictionary size $n$ and the desired probability $p$ of false positives
  * $m=-\frac{n\ln{p}}{(\ln{2})^2}$
* $k$ hashing functions
  * if $k$ is low, too many false positives
  * if $k$ is high, the filter will become too slow
  * optimal $k$ is a function of $m$ and $n$
  * $k = \frac{m}{n}\ln{2}$

## Bloom filter implementation

* Uniformly distributed hashing functions
* Seed value
* Known modification of the input word

```python
from zlib import adler32


class BlomFilter:
    def __init__(self, size: int = 11, k: int = 3):
        self._k = k
        self._filter = [False] * size
```

## Bloom filter example

The standard Python `hash` function is non-deterministic, hence the use of `adler32`. For this example we append $0, 1, 2$ to the word for each hashing.

Small dictionary of three words: *cat*, *cow*, and *dog*.

* $m=11$
* $n=3$
* $k=\frac{11}{3}\ln{2}\approx3$

### Hashing

```python
    def _hash(self, word: str) -> tuple:
        return tuple((adler32(bytes(f"{word}{i}", "utf8")) % len(self._filter) for i in range(self._k)))
```

### Cat

`hash("cat") => (3, 2, 1)`

| 0   | 1     | 2     | 3     | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 0   | **1** | **1** | **1** | 0   | 0   | 0   | 0   | 0   | 0   | 0   |

### Cow

`hash("cow") => (1, 0, 10)`

| 0     | 1     | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10    |
| ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| **1** | **1** | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | **1** |

### Dog

`hash("dog") => (9, 8, 7)`

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7     | 8     | 9     | 10  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --- |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | **1** | **1** | **1** | 1   |

### False positive

`hash("squirrell") => (10, 9, 8)`

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8     | 9     | 10    |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | **1** | **1** | **1** |

## Blom filter (__contains__)

```python
    def __contains__(self, word):
        return all([self._filter[i] for i in self._hash(word)])
```

## Applications

* Spell checking
* DNA sequence analysis

## Summary

* Data lookup
* Checking for membership
* Time vs space complexity

## Thank you

Got questions?

## References

* [Data Structures and Algorithms with Python by Kent Lee and Steve Hubbard](https://dl.acm.org/citation.cfm?id=2732680)
* [Space/time trade-offs in hash coding with allowable errors](https://dl.acm.org/citation.cfm?doid=362686.362692)
* [Bloom70.pdf](http://www.dragonwins.com/domains/getteched/bbc/literature/Bloom70.pdf)
* [Bloom filter - Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
* [PyVideo.org · Handling ridiculous amounts of data with probabilistic data structures](https://pyvideo.org/pycon-us-2011/pycon-2011--handling-ridiculous-amounts-of-data-w.html)
  