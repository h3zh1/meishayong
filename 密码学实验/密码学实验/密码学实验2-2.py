import string


def encode(initString):
    res = [chr((ord(i) - ord('A') + k) % n + ord('A')) for i in initString]
    print("加密:" + ''.join(res))


def decode(initString):
    res = [chr((ord(i) - ord('A') + n - k) % n + ord('A')) for i in initString]
    print("解密:" + ''.join(res))


k, n = 2, 26
choice = input("加密:1 解密:2 >>> :")
initString = input("原文/密文:")
k = int(input("偏移位数:"))
k = k % n
if choice == '1':
    encode(initString)
elif choice == '2':
    decode(initString)
else:
    print("选项有误")
