# https://leetcode.com/problems/palindrome-number/
class Solution:

  def isPalindrome(self, x: int) -> bool:
    s = x.__str__()
    return s == s[::-1]
