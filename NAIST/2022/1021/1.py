n, x = map(int, input().split())
l = list(map(int, input().split()))
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = d[i - 1] + l[i - 1]
ans = sum([d_ <= x for d_ in d])
print(ans)
