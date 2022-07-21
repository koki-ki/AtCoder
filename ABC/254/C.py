n, k = map(int, input().split())
def shoujun(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
a = list(map(int, input().split()))

b = [[] for i in range(k)]

for i in range(n):
    b[i % k].append(a[i])

for i in range(k):
    b[i].sort()

new_a = []

for i in range(n):
    new_a.append(b[i % k][i // k])

if shoujun(new_a):
    print('Yes')
else:
    print('No')