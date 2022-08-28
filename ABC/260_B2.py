n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = []
for i in range(n):
    sum.append(a[i] + b[i])

passed = []
cnta = 0
cntb = 0
cnts = 0

max_ = max(a)
for i in range(n):
    if x == 0:
        break
    if a[i] == max_ and i not in passed:
        passed.append(i)

        max_ = 0
        cnta += 1
        if cnta == x:
            break
        for j in range(n):
            if j not in passed and max_ < a[j]:
                max_ = a[j]


max_ = 0
for i in range(n):
    if i not in passed and max_ < b[i]:
        max_ = b[i]

for i in range(n):
    if y == 0:
        break
    if b[i] == max_ and i not in passed:
        passed.append(i)

        max_ = 0
        cntb += 1
        if cntb == y:
            break
        for j in range(n):
            if j not in passed and max_ < b[j]:
                max_ = b[j]


max_ = 0
for i in range(n):
    if i not in passed and max_ < sum[i]:
        max_ = sum[i]

for i in range(n):
    if z == 0:
        break

    if sum[i] == max_ and i not in passed:
        passed.append(i)

        max_ = 0
        cnts += 1
        if cnts == z:
            break
        for j in range(n):
            if j not in passed and max_ < sum[j]:
                max_ = sum[j]


passed.sort()
for i in range(len(passed)):
    print(passed[i] + 1)