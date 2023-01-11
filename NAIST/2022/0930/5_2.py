n, m = map(int, input().split())
s = []
c = []
for _ in range(m):
    s_, c_ = map(int, input().split())
    s.append(s_)
    c.append(c_)


for i in range(0, 1000):
    flg = True
    if len(str(i)) < n:
        continue
    num = str(i)

    for sj, cj in zip(s, c):
        sj -= 1

        if num[sj] != str(cj):
            flg = False
            break
    if flg:
        print(i)
        exit()

print(-1)
