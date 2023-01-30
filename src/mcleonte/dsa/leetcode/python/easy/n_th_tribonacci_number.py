"""
https://leetcode.com/problems/n-th-tribonacci-number/


The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


def tribonacci(n: int) -> int:
  """
  O(n) O(1)
  """
  if n < 2:
    return n
  a, b, c = 0, 1, 1
  for _ in range(n - 2):
    a, b, c = b, c, a + b + c
  return c
