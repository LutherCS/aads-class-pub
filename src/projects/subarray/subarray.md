# Maximum subarray problem

## Description

The maximum sum subarray problem is the task of finding a contiguous subarray with the largest sum within a given one-dimensional array $A[1...n]$. Formally, the task is to find indices $i$ and $j$ with $1 \leq i \leq j \leq n$, such that the sum

$\sum _{x=i}^{j}A[x]$

is as large as possible. Each number in the input array $A$ could be positive, negative, or zero. Sum of an empty array is zero.

For example, for the array of values [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous subarray with the largest sum is [4, -1, 2, 1], with sum 6.

## Task

Your task in this project is to implement Kadane's algorithm to solve the max subarray problem and verify your solution by passing the provided unit tests.

## References

* [Maximum subarray problem - Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
* [Kadane's algorithm - Algorithmist](https://algorithmist.com/wiki/Kadane%27s_algorithm)
