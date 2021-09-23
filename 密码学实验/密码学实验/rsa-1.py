def fun(n):
    return (p-1)*(q-1)
def ggcd(a,b):
    while b:
        #print(a,b)
        a , b = b , a % b
    return a
def encode(Mstr , e , n):
    return (Mstr ** e) % n

def decode(Cstr , de , n):
    return (Cstr ** de) % n

p = 17
q = 11
n = p * q
nn = fun(n)
e = 7
m = 88
C = encode(m,e,n)
print(C)