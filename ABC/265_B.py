n, m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
bonus = [0] * (n + 1)

for i in range(m):
    x_, y_ = map(int, input().split())
    bonus[x_] = y_

bonus_index = 0

for i in range(1, n):
    t -= a[i]

    if t < 0:
        print('No')
        exit()
    t += bonus[i + 1]

print('Yes')
