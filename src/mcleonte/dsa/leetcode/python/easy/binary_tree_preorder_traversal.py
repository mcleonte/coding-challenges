"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/3027144/Python-or-O(n)-O(n)-or-simple-7-lines

https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/3021955/Daily-LeetCoding-Challenge-January-Day-9/1750309


Given the root of a binary tree, return the preorder traversal of its nodes'
values.

Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional, List
from mcleonte.dsa.leetcode.python import TreeNode


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
  stack, out = [root], []
  while stack:
    if node := stack.pop():
      out.append(node.val)
      stack.append(node.right)
      stack.append(node.left)
  return out
