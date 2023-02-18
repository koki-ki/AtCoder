n, m = map(int, input().split())
a = list(map(int, input().split()))

G = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    G[a[i]][a[i] + 1] = 1
    G[a[i] + 1][a[i]] = 1

x = 1
ans = []
read = [x]

while x != n:
    if G[x][x + 1]:
        read.append(x + 1)
        x += 1
    else:
        read.reverse()
        ans.extend(read)
        read = []
        x += 1
        read.append(x)
read.reverse()
ans.extend(read)
print(*ans)