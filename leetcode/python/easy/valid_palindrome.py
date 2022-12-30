# https://leetcode.com/problems/valid-palindrome/
# https://leetcode.com/problems/valid-palindrome/discuss/2851453/Python-or-O(n)-O(n)-without-isalnum()-or-lower()
# O(n) O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []
        for c in s:
            if "a" <= c <= "z" or "0" <= c <= "9":
                p.append(c)
            elif "A" <= c <= "Z":
                p.append(chr(ord(c) + 32))
        for i in range(len(p) // 2):
            if p[i] != p[-1 - i]:
                return False
        return True
