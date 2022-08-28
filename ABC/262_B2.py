n, m = map(int, input().split())

adj = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u - 1][v - 1] = 1
    adj[v - 1][u - 1] = 1

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if adj[i][j] == 1:
            for k in range(j + 1, n):
                if adj[j][k] == 1 and adj[i][k] == 1:
                    ans += 1

print(ans)