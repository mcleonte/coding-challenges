"""
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/discuss/2960034/Python-or-O(nlogn)-O(1)-or-greater99-short-in-place-solution

https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/discuss/2955466/Daily-LeetCoding-Challenge-December-Day-27/1730738


You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer
arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks
and currently contains rocks[i] rocks. You are also given an integer
additionalRocks, the number of additional rocks you can place in any of the
bags.

Return the maximum number of bags that could have full capacity after placing
the additional rocks in some bags.
"""

from typing import List


def maximum_bags(
    capacity: List[int],
    rocks: List[int],
    additional_rocks: int,
) -> int:
  """
  O(nlogn) O(1)
  """
  for i in range(len(capacity)):
    capacity[i] -= rocks[i]
  capacity.sort()
  for i, bag_capacity in enumerate(capacity):
    if additional_rocks < bag_capacity:
      return i
    additional_rocks -= bag_capacity
  return i + 1
