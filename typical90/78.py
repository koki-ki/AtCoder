# input
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
# main
ans = 0
for v in range(n):
    less = 0
    G[v].sort()
    for nv in G[v]:
        if nv < v:
            less += 1
        if less > 2:
            break
    if less == 1:
        ans += 1
print(ans)
