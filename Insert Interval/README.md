# Insert Interval

This repository contains a Python implementation of the "Insert Interval" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

## Example
### Input:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
### Output:
[[1,2],[3,10],[12,16]]
### Explanation:
Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/insert-interval/

# Note
This code includes some additional parts compared to the code I used on LeetCode.





