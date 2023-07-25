from copy import deepcopy

n = int(input())
a = [list(input()) for _ in range(n)]

copy_a = deepcopy(a)
for i in range(n):
    for j in range(n):
        if i == 0 and 1 <= j <= n - 1:
            copy_a[i][j] = a[i][j - 1]
        elif j == n - 1 and 1 <= i <= n - 1:
            copy_a[i][j] = a[i - 1][j]
        elif i == n - 1 and 0 <= j <= n - 2:
            copy_a[i][j] = a[i][j + 1]
        elif j == 0 and 0 <= i <= n - 2:
            copy_a[i][j] = a[i + 1][j]

for ai in copy_a:
    s = ''.join(ai)
    print(s)