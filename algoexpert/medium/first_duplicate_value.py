"""
Given an array of integers between 1 and n, inclusive, where n is the length of
the array, write a function that returns the first integer that appears more
than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the
input array, your function should return the one whose first duplicate value has
the minimum index.

If no integer appears more than once, your function should return -1.

Note that you're allowed to mutate the input array.
"""


def first_duplicate_value(arr):
  """
  O(n) O(1)
  """
  for n in arr:
    a = abs(n)
    if arr[a - 1] < 0:
      return a
    arr[a - 1] *= -1
  return -1


def first_duplicate_value_2(arr):
  """
  O(n) O(n)
  """
  s = set()
  for n in arr:
    if n in s:
      return n
    s.add(n)
  return -1
