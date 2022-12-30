"""
Helper classes for type hinting and context.
"""


class AncestralTree:

  def __init__(self, name):
    self.name = name
    self.ancestor = None


class BinaryTree:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
