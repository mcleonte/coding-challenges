"""
Write a function that takes in a string and returns its longest substring
without duplicate characters.

You can assume that there will only be one longest substring without
duplication.
"""


def longest_substring_without_duplication(string):
  """
  O(n) O(s) | n = len(string), s = len(set(string))
  """
  mem = {}
  i = out_i = out_j = 0
  for j, char in enumerate(string):
    if char in mem:
      i = max(i, mem[char] + 1)
    if j - i > out_j - out_i:
      out_i, out_j = i, j
    mem[char] = j
  return string[out_i:out_j + 1]
