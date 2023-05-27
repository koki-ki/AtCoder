w, h, n = map(int, input().split())

xmax = w
xmin = 0
ymax = h
ymin = 0

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        xmin = max(xmin, x)
    elif a == 2:
        xmax = min(xmax, x)
    elif a == 3 :
        ymin = max(ymin, y)
    else:
        ymax = min(ymax, y)

if xmax <= xmin or ymax <= ymin:
    ans = 0
else:
    ans = (ymax - ymin) * (xmax - xmin)

print(ans)