# https://leetcode.com/problems/roman-to-integer/
class Solution:
  d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

  def romanToInt(self, s: str) -> int:
    d = self.d
    return (sum(-d[a] if d[b] > d[a] else d[a] for a, b in zip(s[:-1], s[1:])) +
            d[s[-1]])
