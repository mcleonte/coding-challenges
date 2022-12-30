"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""


def reverse_words(s: str) -> str:
  """
  O(n) O(n)
  """
  return " ".join(s.split()[::-1])


def reverse_words_2(s: str) -> str:
  """
  Same as the one-line, without any split or reverse
  O(n) O(n)
  """
  out = []
  i = len(s) - 1
  while i > -1:
    if s[i] == " ":
      i -= 1
    else:
      j = i - 1
      while j > -1 and s[j] != " ":
        j -= 1
      out.append(s[j + 1:i + 1])
      i = j - 1
  return " ".join(out)
