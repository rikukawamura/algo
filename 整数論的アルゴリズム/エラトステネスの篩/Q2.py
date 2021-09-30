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
cards = [True] * 101
cards[0], cards[1] = False, False
primes = get_sieve_of_eratosthenes(100)
# 素数（合成数以外)をfalseとする
for i in primes:
    cards[i] = False
# 2と3の倍数をfalseとする
for p in range(2, 6):
    for q in range(p, 101, p):
        cards[q] = False

print(sum(cards))
