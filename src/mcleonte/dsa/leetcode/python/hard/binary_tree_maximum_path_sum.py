"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them. A node can only appear in the
sequence at most once. Note that the path does not need to pass through the
root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty
path.
"""

from typing import Optional
from .. import TreeNode


def max_path_sum(root: Optional[TreeNode]) -> int:
  """
  O(n) O(1) | n = node count
  """
  out = [float('-inf')]

  def walk(node):
    if not node:
      return 0
    left = walk(node.left)
    right = walk(node.right)
    out[0] = max(out[0], node.val + left + right)
    return max(0, node.val + max(left, right))

  walk(root)
  return out[0]
