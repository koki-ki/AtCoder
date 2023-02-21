n = int(input())
s = ' ' + input()

a = [0 for _ in range(n + 1)]
b = [0 for _ in range(n + 1)]

ans = 0

for i in range(1, n + 1):
    if s[i] == "o":
        a[i] = i
        b[i] = b[i - 1]
    else:
        a[i] = a[i - 1]
        b[i] = i
    ans += min(a[i], b[i])

print(ans)
