def productSum(array, d=1):
  return d * sum(n if type(n) == int else productSum(n, d + 1) for n in array)
