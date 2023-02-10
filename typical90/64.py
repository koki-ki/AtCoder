n, q = map(int, input().split())
a = list(map(int, input().split()))
l = []
r = []
v = []
for _ in range(q):
    li, ri, vi = map(int, input().split())
    li -= 1
    ri -= 1
    l.append(li)
    r.append(ri)
    v.append(vi)

b = [0 for _ in range(n - 1)]
ans = 0
for i in range(n - 1):
    b[i] = a[i + 1] - a[i]
    ans += abs(b[i])

for i in range(q):
    mae = 0
    if l[i] >= 1:
        mae += abs(b[l[i] - 1])
    if r[i] <= n - 2:
        mae += abs(b[r[i]])

    # 更新
    if l[i] >= 1:
        b[l[i] - 1] += v[i]
    if r[i] <= n - 2:
        b[r[i]] -= v[i]

    ato = 0
    if l[i] >= 1:
        ato += abs(b[l[i] - 1])
    if r[i] <= n - 2:
        ato += abs(b[r[i]])

    ans += ato - mae
    print(ans)
