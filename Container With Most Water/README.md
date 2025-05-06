# Container With Most Water

This repository contains a Python implementation of the "Container With Most Water" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


## Example 1
### Input:
height = [1,8,6,2,5,4,8,3,7]
### Output:
49
### Explanation:
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/container-with-most-water/

# Note
This code includes some additional parts compared to the code I used on LeetCode.
I have three solutions here. While the first and second one works correctly, they encounters a time limit error on LeetCode. Therefore, I decided to optimize it, and the final result, which is accepted by LeetCode, is in the solution-3 file.






