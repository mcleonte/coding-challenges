# O(log(n)) O(1)
def binarySearch(a, t):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if t == a[m]:
            return m
        if t > a[m]:
            l = m + 1
        else:
            r = m - 1
    return -1
