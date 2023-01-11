n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)

visited = [False] * (n + 1)
ans = [0] * (n + 1)


def dfs(x):
    visited[x] = True
    for next_node in G[x]:
        if visited[next_node] == False:
            dfs(next_node)


for i in range(1, n + 1):
    dfs(i)
print(max(ans))
