"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/2946408/Python-or-O(n)-O(1)-greater99-or-easy-to-understand-with-good-formatting-and-state-naming

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/2940485/Daily-LeetCoding-Challenge-December-Day-23/1726630


You are given an array prices where prices[i] is the price of a given stock on
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times) with
the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown
one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must
sell the stock before you buy again).
"""

from typing import List


def max_profit(prices: List[int]) -> int:
  """
  O(n) O(1)
  """
  holding_on, holding_off, cooling_off = float('-inf'), 0, 0

  for price in prices:
    holding_on, holding_off, cooling_off = \
      max(
        holding_on,           # holding_on  --> wait --> holding_on
        holding_off - price,  # holding_off --> buy  --> holding_on
      ), \
      max(
        cooling_off,          # cooling_off --> wait --> holding_off
        holding_off,          # holding_off --> wait --> holding_off
      ), \
      holding_on + price      # holding_on  --> sell --> cooling_off

  return max(cooling_off, holding_off)
