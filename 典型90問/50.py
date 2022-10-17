n, l = map(int, input().split())
if l > n:
    print(1)
    exit()

MOD = 10 ** 9 + 7
dp = [0] * (n + 1)
for i in range(l):
    dp[i] = 1
for i in range(l, n + 1):
    dp[i] = dp[i - l] + dp[i - 1]
print(dp[-1] % MOD)
