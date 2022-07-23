N, W = map(int, input().split())
w = [0]
v = [0]

for i in range(N):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)

dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j - w[i] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])


print(dp[N][W])
