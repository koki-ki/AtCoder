n, q = map(int, input().split())
val = [i for i in range(n + 1)]
pos = [i for i in range(n + 1)]

for _ in range(q):
    x = int(input())
    px = pos[x]
    if px == n:
        pn = px - 1
    else:
        pn = px + 1
    vx = val[px]
    vn = val[pn]
    val[px], val[pn] = val[pn], val[px]
    pos[vx], pos[vn] = pos[vn], pos[vx]
print(*val[1:])
