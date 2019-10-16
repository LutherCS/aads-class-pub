---
title: "Knapsack"
keywords: ["algorithms", "data structures", "programming"]
---

## Goals

* Problem description
* Algorithm
* Applications

## Problem description

Resource allocation with constrain.

*NP-complete* problem, so the fast and correct solution is unknown.

### Formal definition

Given a knapsack of *capacity* $C$ and a set of items $S=\{{1,...,n}\}$, where item $i$ has *weight* (size, price) $w_i$ and *value* $v_i$, find the subset $S'\subset{S}$ that maximizes the total value $\sum_{i\in{S'}}{v_i}$ with the constrain that $\sum_{i\in{S'}}{w_i} < C$.

### Informal definition

* Maximize the amount of loot you carry in your bag.
* Making a purchase on limited budget.

### 0/1 knapsack

Either take an item or don't

Maximize $\sum_{i=1}^{n}v_ix_i$ while keeping $\sum_{i=1}^{n}w_ix_i \le C$, where $x_i\in\{{0,1}\}$

### Bounded knapsack

Can take up to $c$ copies of each item

Maximize $\sum_{i=1}^{n}v_ix_i$ while keeping $\sum_{i=1}^{n}w_ix_i \le C$, where $x_i\in\{{0,...,c}\}$

### Unbounded knapsack

Can take as many copies of each item as possible

Maximize $\sum_{i=1}^{n}v_ix_i$ while keeping $\sum_{i=1}^{n}w_ix_i \le C$, where $0 \le x_i$

## Algorithm

Assuming $w_1, w_2, ..., C$ are positive integers, define $m[i,w]$ as the maximum value that can be achieved with weight less than or equal to $w$ using the first $i$ items.

* $m[0, w] = 0$
* $m[i, w] = m[i - 1, w]$ if $w_i>w$
* $m[i, w] = max(m[i - 1, w], m[i - 1, w - w_i] + v_i)$ if $w_i\le w$

Solve the *knapsack* problem by finding $m[n, C]$.

### Example

$C=6.1$, $i(v, w)=\{{(5, 4), (4, 3), (3, 2), (2, 1)}\}$

| i \\ j | 0   | 1   | 2   | 3     | 4   | 5     | 6     |
| ----- | --- | --- | --- | ----- | --- | ----- | ----- |
| 0     | 0   | 0   | 0   | 0     | 0   | 0     | 0     |
| 1     | 0   | 0   | 0   | 0     | 5   | 5     | 5     |
| 2     | 0   | 0   | 0   | **4** | 5   | 5     | 5     |
| 3     | 0   | 0   | 3   | 4     | 5   | **7** | 8     |
| 4     | 0   | 2   | 3   | 5     | 6   | 7     | **9** |

Table 1. Matrix $m$

### Item selection

Initialize $j$ to $C$ and subtract weight of each *selected* item from it. Starting with the last item ($i=n$) and continuing while there is room in the knapsack ($j>0$), only add items where the following is true.

* $v_i > 0$, and
* $m[i,j] = m[i-1,j-w_i]+v_i$

### Example 2

$C=15$, $i(v, w)=\{{(2, 2), (1, 1), (10, 4), (2, 1), (4, 12)}\}$

![Wikipedia knapsack](images/knapsack.svg)

### Example 2 solution

| i \\ j | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 1     | 0   | 0   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   |
| 2     | 0   | 1   | 2   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   |
| 3     | 0   | 1   | 2   | 3   | 10  | 11  | 12  | 13  | 13  | 13  | 13  | 13  | 13  | 13  | 13  | 13  |
| 4     | 0   | 2   | 3   | 4   | 10  | 12  | 13  | 14  | 15  | 15  | 15  | 15  | 15  | 15  | 15  | 15  |
| 5     | 0   | 2   | 3   | 4   | 10  | 12  | 13  | 14  | 15  | 15  | 15  | 15  | 15  | 15  | 15  | 15  |

```text
Items [(2, 2), (1, 1), (10, 4), (2, 1)] sum up to 15
```

### Example 2 update

* Let's add item (5, 10) to our options.
* How will it change the selection?
* Items [(10, 4), (2, 1), (5, 10)] sum up to 17

## Applications

* Combinatorics
* Cryptography
* Finance

### xkcd

![NP-Complete](images/xkcd_np_complete.png)

::: notes

General solutions get you a 50% tip.

:::

## Summary

* Problem description
* Algorithm
* Applications

## Thank you

Got questions?

## References

* [Algorithm Repository: Knapsack Problem](http://algorist.com/problems/Knapsack_Problem.html)
* [Knapsack problem - Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
* [xkcd: NP-Complete](https://xkcd.com/287/)
