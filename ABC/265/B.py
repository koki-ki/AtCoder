n, m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
bonus = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    bonus[x] = y

j = 0
for i in range(1, n):
    if t > a[i]:
        t -= a[i]
        t += bonus[i + 1]
    else:
        print('No')
        exit()

print('Yes')
