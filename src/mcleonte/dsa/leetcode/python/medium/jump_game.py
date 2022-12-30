"""
https://leetcode.com/problems/jump-game/

https://leetcode.com/problems/jump-game/discuss/2955249/Python-or-O(n)-O(1)-or-short-intuitive-solution

https://leetcode.com/problems/jump-game/discuss/2951462/Daily-LeetCoding-Challenge-December-Day-26/1729518


You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
  """
  O(n) O(1)
  """
  max_pos = 0
  for curr_pos, max_jump in enumerate(nums):
    if max_pos < curr_pos:
      return False
    if max_pos < curr_pos + max_jump:
      max_pos = curr_pos + max_jump
  return True
