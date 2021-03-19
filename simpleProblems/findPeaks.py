A = [11,3,4,5,7,6,4,5,10,15]

# checking first element
if A[0] >= A[1]:
  print(A[0])

# checking all middle elements excluding first and last
for i in range(1, len(A) - 1):
  if(A[i] >= A[i+1]) and (A[i] >= A[i-1]):
    print(A[i])

# checking last element
if A[len(A)-1] >= A[len(A)-2]:
  print(A[len(A)-1])