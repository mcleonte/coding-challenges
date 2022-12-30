# Solution complexity: O(n) O(n)
# Description: https://leetcode.com/problems/isomorphic-strings/
# Thread: https://leetcode.com/problems/isomorphic-strings/discuss/2818651/Python-or-O(n)-O(n)-or-shortest-and-cleanest-logic-with-2-prepopulated-hashmaps
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {c: None for c in s}
        n = {c: None for c in t}
        for i, (a, b) in enumerate(zip(s, t)):
            if m[a] != n[b]:
                return False
            m[a] = n[b] = i
        return True
