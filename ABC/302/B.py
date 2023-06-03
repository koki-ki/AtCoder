dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

h, w = map(int, input().split())

s = []
for _ in range(h):
    s.append(input())

for i in range(h):
    for j in range(w):
        for ddx, ddy in zip(dx, dy):
            xs = [j, j + ddx, j + 2 * ddx, j + 3 * ddx, j + 4 * ddx]
            ys = [i, i + ddy, i + 2 * ddy, i + 3 * ddy, i + 4 * ddy]

            if not(0 <= j + 4 * ddx < w and 0 <= i + 4 * ddy < h):
                continue

            strings = ''
            for x, y in zip(xs, ys):
                strings += s[x][y]

            if strings == 'snuke':
                for x, y in zip(xs, ys):
                    print(x + 1, y + 1)

