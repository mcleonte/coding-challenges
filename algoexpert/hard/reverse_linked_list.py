class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) O(1)
def reverseLinkedList(head):
    prev, next = None, head
    while next:
        next.next, prev, next = prev, next, next.next
    return prev
