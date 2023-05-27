INF = 10 ** 9

x, y, z = map(int, input().split())
s = [''] + list(input())
length = len(s)

caps = False
dp = [[INF for _ in range(length)] for _ in range(2)]

dp[0][0] = 0
dp[1][0] = z

is_large = True
for i in range(1, length):
    if s[i] == 'A':
        is_large = True
    else:
        is_large = False

    if is_large:
        dp[0][i] = min(dp[0][i - 1] + y,
                       dp[1][i - 1] + z + x)
        dp[1][i] = min(dp[0][i - 1] + z + x,
                       dp[1][i - 1] + x)
    else:
        dp[0][i] = min(dp[0][i - 1] + x,
                    dp[1][i - 1] + z + x)
        dp[1][i] = min(dp[0][i - 1] + z + x,
                    dp[1][i - 1] + y)

ans = min(dp[0][-1], dp[1][-1])
print(ans)

