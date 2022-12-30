"""
Write a function that takes in a string of words separated by one or more
whitespaces and returns a string that has these words in reverse order. For
example, given the string "tim is great", your function should return "great is
tim".

For this problem, a word can contain special characters, punctuation, and
numbers. The words in the string will be separated by one or more whitespaces,
and the reversed string must contain the same whitespaces as the original
string. For example, given the string "whitespaces    4" you would be expected
to return "4    whitespaces".

Note that you're not allowed to to use any built-in split or reverse
methods/functions. However, you are allowed to use a built-in join
method/function. Also note that the input string isn't guaranteed to always
contain words.
"""


def reverse_words_in_string(string: str):
  """
  O(n) O(n)
  """
  out, j = [], 0
  for i in range(len(string) - 1, -1, -1):
    if string[i] == " ":
      if j:
        out.append(string[i + 1:j])
        j = 0
      out.append(" ")
    elif not j:
      j = i + 1
  if j:
    out.append(string[:j])
  return "".join(out)
