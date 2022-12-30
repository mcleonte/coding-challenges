from fractions import Fraction, gcd


def invert(m):
  n = len(m)
  ixs = range(n)
  for i in ixs:
    m[i] += [0] * n
    m[i][i + n] = 1
  for i in ixs:
    j = 1
    piv = m[i][i]
    while piv == 0 and i + j < n:
      m[i][i + j] = m[i + j][i]
      j += 1
      piv = m[i][i]
    if piv == 0:
      break
    m[i] = [num / piv for num in m[i]]
    for j in ixs:
      if j != i:
        m[j] = [a - b * m[j][i] for a, b in zip(m[j], m[i])]
  return [row[n:] for row in m]


def solution(m):
  rsums = [sum(row) for row in m]
  trs, trm = [], []
  for i, rsum in enumerate(rsums):
    if rsum:
      trs.append(i)
      m[i] = [Fraction(num, rsum) for num in m[i]]
    else:
      trm.append(i)
      m[i][i] = 1
  s0, s1 = len(trs), len(trm)
  if 0 in trm:
    return [1] + [0] * (s1 - 1) + [1]
  r = [[m[i][j] for j in trm] for i in trs]
  q = [[-m[i][j] for j in trs] for i in trs]
  for i in range(s0):
    q[i][i] += 1
  inv_0 = invert(q)[0]
  ps = [sum(inv_0[j] * r[j][i] for j in range(s0)) for i in range(s1)]
  lcm = 1
  for dnm in (p.denominator for p in ps):
    lcm *= dnm // gcd(lcm, dnm)
  return [lcm * p.numerator // p.denominator for p in ps] + [lcm]
