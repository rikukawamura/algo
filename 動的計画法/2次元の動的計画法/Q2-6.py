def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = [li_int_sp() for _ in range(N)]
dp = [[0] * N for _ in range(N)]

params = [(0, -1), (-1, 0)] # 左，上
dp[0][0] = A[0][0]

for i in range(N):
    for j in range(N):
        for dy, dx in params:
            if 0 <= i+dy < N and 0 <= j+dx < N:
                dp[i][j] = max(dp[i][j], dp[i + dy][j + dx] + A[i][j])
#pdb.set_trace()
print(dp[N - 1][N - 1])
