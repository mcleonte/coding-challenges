"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


Given two non-negative integers low and high. Return the count of odd numbers
between low and high (inclusive).
"""


def count_odds(low: int, high: int) -> int:
  """
  O(1) O(1)
  """
  return (high + 1) // 2 - low // 2
