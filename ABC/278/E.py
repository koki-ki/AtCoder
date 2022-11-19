H, W, N, h, w = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

count = [[[0 for _ in range(N + 1)] for _ in range(W)]
         for _ in range(H)]


for i in range(H):
    for j in range(W):
        for x in range(1, N + 1):
            if A[i][j] == x:
                count[i][j][x] = 1

# 二次元累積和
for i in range(H - 1, 0, -1):
    for j in range(W):
        for x in range(1, N + 1):
            count[i - 1][j][x] += count[i][j][x]

for i in range(H):
    for j in range(W - 1, 0, -1):
        for x in range(1, N + 1):
            count[i][j - 1][x] += count[i][j][x]

ans = [[0 for _ in range(W - w + 1)] for _ in range(H - h + 1)]

for i in range(H - h +):
    for j in range(W - w):
        for x in range(1, N + 1):
            if count[0][0][x] - count[i][j][x] + count[i][j + w][x] - count[i + h][j + w][x] + count[i + h][j][x] >= 1:
                ans[i][j] += 1

for i in range(H - h + 1):
    print(*ans[i])
