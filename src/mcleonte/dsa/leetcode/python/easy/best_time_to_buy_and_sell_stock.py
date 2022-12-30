"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/2943861/Python-or-O(n)-O(1)-or-simple-and-most-efficient-with-for-..-if-..-elif


You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
  """
  O(n) O(1)
  """
  lowest = highest = prices[0]
  profit = 0
  for price in prices:
    if price > highest:
      highest = price
    elif price < lowest:
      profit = max(profit, highest - lowest)
      lowest = highest = price
  return max(profit, highest - lowest)
