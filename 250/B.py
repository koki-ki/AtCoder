n, a, b = map(int, input().split())
s1 = '.' * b
s2 = '#' * b
for i in range(n):
    if n == 0:
        for _ in range(a):
            print(s1)
    elif i % 2 == 0:
        for _ in range(a):
            print((s1+s2)*n)
    else:
        for _ in range(a):
            print((s2+s1)*n)