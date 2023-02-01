"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/


For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides
both str1 and str2.
"""

import math


def gcd_of_strings(s1: str, s2: str) -> str:
  """
  O(n1 + n2) O(n1 + n2)
  """
  return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ""
