n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

max1 = max(1 - a, 1 - b)
min1 = min(n - a, n - b)
max2 = max(1 - a, b - n)
min2 = min(n - a, b - 1)

k1s = [i for i in range(max1, min1 + 1)]
k2s = [i for i in range(max2, min2 + 1)]

painted = set()

cnt = 0
for k in k1s:
    painted.add((a + k, b + k))
    cnt += 1
    if cnt ** 2 >= 3 * 10 ** 5:
        break

print('first done')

cnt = 0
for k in k2s:
    painted.add((a + k, b - k))
    cnt += 1
    if cnt ** 2 >= 3 * 10 ** 5:
        break

print('second done')


for x in range(p, q + 1):
    ans = ''
    for y in range(r, s + 1):
        if (x, y) in painted:
            ans += '#'
        else:
            ans += '.'
    print(ans)
