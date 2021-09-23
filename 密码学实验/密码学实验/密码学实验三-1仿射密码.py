import string

k1, k0, n = 3, 5, 26  # 默认值


def getIndex(i):
    global k1, k0, n
    index = ord(i) - ord('A')
    result = (index * k1 + k0) % 26
    return chr(result + ord('A'))


def encode(init_string, encode_dict):
    result = ""
    for i in init_string:
        if i == ' ':
            result += ' '
        else:
            result += encode_dict[i]
    return result


init_string = input("请输入原文:")
k0 = int(input("请输入K0的值:"))
k1 = int(input("请输入K1的值:"))
initString = string.ascii_uppercase
table = [getIndex(i) for i in initString]
# print(list(initString))
# print(table)
encode_dict = {}
for i in range(len(initString)):
    encode_dict[initString[i]] = table[i]

print("密文:" + encode(init_string, encode_dict))
