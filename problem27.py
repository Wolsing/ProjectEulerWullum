
import math
def pent(below):
    listen = [ ((3*n**2)/2 - n/2) for n in range(1,below) ]
    return listen


def isPent(x):
    tester = (math.sqrt(24.0*float(x) + 1.0) + 1.0) / 6.0
    return tester == int(tester)


def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    else:
        return False

def prob44():

    flag = True

    i = 1

    # while loop
    while flag:
        for j in range(1, i):
            a = i*(3*i-1)/2
            b = j*(3*j-1)/2
            if is_pentagonal(a+b) and is_pentagonal(a-b):
                print a-b
                flag = False
                break
        i += 1

 
prob44()

