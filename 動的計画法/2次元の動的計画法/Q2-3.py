def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = [li_int_sp() for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
for i in range(3):
    dp[0][i] = A[0][i]
#pdb.set_trace()
for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = max(dp[i-1][1], dp[i-1][2]) + A[i][j]
        elif j == 1:
            dp[i][j] = max(dp[i-1][0], dp[i-1][2]) + A[i][j]
        elif j == 2:
            dp[i][j] = max(dp[i-1][0], dp[i-1][1]) + A[i][j]
print(max(dp[N-1]))



