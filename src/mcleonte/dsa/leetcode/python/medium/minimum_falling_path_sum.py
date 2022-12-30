"""
https://leetcode.com/problems/minimum-falling-path-sum/

https://leetcode.com/problems/minimum-falling-path-sum/discuss/2909036/Python-or-O(n)-O(1)-greater98-or-tweaked-shortest-solution-to-minimize-computation

https://leetcode.com/problems/minimum-falling-path-sum/discuss/2905656/Daily-LeetCoding-Challenge-December-Day-13/1715675

Given an n x n array of integers mxrix, return the minimum sum of any falling
path through mxrix.

A falling path starts at any element in the first row and chooses the element in
the next row that is either directly below or diagonally left/right.
"""

from typing import List


def min_falling_path_sum(mx: List[List[int]]) -> int:
  """
  O(n) O(1)

  Best to treat the first and last column separately
  and to index each element individually to address
  the overhead mentioned in the second example below.
  """
  for i in range(len(mx) - 1):
    mx[i + 1][0] += min(mx[i][0], mx[i][1])
    mx[i + 1][-1] += min(mx[i][-1], mx[i][-2])
    for j in range(1, len(mx) - 1):
      mx[i + 1][j] += min(mx[i][j - 1], mx[i][j], mx[i][j + 1])
  return min(mx[-1])


def min_falling_path_sum_2(mx: List[List[int]]) -> int:
  """
  O(n) O(1)

  Suboptimal due to usage of max(0,j-1) for every i,j pair, and
  due to slicing mx[..:..], which creates intermediary lists.
  """
  for i in range(len(mx) - 1):
    for j in range(len(mx)):
      mx[i + 1][j] += min(mx[i][max(0, j - 1):j + 2])
  return min(mx[-1])
