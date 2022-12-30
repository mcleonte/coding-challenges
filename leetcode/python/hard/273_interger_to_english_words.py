# https://leetcode.com/problems/integer-to-english-words/
class Solution:

    d = {  # digits
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
    e = {  # edge cases
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

    o = {2: "Thousand", 3: "Million", 4: "Billion"}  # orders

    def numberToWords(self, num: int) -> str:
        d, e, o = self.d, self.e, self.o
        n = str(num)
        n = "0" * (0, 2, 1)[len(n) % 3] + n
        out = []
        threes = [n[i : i + 3] for i in range(0, len(n), 3)]
        for i, (h, t, u) in enumerate(threes):

            try:
                out += d[h], "Hundred"
            except KeyError:
                pass

            try:
                out.append(e[t + u])
            except KeyError:

                try:
                    out.append(e[t])
                except KeyError:
                    try:
                        out.append(d[t] + "ty")
                    except KeyError:
                        pass

                try:
                    out.append(d[u])
                except KeyError:
                    pass

            if h + t + u != "000":
                try:
                    out.append(o[len(threes) - i])
                except KeyError:
                    pass

        return " ".join(out) or "Zero"
