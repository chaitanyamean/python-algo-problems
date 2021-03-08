

## Recursive method  time complexity is O(2^n) and space is O(1)

def fibonacciRecursive(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


fibonacciRecursive(5)


# dynamic programming using memoization 

def fibonacciDP(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n +1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]

print(fibonacciDP(8))