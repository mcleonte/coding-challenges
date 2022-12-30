"""
You're given three inputs, all of which are instances of an AncestralTree class
that have an ancestor property pointing to their youngest ancestor. The first
input is the top ancestor in an ancestral tree, i.e., the only instance that has
no ancestor--its ancestor property points to None / null, and the other two
inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two
descendants.

Note that a descendant is considered its own ancestor. So in the simple
ancestral tree below, the youngest common ancestor to nodes A and B is node A.
"""

from .. import AncestralTree


def get_youngest_common_ancestor(
    _: AncestralTree,
    desc1: AncestralTree,
    desc2: AncestralTree,
):
  """
  O(d) O(1) | d = max( depth(desc1), depth(desc2) )
  """
  i, desc = 0, desc1
  # get the depth of desc1
  while desc:
    i += 1
    desc = desc.ancestor
  # and subtract the depth of desc2
  desc = desc2
  while desc:
    i -= 1
    desc = desc.ancestor
  # bring the youngest descendant to the same depth as the other
  if i < 0:
    desc1, desc2 = desc2, desc1
    i = abs(i)
  for _ in range(i):
    desc1 = desc1.ancestor
  # check at every depth if desc1 and desc2 have the same ancestor
  while desc1:
    if desc1 == desc2:
      return desc1
    desc1, desc2 = desc1.ancestor, desc2.ancestor


def get_youngest_common_ancestor_2(
    anc: AncestralTree,
    desc1: AncestralTree,
    desc2: AncestralTree,
):
  """
  O(d) O(d) | d = max( depth(d1), depth(d2) )
  """
  descs = set()
  while desc1 or desc2:
    if desc1:
      if desc1 in descs:
        return desc1
      else:
        descs.add(desc1)
      desc1 = desc1.ancestor
    if desc2:
      if desc2 in descs:
        return desc2
      else:
        descs.add(desc2)
      desc2 = desc2.ancestor
  return anc
