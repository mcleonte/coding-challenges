# https://leetcode.com/problems/sort-characters-by-frequency/
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/2871158/daily-leetcoding-challenge-december-day-3/1703882
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/2871158/Daily-LeetCoding-Challenge-December-Day-3/1703524
# O(n) O(n)
class Solution:

  def frequencySort(self, s: str) -> str:
    return "".join(k * v for k, v in Counter(s).most_common())
