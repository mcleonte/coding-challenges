"""
Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Bubble Sort algorithm to sort the array.
"""


def bubble_sort(arr):
    """
    O(n^2), O(1)
    """
    for i in range(len(arr) - 1):
        is_sorted = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr


def bubble_sort2(arr):
    """
    O(n^2), O(1)
    """
    i = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        i += 1
    return arr
