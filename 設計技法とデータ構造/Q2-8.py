import pdb
from itertools import accumulate
from bisect import bisect_left

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 0.0000001):
        #print(ng, ok)
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ng

def is_ok(mid):
    cnt = 0
    for l in L: # 各紐を長さmidで割り，何本作れるかを計算
        cnt += l//mid # cntには作れる紐の本数を格納
    if cnt >= K: # cnt >= Kなら割る紐の長さを長くする
        return False
    else: # cnt < Kなら割る紐の長さを短くする
        return True

N, K = int_sp()
L = li_int_sp()
print(meguru_bisect(0, 10**5))
