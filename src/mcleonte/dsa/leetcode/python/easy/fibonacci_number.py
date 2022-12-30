"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1.

Given n, calculate F(n).
"""


def fib(n: int) -> int:
  """
  DP approach
  O(n) O(1)
  """
  a, b = 0, 1
  for _ in range(n):
    a, b = b, b + a
  return a


def fib_2(n: int) -> int:
  """
  Recursive approach
  O(2^n) O(1)
  """
  if n < 2: return n
  return fib_2(n - 1) + fib_2(n - 2)
