from math import sqrt
n, m = map(int, input().split())

cnts = [[-1] * n for _ in range(n)]
cnts[0][0] = 0

checked = [[False] * n for _ in range(n)]

if m > n ** 2:
    for i in range(n):
        print(*cnts[i])
    exit()

for x in range(sqrt(m)):
    y2 = m - x ** 2
    if sqrt(y2) - int(sqrt(y2)) == 0:
        y = int(sqrt(y2))

if x > n or y > n:
    for i in range(n):
        print(*cnts[i])
    exit()

