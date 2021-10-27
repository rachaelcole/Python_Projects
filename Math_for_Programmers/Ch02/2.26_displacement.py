from vectors import *
from vector_draw import *
from random import uniform

"""Let u = (1, 2). Another vector v = (n, m) such that n > m and has a distance of 
13 from u. What is the displacement from u to v?"""

for n in range(-12, 15):
    # Search for possible integer pairs (n, m) where n is within 13 units of 1 and
    # m is within 13 units of -1
    for m in range(-14, 13):
        if distance((n,m), (1, -1)) == 13 and n > m > 0:
            print((n, m))

"""The only result is (13, 4). It is 12 units to the right and 5 units up from (1, -1),
so the displacement is (12, 5)."""