import math

def binarySearch(arr,x,startingPoint,endingpoint):
    low = 0
    high = len(arr) - 1
    while (low<=high):
        m = math.floor((low+high)/2)
        if x < arr[m]:
            high = m - 1
        if x > arr[m]:
            low = m + 1
        if x == arr[m]:
            return 'Element found'
    return 'Not found'

arr = [20,30,40,50,60,70]
print(binarySearch(arr, 70))


# Binary search only works on sorted Arrays
# Binary search will not work on linked list

