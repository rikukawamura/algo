import pdb

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

N, A, B = int_sp()
S = [input() for _ in range(N)]
#pdb.set_trace()
if S[A][B] == 'o':
    print('Yes')
else:
    print('No')