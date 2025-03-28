# Valid Parentheses

This repository contains a Python implementation of the "Valid Parentheses" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


## Example
### Input:
s = "()"
### Output:
true
### Explanation
The ranges are:

[0,2] --> "0->2",

[4,5] --> "4->5",

[7,7] --> "7"


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/valid-parentheses/

# Note
This code includes some additional parts compared to the code I used on LeetCode.
I have two solutions here. While the first one works correctly, it encounters a time limit error on LeetCode. Therefore, I decided to optimize it, and the final result, which is accepted by LeetCode, is in the solution_2 file.





