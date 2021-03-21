'''Given a non-empty sorted array of integers, find the square for the arrays
'''

def sortedArrays(arr):
    sortedArrays = [0 for _ in array]
    for i in range(0, len(arr)):
        value = arr[i]
        sortedArrays[i] = value * value
    sortedArrays.sort()
    return sortedArrays