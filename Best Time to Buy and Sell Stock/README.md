# Best Time to Buy and Sell Stock

This repository contains a Python implementation of the "Best Time to Buy and Sell Stock" problem, commonly encountered in coding interviews and programming challenges.

## Problem Description

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


## Example 1
### Input:
prices = [7,1,5,3,6,4]
### Output:
5
### Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

## Example 2
### Input:
prices = [7,6,4,3,1]
### Output:
0
### Explanation:
In this case, no transactions are done and the max profit = 0.


# Link to Problem
You can view the original problem on LeetCode here: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Note
This code includes some additional parts compared to the code I used on LeetCode.
I have two solutions here. While the first one works correctly, it encounters a time limit error on LeetCode. Therefore, I decided to optimize it, and the final result, which is accepted by LeetCode, is in the solution-2 file.






