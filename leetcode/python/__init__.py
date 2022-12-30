"""
Helper classes for validating type hints.
"""


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class ListNode:

  def __init__(self, val=0, nxt=None):
    self.val = val
    self.next = nxt
