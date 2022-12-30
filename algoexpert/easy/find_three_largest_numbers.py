# O(n) O(1)
def findThreeLargestNumbers(array):
  out = [float("-inf")] * 3
  for n in array:
    if n >= out[2]:
      out[:] = out[1], out[2], n
    elif n >= out[1]:
      out[:2] = out[1], n
    elif n >= out[0]:
      out[0] = n
  return out


# O(n) O(1)
# as an improvement to the previous solution,
# this one can be parametrized for any n largest numbers
def findLargestNumbers(array, c=3):
  out = [float("-inf")] * c
  for n in array:
    for i in range(c - 1, -1, -1):
      if n >= out[i]:
        out[i], n = n, out[i]
  return out


# O(n) O(1)
# as an improvement to the previous solution,
# this one mutates the out list in one go when a larger number is found,
# thus breaking the inner for loop
def findLargestNumbers2(array, c=3):
  out = [float("-inf")] * c
  for n in array:
    for i in range(c - 1, -1, -1):
      if n >= out[i]:
        out.insert(i + 1, n)
        out.pop(0)
        break
  return out
