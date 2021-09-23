
def isPrime( num ):
    for i in range(2, int(num**0.5)+1 ) :
        if num % i == 0:
            return False
    return True
cnt = 0
for i in range(100,201):
    if isPrime(i):
        print(i,end=",")
        cnt +=1
print(cnt)