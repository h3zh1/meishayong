import string
table = []

def encode(initString):
    res = [ ' ' if i==' ' else chr(( (ord(i)-ord('A'))*k)%n+ord('A')) for i in initString ]    
    print("加密:" + (''.join(res)) )    

def decode(initString):
    value_list = [ chr(( (ord(i)-ord('A'))*k)%n+ord('A')) for i in string.ascii_uppercase ]
    key_list = [ i for i in string.ascii_uppercase]
    dict_str = {}
    print(value_list)
    print(key_list)
    for i in range(len(value_list)):
        dict_str[value_list[i]] = key_list[i]
    res = ""
    for i in initString:
        if i==' ':
           res+=' '
        else :
            res+=dict_str[i] 
    print("解密:"+res)
    
k,n = 2,26
choice = input("加密:1 解密:2 >>> :")
initString = input("原文/密文:")
k = int(input("偏移位数:"))
k = k%n
if choice == '1':
    encode(initString)
elif choice =='2':
    decode(initString)
else :
    print("选项有误")
