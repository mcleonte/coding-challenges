class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
            return
        self.insertAfter(self.tail, node)

    def link(self, left, right):
        if left:
            left.next = right
        if right:
            right.prev = left

    def insertBetween(self, prev, node, next):
        self.remove(node)
        self.link(prev, node)
        self.link(node, next)

    def insertBefore(self, node, nodeToInsert):
        self.insertBetween(node.prev, nodeToInsert, node)
        if node == self.head:
            self.head = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        self.insertBetween(node, nodeToInsert, node.next)
        if node == self.tail:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        for _ in range(position - 2):
            node = node.next
        if node != nodeToInsert:
            self.insertAfter(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            n, node = node, node.next
            if n.value == value:
                self.remove(n)

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
