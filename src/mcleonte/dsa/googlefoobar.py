"""
My Google Foobar challenges and solutions.
"""

from fractions import Fraction, gcd


def solar_doomsday(area):
  """
  Phase 1
  """
  areas = []
  while area:
    areas.append(int(area**0.5)**2)
    area -= areas[-1]
  return areas


def hey_i_already_did_that(n, b):
  """
  Phase 2 - Challenge 1
  """
  n = list(map(int, n))
  ids = [n]
  while True:
    y = sorted(n)
    x = y[::-1]
    z = []
    borrow = False
    for a, c in zip(y, x):
      a -= borrow
      borrow = a < c
      z.append(a - c + b * borrow)
    n = z[::-1]
    try:
      return len(ids) - ids.index(n)
    except ValueError:
      ids.append(n)


def gearing_up_for_destruction(pegs):
  """
  Phase 2 - Challenge 2
  """
  spaces = [b - a for a, b in zip(pegs[:-1], pegs[1:])]
  n = 2 * sum(s * (-1)**i for i, s in enumerate(spaces))
  d = 1
  if len(pegs) % 2 == 0:
    if n % 3 == 0:
      n //= 3
    else:
      d = 3
  r = n / d
  for s in spaces:
    r = s - r
    if r < 1:
      return -1, -1
  return n, d


def bomb_baby(m, f):
  """
  Phase 3 - Challenge 1
  """
  x, y = int(m), int(f)
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


def doomsday_fuel(m):
  """
  Phase 3 - Challenge 2
  """

  def invert_matrix(m):
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
  inv_0 = invert_matrix(q)[0]
  ps = [sum(inv_0[j] * r[j][i] for j in range(s0)) for i in range(s1)]
  lcm = 1
  for dnm in (p.denominator for p in ps):
    lcm *= dnm // gcd(lcm, dnm)
  return [lcm * p.numerator // p.denominator for p in ps] + [lcm]


def the_grandest_staircase_of_them_all(n):
  """
  Phase 3 - Challenge 3

  Time and space complexity: O(n^2) O(n)

  Solution derived from the generating function Product(1+x**i) of sequence
  A000009: Number of partitions of n into distinct parts.

  https://oeis.org/A000009
  """
  # given the power series sum( c[i] * x ** i for i in range(n + 1) ),
  # initialize the coefficients
  c = [1] + n * [0]
  # for every term x ** i in the power series, except first term x ** 0
  for i in range(1, n + 1):
    # multiply the power series with (1 + x ** i), by looping through every
    # c[j] * x ** j between c[0] * x ** 0 and c[n-i] * x ** (n - i),
    # in reversed order
    for j in range(n - i, -1, -1):
      # and multiply it with (1 + x ** i) to obtain
      # c[j] * x ** j + c[j] * x ** (i + j), which results in increasing the
      # coefficient of term x ** (i + j) with the coefficient of term x ** j
      c[i + j] += c[j]
  # get the coefficient c[n] of term x ** n, which represents the number of
  # partitions of n into distinct parts, and return it after subtracting 1,
  # to exclude (n,) as a step configuration, since at least 2 steps are required
  return c[-1] - 1
