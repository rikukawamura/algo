def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, A, B = int_sp()
X = li_int_sp()
dp = [[False]*(A+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    #pdb.set_trace()
    for j in range(A+1):
        #pdb.set_trace()
        if dp[i][j] == False:
            continue
        dp[i+1][j] = True
        if 0 <= (j+X[i])%A < A+1:
            dp[i+1][(j+X[i])%A] = True
#pdb.set_trace()
print('Yes' if dp[N][B] != False else 'No')