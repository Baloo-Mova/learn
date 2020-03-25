import math

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        print(0)
    else:
        print(1)
else: 
    D = b ** 2 - (4 * a * c) 
    if D > 0 :
         print(2)

    elif D == 0:
        print(1)

    else:
        print(0) 