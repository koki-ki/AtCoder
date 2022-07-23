n = int(input())
a = []
for _ in range(n):
    a.append(input())

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if a[i][j] == a[j][i] and a[i][j] != 'D':
            print('incorrect')
            exit()

        if a[i][j] == 'D' and a[j][i] != 'D':
            print('incorrect')
            exit()

print('correct')
