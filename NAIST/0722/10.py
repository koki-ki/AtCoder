h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = 0
            for k in range(8):
                nh = i + dy[k]
                nw = j + dx[k]
                if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '#':
                    cnt += 1
            s[i][j] = str(cnt)

for i in range(h):
    print(''.join(s[i]))



