import random
def qfun( a, b,mod ):
    res = 1
    while b !=0 :
        if (b&1) !=0 :
            res= (res % mod * a) % mod
        a=(a % mod ) * a % mod
        b>>=1
    return res

def query_prime(x):
    if x==2 :
        return True;
    if x==1 :
        return False;
    for i in range(1,30):
        base= random.randint(0,0x7fff) % (x-1) + 1
        if qfun(base,x-1,x)!=1 :
            return False
    return True

for i in range(1000, 10000):
    if query_prime(i) == True :
        print(i)
        break