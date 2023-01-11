a, b = map(int, input().split())
MIN = 1 * a
MAX = 6 * a
if MIN <= b and b <= MAX:
    print('Yes')
else:
    print('No')
