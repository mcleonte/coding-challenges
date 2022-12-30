"""
https://leetcode.com/problems/keys-and-rooms/

https://leetcode.com/problems/keys-and-rooms/discuss/2933744/Python-or-O(v+e)-O(v)-and-O(v+e)-O(v+e)-each-with-BFS-and-DFS-(4-solutions)

https://leetcode.com/problems/keys-and-rooms/discuss/2930084/Daily-LeetCoding-Challenge-December-Day-20/1722943


There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
for room 0. Your goal is to visit all the rooms. However, you cannot enter a
locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a
number on it, denoting which room it unlocks, and you can take all of them with
you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if
you visited room i, return true if you can visit all the rooms, or false
otherwise.
"""

from typing import List
from collections import deque


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
  """
  O(v+e) O(v) | DFS with stack
  """
  visited, not_visited = set(), [0]
  while not_visited:
    room = not_visited.pop()
    visited.add(room)
    for key in rooms[room]:
      if key not in visited:
        not_visited.append(key)
  return len(visited) == len(rooms)


def can_visit_all_rooms_2(rooms: List[List[int]]) -> bool:
  """
  O(v+e) O(v+e) | DFS with stack
  """
  visited, not_visited = set(), [0]
  while not_visited:
    room = not_visited.pop()
    if room not in visited:
      visited.add(room)
      not_visited += rooms[room]
  return len(visited) == len(rooms)


def can_visit_all_rooms_3(rooms: List[List[int]]) -> bool:
  """
  O(v+e) O(v) | BFS with queue
  """
  visited, not_visited = set(), deque([0])
  while not_visited:
    room = not_visited.popleft()
    visited.add(room)
    for key in rooms[room]:
      if key not in visited:
        not_visited.append(key)
  return len(visited) == len(rooms)


def can_visit_all_rooms_4(rooms: List[List[int]]) -> bool:
  """
  O(v+e) O(v+e) | BFS with queue
  """
  visited, not_visited = set(), deque([0])
  while not_visited:
    room = not_visited.popleft()
    if room not in visited:
      visited.add(room)
      not_visited += rooms[room]
  return len(visited) == len(rooms)
