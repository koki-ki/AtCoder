n = int(input())
dp = [[0 for _ in range(n)] for _ in range(2)]
x, y = map(int, input().split())
dp[x][0] = max(0, y)

for i in range(1, n):
    x, y = map(int, input().split())
    if x == 0:
        dp[0][i] = max(dp[0][i - 1], dp[0][i - 1] + y, dp[1][i - 1] + y)
        dp[1][i] = dp[1][i - 1]
    else:
        dp[0][i] = dp[0][i - 1]
        dp[1][i] = max(dp[0][i - 1] + y, dp[1][i - 1])

ans = max(dp[0][-1], dp[1][-1])
print(ans)
