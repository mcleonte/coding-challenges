"""
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range
[low, high]. All Node.val are unique.
"""

from typing import Optional

from .. import TreeNode


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
  return (0 if not root else (root.val if low <= root.val <= high else 0) +
          (range_sum_bst(root.left, low, high) if root.val > low else 0) +
          (range_sum_bst(root.right, low, high) if root.val < high else 0))


def range_sum_bst_2(root: Optional[TreeNode], low: int, high: int) -> int:
  if not root: return 0
  out, val = 0, root.val
  if low <= val <= high: out += val
  if low < val: out += range_sum_bst_2(root.left, low, high)
  if val < high: out += range_sum_bst_2(root.right, low, high)
  return out
