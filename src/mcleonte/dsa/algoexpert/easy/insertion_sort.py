"""
Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Insertion Sort algorithm to sort the array.
"""

from typing import List


def insertion_sort(array: List[int]):
  """
  O(n^2) O(1)
  """
  i = 1
  while i < len(array):
    for j in range(i - 1, -1, -1):
      if array[j + 1] >= array[j]:
        break
      array[j + 1], array[j] = array[j], array[j + 1]
    i += 1
  return array
