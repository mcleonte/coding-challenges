"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
  mem = set()
  for num in nums:
    if num in mem:
      return True
    mem.add(num)
  return False
