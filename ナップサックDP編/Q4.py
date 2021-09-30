def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
A = li_int_sp()
mod = 10**3
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    #pdb.set_trace()
    for j in range(M+1):
            if dp[i][j] == 0:
                continue
            dp[i+1][j] += dp[i][j]
            if 0<= j+A[i] < M+1:
                dp[i+1][j+A[i]] += dp[i][j]
#pdb.set_trace()
print(dp[N][M]%mod)