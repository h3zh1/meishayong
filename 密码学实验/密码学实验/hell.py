import libnum
#64位密钥
secret_key = 'mml_good'
### 置换选择1
### 返回c1和d1合并的56位结果用于进行后续的置换选择生成密钥
def exchange1(key):
    #将密钥转成64个二进制位
    bin_rlt = ''
    for i in key:
        bin_rlt+= (8-len(bin(ord(i))[2:]))*'0'+bin(ord(i))[2:]
    #print(bin_rlt)
    #c0矩阵
    c0 = [[57,49,41,33,25,17,9],
    [1,58,50,42,34,26,18],
    [10,2,59,51,43,35,27],
    [19,11,3,60,52,44,36]]
    #d0矩阵
    d0 = [[63,55,47,39,31,23,15],
    [7,62,54,46,38,30,22],
    [14,6,61,53,45,37,29],
    [21,13,5,28,20,12,4]]
    #生成c0的密钥
    c0_key = ''
    for row in range(len(c0)):
        for column in range(len(c0[0])):
            c0_key += bin_rlt[c0[row][column]-1]
    #c0_key = c0_key[1:]+c0_key[0]
    #生成d0的密钥
    d0_key = ''
    for row in range(len(d0)):
        for column in range(len(d0[0])):
            d0_key += bin_rlt[d0[row][column]-1]
    #d0_key = d0_key[1:]+d0_key[0]
    return c0_key+d0_key
#
def exchange2(key,x):
    #print(len(key))
    key1 = key[0:28]
    key2 = key[28:]
    key1 = key1[x:]+key1[0:x]
    key2 = key2[x:]+key2[0:x]
    key = key1+key2
    ex2 = [
        [14,17,11,24,1,5],
        [3,28,15,6,21,10],
        [23,19,12,4,26,8],
        [16,7,27,20,13,2],
        [41,52,31,37,47,55],
        [30,40,51,45,33,48],
        [44,49,39,56,34,53],
        [46,42,50,36,29,32]
    ]
    rlt = ''
    for i in range(8):
        for j in range(6):
            #print(ex2[i][j]-1)
            rlt+=key[ex2[i][j]-1]
    #print(rlt)
    return (key,rlt)
    
def exchange_ip(ming):
    ip = [
        [58,50,42,34,26,18,10,2],
        [60,52,44,36,28,20,12,4],
        [62,54,46,38,30,22,14,6],
        [64,56,48,40,32,24,16,8],
        [57,49,41,33,25,17,9,1],
        [59,51,43,35,27,19,11,3],
        [61,53,45,37,29,21,13,5],
        [63,55,47,39,31,23,15,7]
    ]
    rlt = ''
    for i in range(8):
        for j in range(8):
            rlt += ming[ip[i][j]-1]
    return rlt
def xuanze(key):
    E = [
        [32,1,2,3,4,5],
        [4,5,6,7,8,9],
        [8,9,10,11,12,13],
        [12,13,14,15,16,17],
        [16,17,18,19,20,21],
        [20,21,22,23,24,25],
        [24,25,26,27,28,29],
        [28,29,30,31,32,1]
    ]
    rlt = ''
    for i in range(8):
        for j in range(6):
            rlt+=key[E[i][j]-1]
    return rlt
class s_table():
    def __init__(self):
        self.s = [0]*8
        self.s[0] = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
        ]
        self.s[1] = [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
        ]
        self.s[2] = [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
        ]
        self.s[3] = [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
        ]
        self.s[4] = [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        ]
        self.s[5] = [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
        ]
        self.s[6] = [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
        ]
        self.s[7] = [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
        ]
def atob(key):
    bin_rlt = ''
    for i in key:
        bin_rlt+= (8-len(bin(ord(i))[2:]))*'0'+bin(ord(i))[2:]
    return bin_rlt
def xor(k1,k2):
    rlt = ''
    for i in range(len(k1)):
        rlt += str(int(k1[i])^int(k2[i]))
    return rlt
def s_box(key):
    s_t = s_table()
    s = []
    for i in range(8):
        s.append(key[i*6:i*6+6])
    rlt = ''
    for i in range(8):
        x = int(s[i][0]+s[i][5],2)
        y = int(s[i][1]+s[i][2]+s[i][3]+s[i][4],2)
        rlt+= (4-len(bin(s_t.s[i][x][y])[2:]))*'0'+bin(s_t.s[i][x][y])[2:]
    return rlt
def P_process(key):
    p = [
        [16,7,20,21],
        [29,12,28,17],
        [1,15,23,26],
        [5,18,31,10],
        [2,8,24,14],
        [32,27,3,9],
        [19,13,30,6],
        [22,11,4,25]
    ]
    rlt = ''
    for i in range(8):
        for j in range(4):
            rlt+=key[p[i][j]-1]
    return rlt
def IP_minus(key):
    ip = [
        [40,8,48,16,56,24,64,32],
        [39,7,47,15,55,23,63,31],
        [38,6,46,14,54,22,62,30],
        [37,5,45,13,53,21,61,29],
        [36,4,44,12,52,20,60,28],
        [35,3,43,11,51,19,59,27],
        [34,2,42,10,50,18,58,26],
        [33,1,41,9,49,17,57,25]
    ]
    rlt = ''
    for i in range(8):
        for j in range(8):
            rlt += key[ip[i][j]-1]
    return rlt
def encrypt(ming_or_key,flag):
    ming = ming_or_key
    #生成S盒
    S = s_table()
    #初始置换IP
    if flag==1:
        ming = exchange_ip(atob(ming))
    else:
        ming = exchange_ip(ming)
    print('初始置换IP的结果为：')
    print(ming)
    #划分l0和r0
    l0 = ming[0:32]
    r0 = ming[32:]
    #生成密钥环节
    #置换选择1
    key = exchange1(secret_key)
    #print(key)
    #左移位数
    move = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    #密钥存储用的列表
    ki = []
    #置换选择2
    for i in range(16):
        key,mk = exchange2(key,move[i])
        ki.append(mk)
    #ki是16组密钥
    #16轮加密开始
    start = 0
    ends = 16
    step = 1
    if flag!=1:
        start = 15
        ends = -1
        step = -step
    count = 1
    for i in range(start,ends,step):
        tmp = r0
        #选择运算
        r0 = xuanze(r0)
        #抑或运算
        r = xor(r0,ki[i])
        
        print('第'+str(count)+'轮加解密密钥为：'+ki[i])
        #经过S盒处理
        r = s_box(r)
        print('第'+str(count)+'轮加解密的S盒输出结果：'+r)
        #P置换
        r = P_process(r)
        r = xor(r,l0)
        print('第'+str(count)+'轮加解密的加密函数输出结果：'+r)
        r0 = r
        l0 = tmp
        count+=1
    #IP逆置换
    rlt = IP_minus(r0+l0)
    return rlt
if __name__=='__main__':
    c = input('加密请输入1，解密请输入2，退出输入3:')
    while c!='3':
        if c=='1':
            key = input('请输入8位的明文：')
            #二进制形式显示
            #参数中的1表示加密，2表示解密，会影响密钥的使用
            print('加密后的结果为：'+encrypt(key,1))
        elif c=='2':
            key = input('请输入密文：')
            print('解密后的结果为：'+libnum.n2s(int(encrypt(key,0),2)))
        else:
            break
        c = input('加密请输入1，解密请输入2，退出输入3:')
    