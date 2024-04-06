h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(input()))

n = int(input())
for _ in range(n):
    r, c, e = map(int, input().split())
    r, c = r - 1, c - 1
    a[r][c] = e

if a[sx][sy] == "S":
    print("No")
    exit()
