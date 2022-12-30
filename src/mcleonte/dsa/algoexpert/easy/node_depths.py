"""
The distance between a node in a Binary Tree and the tree's root is called the
node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes'
depths.

Each BinaryTree node has an integer value, a left child node, and a right child
node. Children nodes can either be BinaryTree nodes themselves or None.
"""

from typing import Optional

from .. import BinaryTree


def node_depths(root: Optional[BinaryTree], depth: int = 0):
  if not root: return 0
  return depth + \
      node_depths(root.left, depth + 1) + \
      node_depths(root.right, depth + 1)
