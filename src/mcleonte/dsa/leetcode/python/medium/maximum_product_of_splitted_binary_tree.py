"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/2898997/Python-or-O(n)-O(n)-99-or-DFS-with-cusums

https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/2895717/Daily-LeetCoding-Challenge-December-Day-10/1712430

Given the root of a binary tree, split the binary tree into two subtrees by
removing one edge such that the product of the sums of the subtrees is
maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may
be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after
taking it.
"""

from typing import Optional

from .. import TreeNode


def max_product(root: Optional[TreeNode]) -> int:
  """
  O(n) O(n) | n = node count
  """
  cusums = []

  def cusum(n: Optional[TreeNode]):
    if not n: return 0
    cusums.append(n.val + cusum(n.left) + cusum(n.right))
    return cusums[-1]

  cusum(root)
  return max((cusums[-1] - s) * s for s in cusums) % 1_000_000_007
