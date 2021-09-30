def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
N, M, K = int_sp()
A = li_int_sp()
INF = float('INF')
dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 0
#pdb.set_trace()
for i in range(N):
    #pdb.set_trace()
    for j in range(M+1):
            if dp[i][j] == INF:
                continue
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j+A[i] <= M:
                dp[i+1][j+A[i]] = min(dp[i+1][j+A[i]], dp[i][j]+1)
#pdb.set_trace()
if dp[N][M] <= K:
    print('Yes')
else:
    print('No')