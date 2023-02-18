"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional
from .. import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
  if root is None: return
  root.left, root.right = root.right, root.left
  invert_tree(root.left)
  invert_tree(root.right)
  return root
