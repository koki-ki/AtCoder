n, a, b = map(int, input().split())
c = list(map(int, input().split()))

ab = a + b
for i, v in enumerate(c):
    if v == ab:
        print(i + 1)