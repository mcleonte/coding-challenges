"""
Write a function that takes in an array of positive integers and returns the
maximum sum of non-adjacent elements in the array.

If the input array is empty,
the function should return 0.
"""

from typing import List


def max_subset_sum_no_adjacent(nums: List[int]) -> int:
  """
  O(n) O(1) | without modifying the input
  """
  prev = curr = 0
  for num in nums:
    prev, curr = curr, max(curr, prev + num)
  return curr


def max_subset_sum_no_adjacent_2(nums: List[int]) -> int:
  """
  O(n) O(1) | in place equivalent
  no real point if O(1) is possible also
  without modifying the input, but this
  version could be easier to understand
  """
  if len(nums) < 3: return max(nums)
  nums[1] = max(nums[0], nums[1])
  for i in range(2, len(nums)):
    nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
  return nums[-1]
