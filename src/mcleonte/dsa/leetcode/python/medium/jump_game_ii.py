"""
https://leetcode.com/problems/jump-game-ii/

https://leetcode.com/problems/jump-game-ii/discuss/2960255/Python-or-O(n)-O(1)-or-greater99-with-for-loop

You are given a 0-indexed array of integers nums of length n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index
i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

  0 <= j <= nums[i] and
  i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are
generated such that you can reach nums[n - 1].
"""

from typing import List


def jump(nums: List[int]) -> int:
  """
  O(n) O(1)
  """
  if (target_i := len(nums) - 1) == 0:
    return 0
  jump_count = max_i = next_max_i = 0
  for i, max_jump in enumerate(nums):
    if next_max_i < i + max_jump:
      next_max_i = i + max_jump
    if i == max_i:
      jump_count += 1
      max_i = next_max_i
      if max_i >= target_i:
        return jump_count
