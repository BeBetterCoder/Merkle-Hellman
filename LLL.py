import copy
from sage.all import *

def max(a, b):
    return a if a > b else b

# LLL算法 可以视作是高斯约减算法在高维情况下的推广
def LLL_v0(M, delta=0.75):
    B = M
    Q, mu = B.gram_schmidt()
    n, k = B.nrows(), 1

    while k < n:

        # size reduction step
        for j in reversed(range(k)):
            if abs(mu[k][j]) > 0.5:
                B[k] = B[k] - round(mu[k][j]) * B[j]
                Q, mu = B.gram_schmidt()

        # swap step
        if Q[k].dot_product(Q[k]) >= (delta - mu[k][k - 1] ^ 2) * Q[k - 1].dot_product(Q[k - 1]):
            k = k + 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            Q, mu = B.gram_schmidt()
            k = max(k - 1, 1)

    return B

