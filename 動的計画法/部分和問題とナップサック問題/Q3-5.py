def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
W = li_int_sp()
dp = [[float('INF')]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    #pdb.set_trace()
    for j in range(M+1):
        #pdb.set_trace()
        if dp[i][j] == -float('INF'):
            continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if 0 <= j+W[i] < M+1:
            dp[i+1][j+W[i]] = min(dp[i+1][j+W[i]], dp[i][j]+1)
print(dp[N][M] if dp[N][M] != float('INF') else -1)
