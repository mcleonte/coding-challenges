def bubbleSort(array):
    for i in range(len(array) - 1):
        sorted = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
        if sorted:
            break
    return array


def bubbleSort2(array):
    i = 0
    unsorted = True
    while unsorted:
        unsorted = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                unsorted = True
        i += 1
    return array
