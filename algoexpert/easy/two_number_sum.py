# O(n) O(n)
def twoNumberSum(array, targetSum):
  d = {}
  for n in array:
    if targetSum - n in d:
      return n, targetSum - n
    d[n] = True
  return []
