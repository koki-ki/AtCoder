x1, y1, x2, y2 = map(int, input().split())
x0, y0 = 0, 0
x_, y_ = x1 - x2, y1 - y2

patterns = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

for p in patterns:
    xt = x_ + p[0]
    yt = y_ +  p[1]

    dis2 = xt ** 2 + yt ** 2
    if dis2 == 5:
        print('Yes')
        exit()

print('No')