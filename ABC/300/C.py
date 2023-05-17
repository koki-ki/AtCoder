def check(x, y, c, d, h, w):
    flag = True
    if x - d >= 0 and x + d <= h - 1 and y - d >= 0 and y + d <= w - 1: #and center[x][y] is False:
        for i in range(-d, d + 1):
            if not(c[x - i][y - i] == '#' and c[x - i][y + i] == '#' and c[x + i][y - i] == '#' and c[x + i][y + i] == '#'):
                flag = False
                break
    else:
        flag = False

    if flag:
        # print(x + 1, y + 1, d) # debug
        return 1
    else:
        return 0

h, w = map(int, input().split())
n = min(h, w)
c = []
for _ in range(h):
    c.append(input())
s = [0 for _ in range(n)]
center = [[False for _ in range(w)] for _ in range(h)]

if n % 2 == 0:
    dmax = n // 2 - 1
else:
    dmax = n // 2

for x in range(h):
    for y in range(w):
        for d in range(dmax, 0, -1):
            if check(x, y, c, d, h, w) and not center[x][y]:
                s[d - 1] += 1
                center[x][y] = True

print(*s)

