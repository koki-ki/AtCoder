n, q = map(int, input().split())
G = {}
ans = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in G:
            G[a] = set()
            G[a].add(b)
            continue
        if b not in G:
            G[b] = set()
        G[a].add(b)
    elif t == 2 and b in G[a]:
        G[a].remove(b)
    else:
        if a not in G:
            G[a] = set()
        if b not in G:
            G[b] = set()
        if b in G[a] and a in G[b]:
            ans.append('Yes')
        else:
            ans.append('No')


for a in ans:
    print(a)
