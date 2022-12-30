"""
Write a function that takes in the head of a Singly Linked List, reverses the
list in place (i.e., doesn't create a brand new list), and returns its new head.

Each LinkedList node has an integer value as well as a next node pointig to the
next node in the list or to None if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in
other words, the head will never be None.
"""


def reverse_linked_list(head):
    """
    O(n) O(1)
    """
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev
