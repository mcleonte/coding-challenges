"""
https://leetcode.com/problems/number-of-good-pairs/

https://leetcode.com/problems/number-of-good-pairs/discuss/3095534/Python-or-O(n)-O(n)-or-dead-simple-one-pass-(no-Counter-class)


Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

from collections import defaultdict
from typing import List


def num_identical_pairs(nums: List[int]) -> int:
  """
  O(n) O(n)
  """
  pairs, freq = 0, defaultdict(int)
  for num in nums:
    pairs += freq[num]
    freq[num] += 1
  return pairs
