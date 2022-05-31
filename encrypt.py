from random import randint
import gmpy2, numpy as np
from Crypto.Util.number import *

def enc(path,message):
    # 用列表来存放读取的公钥M
    Pk_list = []
    f = open(path,'r')
    for line in f.readlines():  ##readlines(),函数把所有的行都读取进来
        i = line.strip()
        Pk_list.append(int(i))
    # 把字符串转化为数字，再转化为二进制字符串
    m = bytes_to_long(bytes(message,encoding='utf-8'))
    m_bin = bin(m)[2:]
    # 填充，否则矩阵维数不同，不能相乘
    counter = 0
    while len(m_bin) < len(Pk_list):
        counter = counter+1
        m_bin = '0' + m_bin
    print(f'加密前明文二进制序列一共填充了{counter}个0')
    # 列表存二进制字符，方便做矩阵乘法
    bin_list = []
    for i in range(len(m_bin)):
        bin_list.append(int(i))

    return np.dot(Pk_list,bin_list)




