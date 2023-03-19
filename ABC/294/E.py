l, n1, n2 = map(int, input().split())
v = [[] for _ in range(2)]
l = [[] for _ in range(2)]

for _ in range(n1):
    a, b = map(int, input().split())
    v[0].append(a)
    l[0].append(b)

for _ in range(n2):
    a, b = map(int, input().split())
    v[1].append(a)
    l[1].append(b)

ans = 0
i = 0
j = 0
t1 = 0
t2 = 0
while i < n1 and j < n2:
    len1, num1 = l[0][i], v[0][i]
    len2, num2 = l[1][j], v[1][j]

    if num1 == num2:
        ans += min(len1, len2)
        i += 1
        j += 1
        t1 += len1
        t2 += len2
    elif t1 < t2:
        i += 1
        t1 += len1
    else:
        j += 1
        t2 += len2


print(ans)

