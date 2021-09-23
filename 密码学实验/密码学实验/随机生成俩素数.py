import random

def isPrime( num ):
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0:
            return False
    return True

def isPrime2(a,b):
    #判断俩数是不是互素
    while a != 0:           
        a,b = b % a,a
    if b == 1:       
        return True
    else :
        return False

while True:
    p = random.randint(1,200)
    if isPrime(p):
        print("p = {0}".format(p),end = ' ')
        break
while True:
    q = random.randint(1,200)
    if isPrime(q) and p != q:
        print("q = {0}".format(q),end = ' ')
        break 
    
n = p * q 
un = (p - 1) * (q - 1)
while True:
    e = random.randint(2,un)
    if isPrime2(e,un):
        print("e = {0}".format(e))
        break
#便利
d = 2
while True:
    if (e * d) % un ==1:
        print("d = {0}".format(d))
        break
    else:
        d += 1 