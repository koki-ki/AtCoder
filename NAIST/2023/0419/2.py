from collections import defaultdict

n = int(input())
s = []
dd = defaultdict(int)

for _ in range(n):
    si = input()
    s.append(si)
    dd[si] += 1

    if dd[si] == 1:
        print(si)
    else:
        x = dd[si] - 1
        print(si + '(' + str(x) + ')')


