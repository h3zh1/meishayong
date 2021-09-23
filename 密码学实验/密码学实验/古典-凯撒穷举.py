import string


def encode(initString , k):
    n = 26
    res = [chr((ord(i) - ord('A') + k) % n + ord('A')) for i in initString]
    return ''.join(res)


initString = input("原文/密文:")
print("穷举结果如下:")
for i in range(0,26):
    print("k={} : ".format(i)  + encode(initString,i) )
