# O(n) O(1)
def hasSingleCycle(array):
  i, l = 0, len(array)
  for _ in range(l):
    array[i], i = 0, (i + array[i]) % l
  return i == 0 and not any(array)
