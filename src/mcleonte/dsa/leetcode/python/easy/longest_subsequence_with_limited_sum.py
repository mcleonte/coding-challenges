"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/

https://leetcode.com/problems/longest-subsequence-with-limited-sum/discuss/2950039/Python-or-O(nlogn-+-mlogn)-O(1)-greater99-or-short-in-place-solution

https://leetcode.com/problems/longest-subsequence-with-limited-sum/discuss/2947576/Daily-LeetCoding-Challenge-December-Day-25/1727989


You are given an integer array nums of length n, and an integer array queries of
length m.

Return an array answer of length m where answer[i] is the maximum size of a
subsequence that you can take from nums such that the sum of its elements is
less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""

from typing import List
from bisect import bisect


def answer_queries(nums: List[int], queries: List[int]) -> List[int]:
  """
  O(nlogn + mlogn) O(1)
  """
  nums.sort()
  for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
  for i in range(len(queries)):
    queries[i] = bisect(nums, queries[i])
  return queries
