
##  find if the point is inside circle or not
import math

(Cx, Cy, r) = input().split()

(Px, Py) = input().split()

Cx = float(Cx)
Cy = float(Cy)
r = float(r)
Px = float(Px)
Py = float(Py)

d = math.sqrt((Cx - Px) ** 2 + (Cy - Py) ** 2)

if d < r:
    print('Point is inside Circle')
else:
    print('Point is outside circle')