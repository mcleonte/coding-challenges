# https://leetcode.com/problems/sort-characters-by-frequency/
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/2871234/Python-or-O(nlogn)-O(n)-or-shortest-one-liner
# O(nlogn) O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(k * v for k, v in Counter(s).most_common())
