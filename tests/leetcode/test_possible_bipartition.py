"""
Tests for possible_bipartition
"""

from mcleonte.dsa.leetcode.python.medium.possible_bipartition import possible_bipartition


def test_1():
  assert possible_bipartition(5, [[1, 2], [3, 4], [4, 5], [3, 5]]) is False
