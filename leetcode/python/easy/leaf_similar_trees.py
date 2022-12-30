"""
https://leetcode.com/problems/leaf-similar-trees
https://leetcode.com/problems/leaf-similar-trees/discuss/2891241/Python-or-O(n)-O(1)-at-34ms-93-with-generators-or-O(n)-O(n)-equivalent-at-22ms-99.91
https://leetcode.com/problems/leaf-similar-trees/discuss/2888843/Daily-LeetCoding-Challenge-December-Day-8/1709966

Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the
same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.
"""

from typing import Optional, List
from itertools import zip_longest

from .. import TreeNode


def leaf_similar(
    root1: Optional[TreeNode],
    root2: Optional[TreeNode],
) -> bool:
  """
  Using a generator function to obtain O(1) space complexity
  and a zip object to exit early on the first inequality.

  O(n) O(1) | n = tree node count
  """

  if None in (root1, root2):
    return root1 == root2

  def gen_leaf_vals(node: TreeNode):
    if node.left: yield from gen_leaf_vals(node.left)
    if node.right: yield from gen_leaf_vals(node.right)
    if node.left is None and node.right is None: yield node.val

  return all(a == b for a, b in zip_longest(
      gen_leaf_vals(root1),
      gen_leaf_vals(root2),
  ))


def leaf_similar_2(
    root1: Optional[TreeNode],
    root2: Optional[TreeNode],
) -> bool:
  """
  O(n) O(f) | n = tree node count, f = tree leaf count
  """
  if None in (root1, root2):
    return root1 == root2

  def get_leaf_vals(node: TreeNode, leaves: List[int]):
    if node.left: get_leaf_vals(node.left, leaves)
    if node.right: get_leaf_vals(node.right, leaves)
    if node.left is None and node.right is None: leaves.append(node.val)
    return leaves

  return get_leaf_vals(root1, []) == get_leaf_vals(root2, [])
