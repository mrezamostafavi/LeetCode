# Summary Ranges

This repository contains a Python implementation of the "Summary Ranges" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


## Example
### Input:
nums = [0,1,2,4,5,7]
### Output:
["0->2","4->5","7"]
### Explanation
The ranges are:

[0,2] --> "0->2",

[4,5] --> "4->5",

[7,7] --> "7"


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/summary-ranges/

# Note
This code includes some additional parts compared to the code I used on LeetCode.





