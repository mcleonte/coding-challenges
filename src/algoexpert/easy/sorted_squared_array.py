# O(nlogn) O(1)
def sortedSquaredArray(array):
  for i in range(len(array)):
    array[i] **= 2
  array.sort()  # or any O(nlogn) sorting algo
  return array


# O(n) O(n)
def sortedSquaredArray2(array):
  out = [None] * len(array)
  j, k = 0, -1
  for i in range(len(array) - 1, -1, -1):
    if abs(array[j]) > abs(array[k]):
      out[i] = array[j]**2
      j += 1
    else:
      out[i] = array[k]**2
      k -= 1
  return out
