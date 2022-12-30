# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:

  def reverseWords(self, s: str) -> str:

    # one-liner "cheat"
    # return " ".join(s.split()[::-1])

    # no split or reverse
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
