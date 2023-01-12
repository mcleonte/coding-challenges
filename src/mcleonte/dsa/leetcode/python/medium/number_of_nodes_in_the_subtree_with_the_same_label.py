"""
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/3040475/Python-or-O(n)-O(n)-or-3-liner-DFS-inner-function-with-sum(-_-Counter(-_-)-)

https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/3037858/Daily-LeetCoding-Challenge-January-Day-12/1754202


You are given a tree (i.e. a connected, undirected graph that has no cycles)
consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root
of the tree is the node 0, and each node of the tree has a label which is a
lower-case character given in the string labels (i.e. The node with the number i
has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is
an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of
the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its
descendant nodes. You are given a tree (i.e. a connected, undirected graph that
has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1
edges. The root of the tree is the node 0, and each node of the tree has a label
which is a lower-case character given in the string labels (i.e. The node with
the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is
an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of
the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its
descendant nodes.
"""

from typing import List
from collections import Counter, defaultdict


def count_sub_trees(
    n: int,
    edges: List[List[int]],
    labels: str,
) -> List[int]:
  """
  O(n) O(n)
  """

  def dfs(node: int = 0, prev: int = -1):
    counts = sum((dfs(adj, node) for adj in adjs[node] if adj != prev),
                 Counter({labels[node]: 1}))
    out[node] = counts[labels[node]]
    return counts

  adjs, out = defaultdict(list), [None] * n
  for a, b in edges:
    adjs[a].append(b)
    adjs[b].append(a)
  dfs()
  return out
