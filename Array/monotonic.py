

'''Given a non-empty array of integers, find if the array is monotonic or not
'''

def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i -1]:
            isNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))