def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, M = int_sp()
A = li_int_sp()
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    #pdb.set_trace()
    for j in range(M+1):
            if dp[i][j] == False:
                continue
            dp[i+1][j] = True
            if 0<= j+A[i] < M+1:
                dp[i+1][j+A[i]] = True
if dp[N][M] == True:
    print('Yes')
else:
    print('No')