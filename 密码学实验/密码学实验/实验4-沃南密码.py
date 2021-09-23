# -*- coding: utf-8 -*-
#author@h3zh1
def Encode_key( key , init_str ):
    length_of_str = len(init_str)
    shang = length_of_str // len(key)
    yu = length_of_str % len(key)
    return key * shang + key[:yu]
def Encode( init_str , key ):
    result = ""
    for i in range(len(init_str)):
        result += chr( ord(init_str[i])^ord(init_key[i]) )
    return result
def sayBinary(result):
    bin_result = ""
    for i in result:
        bin_result += bin(ord(i)).replace("0b","").zfill(7) + " "
    return bin_result
init_str = input("请输入密文:")
init_key = input("请输入秘钥:")
final_key = Encode_key(init_key,init_str)
result = Encode(init_str , final_key)
print("密文:" + sayBinary(result) )