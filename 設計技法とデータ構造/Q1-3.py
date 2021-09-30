def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
coins = [50, 10, 5, 1]
A = li_int_sp()
maisu = 0
tmp = 0
for coin, limit in zip(coins, A):
    #pdb.set_trace()
    if N >= coin:
        tmp += N//coin
        if tmp <= limit:
            maisu += tmp
            N -= coin*tmp
        else:
            maisu += limit
            N -= coin * limit
        tmp = 0
print(maisu)