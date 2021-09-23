
def Encode(str1 , num):
    result = ""
    str1 = str1[::-1]
    #print(str1)
    for i in range(0,len(str1),num):
        result += str1[i:i+num] + " "
        #print(result)
    return result 
#str1 = input("请输入明文:")
#NUM = int(input("请输入组数:"))
NUM = 5
str1 = "MING CHEN WU DIAN FA DONG FAN GONG"
str1 = str1.replace(" ","")
res = Encode(str1 , NUM)
print(res)
print("是否是对合运算:" + str(str1 == Encode( Encode(str1 ,NUM),NUM)) )