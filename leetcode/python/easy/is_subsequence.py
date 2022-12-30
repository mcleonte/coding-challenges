# Solution complexity: O(n) O(1)
# Description: https://leetcode.com/problems/is-subsequence/
# Thread: https://leetcode.com/problems/is-subsequence/discuss/2818743/Python-or-O(n)-O(1)-or-fastest-solution-(25-35ms)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, l = 0, len(s)
        if not l:
            return True
        for a in t:
            if a == s[i]:
                i += 1
                if i == l:
                    return True
        return False
