def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A = li_int_sp()
grid = [[0]*4 for _ in range(4)]
grid[0][0] = A[0]
grid[0][1] = A[1]
grid[0][2] = A[2]
grid[0][3] = A[3]
#pdb.set_trace()

param = [(-1, -1), (-1, 0), (-1, 1)] # 左上，真上，右上
for i in range(1, 4):
    for j in range(4):
        for dy, dx in param:
            if 0 <= i+dy < 4 and 0 <= j+dx < 4:
                grid[i][j] += grid[i+dy][j+dx]
print(grid[3][3])
