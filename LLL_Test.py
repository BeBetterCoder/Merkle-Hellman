from base64 import *
from Crypto.Util.number import *
from sage.all import *

def test():
    M = [816358673, 214551389, 683509053, 377954927, 461648693, 819009687, 833612683, 246393449, 258952137, 592274653, 439857687, 164289531, 138621939, 626982035, 733582939, 561376076, 206910526, 470721180, 1105393379, 848577580]
    msg = [1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0]

    S = 6545130222
    s = ''
    for i in msg:
        s = s+str(i)
    print(f"This is bin of plaintext:{s}")
    m = int(s,2)
    print(f'This base32 of plaintext:{b32encode(long_to_bytes(m))}')

    n = len(M)
    L = matrix.zero(n + 1)

    for row, x in enumerate(M):
        L[row, row] = 2
        L[row, -1] = x

    L[-1, :] = 1
    L[-1, -1] = S

    res = L.LLL()
    print("This is the matrix after LLL:")
    print(res)
    vec = res[0]
    result = ''
    for i in vec:
        result = result + str(((-1)*i+1)//2)
    print(f'This is the shortest vector we found:{result[:-1]}')
    print("This is the platetext we found:")
    print(b32encode(long_to_bytes(int(result[:-1],2))))
    if b32encode(long_to_bytes(m)) == b32encode(long_to_bytes(int(result[:-1],2))):
        print("LLL attacks successfully!")
