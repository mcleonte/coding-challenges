"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/3037713/Python-or-O(n)-O(n)-or-2-liner-DFS-inner-function

https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/3032890/Daily-LeetCoding-Challenge-January-Day-11/1753294


Given an undirected tree consisting of n vertices numbered from 0 to n-1, which
has some apples in their vertices. You spend 1 second to walk over one edge of
the tree. Return the minimum time in seconds you have to spend to collect all
apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] =
[ai, bi] means that exists an edge connecting the vertices ai and bi.
Additionally, there is a boolean array hasApple, where hasApple[i] = true means
that vertex i has an apple; otherwise, it does not have any apple.
"""

from typing import List
from collections import defaultdict


def min_time(edges: List[List[int]], has_apple: List[bool]) -> int:
  """
  O(n) O(n)
  """

  def dfs(node: int = 0, prev: int = -1) -> int:
    time = sum(dfs(adj, node) for adj in adjs[node] if adj != prev)
    return time + 1 if time else has_apple[node]

  adjs = defaultdict(list)
  for a, b in edges:
    adjs[a].append(b)
    adjs[b].append(a)
  return max(0, 2 * dfs() - 2)
