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
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok(day):
    if (day*(1+day))//2 >= x:
        return True
    else:
        return False

N = int(input())
X = li_int_sp()
for x in X:
    print(meguru_bisect(0, 10**18))
