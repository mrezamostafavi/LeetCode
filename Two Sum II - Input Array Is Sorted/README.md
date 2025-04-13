# Two Sum II - Input Array Is Sorted

This repository contains a Python implementation of the "Two Sum II - Input Array Is Sorted" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


## Example 1
### Input:
numbers = [2,7,11,15], target = 9
### Output:
[1,2]
### Explanation:
The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Note
This code includes some additional parts compared to the code I used on LeetCode.
I have two solutions here. While the first one works correctly, it encounters a time limit error on LeetCode. Therefore, I decided to optimize it, and the final result, which is accepted by LeetCode, is in the solution-2 file.






