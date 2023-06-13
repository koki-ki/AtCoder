MOD = 1000000007

n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1 if i not in a else 0
    elif i == 2:
        dp[i] = dp[i - 1] + 1 if i not in a else 0
    else:
        dp[i] = (dp[i - 1] + dp[i - 2] if i not in a else 0) % MOD

print(dp[n])

