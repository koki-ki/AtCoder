n, m = map(int, input().split())
adj = [[] for _ in range(m)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b)
    adj[b - 1].append(a)

for i in range(n):
    adj[i] = sorted(list(set(adj[i])))
    print(len(adj[i]), *adj[i])
