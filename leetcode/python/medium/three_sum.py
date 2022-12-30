# https://leetcode.com/problems/3sum/
class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    out = {}
    for i, n in enumerate(nums):
      target = -n
      s = {}
      for j, m in enumerate(nums[i + 1:]):
        if target - m in s:
          f = frozenset({n, m, target - m})
          if f not in out:
            out[f] = [n, m, target - m]
        s[m] = j
    return out.values()
