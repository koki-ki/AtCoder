n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

i = n - 1
j = m - 1

while True:
    if i == 0 or j == 0:
        print(-1)
        exit()

    x = a[i]
    y = b[j]

    if abs(x - y) < d:
        print(x + y)
        exit()

    if x > y:
        i -= 1
    else:
        j -= 1