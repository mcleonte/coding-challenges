# O(1) O(1)
# https://leetcode.com/problems/ugly-number/
# https://leetcode.com/problems/ugly-number/discuss/2828502/Python-or-O(1)-O(1)-or-greater96-one-liner-with-a-couple-of-tricks
class Solution:
    mx = 2**31 * 3**20 * 5**13  # or just m = 30**31 for just 8 more bytes

    def isUgly(self, n: int) -> bool:
        return n > 0 == self.mx % n
