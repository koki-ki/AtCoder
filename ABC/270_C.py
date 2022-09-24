n, x, y = map(int, input().split())
x -= 1
y -= 1

# a = [[0] * n for _ in range(n)]
G = [[] for _ in range(n)]

for _ in range(n - 1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    # a[i][j] = 1
    # a[j][i] = 1
    G[i].append(j)
    G[j].append(i)
ans = []
seen = [False for i in range(n)]


def DFS(G, v):
    seen[v] = True
    ans.append(v)
    for next_v in range(len(G[v])):
        if seen[G[v][next_v]]:
            continue
        DFS(G, G[v][next_v])


DFS(G, x)
print(*ans)
