"""
Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Selection Sort algorithm to sort the array.
"""

from typing import List


def selection_sort(arr: List[int]):
  """
  O(n^2) O(1)
  """
  for i in range(len(arr) - 1):
    k = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[k]:
        k = j
    arr[i], arr[k] = arr[k], arr[i]
  return arr
