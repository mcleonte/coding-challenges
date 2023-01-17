"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".
"""

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
  prefix = []
  for chars in zip(*strs):
    if len(set(chars)) > 1:
      break
    prefix.append(chars[0])
  return ''.join(prefix)
