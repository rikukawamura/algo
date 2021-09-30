import pdb

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, M = int_sp()
rel = [[] for _ in range(N)]
for _ in range(M):
    A, B = int_sp()
    rel[A].append(B)
#pdb.set_trace()
for i in rel:
    j = sorted(i)
    print(*j)
