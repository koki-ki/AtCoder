h, w = map(int, input().split())
g = []
for _ in range(h):
    g.append(input())
#
passed = [[False for _ in range(w)] for _ in range(h)]
x = 0
y = 0
while True:
    if passed[x][y]:
        print(-1)
        exit()
    passed[x][y] = True

    if g[x][y] == 'U' and x != 0:
        x -= 1
    elif g[x][y] == 'D' and x != h - 1:
        x += 1
    elif g[x][y] == 'L' and y != 0:
        y -= 1
    elif g[x][y] == 'R' and y != w - 1:
        y += 1
    else:
        break
print(x + 1, y + 1)
