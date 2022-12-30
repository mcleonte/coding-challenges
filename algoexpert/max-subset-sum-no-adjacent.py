# O(n) O(1)
def maxSubsetSumNoAdjacent(array):

    try:
        prev = array[0]
    except IndexError:
        return 0

    try:
        curr = max(prev, array[1])
    except IndexError:
        return prev

    for i in range(2, len(array)):
        prev, curr = curr, max(curr, prev + array[i])
    return curr
