import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
A = [1]
B = [1]
floor = set()
floor.add(1)

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    floor.add(a)
    floor.add(b)

# 座標圧縮
floor = sorted(floor)
v_to_i = {v: i for i, v in enumerate(floor)}
i_to_v = {i: v for i, v in enumerate(floor)}

# グラフ
G = [[] for _ in range(len(floor))]
for i in range(n):
    a, b = A[i], B[i]
    a = v_to_i[a]
    b = v_to_i[b]
    G[a].append(b)
    G[b].append(a)

visited = [False] * (len(floor))


def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)


dfs(0, G, visited)
ans = 0
for i in range(len(G)):
    if visited[i]:
        ans = i

ans = i_to_v[i]
print(ans)
