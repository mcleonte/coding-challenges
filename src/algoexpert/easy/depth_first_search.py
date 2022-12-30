"""
You're given a Node class that has a name and an array of optional children
nodes. When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty
array, traverses the tree using the Depth-first Search approach, specifically
navigating the tree from left to right, stores all of the nodes' names in the
input array, and returns it.
"""


class Node:

  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def depthFirstSearch(self, array):
    """
    O(n+e) O(e) | n = number of nodes, e = number of edges
    """
    array.append(self.name)
    for node in self.children:
      node.depthFirstSearch(array)
    return array
