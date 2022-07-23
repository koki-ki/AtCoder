n = int(input())
a = []
b = []
c = []

for i in range(n):
    a_, b_, c_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
    dp[i][1] = max(dp[i - 1][0] + b[i], dp[i - 1][2] + b[i])
    dp[i][2] = max(dp[i - 1][0] + c[i], dp[i - 1][1] + c[i])

ans = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(ans)
