n = int(input())
a = []
b = []

def kaiten(a):
    n = len(a)
    new_a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[j][n - 1 - i] = a[i][j]

    return new_a

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

for _ in range(4):
    a = kaiten(a)
    flag = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if b[i][j] != 1:
                    flag = False
    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')



