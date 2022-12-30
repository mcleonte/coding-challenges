"""
https://leetcode.com/problems/single-threaded-cpu/


You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array
tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith task
will be available to process at enqueueTimei and will take processingTimei to
finish processing.

You have a single-threaded CPU that can process at most one task at a time and
will act in the following way:

  If the CPU is idle and there are no available tasks to process, the CPU
  remains idle.

  If the CPU is idle and there are available tasks, the CPU will choose the one
  with the shortest processing time. If multiple tasks have the same shortest
  processing time, it will choose the task with the smallest index.

  Once a task is started, the CPU will process the entire task without stopping.

  The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.
"""

from collections import List
from bisect import bisect


def get_order(tasks: List[List[int]]) -> List[int]:
  """
  O() O(n)
  """
  tasks = sorted((t[0], (t[1], i)) for i, t in enumerate(tasks))
  len_tasks = len(tasks)
  t = tasks[0][0]
  i = j = 0
  while True:
    while tasks[j][0] <= t:
      k = bisect.bisect(
          tasks, tasks[j][1], lo=i, hi=j, key=lambda item: item[1])
      if k != j: tasks.insert(k, tasks.pop(j))
      j += 1
      if j == len_tasks:
        return [task[1][1] for task in tasks]
    t = max(t, tasks[i][0]) + tasks[i][1][0]
    i += 1
