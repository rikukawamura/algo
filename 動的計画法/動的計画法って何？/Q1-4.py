def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, N+1):
    if i-1 >= 0:
        dp[i] += dp[i-1]
    if i-2 >= 0:
        dp[i] += dp[i-2]
    if i-3 >= 0:
        dp[i] += dp[i-3]
print(dp[N])