# https://leetcode.com/problems/minimum-average-difference/
# https://leetcode.com/problems/minimum-average-difference/discuss/2874745/Python-or-O(n)-O(1)-or-Simple-7-line-solution
# https://leetcode.com/problems/minimum-average-difference/discuss/2874587/Daily-LeetCoding-Challenge-December-Day-4/1704592
# O(n) O(1)
class Solution:

  def minimumAverageDifference(self, nums: List[int]) -> int:
    l, r, n, md, mi = 0, sum(nums), len(nums), float("inf"), None
    for i, x in enumerate(nums):
      l, r = l + x, r - x
      d = abs((l // (i + 1)) - ((r // (n - i - 1)) if r else 0))
      if d < md:
        mi, md = i, d
    return mi
