x, y, z = map(int, input().split())
if y < 0 < x or 0 < x < y or x < 0 < y or y < x < 0:
    ans = abs(x)
    print(ans)
    exit()

if 0 < y < x:
    if 0 < z < y:
        ans = x
    elif z < 0 < y:
        ans = abs(z) * 2 + x
    elif y > z:
        ans = -1

if x < y < 0:
    if y < 0 < z:
        ans = abs(z) * 2 + abs(x)
    elif y < z < 0:
        ans = abs(x)
    elif z < y:
        ans = -1

if (y < x and y < z) or (x < y and z < y):
    ans = -1

print(ans)
