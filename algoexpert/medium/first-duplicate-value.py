# O(n) O(1)
def firstDuplicateValue(array):
    for n in array:
        a = abs(n)
        if array[a - 1] < 0:
            return a
        array[a - 1] *= -1
    return -1


# O(n) O(n)
def firstDuplicateValue(array):
    s = set()
    for n in array:
        if n in s:
            return n
        s.add(n)
    return -1
