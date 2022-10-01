x, y, n = map(int, input().split())
ans = 10 ** 18

for i in range(101):
    for j in range(0, 101 - i, 3):
        if i + j == n:
            ans = min(ans, x * i + y * j // 3)
print(ans)