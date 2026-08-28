# LeetCode 34 - Find First and Last Position of Element in Sorted Array

## Problem

Given a sorted array and a target value, find the first and last position of that target.

If the target is not present, return `[-1, -1]`.

## Example

Input:

```text
nums = [5,7,7,8,8,10]
target = 8
```

Output:

```text
[3,4]
```

## Approach

I use binary search to find the first occurrence and the last occurrence of the target separately.

This makes the solution faster than checking every element one by one.

## Complexity

* Time Complexity: `O(log n)`
* Space Complexity: `O(1)`

## Topics

* Array
* Binary Search

## Language

Python

## Author

T.Nandhini
