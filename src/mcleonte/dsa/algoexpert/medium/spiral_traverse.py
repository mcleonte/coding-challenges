"""
Write a function that takes in an n x m two-dimensional array (that can be
square-shaped when n == m) and returns a one-dimensional array of all the
array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to
the right, and proceeds in a spiral pattern all the way until every element has
been visited.
"""

from typing import List


def spiral_traverse(array: List[int]) -> List[int]:

  top, left, bot, right, out = 0, 0, len(array) - 1, len(array[0]) - 1, []

  while True:

    out += (array[top][j] for j in range(left, right + 1))
    top += 1
    if top > bot: break

    out += (array[i][right] for i in range(top, bot + 1))
    right -= 1
    if right < left: break

    out += (array[bot][j] for j in range(right, left - 1, -1))
    bot -= 1
    if bot < top: break

    out += (array[i][left] for i in range(bot, top - 1, -1))
    left += 1
    if left > right: break

  return out
