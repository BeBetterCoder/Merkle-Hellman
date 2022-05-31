import gmpy2, numpy as np
from random import randint

# 获得Merkle-Hellman的密钥,M为公钥,A,B,r为私钥
def getkey(nbits,low_bound,high_bound):
    # 确定序列r的第一个值的范围
    r = [randint(low_bound, high_bound)]

    for x in range(nbits - 1):
        r.append(randint(2 * r[-1], 3 * r[-1]))
    # 生成私钥A,B,B > 2rn
    while True:
        B = randint(2 * r[-1] + 1, 3 * r[-1])
        A = randint(2 * r[-1] + 1, 3 * r[-1])

        if gmpy2.gcd(A, B) == 1:
            break

    # print(f'A = {A}, B = {B}')
    # print(f'r = {r}')

    M = [A * x % B for x in r]
    # print(f'M = {M}')
    # 写入公钥信息
    f1 = open("Pk.txt",'w')
    for i in range(nbits-1):
        f1.write(str(M[i])+"\n")
    # 写入私钥信息
    f2 = open("Sk.txt",'w')
    f2.write(str(A)+'\n')
    f2.write(str(B)+'\n')
    for i in range(nbits-1):
        f2.write(str(r[i])+"\n")

if __name__ == '__main__':
    getkey(100,50,100)