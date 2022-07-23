n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, n):
    candidates = []
    for j in range(max(0, i - k), i):
        candidates.append(dp[j] + abs(h[i] - h[j]))
    dp[i] = min(candidates)

print(dp[n - 1])