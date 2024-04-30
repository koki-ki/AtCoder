n = int(input())
a, b = [], []

for _ in range(n):
    a.append(input())

for _ in range(n):
    b.append(input())

for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            print(i + 1, j + 1)
            exit()
