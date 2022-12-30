"""
Write a function that takes in a non-empty string and that returns a boolean
representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and
backward. Note that single-character strings are palindromes.
"""


def is_palindrome(string):
  """
  O(n) O(1)
  """
  for i in range(len(string) // 2):
    if string[i] != string[-i - 1]:
      return False
  return True


def is_palindrome_2(string):
  """
  O(n) O(1)
  """
  return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


def is_palindrome_3(string):
  """
  O(n) O(n)
  """
  return string == string[::-1]
