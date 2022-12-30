"""
You are given an integer array prices where prices[i] is the price of a given
stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at
most one share of the stock at any time. However, you can buy it then
immediately sell it on the same day,

Find and return the maximum profit you can achieve.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
  """
  O(n) O(1)
  """
  return sum(b - a for a, b in zip(prices, prices[1:]) if a < b)
