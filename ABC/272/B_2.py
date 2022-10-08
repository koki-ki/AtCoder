n, m = map(int, input().split())
yes = [[0] * n for _ in range(n)]

for i in range(n):
    yes[i][i] = 1

for _ in range(m):
    kx = list(map(int, input().split()))
    k = kx[0]
    x = kx[1:]
    # print(x)
    for i in range(k):
        yes[i][i] = 1
        for j in range(i + 1, k):
            yes[x[i] - 1][x[j] - 1] = 1
            yes[x[j] - 1][x[i] - 1] = 1

# print(yes)

for i in range(n):
    # print(yes[i])
    if sum(yes[i]) != n:
        print('No')
        exit()

print('Yes')
