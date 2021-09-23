import string

n = 26


def process_key(key, length):
    """处理密钥和原文同长"""
    key_len = len(key)
    if key_len == length:
        return key
    else:
        shang = length // key_len
        yu = length % key_len
        final_key = shang * key + key[0:yu]
        return final_key


def encode_first(i, init_string, final_key):
    """类凯撒加密"""
    global n
    num = (ord(init_string[i]) + ord(final_key[i]) -
           2 * ord('A')) % n + ord('A')
    return chr(num)


def encode_final(init_string, final_key):
    """不知道写点啥"""
    result = [
        encode_first(i, init_string, final_key)
        for i in range(len(init_string))
    ]
    return ''.join(result)


s = input("输入明文:").replace(" ", "")
key = input("输入密钥:").replace(" ", "")
final_key = process_key(key, len(s))
print(final_key)
result = encode_final(s, final_key)
print("密文为 : {0}".format(result))