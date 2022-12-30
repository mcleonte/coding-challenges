"""
Write a function that takes in two integer matrices and multiplies them
together.

Both matrices will be sparse, meaning that most of their elements will be zero.
Take advantage of that to reduce the number of total computations that your
function performs.

If the matrices can't be multiplied together, your function should return [[]].
"""

from typing import List


def sparse_matrix_multiplication(
    matrix_a: List[List[int]],
    matrix_b: List[List[int]],
) -> List[List[int]]:

  n, m, m2, p = len(matrix_a), len(matrix_a[0]), len(matrix_b), len(matrix_b[0])
  if m != m2:
    return [[]]
  out = []
  for i in range(n):
    out.append([])
    for k in range(p):
      dot = 0
      for j in range(m):
        if matrix_a[i][j] == 0 or matrix_b[j][k] == 0:
          continue
        dot += matrix_a[i][j] * matrix_b[j][k]
      out[-1].append(dot)
  return out
