def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()  # O(nlogn)
  arrayTwo.sort()  # O(nlogn)
  i, j, l1, l2, sd = 0, 0, len(arrayOne), len(arrayTwo), float("inf")
  while i < l1 and j < l2:
    d = arrayOne[i] - arrayTwo[j]
    if abs(d) < sd:
      sd, a, b = abs(d), arrayOne[i], arrayTwo[j]
      if d == 0:
        break
    if d < 0:
      i += 1
    else:
      j += 1
  return a, b
