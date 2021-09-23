# -*- coding: utf-8 -*-
"""
This is h3zh1's DES encryption program
"""
import libnum
#s盒
s = [0]*8
s[0] = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
]
s[1] = [
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
]
s[2] = [
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
]
s[3] = [
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
]
s[4] = [
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
]
s[5] = [
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
]
s[6] = [
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
]
s[7] = [
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
#p盒
p = [
      16,7,20,21,
      29,12,28,17,
      1,15,23,26,
      5,18,31,10,
      2,8,24,14,
      32,27,3,9,
      19,13,30,6,
      22,11,4,25 ]
    
#初始置换表
ip_table = [
            58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            64,56,48,40,32,24,16,8,
            57,49,41,33,25,17, 9,1,
            59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7  ]

reverse_ip_table = [
            40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41, 9,49,17,57,25 ]

secret_key = "hrr_jkpa"
Ming = "12345678"

#一个没什么用的函数
def addSpace(A , num): 
    AA , result = [str(i) for i in A] , ""
    for i in range(0 , len(AA) , num ) :
        result += ''.join(AA[i:i+num]) + " "
    return result

def text2bin( text ) :
    # 字符串转2进制
    init_list = []
    for i in text : 
        i2bin = bin(ord(i)).replace("0b","").zfill(8)
        for j in i2bin : 
            init_list.append( int(j) )
    return init_list

def init_change( Ming_list , ip_table):
    # 明文的初始置换
    af_1st_change = []
    iptablen = len( ip_table )
    for i in range( 0 , iptablen ) : 
        af_1st_change.append( Ming_list[ ip_table[i]-1 ] )
    return af_1st_change

#E置换
def E( R ) :
    #print(R)
    E_table = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1 ]
    RE = []
    for i in range( 0 , len(E_table) ):
        RE.append( R[ E_table[i]-1 ] )
    #print(str(RE))
    return RE

def fun_key() :#chansheng
    #pc-1置换
    c0_table = [
        57,49,41,33,25,17,9,
        1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,
        19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,
        7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,
        21,13,5,28,20,12,4 ]
    #得到密钥的2进制表
    #key2bin_list = text2bin( secret_key )
    key2bin_list = [int(i) for i in secret_key]
    # 56位bin
    key_ch = [] 
    for i in range( len(c0_table) ) : 
        key_ch.append( key2bin_list[ c0_table[i]-1 ])
    #print( key_ch )
    c , d , k = [0] * 17 , [0] * 17 , [0] * 17
    c[0] , d[0] = key_ch[:28] , key_ch[28:]
    #移位表记录16个移位的位数
    move = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    #用于获取Kn的置换表
    k_table = [ 14,17,11,24,1,5,
                3,28,15,6,21,10,
                23,19,12,4,26,8,
                16,7,27,20,13,2,
                41,52,31,37,47,55,
                30,40,51,45,33,48,
                44,49,39,56,34,53,
                46,42,50,36,29,32 ]
    #获取16个C和D
    for i in range( 0 , 16 ) :
        mv = move[i]
        c[i+1] , d[i+1] = (c[i][mv:] + c[i][:mv]) , (d[i][mv:] + d[i][:mv])
        kk = c[i+1] + d[i+1]
        #置换
        k[i+1] = []
        for j in range( 0 , len(k_table) ) : 
            k[i+1].append( kk[ k_table[j]-1 ] )    
    return k  

#列表异或
def xor(astr , bstr):
    result = []
    for i in range( 0 , len(astr)):
        xx = int(astr[i]) ^ int(bstr[i])
        result.append( xx )
    return result

# f函数 == > f(R[n-1] , K[n])    
def ff( R , K , time) : 
    #扩展
    RR = E(R)
    #异或
    arr = xor( K,RR )
    #8次S盒
    result = []
    for i in range(0,8) : 
        base = i * 6
        indexr = str(arr[base])+str(arr[base+5])
        indexc = str(arr[base+1])+str(arr[base+2])+str(arr[base+3])+str(arr[base+4])
        row = int(indexr,2) 
        col = int(indexc,2) 
        #在s盒取值
        snum = s[i][row][col]
        grp = [ int(j) for j in bin(snum).replace("0b","").zfill(4) ]
        result += grp
    #p盒
    speak = [str(j) for j in result]
    time = str(time).zfill(2)
    after_p = []
    for j in range(0 , len(p) ):
        after_p.append( result[p[j]-1] )
        #print(grp)
    print( "s[{}] = ".format(time) + addSpace(result , 4) ) 
    print( "p[{}] = ".format(time) + addSpace(after_p , 4) )
    return after_p
        
def Encode( text , key , flag ) : 
    global Ming , secret_key
    Ming = text
    secret_key = key 
    if flag == 1 :  #转二进制  
        #init_list = text2bin( Ming )
        init_list = [int(i) for i in Ming]
    else : 
        init_list = [int(i) for i in Ming]
    #初始置换
    #print(init_list)
    after_change = init_change(init_list , ip_table)
    L , R = [0] * 17 , [0] * 17  
    R[0] , L[0] = [ int(i) for i in after_change[32:] ] ,[ int(i) for i in after_change[:32] ]
    
    KSet = fun_key()
    for i in range( 1 , 17 ) : 
        L[i] = R[i-1] # 用上一轮
        #根据加密解密来规定秘钥次序
        k_index = i if flag == 1 else 17 - i
        #求R[i]
        R[i] = xor( L[i-1] , ff( R[i-1] , KSet[k_index] , i) ) 
    R16L16 = R[16] + L[16]
    end_list = []
    for i in range(0, len(reverse_ip_table) ) :
        end_list.append( R16L16[ reverse_ip_table[i]-1 ] )
    res = [str(i) for i in end_list]
    return ''.join(res)

if __name__=='__main__':
    
    choice = int(input('加密:1 解密:2 退出3 :'))
    ming_str = input("请输入明文/密文:")
    key_str = input("请输入秘钥:")
    if choice == 1 : 
        jiami =  Encode( ming_str,key_str,choice) 
        print("加密结果:"+jiami)
    elif choice == 2 :
        #jiemi = libnum.n2s(int(Encode(ming_str,key_str,-choice),2)).decode()
        jiemi = Encode(ming_str,key_str,-choice)
        print("解密结果:"+jiemi)
    else:
        pass
    #print(secret_key)
    #print(Ming)
    print("程序已退出……")
    
