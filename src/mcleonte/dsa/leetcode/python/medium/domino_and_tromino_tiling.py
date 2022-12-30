"""
https://leetcode.com/problems/domino-and-tromino-tiling/

https://leetcode.com/problems/domino-and-tromino-tiling/discuss/2946669/Python-or-O(n)-O(1)-greater99-or-DP-+-Queue-short-solution

https://leetcode.com/problems/domino-and-tromino-tiling/discuss/2943847/Daily-LeetCoding-Challenge-December-Day-24/1726799


You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the
answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different
if and only if there are two 4-directionally adjacent cells on the board such
that exactly one of the tilings has both squares occupied by a tile.
"""

from collections import deque


def num_tilings(n: int) -> int:
  """
  O(n) O(1)
  """
  queue = deque([0, 1, 2, 5])
  if n < 4:
    return queue[n]
  for _ in range(n - 3):
    queue.append(queue[-1] * 2 + queue[-3])
    queue.popleft()
  return queue[-1] % 1_000_000_007
