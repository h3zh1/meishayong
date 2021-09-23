import math
"""
MINGCH
ENWUDI
ANFADO
NGFANG
ONG***
"""
def Encode2(str1 , num):
    str1 = str1.replace(" ","")
    #print(len(str1))
    l = []
    m = math.ceil( len(str1)/num )
    n = num
    for i in range(0 , m ):
        result = ""
        for j in range( 0, n ):
            if( i+j*m < len(str1) ):
                result += str1[ i + j * m ]
            else :
                result += "$"
        result + " "
        l.append(result)
    #for i in l:
    #    print(i)
    return ' '.join(l)
NUM = 5
str1 = "MING CHEN WU DIAN FA DONG FAN GONG"
#str1 = input("请输入明文:")
#NUM = int(input("请输入行数:"))
res = Encode2(str1 ,NUM)
print("密文:"+res)
print("是否对合运算:" + str(str1 == Encode2( Encode2(str1 ,NUM),NUM)) )
