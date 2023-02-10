# input
h, w = map(int, input().split())
a = []
b = []
for _ in range(h):
    a.append(list(map(int, input().split())))
for _ in range(h):
    b.append(list(map(int, input().split())))

# main
cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        diff = b[i][j] - a[i][j]
        a[i][j] += diff
        a[i][j + 1] += diff
        a[i + 1][j] += diff
        a[i + 1][j + 1] += diff
        cnt += abs(diff)

if a == b:
    print('Yes')
    print(cnt)
else:
    print('No')