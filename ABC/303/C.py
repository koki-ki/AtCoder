n, m, h, k = map(int, input().split())
S = list(input())

heals = set()
for i in range(m):
    x, y = map(int, input().split())
    heals.add((x, y))

dx = {'R': 1, 'U': 0, 'L': -1, 'D': 0}
dy = {'R': 0, 'U': 1, 'L': 0, 'D': -1}

x = 0
y = 0
cur = (x, y)

flag = True

for s in S:
    h -= 1
    if h < 0:
        flag = False
        break
    x += dx[s]
    y += dy[s]
    cur = (x, y)
    if cur in heals and h < k:
        h = k
        heals.remove(cur)

if flag:
    print('Yes')
else:
    print('No')