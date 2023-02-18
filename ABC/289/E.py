t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    
    cnt = 0
    