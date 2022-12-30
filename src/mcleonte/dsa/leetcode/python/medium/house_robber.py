"""
https://leetcode.com/problems/house-robber/

https://leetcode.com/problems/house-robber/discuss/2909163/Python-or-O(n)-O(1)-greater99-or-2-DP-equivalent-solutions-with-and-without-in-place

https://leetcode.com/problems/house-robber/discuss/2909087/Daily-LeetCoding-Challenge-December-Day-14/1715706

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.
"""

from typing import List


def rob(nums: List[int]) -> int:
  """
  O(n) O(1) | without modifying the input
  """
  prev = curr = 0
  for num in nums:
    prev, curr = curr, max(curr, prev + num)
  return curr


def rob_2(nums: List[int]) -> int:
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
