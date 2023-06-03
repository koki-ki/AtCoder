from itertools import permutations

n, m = map(int, input().split())
s = []

for _ in range(n):
    s.append(input())

s.sort()

for i in permutations(s):
    ok = True
    for j in range(n - 1):
        cnt = 0
        for k in range(m):
            if i[j][k] != i[j + 1][k]:
                cnt += 1

        if cnt != 1:
            print('Yes')
            exit()

print('No')
