h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(h):
    for j in range(w):
        for px, py in zip(dx, dy):
            if not(0 <= i + 4 * px <= h - 1 and 0 <= j + 4 * py <= w - 1):
                continue

            string = ''

            for t in range(5):
                x = i + t * px
                y = j + t * py
                string += s[x][y]

            if string == 'snuke':
                for t in range(5):
                    x = i + t * px + 1
                    y = j + t * py + 1
                    print(x, end=' ')
                    print(y)

