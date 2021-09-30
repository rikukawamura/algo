def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
A = li_int_sp()
dp = [[False]*M for _ in range(N)]
dp[0][0] = True
for i in range(N):
    #pdb.set_trace()
    for j in range(M):
        if 0 <= i-1 < N:
            if dp[i-1][j] == True:
                dp[i][j] = True

        if 0 <= i-1 < N and 0 <= j-A[i-1] < M:
            if dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
print(sum(dp[N-1]))
