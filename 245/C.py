n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0] * n for i in range(2)]
dp[0][0] = 1
dp[1][0] = 1
for i in range(1, n):
    if dp[0][i-1] == 1 and abs(a[i-1] - a[i]) <= k:
        dp[0][i] = 1
    if dp[1][i-1] == 1 and abs(b[i-1] - a[i]) <= k:
        dp[0][i] = 1
    if dp[0][i-1] == 1 and abs(a[i-1] - b[i]) <= k:
        dp[1][i] = 1
    if dp[1][i-1] == 1 and abs(b[i-1] - b[i]) <= k:
        dp[1][i] = 1

if dp[0][n-1] == 1 or dp[1][n-1] == 1:
    print('Yes')
else:
    print('No')