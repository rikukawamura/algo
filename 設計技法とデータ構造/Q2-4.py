def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
import bisect
N, M = int_sp()
A = sorted(li_int_sp())
B = li_int_sp()
len_A = len(A)
for b in B:
    print(bisect.bisect_right(A, b))