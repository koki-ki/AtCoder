a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
if abs(a - b) == 1 or (a == 1 and b == 10):
    print('Yes')
else:
    print('No')
