# https://leetcode.com/problems/determine-if-two-strings-are-close/
# https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/2871072/Python-or-O(n)-O(n)-or-2-liner-and-equivalent-expanded-versions-or-no-sorting
class Solution:

    # O(n) O(n)
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and Counter(c1.values()) == Counter(c2.values())

    # O(n) O(n) - equivalent expanded version
    def closeStrings2(self, word1: str, word2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        v1 = defaultdict(int)
        v2 = defaultdict(int)
        for k in word1:
            d1[k] += 1
        for k in word2:
            d2[k] += 1
        for k in d1.values():
            v1[k] += 1
        for k in d2.values():
            v2[k] += 1
        return d1.keys() == d2.keys() and v1 == v2
