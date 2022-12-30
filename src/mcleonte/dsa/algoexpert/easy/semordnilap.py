"""
Write a function that takes in a list of unique strings and returns a list of
semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of
one word is the same as the forward version of the other. For example the words
"diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and
"semordnilap".

The order of the returned pairs and the order of the strings within each pair
does not matter.
"""

from typing import List


def semordnilap(words: List[str]) -> List[List[str]]:
  """
  O(n) O(n) | n = word count
  """
  out, mem = [], set()
  for w in words:
    wr = w[::-1]
    if wr in mem:
      out.append([w, wr])
    else:
      mem.add(w)
  return out
