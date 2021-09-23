#-*- coding: UTF-8 -*- 
#置换密码P33
#@author : h3zh1
import math
def encode(initString , key):
    key_1 = []
    #处理秘钥
    for i in key :
        if i not in key_1:
            key_1.append(i)
    sort_key = sorted(key_1)
    dict_keys = []
    
    for i in key_1 :
        dict_keys.append(sort_key.index(i))
    key_len = len(dict_keys)    
    
    result = []
    #print(dict_keys)
    row = math.ceil(len(initString)/key_len)
    for i in range(key_len):
        new_res = [ '*' for i in range( row ) ]
        result.append(new_res)
    cnt = 0
    #赋值
    for i in range( row ):
        for j in range( key_len ):
            if cnt < len(initString):
                result[j][i] = initString[cnt]
                cnt+=1
    copy_result = []
    for i in range(key_len):
        new_res = [ '*' for i in range( math.ceil(len(initString)/key_len) ) ]
        copy_result.append(new_res)
    cnt = 0
    for i in dict_keys:
        copy_result[i] = result[cnt]
        cnt+=1
    result_str = ""
    for i in copy_result:
        result_str += (''.join(i) + " ")
        print(''.join(i))
    print("密文:"+result_str)
    
#要加密的字符串
#initString = "MING CHEN WU DIAN FA DONG FAN GONG".replace(" ","")
initString = input("请输入原文:").replace(" ","")
#秘钥Key # AHLNUY
#key = "YULANHUA" 
key = input("请输入秘钥(key):")
#去重
encode(initString,key)