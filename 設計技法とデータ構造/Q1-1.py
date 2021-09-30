def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
coins = [5, 1]
maisu = 0
tmp = 0
for coin in coins:
    tmp += N//coin
    maisu += N//coin
    N -= coin*tmp
    tmp = 0
print(maisu)