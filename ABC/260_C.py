n, x, y = map(int, input().split())
cnt = 0
dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][n - 1] = 1


for i in range(1, n):
    dp[1][n - i] += dp[0][n - i] * x
    dp[0][n - i - 1] += dp[0][n - i]
    # dp[0][n - i] = 0

    dp[0][n - i - 1] += dp[1][n - i]
    dp[1][n - i - 1] += dp[1][n - i] * y
    # dp[1][n - i] = 0

print(dp[1][0])

