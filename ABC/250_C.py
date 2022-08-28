import numpy as np
n, q = map(int, input().split())

a = list(np.arange(1, n+1))
b = list(np.arange(0, n))

x = []
for i in range(n):
    x.append(int(input()) - 1)

print(a)
for i in range(n):
    a1 = a[b[x[i] - 1] - 1]
    a2 = a[b[x[i] - 1] % n]
    b1 = b[x[i] - 1]
    b2 = b[a[b[x[i] - 1]] - 1]
    a[b[x[i] - 1] - 1] = a2
    a[b[x[i] - 1]] = a1
    b[x[i] - 1] = b2
    b[a[b[x[i] - 1]] - 1] = b1
    print(a)
print(a)




