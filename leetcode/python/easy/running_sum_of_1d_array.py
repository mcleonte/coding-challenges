"""
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
  """
  O(n) O(1)
  """
  for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
  return nums
