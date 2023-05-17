x, y = map(int, input().split())
w, s = min(x, y), max(x, y)

if w + 3 > s:
    print('Yes')
else:
    print('No')