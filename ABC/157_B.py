a = []
for _ in range(3):
    a.append(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0


def check(a):
    for i in range(3):
        if a[i][0] == 0 and a[i][1] == 0 and a[i][2] == 0:
            return True
        if a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0:
            return True
    if (a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0) or\
       (a[2][0] == 0 and a[1][1] == 0 and a[0][2] == 0):
        return True

    return False


if check(a):
    print('Yes')
else:
    print('No')
