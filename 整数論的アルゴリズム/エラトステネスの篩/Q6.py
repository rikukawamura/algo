def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    pdb.set_trace()
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0] # pの倍数を削ぎ落とす

import pdb
import math

A, B = int_sp()
prime = [True] * (B+1)
prime[0], prime[1] = False, False
sqrt_B = math.sqrt(B)

for i in range(2, int(sqrt_B)+1):
    if prime[i]:
        for j in range(i+i, B, i):
            prime[j] = False

#pdb.set_trace()
print(sum(prime[A:B+1]))