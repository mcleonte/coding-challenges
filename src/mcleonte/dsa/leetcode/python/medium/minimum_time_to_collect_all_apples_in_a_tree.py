"""
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


def min_time(
    edges: List[List[int]],
    has_apple: List[bool],
) -> int:

  adjs = defaultdict(list)
  for a, b in edges:
    adjs[a].append(b)
    adjs[b].append(a)

  def dfs(node: int = 0, prev: int = -1) -> int:
    res = sum(dfs(adj, node) for adj in adjs[node] if adj != prev)
    return res + 1 if res else has_apple[node]

  return 2 * max(0, dfs() - 1)
