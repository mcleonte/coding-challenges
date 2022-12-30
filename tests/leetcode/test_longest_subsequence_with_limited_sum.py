"""
Tests for longest_subsequence_with_limited_sum
"""

from mcleonte.dsa.leetcode.python.easy.longest_subsequence_with_limited_sum import answer_queries


def test_1():
  args = [
      [736411, 184882, 914641, 37925, 214915],
      [331244, 273144, 118983, 118252, 305688, 718089, 665450],
  ]
  assert answer_queries(*args) == [2, 2, 1, 1, 2, 3, 3]
