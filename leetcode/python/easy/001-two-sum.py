# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            if target - n in s:
                return [s[target - n], i]
            s[n] = i
