n = int(input())
t = []
k = []
a = []
for i in range(n):
    ti, ki, *ai = map(int, input().split())
    t.append(ti)
    k.append(ki)
    a.append(ai)
    for j in range(ki):
        a[i][j] -= 1
need = [False for _ in range(n)]
need[n - 1] = True
for i in range(n - 1, -1, -1):
    if need[i]:
        for j in a[i]:
            need[j] = True
ans = 0

for i in range(n):
    if need[i]:
        ans += t[i]

print(ans)