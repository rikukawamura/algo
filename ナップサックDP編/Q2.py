def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, W = int_sp()
wv = []
for i in range(N):
    w, v = int_sp()
    wv.append([w, v])
w, v = list(map(list, (zip(*wv))))

dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W+1):
        if dp[i][j]==-1:
            continue
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if 0 <= j+w[i] < W+1:
            dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])

#pdb.set_trace()
print(max(dp[N]))