from get_key import getkey
from encrypt import enc
from Crypto.Util.number import *
import base64
from LLL_Test import test

def menu():
    hello = '''This my Merkle-Hellman system,
now you can input numbers to choose functions:
1.get keys
2.encode message
3.LLL break cipher
4.exit\n'''
    print(hello)
    while True:
        choose = input('choose>')
        if choose == '1':
            n,low,high = input('Please input nbits,low_bound,high_bound:').split()
            getkey(int(n),int(low),int(high))
            print('Keys are ready!')

        elif choose == '2':
            path = input("Please input the path of public keys:")
            message = input("Please input your plaintext:")
            c = enc(path,message)
            c_b32 = base64.b32encode(long_to_bytes(c))
            print(f'This is the ciphertext:{c_b32}')
        elif choose == '3':
            test()
        elif choose == '4':
            print('Bye!')
            return 0
        else:
            print('Please input 1-4!')


if __name__ == '__main__':
    menu()