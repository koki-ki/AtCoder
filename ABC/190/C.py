n, m = map(int, input().split())
a, b = [0] * m, [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
k = int(input())
c, d = [0] * k, [0] * k
for i in range(k):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1
ans = 0

for i in range(1 << k):
    cnt = 0
    dishes = [0] * n
    for j in range(k):
        if i % 2 == 0:
            dishes[c[j]] += 1
        else:
            dishes[d[j]] += 1
        i //= 2
    for j in range(m):
        if dishes[a[j]] >= 1 and dishes[b[j]] >= 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
