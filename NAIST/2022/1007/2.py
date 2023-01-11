n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]
for _ in range(m):
    a_, b_ = map(int, input().split())
    a_ -= 1
    b_ -= 1
    adj[a_][b_] += 1
    adj[b_][a_] += 1

for i in range(n):
    print(sum(adj[i]))
