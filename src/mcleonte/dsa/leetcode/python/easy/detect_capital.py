"""
https://leetcode.com/problems/detect-capital/

https://leetcode.com/problems/detect-capital/discuss/2988734/Python-or-O(n)-O(1)-greater96-or-pythonic-one-pass

https://leetcode.com/problems/detect-capital/discuss/2982010/Daily-LeetCoding-Challenge-January-Day-2/1738731


We define the usage of capitals in a word to be right when one of the following
cases holds:

  All letters in this word are capitals, like "USA".
  All letters in this word are not capitals, like "leetcode".
  Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""


def detect_capital_use(word: str) -> bool:
  """
  O(n) O(1)
  """
  if len(word) == 1:
    return True
  if word[0].islower():
    return word.islower()
  if word[1].islower():
    return word.istitle()
  return word.isupper()
