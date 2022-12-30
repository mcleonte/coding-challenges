"""
Write a function that takes in a Binary Tree and returns a list of its branch
sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
branch is a path of nodes in a tree that starts at the root node and ends at any
leaf node.

Each BinaryTree node has an integer value, a left child node, and a right child
node. Children nodes can either be BinaryTree nodes themselves or None.
"""

from typing import Optional

from .. import BinaryTree


def branch_sums(root: Optional[BinaryTree]):
  """
  O(n) O(n) | n = node count
  """
  cusums = []

  def cusum(node: Optional[BinaryTree], s: int = 0):
    if node.left: cusum(node.left, s + node.value)
    if node.right: cusum(node.right, s + node.value)
    if not node.left and not node.right: cusums.append(s + node.value)

  cusum(root)
  return cusums
