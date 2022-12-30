class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) O(1)
def removeKthNodeFromEnd(head, k):
    l, node = 1, head
    while node.next:
        l += 1
        node = node.next
    if l == k:
        head.value, head.next = head.next.value, head.next.next
        return
    node = head
    for _ in range(l - k - 1):
        node = node.next
    node.next = node.next.next
