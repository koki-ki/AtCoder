n = int(input())
l = 12
r = [int("1" * (i + 1)) for i in range(l)]

s = set()
for i in range(l):
    for j in range(l):
        for k in range(l):
            s.add(r[i] + r[j] + r[k])

print(sorted(s)[n - 1])
