def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
grid = [input().strip() for _ in range(N)]
dp = [[0] * N for _ in range(N)]
#params = [(0, 1), (1, 0)] # 右，下
params = [(0, -1), (-1, 0)] # 左，上
dp[0][0] = 1 # スタート地点の通り数は1

for i in range(N):
    for j in range(N):
        for dy, dx in params:
            if 0 <= i+dy < N and 0 <= j+dx < N and grid[i+dy][j+dx] != '#':
                dp[i][j] += dp[i + dy][j + dx]
print(dp[N - 1][N - 1])
