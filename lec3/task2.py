import math

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        print("")
    else:
        x = -c/b
        print("X1: %.2f"%x)
else: 
    D = b ** 2 - (4 * a * c) 
    if D > 0 :
        x1 = (-b + math.sqrt(D)) / 2*a
        x2 = (-b - math.sqrt(D)) / 2*a
        if x1>x2:
            print("X1: %.2f"%x1)
            print("X2: %.2f"%x2) 
        else:
            print("X1: %.2f"%x2)
            print("X2: %.2f"%x1) 

    elif D == 0:
        x = -b / (2*a)
        print("X1: %.2f"%x) 

    else:
        print("") 