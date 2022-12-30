"""
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer num to its English words representation.
"""

DIGITS = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
EDGE_CASES = {
    "2": "Twenty",
    "3": "Thirty",
    "4": "Forty",
    "5": "Fifty",
    "8": "Eighty",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
}
ORDERS = {
    2: "Thousand",
    3: "Million",
    4: "Billion",
}


def number_to_words(num: int) -> str:
  """
  O(n) O(n) | n = len(str(num))
  """
  num = str(num)
  num = "0" * (0, 2, 1)[len(num) % 3] + num  # ensure 3 digits string
  out = []
  triplets = [num[i:i + 3] for i in range(0, len(num), 3)]

  for i, (hundreds, tens, units) in enumerate(triplets):

    try:
      out.append(DIGITS[hundreds])
    except KeyError:
      pass

    try:
      out.append(EDGE_CASES[tens + units])
    except KeyError:

      try:
        out.append(EDGE_CASES[tens])
      except KeyError:
        try:
          out.append(DIGITS[tens] + "ty")
        except KeyError:
          pass

      try:
        out.append(DIGITS[units])
      except KeyError:
        pass

    if hundreds + tens + units != "000":
      try:
        out.append(ORDERS[len(triplets) - i])
      except KeyError:
        pass

  return " ".join(out) or "Zero"
