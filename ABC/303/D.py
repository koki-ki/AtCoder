INF = 10 ** 20

x, y, z = map(int, input().split())
s = list(input())

length = len(s)

dp = [[INF for _ in range(length + 1)] for _ in range(2)]

dp[0][0] = 0

for i in range(length):
    if s[i] == 'a':
        cur = 0
    else:
        cur = 1
    for j in range(2):
        for k in range(2):
            v = dp[j][i]
            if j != k:
                v += z
            if cur == k:
                v += x
            else:
                v += y
            dp[k][i + 1] = min(dp[k][i + 1], v)

ans = min(dp[0][length], dp[1][length])
print(ans)

