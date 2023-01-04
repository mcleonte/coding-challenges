"""
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/discuss/2997380/Python-or-O(n+u)-O(u)-greater96-or-1-n-length-pass-and-1-u-length-pass

https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/discuss/2994683/Daily-LeetCoding-Challenge-January-Day-4/1741195


You are given a 0-indexed integer array tasks, where tasks[i] represents the
difficulty level of a task. In each round, you can complete either 2 or 3 tasks
of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is
not possible to complete all the tasks.
"""
from typing import List
from collections import Counter


def minimum_rounds(tasks: List[int]) -> int:
  """
  O(n+u) O(u)
  n = number of tasks
  u = number of unique task lengths
  """
  rounds = 0
  for c in Counter(tasks).values():
    if c == 1: return -1
    rounds += (c + 2) // 3
  return rounds
