from math import sqrt
n, m = map(int, input().split())

cnts = [[-1] * n for _ in range(n)]
cnts[0][0] = 0


for x in range(int(sqrt(m))):
    y2 = m - x ** 2
    if sqrt(y2) - int(sqrt(y2)) == 0:
        y = int(sqrt(y2))

tovisit = []
visited = []
X, Y = [x, x, -x, -x, y, y, -y, -y], [y, -y, y, -y, x, -x, x, -x]


for x, y in zip(X, Y):
    if 0 <= x <= n - 1 and 0 <= y <= n - 1:
        tovisit.append([x, y, 1])
        visited.append(x, y)
        cnts[x][y] = 1


# print(X)
# print(Y)
# print(tovisit)
# exit()

while tovisit != []:
    next = tovisit.pop(-1)
    nx, ny, nc = next[0], next[1], next[2]

    # checked[nx][ny] = True
    for x, y in zip(X, Y):
        if 0 <= nx + x <= n - 1 and 0 <= ny + y <= n - 1 and cnts[nx + x][nx + y] == -1:
            print(([nx + x, nx + y, nc + 1]))
            tovisit.append([nx + x, nx + y, nc + 1])
            cnts[nx + x][ny + y] = nc + 1
            # checked[nx + x][ny + y] = True
            if [nx + x, ny + y] in visited:
                for i in range(n):
                    print(*cnts[i])
                exit()
            visited.append([nx + x, ny + y])

for i in range(n):
    print(*cnts[i])