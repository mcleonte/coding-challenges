# https://leetcode.com/problems/determine-if-string-halves-are-alike/
# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/2867659/Python-or-O(n)-O(1)-or-Simplest-solution-with-a-single-counter-or-no-sum-substrings-or-double-counters
# O(n) O(1)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c, v = 0, {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i in range(len(s) // 2):
            if s[i] in v:
                c += 1
            if s[-i - 1] in v:
                c -= 1
        return c == 0
