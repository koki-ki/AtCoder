h, w =map(int, input().split())
s = []
zahyou = []
for i in range(h):
    s.append(input())

for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            zahyou.append((i, j))
ans = abs(zahyou[0][0] - zahyou[1][0]) + abs(zahyou[0][1] - zahyou[1][1])

print(ans)