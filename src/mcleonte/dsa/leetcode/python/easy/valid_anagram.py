"""
https://leetcode.com/problems/valid-anagram/


Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
  if len(s) != len(t): return False
  return Counter(s) == Counter(t)
