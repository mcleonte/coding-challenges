"""
https://leetcode.com/problems/valid-palindrome/

https://leetcode.com/problems/valid-palindrome/discuss/2851453/Python-or-O(n)-O(1)-or-nested-while-loops

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palindrome(s: str) -> bool:
  """
  O(n) O(1)
  """
  l, r = 0, len(s) - 1
  while l < r:
    while l < r and not s[l].isalnum():
      l += 1
    while l < r and not s[r].isalnum():
      r -= 1
    if s[l].lower() != s[r].lower():
      return False
    l += 1
    r -= 1
  return True
