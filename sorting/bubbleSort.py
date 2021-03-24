def bubbleSort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1- counter):
            if arr[i] > arr[i+1]:
                swap(i, i+1, arr)
                isSorted = False
        counter += 1
    return arr

def swap(i,j,arr):
    arr[i], arr[j] = arr[j], arr[i]



#     def bubbleSort(array):
#     # Write your code here.
#     isSorted = False
# 	counter = 0
# 	while not isSorted:
# 		isSorted = True
# 		for i in range(len(array) - 1 - counter):
# 			if array[i] > array[i+1]:
# 				swap(i,i+1,array)
# 				isSorted = False
# 		counter += 1
# 	return array

# def swap(i,j,array):
# 	array[i], array[j] = array[j], array[i]