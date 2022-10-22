n, x, y = map(int, input().split())
a = [0] + list(map(int, input().split()))
odds = [a[i] for i in range(3, n + 1) if i % 2 == 1]
evens = [a[i] for i in range(2, n + 1) if i % 2 == 0]
xmax = sum(odds)
ymax = sum(evens)
flgx = False
flgy = False

dp = [[False] * len(odds) for _ in range(ymax)]
dp[0][0] = True
