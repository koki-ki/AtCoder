n, a, x, y = map(int, input().split())

if n >= a:
    num_x = a
    num_y = n - a
else:
    num_x = n
    num_y = 0

ans = num_x * x + num_y * y
print(ans)

