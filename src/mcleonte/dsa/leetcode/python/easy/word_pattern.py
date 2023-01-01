"""
https://leetcode.com/problems/word-pattern/


Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in s.
"""


def word_pattern(pattern: str, s: str) -> bool:
  """
  O(n) O(n)
  """
  mem, words = {}, s.split()
  if len(pattern) != len(words):
    return False
  if len(set(pattern)) != len(set(words)):
    return False
  for p, w in zip(pattern, words):
    if p not in mem:
      mem[p] = w
    elif mem[p] != w:
      return False
  return True
