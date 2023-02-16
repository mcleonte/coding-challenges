"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
"""

from .. import TreeNode
from typing import Optional


def max_depth(root: Optional[TreeNode]) -> int:
  return 0 if root is None else 1 + max(
      max_depth(root.left), max_depth(root.right))
