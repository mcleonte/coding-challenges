# O(n+e) O(n) | n = number of nodes, e = number of edges

# deque.popleft() is O(1), while list.pop(0) is O(n)
from collections import deque


class Node:

  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def breadthFirstSearch(self, array):
    deq = deque([self])
    while len(deq) > 0:
      node = deq.popleft()
      array.append(node.name)
      deq += node.children
    return array
