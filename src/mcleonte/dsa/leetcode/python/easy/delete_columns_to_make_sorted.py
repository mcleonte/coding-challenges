"""
https://leetcode.com/problems/delete-columns-to-make-sorted/

https://leetcode.com/problems/delete-columns-to-make-sorted/discuss/2994408/Python-or-O(nm)-O(1)-or-short-one-liner-with-zip(*)-and-itertools.pairwise

https://leetcode.com/problems/delete-columns-to-make-sorted/discuss/2989143/Daily-LeetCoding-Challenge-January-Day-3/1740321


You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.
For example, strs = ["abc", "bce", "cae"] can be arranged as:

  abc
  bce
  cae

You want to delete the columns that are not sorted lexicographically. In the
above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are
sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
"""

from typing import List
from itertools import pairwise


def min_deletion_size(strs: List[str]) -> int:
  """
  O(nm) O(1)
  """
  return sum(any(a > b for a, b in pairwise(col)) for col in zip(*strs))
