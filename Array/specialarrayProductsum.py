'''Given a special non-empty array of integers, find the product of sum
'''

def productArray(arr, multiplier = 1):
    sum = 0
    for i in arr:
        if type(i) is list:
            sum += productArray(i, multiplier + 1)
        else:
            sum += i
    return sum * multiplier
