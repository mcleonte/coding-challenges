"""
You're given an array of integers and another array of three distinct integers.
The first array is guaranteed to only contain integers that are in the second
array, and the second array represents a desired order for the integers in the
first array. For example, a second array of [x, y, z] represents a desired order
of [X, X, ..., X, Y, Y, ..., Y, Z, z, ..., z] in the first array.

Write a function that sorts the first array according to the desired order in
the second array.

The function should perform this in place (i.e., it should mutate the input
array), and it shouldn't use any auxiliary space (i.e., it should run with
constant space : 0(1) space).

Note that the desired order won't necessarily be ascending or descending and
that the first array won't necessarily contain all three integers found in the
second array-it might only contain one or two.
"""

from typing import List


def three_number_sort(arr: List[int], order: List[int]):
  i, j, k = 0, 0, len(arr) - 1
  while j <= k:
    if arr[j] == order[0]:
      arr[j], arr[i] = arr[i], arr[j]
      i += 1
      j += 1
    elif arr[j] == order[2]:
      arr[k], arr[j] = arr[j], arr[k]
      k -= 1
    else:
      j += 1
  return arr
