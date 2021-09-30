import pdb
from bisect import bisect_left

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, M = int_sp()
A = li_int_sp()
B = li_int_sp()
A = sorted(A, reverse=True)
B = sorted(B, reverse=False)
#pdb.set_trace()

cnt = 0
for a in A:
    del_ind = bisect_left(B, a)
    try:
        del B[del_ind]
        cnt += 1
    except IndexError:
        continue
print(cnt)