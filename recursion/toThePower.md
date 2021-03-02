
`To the power Problem`

import math

def powerRec(a,b):
    if b == 1:
      return a
    if b % 2 == 0:
       tmp = powerRec(a, b/2)
       return tmp * tmp
    else:
        tmp = powerRec(a, math.floor(b/2))
        return tmp * tmp * a

print(powerRec(2,5))