n, m = map(int, input().split())
a = []
b = []
for _ in range(m):
    i, j = map(int, input().split())
    a.append(i)
    b.append(j)

k = int(input())
c = []
d = []
for _ in range(k):
    i, j = map(int, input().split())
    c.append(i)
    d.append(j)

cnt = 0
for i in range(2 ** k):
    dishes = [False for _ in range(n + 1)]
    for j in range(k):
        put_c_or_d = (i >> j) % 2
        if put_c_or_d:
            dishes[c[j]] = True
        else:
            dishes[d[j]] = True

    tmp_cnt = 0
    for a_, b_ in zip(a, b):
        if dishes[a_] and dishes[b_]:
            tmp_cnt += 1

    cnt = max(cnt, tmp_cnt)

print(cnt)
