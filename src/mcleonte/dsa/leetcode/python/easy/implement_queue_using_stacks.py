"""
https://leetcode.com/problems/implement-queue-using-stacks/

https://leetcode.com/problems/implement-queue-using-stacks/discuss/2919409/Python-or-amortized-O(1)-or-most-elegant-solution-with-@property-decorator

https://leetcode.com/problems/implement-queue-using-stacks/discuss/2916051/Daily-LeetCoding-Challenge-December-Day-16/1718658


Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue (push,
peek, pop, and empty).

Implement the MyQueue class:

 - void push(int x) Pushes element x to the back of the queue.
 - int pop() Removes the element from the front of the queue and returns it.
 - int peek() Returns the element at the front of the queue.
 - boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

 - You must use only standard operations of a stack, which means only push to
   top, peek/pop from top, size, and is empty operations are valid.

 - Depending on your language, the stack may not be supported natively. You may
   simulate a stack using a list or deque (double-ended queue) as long as you
   use only a stack's standard operations.

Follow-up: Can you implement the queue such that each operation is amortized
O(1) time complexity? In other words, performing n operations will take overall
O(n) time even if one of those operations may take longer.
"""


class MyQueue:
  """
  Each method is O(1) time complexity, while the "left"
  property is amortized O(1) time complexity, since
  each append-pop operation is done once for each
  element added to the queue.
  """

  def __init__(self):
    self.right = []
    self._left = []

  @property
  def left(self):
    if not self._left:
      while self.right:
        self._left.append(self.right.pop())
    return self._left

  def push(self, x: int) -> None:
    self.right.append(x)

  def pop(self) -> int:
    return self.left.pop()

  def peek(self) -> int:
    return self.left[-1]

  def empty(self) -> bool:
    return not self.left
