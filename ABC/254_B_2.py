n = int(input())
a = [[1]]
print(*a[0])
for i in range(1, n):
    a.append([0] * (i + 1))
    for j in range(i + 1):
        if j == 0 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

    print(*a[i])