"""
https://leetcode.com/problems/find-if-path-exists-in-graph/


There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
edge between vertex ui and vertex vi. Every vertex pair is connected by at most
one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to
vertex destination.

Given edges and the integers n, source, and destination, return true if there is
a valid path from source to destination, or false otherwise.
"""

from typing import List
from collections import deque


def valid_path(
    n: int,
    edges: List[List[int]],
    source: int,
    destination: int,
) -> bool:
  """
  O(n+e) O(n+e) | n = node count, e = edge count
  """
  if source == destination:
    return True

  adjs = [[] for _ in range(n)]
  for node1, node2 in edges:
    adjs[node1].append(node2)
    adjs[node2].append(node1)

  visited, not_visited = set(), deque([source])
  while not_visited:
    node = not_visited.popleft()
    visited.add(node)
    for adj_node in adjs[node]:
      if adj_node == destination:
        return True
      if adj_node not in visited:
        not_visited.append(adj_node)

  return False
