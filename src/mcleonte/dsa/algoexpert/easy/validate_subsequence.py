# O(n) O(1)
def isValidSubsequence(array, sequence):
  i, l = 0, len(sequence)
  for n in array:
    if n == sequence[i]:
      i += 1
      if i == l:
        return True
  return False


# O(n) O(1)
def isValidSubsequence2(array, sequence):
  i, j, a, s = 0, 0, len(array), len(sequence)
  while i < a and j < s:
    if array[i] == sequence[j]:
      j += 1
    i += 1
  return j == s
