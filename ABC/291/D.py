MOD = 998244353

n = int(input())
a = [0]
b = [0]
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [[0 for _ in range(2)] for _ in range(n + 1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n + 1):
    if a[i - 1] != a[i]:
        dp[i][0] += dp[i - 1][0]
    if b[i - 1] != a[i]:
        dp[i][0] += dp[i - 1][1]
    if a[i - 1] != b[i]:
        dp[i][1] += dp[i - 1][0]
    if b[i - 1] != b[i]:
        dp[i][1] += dp[i - 1][1]
    dp[i][0] %= MOD
    dp[i][1] %= MOD

ans = sum(dp[n])
ans %= MOD

print(ans)