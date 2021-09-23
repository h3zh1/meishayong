def fun(n):
    return (p-1)*(q-1)
def ggcd(a,b):
    while b:
        #print(a,b)
        a , b = b , a % b
    return a
        
p = 5
q = 13

n = p * q
nn = fun(n)
e , d = 0 , 0
                
#print(e,d,nn)

C = (88 ** e) % n
print(C)
M = (C ** d) % n
print(M)
