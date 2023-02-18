s = input()
p = "atcoder"
n = len(p)
l = [p.index(c) for c in s]

ans = 0
for i in range(n - 1):
    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            ans += 1

print(ans)
