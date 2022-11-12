n = int(input())
a = [1]
b = [1]
f = [1]

for _ in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    f.append(a_)
    f.append(b_)


fz = sorted(set(f))
v_to_i = {v: i for i, v in enumerate(fz)}
i_to_v = {i: v for i, v in enumerate(fz)}

G = [[] for _ in range(len(fz) + 1)]

for i in range(n):
    a_, b_ = a[i], b[i]
    a_ = v_to_i[a_]
    b_ = v_to_i[b_]
    G[a_].append(b_)
    G[b_].append(a_)

visited = [False] * (len(i_to_v) + 1)


def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)


dfs(0, G, visited)
ans = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        ans = i
print(i_to_v[ans])
