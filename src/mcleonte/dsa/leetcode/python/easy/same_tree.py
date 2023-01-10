"""
https://leetcode.com/problems/same-tree/

https://leetcode.com/problems/same-tree/discuss/3032737/Python-or-O(n)-O(n)-or-non-recursive-with-one-stack

https://leetcode.com/problems/same-tree/discuss/3027351/Daily-LeetCoding-Challenge-January-Day-10/1751744


Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical, and
the nodes have the same value.
"""

from typing import Optional
from mcleonte.dsa.leetcode.python import TreeNode


def is_same_tree(
    p: Optional[TreeNode],
    q: Optional[TreeNode],
) -> bool:
  """
  O(n) O(n)
  """
  stack = [p, q]
  while stack:
    n, m = stack.pop(), stack.pop()
    if n is None and m is None:
      continue
    if n is None or m is None or n.val != m.val:
      return False
    stack += n.left, m.left, n.right, m.right
  return True
