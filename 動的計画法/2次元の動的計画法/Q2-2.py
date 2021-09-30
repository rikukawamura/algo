def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = li_int_sp()
grid = [[0]*N for _ in range(N)]
for i in range(N):
    grid[0][i] = A[i]

param = [(-1, -1), (-1, 0), (-1, 1)] # 左上，真上，右上
for i in range(1, N):
    for j in range(N):
        for dy, dx in param:
            if 0 <= i+dy < N and 0 <= j+dx < N:
                grid[i][j] = (grid[i][j] + grid[i+dy][j+dx]) % 100

print(grid[N-1][N-1])
