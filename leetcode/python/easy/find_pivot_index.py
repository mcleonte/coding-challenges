# Solution complexity: O(n) O(1)
# Description: https://leetcode.com/problems/find-pivot-index/
# Thread: https://leetcode.com/problems/find-pivot-index/discuss/2815043/Python-or-O(n)-O(1)-or-very-clean
class Solution:

  def pivotIndex(self, nums: List[int]) -> int:
    lsum = 0
    rsum = sum(nums)
    for i, n in enumerate(nums):
      rsum -= n
      if lsum == rsum:
        return i
      lsum += n
    return -1
