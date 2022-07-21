h, w = map(int, input().split())

c = []
for i in range(h):
    c.append(input())

sh, sw = 0, 0
gh, gw = 0, 0

# スタート、ゴールの位置
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sh, sw = i, j
        if c[i][j] == 'g':
            gh, gw = i, j




