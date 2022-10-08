n, s = map(int, input().split())
sum = 0
more = []
moji = []

for i in range(n):
    a, b = map(int, input().split())
    sum += min(a, b)
    more.append((i, max(a, b) - min(a, b)))
    if a >= b:
        moji.append('H')
    else:
        moji.append('T')

nokori = s - sum
more.sort(key=lambda x: x[1])
ruiseki = [0] * n
ruiseki[0] = more[0][1]
# print(more)
for i in range(1, n):
    ruiseki[i] += ruiseki[i - 1] + more[i][1]

for i in range(n):
    for j in range(i + 1, n):
        if ruiseki[j] - ruiseki[i] == nokori:
            for k in range(i + 1, j + 1):
                if moji[more[k][0]] == 'H':
                    moji[more[k][0]] = 'T'
                else:
                    moji[more[k][0]] = 'H'
            print('Yes')
            ans = ''.join(moji)
            print(ans)
            exit()
print('No')
