"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/

https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/2922958/Python-or-O(n)-O(n)-or-clean-solution-with-memoized-lambda-functions

https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/2919588/Daily-LeetCoding-Challenge-December-Day-17/1719714


Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any division
by zero operation.
"""

from typing import List

calc = {
    "+": lambda a, b: b + a,
    "-": lambda a, b: b - a,
    "*": lambda a, b: b * a,
    "/": lambda a, b: int(b / a),
}


def eval_rpn(tokens: List[str]) -> int:
  """
  O(n) O(n)
  """
  stack = []
  for t in tokens:
    if t in calc:
      stack.append(calc[t](stack.pop(), stack.pop()))
    else:
      stack.append(int(t))
  return stack[-1]
