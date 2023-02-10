from itertools import permutations

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
m = int(input())
bad = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad[x][y] = True
    bad[y][x] = True
if n == 1:
    print(a[0][0])
    exit()
# main
ans = 1 << 20
perms = list(permutations(range(n)))
success = False

for perm in perms:
    failed = False
    tmp = 0
    for j in range(n - 1):
        x = perm[j]
        y = perm[j + 1]
        if bad[x][y]:
            failed = True
            break
        tmp += a[x][j]
    if failed:
        continue
    tmp += a[y][n - 1]
    ans = min(ans, tmp)
    success = True

if success:
    print(ans)
else:
    print(-1)