import sys
sys.setrecursionlimit(10**6)
# dfs
def dfs(v, G, seen):
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]:
            continue
        dfs(v2, G, seen)
    return

# input
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

seen = [False for _ in range(n)]
num = 0

for v in range(n):
    if seen[v]:
        continue
    dfs(v, G, seen)
    num += 1

ans = m - n + num
print(ans)