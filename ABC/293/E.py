def power(a, b, m):
    p = a
    ans = 1
    for i in range(40):
        wari = 1 << i
        if (b // wari) % 2 == 1:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

a, x, m = map(int, input().split())
if a == 1:
    ans = x % m
else:
    ans = (power(a, x, m * (a - 1)) - 1) // (a - 1)
print(ans)