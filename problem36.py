
def getBinary(x):
    s = str(bin(x))
    newStr = s.replace("0b","")
    return newStr

def palindromicInBasesLessThan(x):
    listen = []
    for i in range(0, x + 1):
        if ((str(i)[::-1] == str(i)) and (getBinary(i)[::-1] == getBinary(i))):
            listen.append(i)
    return listen, sum(listen), len(listen)

print palindromicInBasesLessThan(1000000)

### genius code fundet på PE forum problem 36 ###
def int2bin(x): 
    d = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'} 
    return ''.join([d[int(dig)] for dig in oct(x)]).lstrip("0") 
    
print sum([i for i in range(1,1000000) if int2bin(i)==int2bin(i)[::-1] and str(i)==str(i)[::-1]])

