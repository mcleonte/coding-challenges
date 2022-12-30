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

You can assume [createSet will never be called with the same value twice.
"""


class UnionFind:
  """
  Union Find / Disjoint Set data structure
  """

  def __init__(self):
    self.sets = {}

  def create_set(self, value):
    if value not in self.sets:
      self.sets[value] = {value}

  def find(self, value):
    if value not in self.sets:
      return None
    while isinstance(self.sets[value], int):
      value = self.sets[value]
    return value

  def union(self, value1, value2):
    key1 = self.find(value1)
    key2 = self.find(value2)
    if None != key1 != key2 != None:
      self.sets[key1] |= self.sets[key2]
      self.sets[key2] = key1
