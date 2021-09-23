p = 47
q = 71
e = 79
n = p * q
un = (p - 1) * (q - 1)
for d in range(10000):
    if (e * d) % un == 1:
        print("d = {0}".format(d))
        break