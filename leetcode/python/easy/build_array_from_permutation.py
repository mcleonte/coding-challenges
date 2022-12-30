"""
https://leetcode.com/problems/build-array-from-permutation/
https://leetcode.com/problems/build-array-from-permutation/discuss/2867917/Python-or-O(n)-O(1)-or-Very-short-solution-with-detailed-description
"""

from typing import List


def build_array(nums: List[int]) -> List[int]:
  """
  For O(1) space it is required to store 2 numbers, nums[i] and nums[nums[i]],
  as a single number at index i. Thus, nums[nums[i]] can be stored as a
  quotient, while the original value nums[i] can "separately" be kept as a
  remainder, where the divisor is len(nums).

  As such, after the first pass, each number is modified as n = n + nums[n] * l.

  However, this operation might be applied at index n before being applied at
  index i, and we need only the original value at index n to store it as a
  quotient at index i. By following the same logic, the original value at index
  n is obtained by extracting only the remainder from nums[n].

  Therefore, the first pass needs to be modified to n = n + ( nums[n] % l ) * l.

  Finally, after the second pass, each number has its remainder removed,
  the original value, keeping only the quotient, the new value.

  O(n) O(1)
  """
  l = len(nums)
  for i in range(l):
    nums[i] += nums[nums[i]] % l * l
  for i in range(l):
    nums[i] //= l
  return nums


def build_array_2(nums: List[int]) -> List[int]:
  """
  O(n) O(n)
  """
  return [nums[n] for n in nums]
