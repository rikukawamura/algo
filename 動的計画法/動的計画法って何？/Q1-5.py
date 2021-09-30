def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
A = li_int_sp()
dp = [float('INF')]*N
dp[0] = 0
#pdb.set_trace()
for i in range(1, N):
    for j in range(1, M+1):
        if i-j < 0:
            break
        dp[i] = min(dp[i], dp[i-j]+j*A[i])
print(dp[N-1])