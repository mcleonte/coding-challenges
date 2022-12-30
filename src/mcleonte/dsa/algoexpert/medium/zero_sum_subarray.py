"""
You're given a list of integers nums. Write a function that returns a boolean
representing whether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray where all of the values add up to zero. A
subarray is any contiguous section of the array. For the purposes of this
problem, a subarray can be as small as one element and as long as the original
array.
"""

from typing import List


def zero_sum_subarray(nums: List[int]):
  """
  O(n) O(n)

  sum(nums[i:j]) == 0 <=> sum(nums[:i]) == sum(nums[:j])
  """
  sums, cusum = {0}, 0
  for num in nums:
    cusum += num
    if cusum in sums:
      return True
    sums.add(cusum)
  return False
