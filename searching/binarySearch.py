import math

def binarySearch(arr,x,startingPoint,endingpoint):
    l = startingPoint
    r = endingpoint
    while (l<r):
        m = math.floor((l+r)/2)
        if x < arr[m]:
            r = m - 1
        if x > arr[m]:
            l = m + 1
        if x == arr[m]:
            return 'Element found'
    return 'Not found'

arr = [20,30,40,50,60,70]
print(binarySearch(arr, 70, 1, len(arr)) )
