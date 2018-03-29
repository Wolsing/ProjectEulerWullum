
def factorial1(x):
    produkt = 1
    n = x
    while n > 0:
        produkt *= n
        n = n - 1
    return produkt

def factorialDigits(x):
    sum = 0
    for i in str(x):
        sum = factorial1(int(i)) + sum
    return sum

def isEqualFactBelow(x):
    sum = 0
    while x > 2:
        if x == factorialDigits(x):
            sum += x
            print x
            x = x - 1
        else:
            x = x - 1
    return sum
    
print isEqualFactBelow(1000000)
