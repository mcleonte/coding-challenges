"""
https://leetcode.com/problems/maximum-ice-cream-bars/

https://leetcode.com/problems/maximum-ice-cream-bars/discuss/3009169/Python-or-O(nlogn)-O(1)-or-in-place-one-liner-with-early-exit

https://leetcode.com/problems/maximum-ice-cream-bars/discuss/3005081/Daily-LeetCoding-Challenge-January-Day-6/1744969


It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length
n, where costs[i] is the price of the ith ice cream bar in coins. The boy
initially has coins coins to spend, and he wants to buy as many ice cream bars
as possible.

Return the maximum number of ice cream bars the boy can buy with coins coins.
"""

from typing import List


def max_ice_cream(costs: List[int], coins: int) -> int:
  """
  O(nlogn) O(1) | early exit
  """
  costs.sort()
  for c, cost in enumerate(costs):
    if cost > coins:
      return c
    coins -= cost
  return len(costs)


def max_ice_cream_2(costs: List[int], coins: int) -> int:
  """
  O(nlogn) O(1) | early exit | one-liner
  """
  return next((c for c, cost in enumerate(costs.sort() or costs)
               if (coins := coins - cost) < 0), len(costs))
