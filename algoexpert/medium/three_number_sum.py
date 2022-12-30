# O(n^2) O(n)
def threeNumberSum(array, targetSum):
  array.sort()  # O(nlogn)
  out, l = [], len(array)
  for i in range(l - 1):
    j, k, t = i + 1, l - 1, targetSum - array[i]
    while j < k:
      s = array[j] + array[k]
      if s == t:
        out.append([array[i], array[j], array[k]])
        j += 1
        k -= 1
      elif s < t:
        j += 1
      else:
        k -= 1
  return out


# O(n^3) O(n)
def threeNumberSum(array, targetSum):
  array.sort()  # O(nlogn)
  out, l = [], len(array)
  for i in range(l - 2):
    t = targetSum - array[i]
    for j in range(i + 1, l - 1):
      t2 = t - array[j]
      for k in range(j + 1, l):
        if array[k] == t2:
          out.append([array[i], array[j], array[k]])
  return out
