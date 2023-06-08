MOD = 998244353

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1048576)]

for i in range(1, 10):
    dp[1][i] = 1

for d in range(2, n + 1):
    for i in range(1, 10):
        for j in range(max(1, i-1), min(9, i+1) + 1):
            dp[d][j] += dp[d-1][i]
            dp[d][j] %= MOD

res = 0
for i in range(1, 10):
    res += dp[n][i]
    res %= MOD

print(res)