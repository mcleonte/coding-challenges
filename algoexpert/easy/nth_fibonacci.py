# O(n) O(1)
# dynamic programming
def getNthFib(n):
  a, b = 0, 1
  for _ in range(n - 2):
    a, b = b, a + b
  return b if n > 1 else a


# O(2^n) O(n)
# recursion
def getNthFib2(n):
  if n in (1, 2):
    return n - 1
  return getNthFib2(n - 1) + getNthFib2(n - 2)
