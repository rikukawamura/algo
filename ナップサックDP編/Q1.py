def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = li_int_sp()
dp = [0]*(N+1)
for i in range(N):
    dp[i+1] = max(dp[i], dp[i]+A[i])
print(dp[N])
