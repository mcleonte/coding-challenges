# O(n) O(1)
def isMonotonic(arr):
    f = None
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            xf, f = f, arr[i] > arr[i + 1]
            if xf != f and xf is not None:
                return False
    return True
