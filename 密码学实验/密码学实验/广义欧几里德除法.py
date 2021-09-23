def ojldfun ( a , b ):
    if (b == 0):
        return 1, 0, a
    else:
         x1 , y1 , q = ojldfun( b , a % b ) 
         x , y = y1, ( x1 - (a // b) * y1 )
    return x, y, q

a = 2947
b = 3772

s , t , q = ojldfun(a,b)

print( "s = {}, t = {}".format(s,t) )
print( "{} * {} + {} * {} = ({},{})".format(s,a,t,b,a,b) )