"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/2857882/Python-or-O(n)-O(1)-95.81-with-simplest-solution
"""

from typing import Optional
from .. import ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
  """
  O(n) O(1)
  """
  if head is None:
    return head
  curr = head
  while curr.next:
    if curr.val == curr.next.val:
      curr.next = curr.next.next
    else:
      curr = curr.next
  return head
