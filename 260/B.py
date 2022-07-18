n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = []
for i in range(n):
    sum.append(a[i] + b[i])

passed = []
max_ = max(a)
cnta = 0
cntb = 0
cnts = 0

for i in range(n):
    if a[i] == max_ and i in passed:
        passed.append(i)
        a[i] = 0
        max_ = max(a)
        cnta += 1
        for j in range(n):
            if max_ < a[j] and j not in passed:
                max_ = a[j]
    if cnta == x:
        break

max_ = 0
for i in range(n):
    if max_ < b[i] and i not in passed:
        max_ = b[i]

for i in range(n):
    if b[i] == max_ and i not in passed:
        passed.append(i)
        b[i] = 0
        max_ = 0
        cntb += 1
        for j in range(n):
            if max_ < b[j] and j not in passed:
                max_ = b[j]
    if cntb == y:
        break

max_ = 0
for i in range(n):
    if max_ < sum[i] and i not in passed:
        max_ = sum[i]


for i in range(n):
    if i == 3:
        print(i, max_, sum[i])
    if sum[i] == max_ and i not in passed:
        passed.append(i)
        sum[i] = 0
        cnts += 1

        max_ = 0

        for j in range(n):
            if max_ < sum[j] and j not in passed:
                max_ = sum[j]

    if cnts == z:
        break

passed.sort()
for i in range(len(passed)):
    print(passed[i] + 1)

