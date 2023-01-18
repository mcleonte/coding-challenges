"""
https://leetcode.com/problems/length-of-last-word/

https://leetcode.com/problems/length-of-last-word/discuss/3070253/Python-or-O(n)-O(1)-or-constant-space-with-while-loops


Given a string s consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


def length_of_last_word(s: str) -> int:
  """
  O(n) O(1)
  """
  i = len(s) - 1
  while i != -1 and s[i] == " ":
    i -= 1
  j = i
  while i != -1 and s[i] != " ":
    i -= 1
  return j - i
