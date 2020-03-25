import math

def linear(b,c):
    if b == 0:
        return 0
    else:
        return 1

def squarer(a,b,c):
    D = b ** 2 - (4 * a * c) 
    if D > 0 :
        return 2 
    elif D == 0:
        return 1 
    else:
        return 0 

def solver(a,b,c):
    if a == 0:
        return linear(b,c)
    else: 
        return squarer(a,b,c) 


