"""
You're given an array of integers and an integer. Write a function that moves
all instances of that integer in the array to the end of the array and returns
the array.

The function should perform this in place (i.e., it should mutate the input
array) and doesn't need to maintain the order of the other integers.
"""

from typing import List


def move_element_to_end(array: List[int], to_move: int) -> List[int]:
  i, j = 0, len(array) - 1
  while i <= j:
    if array[i] == to_move:
      array[i], array[j] = array[j], array[i]
      j -= 1
    else:
      i += 1
  return array
