"""
Tests for single_threaded_cpu
"""

from mcleonte.dsa.leetcode.python.medium.single_threaded_cpu import get_order


def test_1():
  arg = [[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]]
  assert get_order(arg) == [5, 0, 1, 3, 2, 4]


def test_2():
  arg = [[1, 2], [2, 4], [3, 2], [4, 1]]
  assert get_order(arg) == [0, 2, 3, 1]


def test_3():
  arg = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
  assert get_order(arg) == [4, 3, 2, 0, 1]
