# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) O(1) | d = max( depth(d1), depth(d2) )
def getYoungestCommonAncestor(a, d1, d2):
    i, d = 0, d1
    # get the depth of d1
    while d:
        i += 1
        d = d.ancestor
    # and subtract the depth of d2
    d = d2
    while d:
        i -= 1
        d = d.ancestor
    # bring the youngest descendant to the same depth as the other
    if i < 0:
        d1, d2 = d2, d1
        i = abs(i)
    for _ in range(i):
        d1 = d1.ancestor
    # check at every depth if d1 and d2 have the same ancestor
    while d1:
        if d1 == d2:
            return d1
        d1, d2 = d1.ancestor, d2.ancestor


# O(d) O(d) | d = max( depth(d1), depth(d2) )
def getYoungestCommonAncestor2(a, d1, d2):
    ds = set()
    while d1 or d2:
        if d1:
            if d1 in ds:
                return d1
            else:
                ds.add(d1)
            d1 = d1.ancestor
        if d2:
            if d2 in ds:
                return d2
            else:
                ds.add(d2)
            d2 = d2.ancestor
    return a
