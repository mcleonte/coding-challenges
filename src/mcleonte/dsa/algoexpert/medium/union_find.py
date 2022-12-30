"""
Write a UnionFind class that implements the union-find (also called a disjoint
set) data structure. This class should support three methods:

The union-find data structure is similar to a traditional set data structure in
that it contains a collection of unique values. However, these values are spread
out amongst a variety of distinct disjoint sets, meaning that no set can have
duplicate values, and no two sets can contain the same value.

- createSet(value): Adds a given value in a new set containing only that value.

- union(valueOne, valueTwo): Takes in two values and determines which sets they
  are in. If they are in different sets, the sets are combined into a single
  set. If either value is not in a set or they are in the same set, the function
  should have no effect.

- find (value): Returns the "representative" value of the set for which a value
  belongs to. This can be any value in the set, but it should always be the same
  value, regardless of which value in the set find is passed. If the value is
  not in a set, the function should return null/ None. Note that after a set is
  part of a union, its representative can potentially change.

You can assume createSet will never be called with the same value twice.
"""


class UnionFind:
  """
  Union Find / Disjoint Set data structure
  with ranks and path compression implemented
  for optimized (near) constant time complexity.
  """

  def __init__(self):
    self.tree = {}
    self.rank = {}

  def create_set(self, value):
    """
    O(1) O(1)
    """
    if value not in self.tree:
      self.tree[value] = value
      self.rank[value] = 0

  def find(self, value):
    """
    ~O(1) O(1)
    """
    if value not in self.tree:
      return None
    root = value
    # walk until root found
    while root != self.tree[root]:
      root = self.tree[root]
    # path compression
    while root != self.tree[value]:
      value, self.tree[value] = self.tree[value], root
    return root

  def union(self, value1, value2):
    """
    ~O(1) O(1)
    """
    key1 = self.find(value1)
    key2 = self.find(value2)
    if key1 is None or key2 is None or key1 == key2:
      return
    rank1, rank2 = self.rank[key1], self.rank[key2]
    if rank1 > rank2:
      self.tree[key2] = key1
      self.rank.pop(key2)
    elif rank1 < rank2:
      self.tree[key1] = key2
      self.rank.pop(key1)
    else:
      self.tree[key1] = key2
      self.rank[key2] += 1
      self.rank.pop(key1)
