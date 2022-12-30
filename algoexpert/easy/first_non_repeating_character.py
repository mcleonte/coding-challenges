from collections import Counter


# O(n) O(n)
def firstNonRepeatingCharacter(string):
  r = Counter(string)
  for i, c in enumerate(string):
    if r[c] == 1:
      return i
  return -1
