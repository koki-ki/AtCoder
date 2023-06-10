import sys
sys.setrecursionlimit(10**6)

def dfs(vs, v, G, d, guarded, longest_nodes):
    guarded[v] = True
    if d == 0:
        return

    if d == 1:
        for nv in G[v]:
            longest_nodes[vs].add(nv)

    for nv in longest_nodes[v]:
        longest_nodes[vs].add(nv)
        dfs(vs, nv, G, d - 1, guarded, longest_nodes)

n, m, k = map(int, input().split())

G = [[] for _ in range(n + 1)]
longest_nodes = [set() for _ in range(n + 1)]

for _ in range(m):
    ai, bi = map(int, input().split())
    G[ai].append(bi)
    G[bi].append(ai)
    longest_nodes[ai].add(bi)

guarded = [False for _ in range(n + 1)]
longest_dist = [0 for _ in range(n + 1)]

for _ in range(k):
    pi, hi = map(int, input().split())
    dfs(pi, pi, G, hi, guarded, longest_nodes)


ans = guarded.count(True)
print(ans)

ans = []
for i, guard in enumerate(guarded):
    if guard:
        ans.append(i)

print(*ans)


