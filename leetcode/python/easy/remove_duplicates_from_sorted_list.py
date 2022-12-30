# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/2857882/Python-or-O(n)-O(1)-95.81-with-simplest-solution
# O(n) O(1)
class Solution:

  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
      return head
    curr = head
    while curr.next:
      if curr.val == curr.next.val:
        curr.next = curr.next.next
      else:
        curr = curr.next
    return head
