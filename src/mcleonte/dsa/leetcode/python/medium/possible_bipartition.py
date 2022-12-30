"""
We want to split a group of n people (labeled from 1 to n) into two groups of
any size. Each person may dislike some other people, and they should not go into
the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
indicates that the person labeled ai does not like the person labeled bi, return
true if it is possible to split everyone into two groups in this way.
"""

from typing import List
from collections import defaultdict, deque


def possible_bipartition(_: int, dislikes: List[List[int]]) -> bool:

  def dfs(person: int, group: bool = False) -> bool:
    groups[person] = group
    for neighbour in people[person]:
      if groups[neighbour] == group:
        return False
      if groups[neighbour] is None:
        if not dfs(neighbour, not group):
          return False
    return True

  groups = defaultdict(lambda: None)
  people = defaultdict(list)
  for a, b in dislikes:
    people[a].append(b)
    people[b].append(a)
  for person in people:
    if groups[person] is None and not dfs(person):
      return False
  return True


def possible_bipartition_2(_: int, dislikes: List[List[int]]) -> bool:
  graph, colors = defaultdict(list), {}
  for node1, node2 in dislikes:
    graph[node1].append(node2)
    graph[node2].append(node1)
  for node in graph:
    if node not in colors:
      colors[node] = 0
      queue = deque([node])
      while queue:
        node = queue.popleft()
        color = colors[node]
        for neighbour in graph[node]:
          if neighbour in colors:
            if color == colors[neighbour]:
              return False
          else:
            colors[neighbour] = not color
            queue.append(neighbour)
  return True
