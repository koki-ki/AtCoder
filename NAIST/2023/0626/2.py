a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

exist = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            exist[i][j] = True

for i in range(3):
    if exist[i][0] and exist[i][1] and exist[i][2]:
        print('Yes')
        exit()

for j in range(3):
    if exist[0][j] and exist[1][j] and exist[2][j]:
        print('Yes')
        exit()

if (exist[0][0] and exist[1][1] and exist[2][2]) or (exist[0][2] and exist[1][1] and exist[2][0]):
    print('Yes')
    exit()

print('No')