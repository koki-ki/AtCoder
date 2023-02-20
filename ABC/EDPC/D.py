INF = 10 ** 10

N, W = map(int, input().split())
w = [0 for _ in range(N + 1)]
v = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[- INF for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(W + 1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i - 1][j - w[i]] + v[i],
                           dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
ans = max(dp[-1])
print(ans)