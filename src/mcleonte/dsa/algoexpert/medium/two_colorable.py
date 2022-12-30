"""
You're given a list of edges representing a connected, unweighted, undirected
graph with at least one node. Write a function that returns a boolean
representing whether the given graph is two-colorable.

A graph is two-colorable (also called bipartite) if all of the nodes can be
assigned one of two colors such that no nodes of the same color are connected by
an edge.

The given list is what's called an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges, where each
index in edges contains vertex's siblings, in no particular order. Each
individual edge is represented by a positive integer that denotes an index in
the list that this vertex is connected to. Note that this graph is undirected,
meaning that if a vertex appears in the edge list of another vertex, then the
inverse will also be true.

Also note that this graph may contain self-loops. A self-loop is an edge that
has the same destination and origin; in other words, it's an edge that connects
a vertex to itself. Any self-loop should make a graph not 2-colorable.
"""

from collections import defaultdict


def two_colorable(edges):
  """
  O(v+e) O(v)
  """
  colors, stack = defaultdict(bool), [0]
  while stack:
    node1 = stack.pop()
    for node2 in edges[node1]:
      if node2 not in colors:
        colors[node2] = not colors[node1]
        stack.append(node2)
      elif colors[node1] is colors[node2]:
        return False
  return True
