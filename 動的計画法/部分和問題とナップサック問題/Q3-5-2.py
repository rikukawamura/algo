def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
# 入力
N, M = map(int, input().split())
W = list(map(int, input().split()))

# (N+1) x (M+1) の配列を用意する
# 最小化問題なので、配列全体を INF で初期化する
INF = 10000000  # 十分大きい値とする
dp = [[INF] * (M+1) for _ in range(N+1)]

# 初期状態
dp[0][0] = 0

# 各品物を順に考慮していく (マス目を下へと更新していく)
for i in range(N):
    for j in range(M+1):
        # 最初の i 個のボールのみを用いて重さを j にすることが不可能の場合はスキップ
        if dp[i][j] == INF:
            continue

        # i 番目のボールを入れない場合 (1 つ下のマスへ進む場合)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        # i 番目のボールを入れる場合 (1 つ下、A[i] つ右のマスへ進む場合)
        if j+W[i] <= M:
            dp[i+1][j+W[i]] = min(dp[i+1][j+W[i]], dp[i][j] + 1)
pdb.set_trace()
# 答え
print(dp[N][M] if dp[N][M] != INF else -1)
