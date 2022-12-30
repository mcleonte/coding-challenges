# O(n) O(1)
def arrayOfProducts(array):
  p, z = 1, 0
  for n in array:
    if n:
      p *= n
    else:
      z += 1
  for i in range(len(array)):
    if z > (array[i] == 0):
      array[i] = 0
    else:
      array[i] = p * (array[i] or 1)**-1
  return array
