def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
dp = [0]*(N+1)
dp[0], dp[1] = 1, 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])