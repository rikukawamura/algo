def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
W = li_int_sp()
sum_W = sum(W)
dp = [[False]*(sum_W+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    #pdb.set_trace()
    for j in range(sum_W):
        #pdb.set_trace()
        if dp[i][j] == False:
            continue
        dp[i + 1][abs(j-W[i])] = True
        dp[i + 1][j+W[i]] = True
#pdb.set_trace()

for i, j in enumerate(dp[N]):
    if j:
        print(i)
        break
