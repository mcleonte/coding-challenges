"""
https://leetcode.com/problems/possible-bipartition/

https://leetcode.com/problems/possible-bipartition/discuss/2940305/Python-or-O(v+e)-O(v+e)-99.56-677ms-or-very-clean-and-short-solution

https://leetcode.com/problems/possible-bipartition/discuss/2933873/Daily-LeetCoding-Challenge-December-Day-21/1724844


We want to split a group of n people (labeled from 1 to n) into two groups of
any size. Each person may dislike some other people, and they should not go into
the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
indicates that the person labeled ai does not like the person labeled bi, return
true if it is possible to split everyone into two groups in this way.
"""

from typing import List
from collections import defaultdict


def possible_bipartition(_: int, dislikes: List[List[int]]) -> bool:
  """
  O(v+e) O(v+e)
  """

  people, groups, stack = defaultdict(list), defaultdict(bool), []

  for person_a, person_b in dislikes:
    people[person_a].append(person_b)
    people[person_b].append(person_a)

  for person in people:
    if person in groups:
      continue
    stack.append(person)
    while stack:
      person = stack.pop()
      for person_b in people[person]:
        if person_b not in groups:
          groups[person_b] = not groups[person]
          stack.append(person_b)
        elif groups[person_b] is groups[person]:
          return False
  return True
