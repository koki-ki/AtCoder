n, m = map(int, input().split())

friends = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a = list(input().split())
    for i in range(n - 1):
        x, y  = a[i], a[i + 1]
        x = int(x) - 1
        y = int(y) - 1
        friends[x][y] += 1
        friends[y][x] += 1

ans = 0

for i in range(n - 1):
    ans += friends[i][i + 1:].count(0)

print(ans)

