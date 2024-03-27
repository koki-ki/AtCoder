def my_ceil(x, y):
    return -(-x // y)


INF = 10 ** 18
n, s, m, l = map(int, input().split())
ans = INF

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i * 6 + j * 8 + k * 12 >= n:
                tmp = i * s + j * m + k * l
                ans = min(ans, tmp)


print(ans)
