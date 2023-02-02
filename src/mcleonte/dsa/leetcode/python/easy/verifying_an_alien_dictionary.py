"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/3133742/Python-or-O(n)-O(1)-or-simple-and-concise-6-lines

https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/3129127/Daily-LeetCoding-Challenge-February-Day-2/1785259


In an alien language, surprisingly, they also use English lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographically in this alien language.
"""
from typing import List
import itertools


def is_alien_sorted(words: List[str], order: str) -> bool:
  """
  O(n) O(1) | n = sum(map(len, words))
  """
  idx = {None: -1} | {letter: i for i, letter in enumerate(order)}
  for i in range(len(words) - 1):
    for a, b in itertools.zip_longest(words[i], words[i + 1]):
      if a is None or idx[a] < idx[b]: break
      if b is None or idx[a] > idx[b]: return False
  return True
