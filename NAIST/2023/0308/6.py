from collections import deque
n = int(input())
sx, sy, tx, ty = map(int, input().split())
x = []
y = []
r = []
for _ in range(n):
    xi, yi, ri = map(int, input().split())
    x.append(xi)
    y.append(yi)
    r.append(ri)
start_is_on = []
goal_is_on = []

A = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist2 = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        if (r[i] - r[j]) ** 2 <= dist2 <= (r[i] + r[j]) ** 2:
            A[i][j] = True

    if (x[i] - sx) ** 2 + (y[i] - sy) ** 2 == r[i] ** 2:
        start_is_on.append(i)
    if (x[i] - tx) ** 2 + (y[i] - ty) ** 2 == r[i] ** 2:
        goal_is_on.append(i)

seen = [False for _ in range(n)]
s = start_is_on.pop(-1)
t = goal_is_on.pop(-1)
seen[s] = True

Q = deque()
Q.append(s)

while len(Q) > 0:
    g = Q.popleft()
    for nextg in range(n):
        if seen[nextg]:
            continue
        if A[g][nextg]:
            seen[nextg] = True
            Q.append(nextg)

if seen[t]:
    print("Yes")
else:
    print("No")