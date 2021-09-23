def maxfun(a,b):
    while a != 0:           
        a,b = b % a,a
    return b
print("55和85的最大公因数 = {} ".format( maxfun(55,85) ) )
print( "202和282的最大公因数 = {} ".format( maxfun(202,282 ) ) )