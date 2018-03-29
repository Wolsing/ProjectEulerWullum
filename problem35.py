import math
def primes_less_than(n):
    printliste = []
    bools = [True for x in range(1, n+1)]

    for i in range(2, int(math.floor(math.sqrt(n)))):
        if bools[i] == True:
            j = i**2
            p = 0
            while j+p*i < n:
                bools[j+p*i] = False
                p += 1
    for i in range(2, len(bools)):
        if bools[i] == True:
            printliste.append(i)
    return printliste


def numberToList(x):
    listen = []
    for i in str(x):
        listen.append(int(i))
    return listen


def listToNumber(x):
    s = ''.join(map(str, x))
    return int(s)


def rotate_number(x):
    listen = numberToList(x)
    samletRoteret = []
    n = 0
    while n < len(listen):
        t = listen[0]
        del listen[0]
        listen.append(t)
        samletRoteret.append(listToNumber(listen))
        n += 1 
    return samletRoteret


def cyclicPrimesBelow(x):
    antal = []
    primtal = primes_less_than(x)
    for i in primtal:
        listen = rotate_number(i)
        if all(j in primtal for j in listen) == True:
            antal.append(i)
    return antal, len(antal)
         
print cyclicPrimesBelow(1000000)