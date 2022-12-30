"""
Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Insertion Sort algorithm to sort the array.
"""

from typing import List


def insertion_sort(arr: List[int]):
  """
  O(n^2) O(1)
  """
  i = 1
  while i < len(arr):
    for j in range(i - 1, -1, -1):
      if arr[j + 1] >= arr[j]:
        break
      arr[j + 1], arr[j] = arr[j], arr[j + 1]
    i += 1
  return arr
