n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
ans = []

for i in range(len(a)):
    if a[i] not in b:
        ans.append(a[i])
for i in range(len(b)):
    if b[i] not in a:
        ans.append(b[i])
ans.sort()
print(*ans)

