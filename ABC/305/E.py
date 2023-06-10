import sys
sys.setrecursionlimit(10**6)

def dfs(vs, v, G, d, guarded, longest_dist, longest_nodes):
    guarded[v] = True
    if d == 0:
        longest_nodes[vs].add(v)
        longest_dist[vs] = d
        return

    for nv in longest_nodes[v]:
        dfs(vs, nv, G, d - 1, guarded, longest_dist, longest_nodes)

n, m, k = map(int, input().split())

G = [[] for _ in range(n + 1)]

for _ in range(m):
    ai, bi = map(int, input().split())
    G[ai].append(bi)
    G[bi].append(ai)

guarded = [False for _ in range(n + 1)]
longest_dist = [0 for _ in range(n + 1)]
longest_nodes = [set([i]) for i in range(n + 1)]

for _ in range(k):
    pi, hi = map(int, input().split())
    dfs(pi, pi, G, hi, guarded, longest_dist, longest_nodes)

ans = guarded.count(True)
print(ans)

ans = []
for i, guard in enumerate(guarded):
    if guard:
        ans.append(i)

print(*ans)


