def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, X, Y = int_sp()
dp = [0]*N
dp[0], dp[1] = X, Y
for i in range(2, N):
    dp[i] = (dp[i-2]+dp[i-1]) % 100

print(dp[N-1])