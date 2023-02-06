"""
https://leetcode.com/problems/shuffle-the-array/

Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
  """
  O(n) O(n)
  """
  out = [None] * (2 * n)
  for i in range(n):
    out[2 * i] = nums[i]
    out[2 * i + 1] = nums[i + n]
  return out
