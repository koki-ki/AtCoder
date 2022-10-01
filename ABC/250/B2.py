n, a, b = map(int, input().split())
S = ['.' * b, '#' * b]

for i in range(n):
    for _ in range(a):
        s = ''
        for j in range(n):
            s += S[(i + j) % 2]
        print(s)
