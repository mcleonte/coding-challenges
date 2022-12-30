"""
https://leetcode.com/problems/determine-if-two-strings-are-close/
https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/2871072/Python-or-O(n)-O(n)-or-2-liner-and-equivalent-expanded-versions-or-no-sorting
https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/2868003/Daily-LeetCoding-Challenge-December-Day-2/1703445


Two strings are considered close if you can attain one from the other using the
following operations:

  Operation 1: Swap any two existing characters.

    For example, abcde -> aecdb

  Operation 2: Transform every occurrence of one existing character into another
  existing character, and do the same with the other character.

    For example, aacabb -> bbcbaa
    (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close,
and false otherwise.
"""

from collections import defaultdict, Counter


def close_strings(word1: str, word2: str) -> bool:
  """
  O(n) O(n)
  """
  cnt1, cnt2 = Counter(word1), Counter(word2)
  return cnt1.keys() == cnt2.keys() and Counter(cnt1.values()) == Counter(
      cnt2.values())


def close_strings_2(word1: str, word2: str) -> bool:
  """
  O(n) O(n)
  """
  cnt1 = defaultdict(int)
  cnt2 = defaultdict(int)
  cnt1v = defaultdict(int)
  cnt2v = defaultdict(int)
  for k in word1:
    cnt1[k] += 1
  for k in word2:
    cnt2[k] += 1
  for k in cnt1.values():
    cnt1v[k] += 1
  for k in cnt2.values():
    cnt2v[k] += 1
  return cnt1.keys() == cnt2.keys() and cnt1v == cnt2v
