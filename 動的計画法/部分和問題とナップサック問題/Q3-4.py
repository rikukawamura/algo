def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
W = li_int_sp()
V = li_int_sp()
dp = [[-1]* (M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    #pdb.set_trace()
    for j in range(M):
        #pdb.set_trace()
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if 0 <= j+W[i] < M+1:
            dp[i+1][j+W[i]] = max(dp[i+1][j+W[i]], dp[i][j]+V[i])
#pdb.set_trace()
max_val = -float('INF')
for i in dp:
    max_val = max(max_val, max(i))
print(max_val)
