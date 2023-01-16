"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
  stack, pairs = [], {'(': ')', '[': ']', '{': '}'}
  for char in s:
    if char in pairs:
      stack.append(char)
    elif not stack or char != pairs[stack.pop()]:
      return False
  return not stack
