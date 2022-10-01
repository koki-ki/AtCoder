n, x = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] * (n + 1)

ans = 0
i = x
while True:
    if b[i] == 1:
        break
    else:
        b[i] = 1
        i = a[i]
        ans += 1
print(ans)
