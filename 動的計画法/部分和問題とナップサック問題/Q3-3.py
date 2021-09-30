def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
A = li_int_sp()
B = li_int_sp()
dp = [[-1]* M for _ in range(N)]
dp[0][0] = 0
for i in range(N-1):
    #pdb.set_trace()
    for j in range(M):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if 0 <= j+A[i] < M:
            dp[i+1][j+A[i]] = max(dp[i+1][j+A[i]], dp[i][j]+B[i])

print(dp[N-1][M-1])
