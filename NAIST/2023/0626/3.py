n, a, b = map(int, input().split())

a, b = min(a, b), max(a, b)

if (a - b) % 2 == 0:
    ans = (b - a) // 2
else:
    if a - 1 <= n - b:
        ans = (a - 1) + (b - a - 1) // 2 + 1
    else:
        ans = (n - b) + (b - a - 1) // 2 + 1

print(ans)