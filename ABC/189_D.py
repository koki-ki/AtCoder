n = int(input())
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n + 1):
    s = input()
    if s == 'AND':
