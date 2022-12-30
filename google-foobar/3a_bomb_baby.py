def solution(M, F):
  x, y = int(M), int(F)
  if x < y:
    x, y = y, x
  c = -1
  while y > 0:
    q, r = divmod(x, y)
    x, y = y, r
    c += q
  if x != 1:
    return "impossible"
  return str(c)
