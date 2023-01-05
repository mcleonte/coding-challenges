"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/3002730/Python-or-O(nlogn)-O(1)-or-clean-and-concise-solution

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/3000317/Daily-LeetCoding-Challenge-January-Day-5/1742887


There are some spherical balloons taped onto a flat wall that represents the
XY-plane. The balloons are represented as a 2D integer array points where
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
between xstart and xend. You do not know the exact y-coordinates of the
balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from
different points along the x-axis. A balloon with xstart and xend is burst by an
arrow shot at x if xstart <= x <= xend. There is no limit to the number of
arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting
any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to
burst all balloons.
"""

from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
  """
  O(nlogn) O(1)
  """
  points.sort()
  arrows, overlap_end = 0, float('-inf')
  for pt_start, pt_end in points:
    if pt_start > overlap_end:
      overlap_end = pt_end
      arrows += 1
    elif pt_end < overlap_end:
      overlap_end = pt_end
  return arrows
