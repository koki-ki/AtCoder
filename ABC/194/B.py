n = int(input())
a = []
b = []
c = []

for _ in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(a_ + b_)

ans = 10 ** 9
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = min(ans, max(a[i], b[j]))

ans = min(ans, min(c))
print(ans)
