"""
https://leetcode.com/problems/daily-temperatures/

https://leetcode.com/problems/daily-temperatures/discuss/2926524/Python-or-O(n)-O(n)-or-concise-and-clean-solution

https://leetcode.com/problems/daily-temperatures/discuss/2923180/Daily-LeetCoding-Challenge-December-Day-18/1720896


Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List


def daily_temperatures(temps: List[int]) -> List[int]:
  """
  O(n) O(n)
  """
  stack, out = [], [0] * len(temps)
  for i, temp in enumerate(temps):
    while stack and temp > temps[stack[-1]]:
      j = stack.pop()
      out[j] = i - j
    stack.append(i)
  return out
