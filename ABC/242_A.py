a, b, c, x = map(int, input().split())
if x in range(1, a + 1):
    print(1.0)
elif x in range(a + 1, b + 1):
    print(c / (b - a))
else:
    print(0)
