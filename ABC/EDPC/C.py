n = int(input())

dp = [[0 for _ in range(3)] for _ in range(n)]
a = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    a[i][0], a[i][1], a[i][2] = map(int, input().split())

dp[0][0], dp[0][1], dp[0][2] = a[0][0], a[0][1], a[0][2]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1] + a[i][0], dp[i - 1][2] + a[i][0])
    dp[i][1] = max(dp[i - 1][0] + a[i][1], dp[i - 1][2] + a[i][1])
    dp[i][2] = max(dp[i - 1][1] + a[i][2], dp[i - 1][0] + a[i][2])

print(max(dp[-1]))
