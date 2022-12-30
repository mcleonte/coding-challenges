"""
Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of change, the
minimum sum of money, that you cannot create. The given coins can have any
positive integer value and aren't necessarily unique, i.e., you can have
multiple coins of the same value.

For example, if you're given coins = [1, 2, 5], the minimum amount of change
that you can't create is 4. If you're given no coins, the minimum amount of
change that you can't create is 1.
"""

from typing import List


def non_constructible_change(coins: List[int]):
  """
  O(nlogn) O(1)
  """
  coins.sort()  # O(nlogn)
  change = 0
  for coin in coins:
    if coin > change + 1:
      return change + 1
    change += coin
  return change + 1
