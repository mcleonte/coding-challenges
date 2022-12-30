"""
https://leetcode.com/problems/middle-of-the-linked-list/
https://leetcode.com/problems/middle-of-the-linked-list/discuss/2878866/Python-or-O(n)-O(1)-or-only-variable-assignments-or-no-math-or-boolean-operations
https://leetcode.com/problems/middle-of-the-linked-list/discuss/2878420/Daily-LeetCoding-Challenge-December-Day-5/1705930
"""

"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""


class Solution:
    """
    O(n) O(1)
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = n = head
        while True:
            try:
                m, n = m.next, n.next.next
            except:
                return m
