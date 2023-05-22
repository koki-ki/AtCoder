from bisect import bisect_left as bl

n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

i = n
j = m

while True:
    if i == 0 or j == 0:
        print(-1)
        exit()

    x = a[-1]
    y = b[-1]

    if abs(x - y) <= d:
        print(x + y)
        exit()

    if x > y:
        a.pop()
        i -= 1
    else:
        b.pop()
        j -= 1
