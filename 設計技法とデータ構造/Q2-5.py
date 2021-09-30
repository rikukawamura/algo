import pdb
from bisect import bisect_left

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, K = int_sp()
A = sorted(li_int_sp())
len_A = len(A)
total = 0
for a in A:
    thr = K-a
    ind = bisect_left(A, thr)
    #pdb.set_trace()
    total += len(A)-ind
print(total)

