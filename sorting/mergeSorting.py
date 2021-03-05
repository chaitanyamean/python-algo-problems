# merge Sort code

def mergeSort(array):
    if len(array) == 1:
       return array
    middleIdx = len(array) // 2
    leftSide = array[:middleIdx]
    rightSide = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftSide), mergeSort(rightSide))


def mergeSortedArrays(leftSide, rightSide):
    sortedArray = [None] * (len(leftSide) + len(rightSide))
    i = j = k = 0
    while i < len(leftSide) and j < len(rightSide):
        if leftSide[i] < rightSide[j]:
            sortedArray[k] = leftSide[i]
            i +=1
        else:
            sortedArray[k] = rightSide[j]
            j +=1
        k +=1
    while i < len(leftSide):
        sortedArray[k] = leftSide[i]
        i +=1
        k +=1
    while j < len(rightSide):
        sortedArray[k] = rightSide[j]
        j += 1
        k += 1
    return sortedArray
         
