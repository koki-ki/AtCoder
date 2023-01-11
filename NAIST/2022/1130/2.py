x1, y1, x2, y2 = map(int, input().split())
if y1 == y2 and x2 < x1:
    x3 = x2
    y3 = y1 - (x1 - x2)
    x4 = x1
    y4 = y3
    print(x3, y3, x4, y4)
    exit()

if x1 == x2 and y1 < y2:
    x3 = x2 + (y1 - y2)
    y3 = y2
    x4 = x3
    y4 = y1
    print(x3, y3, x4, y4)
    exit()

if y1 == y2 and x1 < x2:
    x3 = x2
    y3 = y1 + (x1 - x2)
    x4 = x1
    y4 = y3
    print(x3, y3, x4, y4)
    exit()

if x1 == x2 and y1 > y2:
    x3 = x1 - (y2 - y1)
    y3 = y1
    x4 = x3
    y4 = y2
    print(x3, y3, x4, y4)
    exit()

print(-1)
