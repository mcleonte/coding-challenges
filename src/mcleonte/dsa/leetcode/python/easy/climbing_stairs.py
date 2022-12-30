"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""


def climb_stairs(n: int) -> int:
  """
  DP approach
  O(n) O(1)
  """
  a = b = 1
  for _ in range(n):
    a, b = b, a + b
  return a


def climb_stairs_2(n: int) -> int:
  """
  Recursive approach
  O(2^n) O(1)
  """
  if n < 2: return 1
  return \
      climb_stairs_2(n - 1) + \
      climb_stairs_2(n - 2)
