def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 0.0001):
        #pdb.set_trace()
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    #pdb.set_trace()
    return ok

def is_ok(x):
    if x*(x*(x+1)+2)+3 >= N:
        return True
    else:
        return False

import pdb
N = int(input())
x = meguru_bisect(0, 100)
print(x)