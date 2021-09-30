def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
D = sorted(li_int_sp())
dp = [0]*(N+1)
dp[0] = 1
for i in range(2, N+1):
    for j in D:
        if i-j < 0:
            break
        dp[i] += dp[i-j]
#pdb.set_trace()
if dp[-1] != 0:
    print('Yes')
else:
    print('No')
