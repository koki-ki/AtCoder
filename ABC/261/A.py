l1, r1, l2, r2 = map(int, input().split())
a = [0] * 101
for i in range(l1, r1):
    a[i] += 1

for i in range(l2, r2):
    a[i] += 1

print(a.count(2))